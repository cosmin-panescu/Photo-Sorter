# 📸 Wedding & Event Photo Sorter

Aplicație ultra-rapidă, sigură și ușor de utilizat pentru sortarea și organizarea fotografiilor de la nunți și evenimente (inclusiv galerii mari de 2000–5000+ imagini).

Rulează un server local cu interfață web modernă direct în browser (Safari, Chrome, Edge, Firefox) și comunică nativ cu sistemul de operare.

---

## ✨ Caracteristici principale

- **Zero dependințe externe:** Folosește exclusiv biblioteca standard Python 3. Nu necesită instalare de pachete (`pip`).
- **Cross-Platform nativ (macOS & Windows):**
  - Pe macOS: Deschide automat selectorul nativ **Finder**.
  - Pe Windows: Deschide automat dialogul nativ **Windows Explorer**.
- **Arhitectură modulară:** Backend Python robust + Frontend curat (`index.html`).
- **Streaming eficient (Chunked 64KB):** Încarcă și afișează instantaneu fotografii de înaltă rezoluție (20–50 MB) fără a consuma memoria RAM.
- **Sortare naturală a fișierelor:** `IMG_2.jpg` vine înaintea lui `IMG_10.jpg`, identic cu managerul de fișiere din sistem.
- **Salvare automată atomică:** Progresul tău este salvat în siguranță la fiecare pas. Poți închide oricând și relua de unde ai rămas.
- **Protecție fișiere:** Copiază fotografiile în subfoldere fără a afecta originalele (păstrează metadatele EXIF) și oferă opțiunea de ștergere definitivă la comandă.

---

## ⌨️ Comenzi rapide tastatură

| Acțiune | macOS | Windows / Linux |
| :--- | :--- | :--- |
| **Copiază în folder** | Tastează numele + <kbd>Enter</kbd> | Tastează numele + <kbd>Enter</kbd> |
| **Poza următoare** | <kbd>→</kbd> (Săgeată Dreapta) | <kbd>→</kbd> (Săgeată Dreapta) |
| **Poza anterioară** | <kbd>←</kbd> (Săgeată Stânga) | <kbd>←</kbd> (Săgeată Stânga) |
| **Șterge textul tastat** | <kbd>ESC</kbd> | <kbd>ESC</kbd> |
| **Șterge poza definitiv** | <kbd>⌘</kbd> + <kbd>⌫</kbd> (sau butonul roșu) | <kbd>Delete</kbd> (sau butonul roșu) |

---

## 🚀 Cum se rulează

### Pe macOS:
Deschide aplicația **Terminal** și rulează:
```bash
python3 sort_photos.py
```
*(Poți specifica și calea direct: `python3 sort_photos.py "/cale/catre/poze"`)*

### Pe Windows:
Deschide **Command Prompt** sau **PowerShell** și rulează:
```cmd
python sort_photos.py
```

Aplicația va porni serverul local și va deschide automat interfața în browser la adresa `http://127.0.0.1:8765`.
Dacă portul este ocupat, va căuta automat următorul port liber.

---

## 📂 Structura proiectului

```text
├── sort_photos.py   # Server backend Python (concurent, thread-safe, API)
├── index.html       # Interfață utilizator web (HTML5, CSS3, JavaScript)
├── .gitignore       # Fișiere ignorate de Git (cache, progres temporar)
└── README.md        # Documentația proiectului
```
