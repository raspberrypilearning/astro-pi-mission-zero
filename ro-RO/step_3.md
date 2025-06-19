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
title: Vulpe
---

![O grilă cu 8 x 8 pătrate care arată o față de vulpe.](images/fish.png)

Creat de echipa i_pupi, Italia

```python
c = (0, 0, 0) # Negru
a = (255, 255, 255) # Alb
t = (255, 140, 0) # Portocaliu închis

imagine = [
t, a, t, c, c, t, a, t,
t, a, t, c, c, t, a, t,
t, t, t, t, t, t, t, t,
t, a, c, t, t, c, a, t,
t, t, t, t, t, t, t, t,
a, a, a, c, c, a, a, a,
c, a, a, a, a, a, a, c,
c, c, a, a, a, a, c, c]

```

--- /collapse ---


--- collapse ---

---
title: Elefant
---

![O grilă cu 8 x 8 pătrate care arată un elefant.](images/walrus.png)

Creat de echipa ILiFanT, Finlanda

```python
c = (0, 0, 0) # Negru
b = (105, 105, 105) # Gri închis
a = (255, 255, 255) # Alb

imagine = [
    c, c, c, c, c, c, c, c,
    c, b, b, b, c, c, c, c,
    c, b, c, b, c, c, b, b,
    c, b, c, c, c, b, b, b,
    c, b, b, c, c, b, c, b,
    c, b, b, b, b, b, b, b,
    c, c, b, b, a, b, b, b,
    c, c, c, c, a, b, b, b]

```

--- /collapse ---

--- collapse ---
---
title: Cactus
---

![O grilă cu 8 x 8 pătrate care arată un cactus.](images/paxi.png)

Creat de echipa 6TETHASI, Olanda

```python
a = (255, 255, 255) # Alb
c = (0, 0, 0) # Negru
n = (154, 205, 50) # GalbenVerde
q = (255, 255, 0) # Galben
t = (255, 140, 0) # Portocaliu închis

imagine = [   
  q, q, c, n, c, c, a, c,
  q, c, c, n, c, a, a, a,
  c, n, c, n, c, c, c, c,
  c, n, n, n, c, n, c, c,
  c, a, n, n, n, n, c, c,
  a, a, a, n, c, a, a, a,
  c, c, c, n, a, a, a, c,
  t, t, t, t, t, t, t, t]

```

--- /collapse ---


--- collapse ---
---
title: Crocodil
---

![O grilă cu 8 x 8 pătrate care arată un cap de crocodil.](images/dog.png)

Created by team ptpr_07, Spain
```python

a = (255, 255, 255) # Alb
c = (0, 0, 0) # Negru
f = (25, 25, 112) # Bleumarin
m = (34, 139, 34) # Verde pădure

imagine = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]


```

--- /collapse ---

--- collapse ---
---
title: Curcubeu
---

![A grid with 8 x 8 squares showing a rainbow coloured chameleon.](images/chameleon.png)

Created by team The_ETs, United Kingdom

```python

c = (100, 149, 237) # Floarea de colțAlbastru
a = (255, 255, 255) # Alb
v = (255, 0, 0) # Roșu
t = (255, 140, 0) # Portocaliu închis
q = (255, 255, 0) # Galben
l = (0, 255, 127) # VerdePrimăvară
e = (0, 0, 205) # Albastru mediu

curcubeu = [
  c, c, c, c, c, c, c, c, 
  v, v, v, v, c, c, c, c,
  t, t, t, t, v, v, c, c,
  q, q, q, q, t, v, c, c,
  l, l, l, l, q, t, v, c,
  e, e, e, l, q, t, v, c,
  c, c, e, a, a, a, a, c,
  c, a, a, a, a, a, a, a
]

```

--- /collapse ---

--- collapse ---
---
title: Dragon
---

![A grid with 8 x 8 squares showing a kite.](images/kite.png)

Created by team Val, Greece

```python

b = (105, 105, 105) # GriȘters
c = (0, 0, 0) # Negru
d = (100, 149, 237) # Floarea de colțAlbastru
v = (255, 0, 0) # Roșu
z = (153, 50, 204) # OrhideeÎntunecată

imagine = [
    c, c, v, c, v, c, c, c,
    c, z, z, z, z, v, c, c,
    z, b, z, b, z, c, c, c,
    z, z, z, z, z, v, c, c,
    c, c, d, d, d, c, c, z,
    c, z, d, z, z, z, z, c,
    c, c, d, d, z, c, c, c,
    c, c, z, c, z, c, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Chicken
---

![A grid with 8 x 8 squares showing a Chicken.](images/chicken.png)

Created by team Slepicky, Czech Republic

```python

a = (255, 255, 255) # Alb
c = (0, 0, 0) # Negru
f = (25, 25, 112) # Bleumarin
m = (34, 139, 34) # Verde pădure

imagine = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

# Afișează imaginea 
sense.set_pixels(imagine)

```

--- /collapse ---

--- /task ---

--- task ---

**Găsește:** linia care spune `# Afișează imaginea` și adaugă o linie de cod pentru a afișa imaginea ta pe matricea LED:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 18, 19
---
Imaginea mea nu apare:

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

![Butonul Mission Zero Salvare](images/mz_savebutton_v2.png)

--- /task --- 
