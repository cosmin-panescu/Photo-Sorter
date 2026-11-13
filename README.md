# 📸 Photo Sorter & Organizer

> **O aplicație ultra-rapidă, sigură și intuitivă pentru sortarea și organizarea oricărei colecții mari de fotografii (vacanțe, evenimente, ședințe foto, arhive de familie, portofolii sau proiecte personale) în doar câteva minute, direct de pe tastatură.**

---

## 🚀 Descărcare & Pornire Rapidă (Quick Start)

Nu ai nevoie de instalări complicate, baze de date sau biblioteci suplimentare (`pip`). Ai nevoie doar de **Python 3** (preinstalat pe Mac, gratuit din Microsoft Store pe Windows).

Alege metoda preferată de descărcare:

### Metoda 1: Prin Git (Recomandat — doar 3 comenzi)

Deschide **Terminal** (pe Mac) sau **Command Prompt / PowerShell** (pe Windows) și rulează:

```bash
# 1. Clonează proiectul pe calculatorul tău
git clone https://github.com/cosmin-panescu/Photo-Sorter.git

# 2. Navighează în folderul proiectului
cd Photo-Sorter

# 3. Pornește aplicația
python3 sort_photos.py   # pe macOS / Linux
python sort_photos.py    # pe Windows
```

---

### Metoda 2: Fără Git (Descărcare directă ca fișier ZIP)

Dacă nu ai Git instalat sau preferi o descărcare clasică:
1. Apasă pe butonul verde **`Code`** din partea de sus a paginii de GitHub, apoi dă click pe **`Download ZIP`**.
2. Dezarhivează fișierul descărcat pe Desktop (vei obține folderul `Photo-Sorter-main`).
3. Deschide Terminalul / Command Prompt în acel folder:
   - **Pe Mac:** tastează `cd ~/Desktop/Photo-Sorter-main && python3 sort_photos.py`
   - **Pe Windows:** intră în folder, dă click dreapta și alege *„Open in Terminal”*, apoi scrie `python sort_photos.py`

🎉 **Gata!** Browserul tău (Safari, Chrome, Edge sau Firefox) se va deschide automat la adresa `http://127.0.0.1:8765`.

---

## 🎯 Ce face această aplicație?

Dacă ai un folder cu sute sau mii de fotografii (2.000 – 10.000+ de fișiere) și vrei să le sortezi pe categorii, persoane, locații sau teme, organizarea manuală clasică prin *drag & drop* de la mouse durează ore sau zile întregi.

**Photo Sorter & Organizer simplifică totul:**
1. Îți afișează fotografiile una câte una, la rezoluție maximă, direct în browser.
2. Tu doar tastezi numele categoriei sau al folderului dorit (ex: `Vacanță Grecia`, `Familie`, `Portrete`, `Peisaje`, `De Editat`, `Top 100`) și apeși **Enter**. Fotografia este copiată automat în acel folder.
3. Apeși săgeata dreaptă `→` pentru următoarea poză.
4. Dacă o poză este mișcată, dublată sau nereușită, o poți șterge definitiv de pe disc cu o singură tastă.
5. **Nu pierzi niciodată progresul:** poți închide programul oricând; data viitoare când îl deschizi, continuă exact de la poza la care ai rămas!

---

## 🌟 De ce este atât de utilă?

- 🔒 **100% Sigur și Confidențial:** Totul rulează local, pe calculatorul tău, complet offline. Nicio fotografie nu părăsește dispozitivul tău.
- 🛡️ **Păstrează fotografiile originale intacte:** Imaginile sunt doar **copiate** în folderele nou create. Metadatele originale (data, ora, rezoluția aparatului foto, setările EXIF) rămân neatinse.
- ⚡ **Zero dependențe externe:** Funcționează exclusiv cu biblioteca standard din Python 3.
- 💻 **Cross-Platform nativ:** Dialoguri native de sistem (Finder pe macOS, Windows Explorer pe Windows).
- 🚀 **Performanță ridicată:** Încarcă instantaneu fotografii mari de 30–50 MB fără să consume memoria RAM (streaming în bucăți de 64 KB).

---

## 📖 Ghid de utilizare pas cu pas

### Pasul 1: Selectarea folderului cu fotografii

1. La deschiderea aplicației în browser, vei vedea în mijloc butonul:
   > **`📂 Alege folder cu poze`**
2. Dă click pe el. Se va deschide fereastra nativă (**Finder** pe Mac sau **Windows Explorer** pe Windows).
3. Alege folderul în care se află fotografiile și apasă **Open / Selectează folderul**.
4. Prima poză va apărea imediat pe ecran!

> [!NOTE]
> Aplicația reține automat ultimul folder ales. Dacă închizi programul și îl repornești, acesta își amintește automat unde ai rămas.

---

### Pasul 2: Sortarea fotografiilor în foldere

1. Privește fotografia afișată pe ecran.
2. În caseta de jos, tastează numele folderului în care vrei să ajungă poza (de exemplu: `Familie`, `Portrete`, `Peisaje`, `De Editat`, `Top 100`).
3. Apasă tasta **`Enter`**.
   - Poza curentă va fi copiată instantaneu într-un folder cu acel nume (folderul este creat automat chiar în folderul tău cu poze).
   - Vei vedea o etichetă verde care confirmă: `✓ Copiată în: Familie`.
4. **O poză aparține mai multor categorii?** Nicio problemă! Poți tasta imediat alt nume (ex: `Favorit`) și apeși din nou **Enter**. Aceeași poză va fi copiată și în al doilea folder!
5. **Butoane rapide:** Pe măsură ce creezi foldere, ele apar ca butoane rapide deasupra casetei de text. Data viitoare când vrei să trimiți o poză în același folder, poți da click direct pe butonul lui!

---

### Pasul 3: Navigarea între fotografii

- Apasă **`Săgeată Dreapta (→)`** pentru a trece la poza următoare.
- Apasă **`Săgeată Stânga (←)`** pentru a te întoarce la poza anterioară.
- *(Poți folosi și butoanele mari cu săgeți `‹` și `›` care plutesc pe marginile imaginii).*

---

### Pasul 4: Ștergerea fotografiilor nereușite

Dacă dai peste o fotografie neclară, mișcată, dublură sau un cadru ratat pe care nu vrei să îl păstrezi deloc:
- **Pe Mac:** Apasă **`Command + Backspace`** (adică tasta `⌘` + tasta `delete`).
- **Pe Windows:** Apasă tasta **`Delete`** (Del).
- *(Sau dă click pe butonul roșu **`🗑️ Șterge poza`** din partea de jos).*

Poza va fi ștearsă definitiv de pe disc (inclusiv din eventualele foldere în care o copiaseși mai devreme), iar pe ecran va apărea imediat poza următoare.

---

### Pasul 5: Închiderea și reluarea lucrului

- **Vrei să iei o pauză?** Pur și simplu închide fila din browser și oprește Terminalul cu **`Ctrl + C`**.
- **Când vrei să continui:** Pornește din nou scriptul. Acesta își amintește automat exact la ce poză ai rămas (ex: *Poza 540 din 3.200*) și ce foldere ai creat deja, ca să continui fără să o iei de la capăt!

---

## ⌨️ Tabel recapitulativ: Comenzi rapide

| Ce vrei să faci? | Pe Mac (Apple) | Pe Windows / Linux |
| :--- | :--- | :--- |
| **Copiază poza în folder** | Scrie numele + <kbd>Enter</kbd> | Scrie numele + <kbd>Enter</kbd> |
| **Treci la poza următoare** | <kbd>→</kbd> (Săgeată Dreapta) | <kbd>→</kbd> (Săgeată Dreapta) |
| **Mergi la poza anterioară** | <kbd>←</kbd> (Săgeată Stânga) | <kbd>←</kbd> (Săgeată Stânga) |
| **Șterge textul tastat greșit** | <kbd>ESC</kbd> | <kbd>ESC</kbd> |
| **Șterge poza definitiv (de tot)** | <kbd>⌘ Command</kbd> + <kbd>⌫ Backspace</kbd> | <kbd>Delete</kbd> |
| **Alege alt folder cu poze** | Click pe **📁 Alege alt folder** | Click pe **📁 Alege alt folder** |

---

## ❓ Întrebări Frecvente (FAQ)

### 1. Se modifică sau se strică pozele mele originale?
**Nu.** Toate fotografiile originale rămân exact cum au fost create de cameră sau telefon. La sortare, fișierele sunt doar **copiate** în folderele respective. Singura excepție este dacă apeși intenționat pe comanda de ștergere definitivă (`Delete` / `⌘⌫`).

### 2. Unde se creează folderele noi?
Toate folderele (ex: `Familie`, `Vacanță`, `Portrete`) sunt create automat **chiar în interiorul folderului principal cu poze** pe care l-ai selectat.

### 3. Ce formate de imagini sunt acceptate?
Aplicația recunoaște automat toate formatele foto uzuale:
- `.jpg` / `.jpeg`
- `.png`
- `.webp`
- `.heic` (formatul standard de pe iPhone)
- `.bmp`, `.tiff`

### 4. Ce fac dacă portul 8765 este ocupat?
Nu trebuie să faci nimic! Aplicația detectează automat porturile libere și trece singură la `8766`, `8767` etc., fără erori.

---

## 📁 Structura fișierelor proiectului

```text
├── sort_photos.py   # Serverul local Python (gestionează fișierele, discul și sistemul)
├── index.html       # Interfața vizuală din browser (design modern, rapid, responsive)
├── .gitignore       # Instrucțiuni pentru Git (evită urcarea fișierelor temporare)
└── README.md        # Ghidul complet pe care îl citești acum
```

---

## 💡 Cerințe de sistem

- Orice calculator cu **macOS** (10.13+) sau **Windows** (10 sau 11).
- **Python 3** instalat (pe Mac este deja prezent; pe Windows se poate instala gratuit din Microsoft Store sau de pe [python.org](https://www.python.org)).
- Orice browser web modern (**Safari**, **Google Chrome**, **Microsoft Edge**, **Mozilla Firefox**).
