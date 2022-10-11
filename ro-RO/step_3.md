## Afișează un mesaj și alege un nume pentru noile calculatoare Astro Pi

Matricea LED a Astro Pi poate afișa culori. În acest pas, vei afișa imagini din natură pe matricea LED a Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
O <span style="color: #0faeb0">**matrice LED**</span> este o grilă de LED-uri care poate fi controlată individual sau de un grup pentru a crea diferite efecte de iluminat. Matricea LED de pe Sense HAT are 64 de LED-uri afișate într-o grilă de 8 x 8. LED-urile pot fi programate pentru a produce o gamă largă de culori.
</p>

![O captură de ecran a ferestrei de emulator care arată Unitatea de zbor cu matricea LED care afișează o poză a unei flori.](images/fu-pic.png)

--- task ---

Deschide proiectul [Mission Zero starter](http://rpf.io/mzcode){:target="_blank"}.

Vei vedea că au fost adăugate automat pentru tine câteva linii de cod.

Acest cod se conectează la Astro Pi, se asigură că afișajul LED al lui Astro Pi este afișat corect și setează senzorul de culoare. Lasă codul acolo, pentru că vei avea nevoie de el.

--- code ---
---
Adaugă acest rând sub celelalte linii de cod:
title: Ce caractere pot fi folosite?
---
# Importă bibliotecile
from sense_hat import SenseHat from time import sleep

# Configurează Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Configurează senzorul de culoare
Apasă pe butonul **Run** și urmărește cum mesajul `Astro Pi` se derulează pe ecranul LED.

--- /code ---

![O captură de ecran a emulatorului Sense HAT cu linii de cod de început afișate în panoul din stânga.](images/sense-hat-emulator2.png)

--- /task ---

### Culori RGB

Culorile pot fi create folosind diferite proporții de roșu, verde și albastru. Poți afla mai multe despre culorile RGB aici:

[[[generic-theory-simple-colours]]]

Matricea LED este o grilă de 8 x 8. Fiecare LED din grilă poate fi setat la o culoare diferită. Aici este o listă de variabile pentru 24 de culori diferite. Fiecare culoare are o valoare pentru roşu, verde şi albastru:

[[[ambient-colours]]]

### Alege o imagine

--- task ---

**Alege:** Alege o imagine pentru a fi afișată din opțiunile de mai jos. Python stochează informația pentru o imagine într-o listă. Codul pentru fiecare imagine include variabilele de culoare folosite şi lista.

Va trebui să **copiezi** tot codul pentru imaginea aleasă, apoi **lipește-l** în proiect sub linia care spune `# Adăugă variabilele de culoare și imaginea`.

--- collapse ---

---
title: Pui
---

![O grilă cu 8 x 8 pătrate care arată un pui într-un ou.](images/chick.png)

--- code ---
---
Dacă ai vrea să votezi, mesajul tău trebuie să înceapă cu aceste cuvinte, în caz contrar nu vom putea să îți luăm în calcul răspunsul.
line_numbers: false
---
a = (255, 255, 255) # White c = (0, 0, 0) # Black e = (0, 0, 205) # MediumBlue q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange w = (255, 192, 203) # Pink

image = [ c, c, c, q, q, q, c, c, c, c, t, q, e, q, c, c, c, c, c, q, q, q, c, c, c, w, w, w, w, w, w, c, c, w, a, a, a, a, w, c, c, w, a, a, a, a, w, c, c, c, w, a, a, w, c, c, c, c, c, w, w, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Floare
---

![O grilă cu 8 x 8 pătrate care arată o floare roz pe o tulpină verde.](images/flower.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange y = (255, 20, 147) # DeepPink

image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Crab
---

![O grilă cu 8 x 8 pătrate care arată un crab.](images/crab.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
a = (255, 255, 255) # White c = (0, 0, 0) # Black v = (255, 0, 0) # Red

image = [ c, a, a, c, a, a, c, c, c, a, c, c, a, c, c, c, c, v, c, c, v, c, c, c, c, v, c, c, v, c, c, c, v, v, v, v, v, c, v, v, v, v, c, c, v, v, v, c, v, v, v, v, v, c, v, v, v, c, v, c, v, c, c, c]

--- /code ---

--- /collapse ---


--- collapse ---
---
title: Crocodil
---

![O grilă cu 8 x 8 pătrate care arată un cap de crocodil.](images/croc.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
a = (255, 255, 255) # White c = (0, 0, 0) # Black f = (25, 25, 112) # MidnightBlue m = (34, 139, 34) # ForestGreen

image = [ m, m, m, m, m, c, c, c, m, f, m, f, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, a, c, c, c, a, m, m, c, c, c ,c ,c ,c, m, m, c, c, c, a, c, c, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]

--- /code ---


--- /collapse ---

--- collapse ---
---
title: Şarpe
---

![O grilă cu 8 x 8 pătrate care arată un șarpe.](images/snake.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
 c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow v = (255, 0, 0) # Red

image = [ c, c, c, c, c, c, c, m, c, m, m, m, m, m, m, m, c, m, c, c, c, c, c, c, c, m, m, m, m, m, c, c, c, c, c, c, c, m, c, c, q, m, q, m, m, m, c, c, m, m, m, c, c, c, c, c, v, c, c, c, c, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Broască
---

![O grilă cu 8 x 8 pătrate care arată o broască.](images/frog.png)

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start:
line_highlights:
---
c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow v = (255, 0, 0) # Red

image = [ c, m, m, m, c, m, m, m, c, m, q, m, c, m, q, m, m, m, m, m, m, m, m, m, m, v, v, v, v, v, v, v, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, m, m, m, c, m]

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Găsește:** linia care spune `# Afișează imaginea` și adaugă o linie de cod pentru a afișa imaginea ta pe matricea LED:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 12
---
image = [ c, c, c, q, q, q, c, c, c, c, t, q, e, q, c, c, c, c, c, q, q, q, c, c, c, w, w, w, w, w, w, c, c, w, a, a, a, a, w, c, c, w, a, a, a, a, w, c, c, c, w, a, a, w, c, c, c, c, c, w, w, c, c, c]

# Afișează imaginea
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Apasă **Rulează** în partea de jos a editorului, pentru a vedea imaginea afișată pe matricea LED.

--- /task ---

--- task ---

**Debug**

Codul meu are o eroare de sintaxă:

- Verifică dacă codul tău se potrivește cu codul din exemplele de mai sus
- Verifică dacă ai indentat codul din lista ta
- Verifică dacă lista ta este înconjurată de `[` și `]`
- Verifică dacă fiecare variabilă de culoare din listă este separată de virgulă

Imaginea mea nu apare:

- Verifică dacă `sense.set_pixels(image)` nu este indentat

--- /task ---



