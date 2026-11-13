# 📸 Wedding & Event Photo Sorter

> **O aplicație simplă, rapidă și sigură pentru oricine dorește să organizeze mii de fotografii de la evenimente (nunți, botezuri, aniversări, vacanțe) în doar câteva minute, direct de pe tastatură.**

---

## 🎯 Ce face această aplicație?

Dacă ai primit un folder uriaș cu poze de la nuntă sau un eveniment (2.000 – 5.000+ de fotografii) și vrei să le trimiți fiecărui invitat pozele în care apare, sortarea manuală în foldere poate dura zile întregi.

**Photo Sorter simplifică totul:**
1. Îți afișează fotografiile una câte una, la rezoluție maximă, direct în browser.
2. Tu doar tastezi numele persoanei sau al grupului (ex: `Bunici`, `Familie`, `Masa 4`) și apeși **Enter**. Poza este copiată automat în folderul respectiv.
3. Apeși săgeata dreaptă `→` pentru următoarea poză.
4. Dacă o poză este mișcată sau nereușită, o poți șterge definitiv de pe disc cu o singură tastă.
5. **Nu pierzi niciodată progresul:** poți închide programul oricând; data viitoare când îl deschizi, va continua exact de la poza la care ai rămas!

---

## 🌟 De ce este atât de ușor de folosit?

- 🔒 **100% Sigur și Confidențial:** Totul rulează local, pe calculatorul tău, fără internet. Nicio fotografie nu este urcată pe vreun server extern.
- 🛡️ **Păstrează fotografiile originale intacte:** Imaginile sunt doar **copiate** în folderele nou create. Metadatele originale (data, ora, rezoluția și calitatea aparatului foto) rămân neatinse.
- ⚡ **Zero instalări complicate:** Nu trebuie să instalezi biblioteci externe sau module Python suplimentare (`pip`). Funcționează direct cu Python-ul standard.
- 💻 **Cross-Platform:** Funcționează identic pe **macOS** și pe **Windows** (și Linux).
- 🚀 **Performanță maximă:** Deschide instantaneu fotografii mari de 30–50 MB fără să blocheze memoria calculatorului.

---

## 📖 Ghid de utilizare pas cu pas (Pentru oricine)

Nu ai nevoie de experiență tehnică pentru a folosi acest program. Iată pașii simpli:

### Pasul 1: Pornirea programului

#### 🍎 Pe Mac:
1. Apasă **`Cmd + Space`** (Spotlight), tastează **Terminal** și apasă **Enter**.
2. Scrie comanda de mai jos și apasă **Enter**:
   ```bash
   cd "~/Desktop/images to folders" && python3 sort_photos.py
   ```
*(Se va deschide automat browserul tău implicit: Safari sau Chrome).*

#### 🪟 Pe Windows:
1. Apasă tasta **`Windows`**, tastează **cmd** (sau PowerShell) și apasă **Enter**.
2. Scrie comanda de mai jos și apasă **Enter**:
   ```cmd
   python sort_photos.py
   ```
*(Se va deschide automat browserul tău implicit: Edge sau Chrome).*

---

### Pasul 2: Selectarea folderului cu poze

1. Când se deschide pagina în browser, vei vedea un buton mare în mijloc:
   > **`📂 Alege folder cu poze`**
2. Dă click pe el. Se va deschide fereastra ta obișnuită de fișiere (**Finder** pe Mac sau **Windows Explorer** pe Windows).
3. Selectează folderul în care se află fotografiile de la eveniment și apasă **Open / Selectează folderul**.
4. Toate fotografiile vor fi încărcate instantaneu și prima poză va apărea pe ecran!

> [!NOTE]
> Programul va ține minte folderul ales! Data viitoare când îl pornești, nu mai trebuie să cauți folderul; îl va deschide automat.

---

### Pasul 3: Sortarea fotografiilor în foldere

1. Privește fotografia afișată pe ecran.
2. În caseta de jos, tastează numele persoanei sau al categoriei (de exemplu: `Mire`, `Nasul`, `Masa 2`, `Prieteni Liceu`).
3. Apasă tasta **`Enter`**.
   - Poza curentă va fi copiată instantaneu într-un folder cu acel nume (folderul este creat automat în interiorul folderului tău cu poze).
   - Vei vedea o etichetă verde care confirmă: `✓ Copiată în: Mire`.
4. **O poză cu mai multe persoane?** Nicio problemă! Poți tasta imediat alt nume (ex: `Mireasa`) și apeși din nou **Enter**. Aceeași poză va fi copiată și în al doilea folder!
5. **Butoane rapide:** Pe măsură ce creezi foldere, ele apar ca butoane rapide deasupra tastaturii. Data viitoare când apare aceeași persoană, poți da click direct pe butonul ei sau doar tastezi primele litere!

---

### Pasul 4: Navigarea între fotografii

- Apasă **`Săgeată Dreapta (→)`** pentru a trece la poza următoare.
- Apasă **`Săgeată Stânga (←)`** pentru a te întoarce la poza anterioară.
- *(Poți folosi și butoanele mari cu săgeți `‹` și `›` care plutesc pe marginile pozei).*

---

### Pasul 5: Ștergerea fotografiilor nereușite

Dacă dai peste o fotografie neclară, mișcată sau cu ochii închiși pe care nu vrei să o păstrezi deloc:
- **Pe Mac:** Apasă **`Command + Backspace`** (adică tasta `⌘` + tasta de ștergere `delete`).
- **Pe Windows:** Apasă tasta **`Delete`** (Del).
- *(Sau dă click pe butonul roșu **`🗑️ Șterge poza`** din partea de jos).*

Poza va fi ștearsă definitiv de pe disc (inclusiv din eventualele foldere în care o copiaseși mai devreme), iar pe ecran va apărea imediat poza următoare.

---

### Pasul 6: Închiderea și reluarea lucrului

- **Ai obosit sau vrei să iei o pauză?** Pur și simplu închide fila din browser și oprește Terminalul cu **`Ctrl + C`**.
- **Când vrei să continui:** Pornește din nou scriptul. Acesta își amintește automat exact la ce poză ai rămas (ex: *Poza 412 din 2.850*) și ce foldere ai creat deja, ca să continui fără să o iei de la capăt!

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
**Nu.** Toate fotografiile originale rămân exact cum au fost descărcate din aparatul foto. La sortare, fișierele sunt doar **duplicate/copiate** în folderele respective. Singura excepție este dacă apeși intenționat pe butonul de ștergere definitivă (`Delete` / `⌘⌫`).

### 2. Unde se creează folderele cu persoane?
Toate folderele noi (ex: `Mire`, `Nasul`, `Familie`) sunt create automat chiar **în interiorul folderului principal cu poze** pe care l-ai selectat. Nu se împrăștie prin calculator.

### 3. Ce formate de imagini sunt acceptate?
Aplicația recunoaște automat cele mai populare formate foto:
- `.jpg` / `.jpeg`
- `.png`
- `.webp`
- `.heic` (formatul standard iPhone)
- `.bmp`, `.tiff`

### 4. Ce fac dacă portul 8765 este ocupat?
Nu trebuie să faci nimic! Aplicația este inteligentă: testează automat porturile libere și trece singură la `8766`, `8767` etc., fără să afișeze erori.

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
