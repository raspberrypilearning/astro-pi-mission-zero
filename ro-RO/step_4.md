## Detectează o culoare

În acest pas, vei seta senzorul de culoare și luminozitate. Vei folosi acest senzor pentru a măsura cantitatea de lumină roșie, verde și albastră care ajunge la senzor. Aceste valori vor fi folosite apoi pentru a schimba una dintre culorile din imaginea aleasă.

Asta înseamnă că imaginea se poate schimba în funcție de ceea ce vede senzorul. De exemplu, un astronaut care poartă un tricou albastru ar vedea o versiune diferită a imaginii față de un astronaut care poartă un tricou roșu.

În imaginea balenei pe care am folosit-o în pasul anterior, culoarea de fundal a fost neagră. Am folosit variabila `c` pentru a stoca codul său de culoare RGB:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Folosește senzorul de culoare pentru a schimba una dintre culorile tale.

Sub liniile unde definești culorile, adaugă următorul cod:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4
---
# Detectează o culoare
rgb = sense.color # obține culoarea de la senzor
c = (rgb.red, rgb.green, rgb.blue) # utilizează culoarea de la senzor

--- /code ---

--- /task ---

Acest cod înlocuiește valorile RGB stocate în `c` cu valorile pentru culoarea detectată de către senzor.

Sfat: Dacă nu ai folosit variabila `c` în propria imagine, înlocuiește `c` cu una dintre variabilele de culoare pe care le-ai folosit. Acest lucru va permite senzorului să schimbe culoarea respectivă.

--- task ---

**Test:** Mută glisorul de culori la o culoare aleasă de tine și apoi **execută** codul tău. Culoarea de fundal se va schimba. Repetați acest test din nou cu o nouă culoare.

**Sfat:** Va trebui să apeși pe 'Rulează' de fiecare dată când schimbi culoarea.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Acum ai afișat o imagine și ai detectat o culoare și ai folosit-o în programul tău, iar codul tău este gata de trimitere! 

Poți salva și trimite programul tău folosind formularul de la baza editorului de cod.
  
Totuși, este posibil să vrei să adaugi mai multe imagini la proiect sau să-i dai viață cu animație. Următorii pași arată cum să faci asta.
</p>

## Animează proiectul tău (opțional)

Programul tău Mission Zero poate rula pe Stația Spațială Internațională (ISS) timp de până la 30 de secunde. Poți folosi acest timp de funcționare pentru a afișa o animație pe matricea LED-urilor, comutând între două sau mai multe imagini diferite.

--- task ---


**Adaugă** a doua imagine sub linia de cod `sense.set_pixels(imagine)`. Dă-i numele variabilei `imagine2` şi schimbă câţiva pixeli pentru a face cadrul de animaţie să arate diferit. Apoi adaugă o scurtă pauză după ea.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
imagine = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(imagine)

# Imaginile/cadrele suplimentare se pun aici:

imagine2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

În partea de jos a fișierului de cod, configurează bucla `for` să se repete de `14` ori și să alterneze între afișarea imaginii `imagine` și a imaginii `imagine2`, cu pauză de 1 secundă la fiecare cadru.

**Sfat:** Asigură-te că liniile de cod de sub `for i in range(14):` sunt indentate cu un spațiu pentru a sta **în interiorul** blocului buclei.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
imagine2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Repetă de 14 ori (14 * 2 secunde = 28 de secunde animație în total)
for i in range(14):
  # Afișează a doua imagine
  sense.set_pixels(imagine2)
  sleep(1)

  # Afișează prima imagine
  sense.set_pixels(imagine)
  sleep(1)
  
--- /code ---

--- /task ---

--- task ---

**Test:** Rulează codul din nou. Programul tău va afișa instantaneu culoarea detectată, apoi va repeta procesul de afișare animată.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Dacă dorești să ai mai mult de două cadre în animația ta, trebuie să te asiguri că programul va rula pentru cel mult 30 de secunde. De exemplu, dacă ai 10 imagini care sunt afișate fiecare timp de 1 secundă, trebuie să modifici bucla `for` pentru a se repeta de 3 ori (10 * 3 = 30 de secunde)
</p>

--- task ---

**Verifică dacă există erori**

Codul meu are o eroare de sintaxă sau nu modifică cadrele:
- Verifică dacă codul buclei `for` se potriveşte cu indentarea din exemplu.
- Asigură-te că ai denumit a doua matrice de imagine `imagine2` și că este plasată în afara și înainte de începerea buclei.
- Verifică dacă timpii de `sleep` sunt setați la exact `1` secundă pentru a evita trecerea peste limita strictă de execuție de 30 secunde de pe ISS.

--- /task ---

--- task ---

**Salvează-ți progresul**

Poți salva programul tău în proiectul Mission Starter introducând numele echipei, numele membrilor echipei și codul de clasă care ți-a fost dat. Poți reîncărca programul tău pe orice dispozitiv cu o conexiune la internet prin introducerea numelui echipei și a codului de clasă.

--- /task ---

--- task ---

--- collapse ---
---
title: Exemplu de cod pentru balenă complet
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
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

# Adaugă variabile de culoare și imagine
a = (255, 255, 255) # Alb
c = (0, 0, 0)       # Negru
f = (36, 128, 200)  # Albastru oceanic
g = (0, 204, 255)   # Albastru ceresc

# Detectează o culoare
rgb = sense.color # obține culoarea de la senzor
c = (rgb.red, rgb.green, rgb.blue)

imagine = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(imagine)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Exemplu de cod pentru balenă complet (cu animație)
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
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

# Adaugă variabile de culoare și imagine
a = (255, 255, 255) # Alb
c = (0, 0, 0)       # Negru
f = (36, 128, 200)  # Albastru oceanic
g = (0, 204, 255)   # Albastru ceresc

# Detectează o culoare
rgb = sense.color # obține culoarea de la senzor
c = (rgb.red, rgb.green, rgb.blue)

imagine = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(imagine)

# TRIMITEREA DE BAZĂ este deja finalizată

# Imaginile/cadrele suplimentare se pun aici:
imagine2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Repetă de 14 ori (14 * 2 secunde = 28 de secunde animație în total)
for i in range(14):
  # Afișează a doua imagine
  sense.set_pixels(imagine2)
  sleep(1)

  # Afișează prima imagine
  sense.set_pixels(imagine)
  sleep(1)
  
--- /code ---

--- /collapse ---

--- /task ---
