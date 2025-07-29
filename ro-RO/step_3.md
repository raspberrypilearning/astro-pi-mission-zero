## Afișează o imagine

Matricea LED a Astro Pi poate afișa culori. În acest pas, vei afișa imagini din natură pe matricea LED a Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
O <span style="color: #0faeb0">**matrice LED**</span> este o grilă de LED-uri care poate fi controlată individual sau de un grup pentru a crea diferite efecte de iluminat. Matricea LED de pe Sense HAT are 64 de LED-uri afișate într-o grilă de 8 x 8. LED-urile pot fi programate pentru a produce o gamă largă de culori.
</p>

![O captură de ecran a ferestrei de emulator care arată Unitatea de zbor cu matricea LED care afișează o poză a unei flori.](images/fu-pic.png)

--- task ---

Deschide proiectul [Mission Zero starter](https://missions.astro-pi.org/ro/mz/code_submissions/){:target="_blank"}.

Vei vedea că au fost adăugate automat pentru tine câteva linii de cod.

Acest cod se conectează la Astro Pi, se asigură că afișajul LED al lui Astro Pi este afișat corect și setează senzorul de culoare. Lasă codul acolo, pentru că vei avea nevoie de el.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Importă bibliotecile
from sense_hat import SenseHat from time import sleep

# Configurează Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Configurează senzorul de culoare
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![O captură de ecran a emulatorului Sense HAT cu linii de cod de început afișate în panoul din stânga.](images/sense-hat-emulator3.png)

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
title: Fish
---

![A grid with 8 x 8 squares showing a fish.](images/fish.png)

Created by team chalka, Poland

```python
z = (153, 50, 204) # DarkOrchid
q = (255, 255, 0) # Yellow
d = (51, 153, 255) # blue
c = (0, 0, 0) # Black

image = [
d, d, z, d, d, d, d, d,
d, d, d, z, z, d, d, d,
z, d, q, q, q, q, d, d,
z, z, q, q, q, c, q, d,
z, z, z, q, q, q, q, d,
z, z, q, q, q, q, q, d,
z, d, q, z, z, q, d, d,
d, d, d, z, d, d, d, d]

```

--- /collapse ---


--- collapse ---

---
title: Walrus
---

![A grid with 8 x 8 squares showing a walrus.](images/walrus.png)

Created by team Walrus, Finland

```python
h = (0, 255, 255) # Cyan
c = (0, 0, 0) # Black
s = (139, 69, 19) # SaddleBrown
a = (255, 255, 255) # White
r = (184, 134, 11) # DarkGoldenrod

image = [
h, h, h, h, h, h, h, h,
h, h, s, s, s, h, h, h,
h, s, s, s, s, s, h, h,
h, s, c, s, c, s, s, s,
h, r, r, r, r, r, s, s,
h, h, a, s, a, s, s, s,
h, h, a, s, a, s, s, s,
r, r, s, s, s, s, s, s]

```

--- /collapse ---

--- collapse ---
---
title: Paxi
---

![A grid with 8 x 8 squares showing Paxi.](images/paxi.png)

Created by team tony_pi, Italy

```python
v = (255, 0, 0) # Red
m = (34, 139, 34) # ForestGreen
c = (0, 0, 0) # Black 
e = (100, 149, 237) # CornflowerBlue
l = (0, 255, 0) # Green

image = [
    c, v, m, c, c, m, v, c,
    c, c, v, v, v, v, c, c,
    c, v, c, e, l, e, v, c,
    c, v, c, l, l, l, v, c,
    c, v, c, l, c, l, v, c,
    c, c, v, v, v, v, c, c,
    c, c, l, c, c, l, c, c,
    c, m, m, c, c, m, m, c]

```

--- /collapse ---


--- collapse ---
---
title: Dog
---

![A grid with 8 x 8 squares showing a dog head.](images/dog.png)

Created by team ptpr_07, Spain

```python

c = (0, 0, 0) # Black
r = (184, 134, 11) # DarkGoldenrod
s = (139, 69, 19) # SaddleBrown
y = (255, 20, 147) # DeepPink

image = [
    c, r, r, c, c, r, r, c,
    c, r, s, s, s, s, r, c,
    c, r, c, s, s, c, r, c,
    c, s, s, s, s, s, s, c,
    c, s, s, s, s, s, s, c,
    c, s, s, c, c, s, s, c,
    c, c, s, y, y, s, c, c,
    c, c, c, y, y, c, c, c]


```

--- /collapse ---

--- collapse ---
---
title: Chameleon
---

![A grid with 8 x 8 squares showing a rainbow-coloured chameleon.](images/chameleon.png)

Created by team The_ETs, United Kingdom

```python

c = (0, 0, 0) # Black
s = (139, 69, 19) # SaddleBrown
a = (255, 255, 255) # White
v = (255, 0, 0) # Red
t = (255, 140, 0) # DarkOrange
q = (255, 255, 0) # Yellow
m = (34, 139, 34) # ForestGreen
h = (0, 255, 255) # Cyan
z = (153, 50, 204) # DarkOrchid
y = (255, 20, 147) # DeepPink

image = [
    a, a, v, v, t, a, a, a,
    a, v, v, t, t, q, a, a,
    v, c, t, t, q, q, m, a,
    v, t, t, q, q, m, m, h,
    s, s, q, s, s, m, s, h,
    a, a, a, a, a, a, a, z,
    a, a, a, a, y, a, a, z,
    a, a, a, a, a, y, z, a]

```

--- /collapse ---

--- collapse ---
---
title: Kite
---

![A grid with 8 x 8 squares showing a kite.](images/kite.png)

Created by team Val, Greece

```python

c = (0, 0, 0) # Black
m = (34, 139, 34) # ForestGreen
v = (255, 0, 0) # Red
q = (255, 255, 0) # Yellow
e = (0, 0, 205) # MediumBlue
h = (0, 255, 255) # Cyan

image = [
    h, h, h, h, h, h, h, h, 
    h, h, h, e, e, v, v, h, 
    h, h, h, e, e, v, v, h, 
    h, h, h, q, q, m, m, h, 
    h, h, h, q, q, m, m, h,
    h, h, c, h, h, h, h, h, 
    h, c, h, h, h, h, h, h, 
    c, h, h, h, h, h, h, h]

```

--- /collapse ---

--- collapse ---
---
title: Chicken
---

![A grid with 8 x 8 squares showing a chicken.](images/chicken.png)

Created by team Slepicky, Czechia

```python

v = (255, 0, 0) # Red
c = (0, 0, 0) # Black
b = (105, 105, 105) # DimGray
q = (255, 255, 0) # Yellow
r = (184, 134, 11) # DarkGoldenrod

image =  [
    c, c, v, v, v, c, c, c,
    c, v, b, b, r, c, c, r,
    c, b, c, b, b, c, r, b,
    q, r, b, b, b, b, b, r,
    c, v, b, b, b, b, r, b,
    c, v, b, r, r, r, b, r,
    c, c, c, r, b, q, r, c,
    c, c, c, c, q, q, c, c]

```

--- /collapse ---

--- /task ---

--- task ---

**Find:** the line that says `# Display the image` and add a line of code to display your image on the LED matrix:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 18, 19
---
z = (153, 50, 204) # DarkOrchid q = (255, 255, 0) # Yellow d = (51, 153, 255) # blue c = (0, 0, 0) # Black

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

# Display the image
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

- Verifică dacă `sense.set_pixels(imagine)` nu este indentat

--- /task ---


--- task ---

**Salvează-ți progresul**

Acum că ai afișat o imagine, poți salva programul tău în proiectul Mission Starter introducând numele echipei tale, numele membrilor echipei şi codul de clasă care vi s-a dat. Poți reîncărca programul tău pe orice dispozitiv cu o conexiune la internet prin introducerea numelui echipei și a codului de clasă.

![The Mission Zero Save button.](images/mz_savebutton_v2.png)

--- /task --- 
