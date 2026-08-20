## Afișează o imagine

Imaginea pe care o afișezi va fi formată din 64 de pătrate colorate numite **pixeli**. Pixelii sunt aranjați într-o grilă de 8 x 8. Fiecare pixel poate avea o culoare diferită. Alegând culorile cu atenție, poți crea o imagine. Iată un exemplu de balenă făcută folosind diferite nuanţe de albastru pe un fundal negru.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
O <span style="color: #0faeb0">**matrice LED**</span> este o grilă de LED-uri care poate fi controlată individual sau de un grup pentru a crea diferite efecte de iluminat. Matricea LED de pe Sense HAT are 64 de LED-uri afișate într-o grilă de 8 x 8. LED-urile pot fi programate pentru a produce o gamă largă de culori.
</p>

![o imagine de 8x8 a unei balene cu litere etichetând culori diferite](images/whale.png)

Observați că fiecare pătrat este etichetat cu un cod care reprezintă o anumită culoare. În această imagine se folosesc 3 culori:
+ c = Negru
+ f = Albastru oceanic
+ g = Albastru ceresc


--- task ---

Deschide proiectul [Mission Zero starter](https://missions.astro-pi.org/ro/mz/code_submissions/){:target="_blank"}.

Vei vedea că au fost adăugate automat pentru tine câteva linii de cod.

Acest cod se conectează la Astro Pi, se asigură că afișajul LED al lui Astro Pi este afișat corect și setează senzorul de culoare. Lasă codul acolo, pentru că vei avea nevoie de el.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
---
# Importă bibliotecile
from sense_hat import SenseHat
from time import sleep

# Configurează Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Configurează senzorul de culoare
sense.color.gain = 60 # Setează sensibilitatea senzorului
sense.color.integration_cycles = 64 # Intervalul la care va avea loc citirea

--- /code ---

![O captură de ecran a emulatorului Sense HAT cu linii de cod de început afișate în panoul din stânga.](images/sense-hat-emulator3.png)

--- /task ---

### Culori RGB

Culorile pot fi create folosind diferite proporții de roșu, verde și albastru. Poți afla mai multe despre culorile RGB aici:

![Trei cursoare care demonstrează valorile culorilor RGB](images/rgbsliders.gif)

Matricea LED este o grilă de 8 x 8. Fiecare LED din grilă poate fi setat la o culoare diferită. Putem folosi literele de la A la z ca nume de variabile pentru a reprezenta 24 de culori diferite. Fiecare culoare are o valoare pentru roşu, verde şi albastru.

--- collapse ---

---
title: Lista Variabilelor de Culoare
---

![O grilă de 24 de pătrate colorate, fiecare etichetat cu o literă diferită a alfabetului](images/palette.png)

```python
a = (255, 255, 255) # Alb
b = (171, 171, 171) # Gri
c = (0, 0, 0) # Negru
d = (25, 25, 113) # Albastru marin
e = (0, 0, 255) # Albastru pur
f = (36, 128, 200) # Albastru oceanic
g = (0, 204, 255) # Albastru ceresc
h = (86, 255, 255) # Cian electric
j = (0, 255, 0) # Verde pur
k = (46, 139, 33) # Verde frunză
l = (57, 97, 17) # Verde măsliniu
m = (30, 65, 6) # Verde pădure
n = (126, 88, 25) # Maro pământ
o = (179, 96, 65) # Maro teracotă
p = (180, 34, 34) # Cărămiziu
q = (255, 0, 0) # Roșu pur
r = (232, 118, 5) # Portocaliu
s = (241, 231, 100) # Galben pal
t = (255, 255, 0) # Galben pur
u = (255, 209, 209) # Roz pal
v = (255, 177, 177) # Roz îmbujorat
w = (249, 169, 255) # Roz deschis
y = (248, 97, 255) # Purpuriu
z = (220, 53, 232) # Mov

```

--- /collapse ---

### Alege o imagine

--- task ---

**Alege:** Alege o imagine pentru a fi afișată din opțiunile de mai jos. Python stochează informația pentru o imagine într-o listă. Codul pentru fiecare imagine include variabilele de culoare folosite şi lista.

Va trebui să **copiezi** tot codul pentru imaginea aleasă, apoi **lipește-l** în proiect sub linia care spune `# Adăugă variabilele de culoare și imaginea`.

--- collapse ---

---
title: Balenă
---

![O grilă cu 8 x 8 pătrate ce arată o balenă.](images/whale.png)

Creat de Team Naicom, Italia

```python
c = (0, 0, 0)       # Negru
f = (36, 128, 200)  # Albastru oceanic
g = (0, 204, 255)   # Albastru ceresc

imagine = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, a,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

```

--- /collapse ---


--- collapse ---

---
title: Lemon
---

![O grilă cu 8 x 8 pătrate ce arată o lămâie.](images/lemon.png)

Creat de echipa g4lemoni, Grecia

```python
c = (0, 0, 0)       # Negru
k = (46, 139, 33)   # Verde frunză
t = (255, 255, 0)   # Galben pur

imagine = [
c, c, c, k, k, c, c, c,
c, c, k, c, k, c, c, c,
c, k, c, t, t, c, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, c, t, t, c, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Porc
---

![O grilă cu 8 x 8 pătrate ce arată un porc.](images/pig.png)

Creat de Gary, Marea Britanie

```python
a = (255, 255, 255) # Alb
v = (255, 177, 177) # Roz îmbujorat
y = (248, 97, 255)  # Mov
o = (179, 96, 65)   # Maro teracotă
c = (0, 0, 0)       # Negru

imagine = [
a, a, y, a, a, y, a, a,
a, y, y, y, y, y, y, a,
a, y, c, y, c, y, y, y,
v, v, v, v, v, y, y, y,
v, o, v, o, v, y, y, y,
v, v, v, v, v, y, y, y,
a, y, y, y, y, y, y, y,
a, a, y, a, a, a, y, a]

```

--- /collapse ---


--- collapse ---
---
title: Furtună
---

![O grilă cu 8 x 8 pătrate ce arată un nor de furtună.](images/storm.png)

Creat de echipa hop2p023, Spania

```python

c = (0, 0, 0)       # Negru
f = (36, 128, 200)  # Albastru oceanic
g = (0, 204, 255)   # Albastru ceresc
t = (255, 255, 0)   # Galben pur

imagine = [
c, c, c, c, c, c, c, c,
c, c, f, f, f, f, c, c,
c, f, f, f, f, f, f, c,
c, g, c, g, t, g, c, c,
c, c, c, t, t, c, c, c,
c, c, t, t, c, c, c, c,
c, c, g, c, c, c, c, g,
c, g, c, c, c, c, c, c]


```

--- /collapse ---

--- collapse ---
---
title: Rață
---

![O grilă cu 8 x 8 pătrate ce arată o rață.](images/duck.png)

Creat de Peter, Irlanda

```python

c = (0, 0, 0) # Negru
l = (57, 97, 17)    # Verde măsliniu
m = (30, 65, 6)     # Verde Pădure
r = (232, 118, 5)   # Portocaliu
a = (255, 255, 255) # Alb
b = (171, 171, 171) # Gri

imagine = [
c, l, l, c, c, c, c, c,
r, r, m, c, c, c, c, c,
c, l, l, c, c, c, c, c,
c, a, a, l, a, a, c, c,
c, l, l, a, a, a, b, a,
c, a, a, b, b, b, a, a,
c, c, a, a, a, a, c, c,
c, c, c, r, c, r, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Broască
---

![O grilă cu 8 x 8 pătrate ce arată o broască.](images/frog.png)

Creat de echipa Jmeno, Republica Cehă

```python

a = (255, 255, 255) # Alb
b = (171, 171, 171) # Gri
c = (0, 0, 0)       # Negru
q = (255, 0, 0)     # Roșu pur
j = (0, 255, 0)     # Verde pur
k = (46, 139, 33)   # Verde frunză
n = (126, 88, 25)   # Maro Pământ

imagine = [
a, a, a, a, a, a, a, a,
a, a, a, a, a, b, a, b,
a, a, a, a, a, a, c, a,
a, a, c, a, c, a, q, a,
a, a, j, j, j, q, a, a,
a, j, j, k, q, a, a, a,
j, k, j, k, k, a, a, a,
k, k, k, j, k, n, n, n]

```

--- /collapse ---

--- collapse ---
---
title: Copac înflorit
---

![O grilă cu 8 x 8 pătrate ce arată un copac înflorit.](images/blossom.png)

Creat de echipa Zssh14, Slovacia

```python

t = (255, 255, 0)   # Galben pur
g = (0, 204, 255)   # Albastru ceresc
w = (249, 169, 255) # Roz deschis
y = (248, 97, 255)  # Mov
z = (220, 53, 232)  # Violet
n = (126, 88, 25)   # Maro Pământ
o = (179, 96, 65)   # Maro teracotă
k = (46, 139, 33)   # Verde frunză

imagine =  [
t, g, g, w, w, y, g, g,
g, g, w, w, y, y, z, g,
g, w, y, z, y, z, z, z,
w, y, z, z, g, n, w, g,
g, g, o, o, n, w, y, z,
g, g, g, g, n, g, g, g,
g, g, g, o, n, n, g, g,
k, k, o, n, n, n, k, k]

```

--- /collapse ---

--- /task ---

--- task ---

**Găsește:** linia care spune `# Afișează imaginea` și adaugă o linie de cod pentru a afișa imaginea ta pe matricea LED:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Negru
f = (36, 128, 200)  # Albastru oceanic
g = (0, 204, 255)   # Albastru ceresc

imagine = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, a,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

# Afișează imaginea
sense.set_pixels(imagine)

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

![Butonul de salvare Mission Zero.](images/mz_savebutton_v2.png)

--- /task --- 

