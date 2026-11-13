import os
import sys
import re
import json
import shutil
import socket
import mimetypes
import webbrowser
import threading
import subprocess
from typing import List, Dict, Any, Optional
from urllib.parse import urlparse
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_HTML_PATH = os.path.join(BASE_DIR, "index.html")
CONFIG_FILE = os.path.expanduser("~/.photo_sorter_config.json")

IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".bmp", ".webp", ".heic", ".tiff", ".tif"
}

def get_index_html() -> bytes:
    """Incarca interfata web din fisierul extern index.html."""
    if os.path.isfile(INDEX_HTML_PATH):
        try:
            with open(INDEX_HTML_PATH, "rb") as f:
                return f.read()
        except OSError as e:
            return f"<h1>Eroare la citirea index.html: {e}</h1>".encode("utf-8")
    return b"<h1>Eroare: Fisierul index.html nu a fost gasit in directorul aplicatiei!</h1>"

def natural_sort_key(s: str) -> list:
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def sanitize_folder_name(name: str) -> str:
    if not name:
        return ""
    # Elimina caracterele invalide pe Windows si Unix
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '', name).strip()
    name = name.strip('. ')
    reserved = {"con", "prn", "aux", "nul"}
    if name.lower() in reserved or (len(name) >= 4 and name[:3].lower() in ("com", "lpt") and name[3].isdigit()):
        name = f"_{name}"
    return name

def load_last_dir() -> str:
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                d = data.get("last_dir", "")
                if d and os.path.isdir(d):
                    return os.path.abspath(d)
        except Exception:
            pass
    return ""

def save_last_dir(path: str) -> None:
    if not path or not os.path.isdir(path):
        return
    abs_path = os.path.abspath(path)
    tmp_config = f"{CONFIG_FILE}.tmp"
    try:
        with open(tmp_config, "w", encoding="utf-8") as f:
            json.dump({"last_dir": abs_path}, f, ensure_ascii=False, indent=2)
        os.replace(tmp_config, CONFIG_FILE)
    except Exception:
        if os.path.exists(tmp_config):
            try:
                os.remove(tmp_config)
            except OSError:
                pass

def choose_folder_native(prompt: str = "Selecteaza folderul cu poze de sortat") -> str:
    """
    Deschide dialogul nativ al sistemului de operare:
    - macOS: AppleScript / Finder NSOpenPanel
    - Windows: PowerShell FolderBrowserDialog (nativ fara dependinte)
    - Fallback: Tkinter askdirectory
    """
    system = sys.platform

    # 1. macOS: Finder Dialog
    if system == "darwin":
        safe_prompt = prompt.replace('"', '\\"')
        script = f'''
        tell application "System Events"
            activate
        end tell
        try
            set chosenFolder to choose folder with prompt "{safe_prompt}"
            return POSIX path of chosenFolder
        on error
            return ""
        end try
        '''
        try:
            res = subprocess.run(
                ["osascript", "-e", script],
                capture_output=True,
                text=True,
                timeout=180
            )
            path = res.stdout.strip()
            if path and os.path.isdir(path):
                return os.path.abspath(path)
        except Exception:
            pass

    # 2. Windows: Native FolderBrowserDialog prin PowerShell
    elif system == "win32":
        safe_prompt = prompt.replace("'", "''")
        ps_script = (
            "Add-Type -AssemblyName System.Windows.Forms; "
            "$f = New-Object System.Windows.Forms.FolderBrowserDialog; "
            f"$f.Description = '{safe_prompt}'; "
            "$f.ShowNewFolderButton = $false; "
            "if ($f.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) { Write-Output $f.SelectedPath }"
        )
        try:
            res = subprocess.run(
                ["powershell", "-NoProfile", "-NonInteractive", "-Command", ps_script],
                capture_output=True,
                text=True,
                timeout=180
            )
            path = res.stdout.strip()
            if path and os.path.isdir(path):
                return os.path.abspath(path)
        except Exception:
            pass

    # 3. Fallback generic cu Tkinter
    try:
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        chosen = filedialog.askdirectory(title=prompt)
        root.destroy()
        if chosen and os.path.isdir(chosen):
            return os.path.abspath(chosen)
    except Exception:
        pass

    return ""

class SorterState:
    def __init__(self, source_dir: str = ""):
        self.lock = threading.RLock()
        self.source_dir: str = ""
        self.images: List[str] = []
        self.current_index: int = 0
        self.known_folders: List[str] = []
        self.progress_file: str = ""
        if source_dir:
            self.set_directory(source_dir)

    def set_directory(self, path: str) -> None:
        with self.lock:
            if not path or not os.path.exists(path):
                self.source_dir = ""
                self.images = []
                self.current_index = 0
                self.known_folders = []
                self.progress_file = ""
                return

            self.source_dir = os.path.abspath(path)

            try:
                # Colecteaza doar imaginile din radacina folderului, cu sortare naturala
                all_entries = os.listdir(self.source_dir)
                valid_images = [
                    f for f in all_entries
                    if not f.startswith(".")
                    and os.path.splitext(f)[1].lower() in IMAGE_EXTENSIONS
                    and os.path.isfile(os.path.join(self.source_dir, f))
                ]
                self.images = sorted(valid_images, key=natural_sort_key)
            except OSError:
                self.images = []

            self.progress_file = os.path.join(self.source_dir, ".sort_progress")
            self.current_index = 0
            self._load_progress()
            self.known_folders = self._scan_folders()

    def _scan_folders(self) -> List[str]:
        folders = []
        if not self.source_dir or not os.path.exists(self.source_dir):
            return folders
        try:
            for item in os.listdir(self.source_dir):
                if item.startswith("."):
                    continue
                full_p = os.path.join(self.source_dir, item)
                if os.path.isdir(full_p):
                    folders.append(item)
        except OSError:
            pass
        return sorted(folders, key=natural_sort_key)

    def _load_progress(self) -> None:
        if self.progress_file and os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, "r", encoding="utf-8") as f:
                    saved = int(f.read().strip())
                if 0 <= saved < len(self.images):
                    self.current_index = saved
            except Exception:
                pass

    def _save_progress(self) -> None:
        if not self.source_dir or not self.images or not self.progress_file:
            return
        tmp_file = f"{self.progress_file}.tmp"
        try:
            with open(tmp_file, "w", encoding="utf-8") as f:
                f.write(str(self.current_index))
            os.replace(tmp_file, self.progress_file)
        except OSError:
            if os.path.exists(tmp_file):
                try:
                    os.remove(tmp_file)
                except OSError:
                    pass

    def get_current_folders(self) -> List[str]:
        if not self.images or self.current_index >= len(self.images):
            return []
        current_file = self.images[self.current_index]
        found = []
        for folder in self.known_folders:
            target = os.path.join(self.source_dir, folder, current_file)
            if os.path.exists(target):
                found.append(folder)
        return found

    def copy_current_to(self, raw_folder_name: str) -> Dict[str, Any]:
        with self.lock:
            folder_name = sanitize_folder_name(raw_folder_name)
            if not folder_name:
                return {
                    "success": False,
                    "error": "Numele folderului este invalid sau contine doar caractere interzise."
                }
            if not self.images or self.current_index >= len(self.images):
                return {"success": False, "error": "Nu exista nicio imagine selectata."}

            target_dir = os.path.abspath(os.path.join(self.source_dir, folder_name))

            # Protectie Path Traversal: asigura ca destinatia ramane strict in source_dir
            if not target_dir.startswith(self.source_dir):
                return {"success": False, "error": "Cale nepermisa in afara folderului sursa."}

            try:
                os.makedirs(target_dir, exist_ok=True)
            except OSError as e:
                return {"success": False, "error": f"Nu s-a putut crea folderul: {e}"}

            if folder_name not in self.known_folders:
                self.known_folders.append(folder_name)
                self.known_folders.sort(key=natural_sort_key)

            current_file = self.images[self.current_index]
            src = os.path.join(self.source_dir, current_file)
            dst = os.path.join(target_dir, current_file)

            try:
                if not os.path.exists(dst):
                    shutil.copy2(src, dst)
            except OSError as e:
                return {"success": False, "error": f"Eroare la copierea fisierului: {e}"}

            return {
                "success": True,
                "folder": folder_name,
                "copied_folders": self.get_current_folders(),
                "known_folders": self.known_folders
            }

    def delete_current(self) -> Dict[str, Any]:
        with self.lock:
            if not self.images or self.current_index >= len(self.images):
                return {"success": False, "error": "Nu exista nicio imagine de sters."}

            current_file = self.images[self.current_index]
            src = os.path.join(self.source_dir, current_file)

            try:
                if os.path.exists(src):
                    os.remove(src)
            except OSError as e:
                return {"success": False, "error": f"Nu s-a putut sterge fisierul ({e})."}

            # Curatare din subfolderele in care fusese deja copiata in sesiunea curenta
            for folder in self.known_folders:
                sub_copy = os.path.join(self.source_dir, folder, current_file)
                if os.path.exists(sub_copy):
                    try:
                        os.remove(sub_copy)
                    except OSError:
                        pass

            # Eliminare din lista de lucru
            self.images.pop(self.current_index)
            if self.current_index >= len(self.images) and len(self.images) > 0:
                self.current_index = len(self.images) - 1

            self._save_progress()
            return {
                "success": True,
                "deleted_file": current_file,
                "state": self.to_dict()
            }

    def navigate(self, delta: int = 0, to_index: Optional[int] = None) -> Dict[str, Any]:
        with self.lock:
            if not self.images:
                return self.to_dict()
            if to_index is not None:
                self.current_index = max(0, min(len(self.images) - 1, to_index))
            else:
                self.current_index = max(0, min(len(self.images) - 1, self.current_index + delta))
            self._save_progress()
            return self.to_dict()

    def to_dict(self) -> Dict[str, Any]:
        total = len(self.images)
        current_file = self.images[self.current_index] if total > 0 and self.current_index < total else ""
        folder_name = os.path.basename(self.source_dir) if self.source_dir else ""
        return {
            "source_dir": self.source_dir,
            "folder_name": folder_name,
            "total": total,
            "current_index": self.current_index,
            "current_file": current_file,
            "copied_folders": self.get_current_folders(),
            "known_folders": self.known_folders
        }


# Instanta globala
state = SorterState()

class SorterHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path in ("/", "/index.html"):
            content = get_index_html()
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.send_header("Content-length", str(len(content)))
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(content)
            return

        if path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return

        if path == "/api/state":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            with state.lock:
                data = json.dumps(state.to_dict()).encode("utf-8")
            self.wfile.write(data)
            return

        if path.startswith("/image/"):
            try:
                parts = path.strip("/").split("/")
                if len(parts) < 2 or not parts[1].isdigit():
                    self.send_error(400, "Index invalid")
                    return

                idx = int(parts[1])
                with state.lock:
                    if 0 <= idx < len(state.images) and state.source_dir:
                        filename = state.images[idx]
                        filepath = os.path.abspath(os.path.join(state.source_dir, filename))
                    else:
                        self.send_error(404, "Imagine negasita")
                        return

                # Protectie Path Traversal
                if not filepath.startswith(state.source_dir) or not os.path.isfile(filepath):
                    self.send_error(403, "Acces interzis")
                    return

                mime, _ = mimetypes.guess_type(filepath)
                if not mime:
                    mime = "image/jpeg"

                file_size = os.path.getsize(filepath)

                self.send_response(200)
                self.send_header("Content-type", mime)
                self.send_header("Content-length", str(file_size))
                self.send_header("Cache-Control", "public, max-age=1800")
                self.end_headers()

                # Streaming in bucati de 64KB pentru eficienta memoriei RAM
                with open(filepath, "rb") as f:
                    shutil.copyfileobj(f, self.wfile, length=64 * 1024)
                return

            except (BrokenPipeError, ConnectionResetError):
                # Clientul a navigat mai departe inainte ca imaginea sa fie trimisa complet
                return
            except Exception as e:
                try:
                    self.send_error(500, str(e))
                except Exception:
                    pass
                return

        self.send_error(404, "Resursa negasita")

    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length > 0 else b"{}"
        try:
            data = json.loads(body.decode("utf-8")) if body else {}
        except Exception:
            data = {}

        if parsed.path == "/api/choose_dir":
            chosen = choose_folder_native()
            with state.lock:
                if chosen:
                    state.set_directory(chosen)
                    save_last_dir(chosen)
                res = state.to_dict()
            self._send_json(res)
            return

        if parsed.path == "/api/copy":
            folder = data.get("folder", "")
            with state.lock:
                res = state.copy_current_to(folder)
            self._send_json(res)
            return

        if parsed.path == "/api/delete":
            with state.lock:
                res = state.delete_current()
            self._send_json(res)
            return

        if parsed.path == "/api/navigate":
            delta = data.get("delta", 0)
            to_idx = data.get("to_index", None)
            with state.lock:
                res = state.navigate(delta=delta, to_index=to_idx)
            self._send_json(res)
            return

        self.send_error(404, "Endpoint necunoscut")

    def _send_json(self, data: dict):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))


class ReusableThreadingServer(ThreadingHTTPServer):
    allow_reuse_address = True
    daemon_threads = True


def find_available_port(start_port: int = 8765, max_tries: int = 25) -> int:
    """Gaseste un port liber pentru a evita crash-ul 'Address already in use'."""
    for p in range(start_port, start_port + max_tries):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                s.bind(("127.0.0.1", p))
                return p
            except OSError:
                continue
    return start_port


def run_server(port: int = 8765):
    assigned_port = find_available_port(port)
    server = ReusableThreadingServer(("127.0.0.1", assigned_port), SorterHandler)
    url = f"http://127.0.0.1:{assigned_port}"

    print("\n" + "=" * 60)
    print("  Wedding Photo Sorter")
    if state.source_dir:
        print(f"  Folder activ: {state.source_dir}")
        print(f"  Imagini gasite: {len(state.images)}")
    else:
        print("  Folder activ: (niciun folder selectat inca)")
        print("  Apasa butonul din browser pentru a alege folderul!")
    print(f"  Interfata web activa la: {url}")
    print("  Apasa CTRL+C in terminal pentru a opri oricand.")
    print("=" * 60 + "\n")

    threading.Timer(0.8, lambda: webbrowser.open(url)).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nProgramul a fost oprit curat. Progresul a fost salvat!")
    finally:
        server.server_close()

if __name__ == "__main__":
    initial_port = 8765
    target_dir = ""

    for arg in sys.argv[1:]:
        if arg.isdigit():
            initial_port = int(arg)
        elif os.path.isdir(arg):
            target_dir = os.path.abspath(arg)

    if target_dir:
        state.set_directory(target_dir)
        save_last_dir(target_dir)
    else:
        last = load_last_dir()
        if last:
            state.set_directory(last)

    run_server(initial_port)
