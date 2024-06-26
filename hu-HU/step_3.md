## Jeleníts meg egy képet

Az Astro Pi LED-mátrixa színeket is meg tud jeleníteni. Ebben a lépésben a természetről szóló képeket fogsz megjeleníteni az Astro Pi LED-mátrixán.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A <span style="color: #0faeb0">**LED mátrix**</span> egy LED-ekből álló rács, amely egyenként vagy csoportosan vezérelhető, hogy létrehozz különféle fényhatásokat. A Sense HAT LED-mátrixa 64 LED-ből áll egy 8*8-as rácson elhelyezve. A LED-eket be lehet programozni, hogy a színek széles skáláját mustassák.
</p>

![Képernyőkép az emulátorról, amely a Repülési Egységet mutatja, a LED-mátrixon egy virágnak a képével.](images/fu-pic.png)

--- task ---

Nyisd meg a [Mission Zero kezdőprojektet](https://missions.astro-pi.org/hu/mz/code_submissions/new){:target="_blank"}.

Látni fogod, hogy néhány kódsort már automatikusan hozzáadtunk neked.

Ez a kód az Astro Pi-hoz kapcsolódik, és biztosítja, hogy az Astro Pi LED kijelzője a helyes irányba mutat, majd beállítja a színérzékelőt. Hagyd meg a kódot, mert szükséged lesz rá!

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
---
# Programkönyvtárak importálása
from sense_hat import SenseHat
from time import sleep

# Sense HAT beállítása
sense = SenseHat()
sense.set_rotation(270)

# Színérzékelő beállítása
sense.color.gain = 60 # Az érzékelő érzékenységének beállítása
sense.color.integration_cycles = 64 # Az egyes leolvasások között eltelt idő

--- /code ---

![Képernyőkép a Sense Hat emulátorról a kezdőkóddal a bal oldali panelen.](images/sense-hat-emulator2.png)

--- /task ---

### RGB-színek

Bármilyen színt létrehozhatsz a vörös, a zöld és a kék különböző arányainak használatával. Itt többet tudhatsz meg az RGB-színekről:

[[[generic-theory-simple-colours]]]

A LED-mátrix egy 8*8-as rács. A rácson mindegyik LED más színre állítható be. Itt egy lista színváltozókból 24 különböző színhez. Mindegyik szín egy vörös, zöld és kék értékkel rendelkezik:

[[[ambient-colours]]]

### Válassz egy képet

--- task ---

**Válassz:** Az alábbi képek között keress egyet, amely tetszik. A Python a kép információit egy listában tárolja. Mindegyik kép kódja tartalmazza a felhasznált színváltozókat és a listát.

Ki kell **másolnod** a választott képed kódját, aztán **beillesztened** a projektedbe a `Színváltozók és kép hozzáadása` sor alá.

--- collapse ---

---
title: Csirke
---

![Egy 8*8-as rács, amely egy tojás és egy csibe képét mutatja.](images/chick.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # White (fehér)
c = (0, 0, 0) # Black (fekete)
e = (0, 0, 205) # MediumBlue (kék)
q = (255, 255, 0) # Yellow (sárga)
t = (255, 140, 0) # DarkOrange (narancssárga)
w = (255, 192, 203) # Pink (rózsaszín)

kep = [
  c, c, c, q, q, q, c, c,
  c, c, t, q, e, q, c, c,
  c, c, c, q, q, q, c, c,
  c, w, w, w, w, w, w, c,
  c, w, a, a, a, a, w, c,
  c, w, a, a, a, a, w, c,
  c, c, w, a, a, w, c, c,
  c, c, c, w, w, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Virág
---

![Egy 8*8-as rács, amely egy zöld szárú rózsaszín virág képét mutatja.](images/flower.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
c = (0, 0, 0) # Black (fekete)
m = (34, 139, 34) # ForestGreen (sötétzöld)
q = (255, 255, 0) # Yellow (sárga)
t = (255, 140, 0) # DarkOrange (narancssárga)
y = (255, 20, 147) # DeepPink (sötét rózsaszín)

kep = [
  c, c, y, y, y, y, c, c,
  c, y, y, t, t, y, y, c,
  y, y, t, q, q, t, y, y,
  c, y, y, t, t, y, y, c,
  c, c, y, y, y, y, c, c,
  m, c, c, m, m, c, c, m,
  c, m, m, m, m, m, m, c,
  c, c, c, m, m, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Rák
---

![Egy 8*8-as rács, amely egy tojás és egy rák képét mutatja.](images/crab.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # White (fehér)
c = (0, 0, 0) # Black (fekete)
v = (255, 0, 0) # Red (piros)

kep = [
  c, a, a, c, a, a, c, c,
  c, a, c, c, a, c, c, c,
  c, v, c, c, v, c, c, c,
  c, v, c, c, v, c, c, c,
  v, v, v, v, v, c, v, v,
  v, v, c, c, v, v, v, c,
  v, v, v, v, v, c, v, v,
  v, c, v, c, v, c, c, c]

--- /code ---

--- /collapse ---


--- collapse ---
---
title: Krokodil
---

![Egy 8*8-as rács, amely egy tojás és egy krokodil képét mutatja.](images/croc.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # White (fehér)
c = (0, 0, 0) # Black (fekete)
f = (25, 25, 112) # MidnightBlue (éjkék)
m = (34, 139, 34) # ForestGreen (sötétzöld)

kep = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

--- /code ---


--- /collapse ---

--- collapse ---
---
title: Kígyó
---

![Egy 8*8-as rács, amely egy tojás és egy kígyó képét mutatja.](images/snake.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
 c = (0, 0, 0) # Black (fekete)
 m = (34, 139, 34) # ForestGreen (sötétzöld)
 q = (255, 255, 0) # Yellow (sárga)
 v = (255, 0, 0) # Red (piros)

kep = [
  c, c, c, c, c, c, c, m,
  c, m, m, m, m, m, m, m,
  c, m, c, c, c, c, c, c,
  c, m, m, m, m, m, c, c,
  c, c, c, c, c, m, c, c,
  q, m, q, m, m, m, c, c,
  m, m, m, c, c, c, c, c,
  v, c, c, c, c, c, c, c]
  
--- /code ---

--- /collapse ---

--- collapse ---
---
title: Béka
---

![Egy 8*8-as rács, amely egy tojás és egy béka képét mutatja.](images/frog.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
c = (0, 0, 0) # Black (fekete)
m = (34, 139, 34) # ForestGreen (sötétzöld)
q = (255, 255, 0) # Yellow (sárga)
v = (255, 0, 0) # Red (piros)

kep = [
  c, m, m, m, c, m, m, m,
  c, m, q, m, c, m, q, m,
  m, m, m, m, m, m, m, m,
  m, v, v, v, v, v, v, v,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, m, m, m, c, m]

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Keresd meg** a `# Kép megjelenítése` sort, majd adj hozzá egy új sor kódot, hogy megjelenítsd a képet a LED-mátrixon:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 12
---
kep = [
  c, c, c, q, q, q, c, c,
  c, c, t, q, e, q, c, c,
  c, c, c, q, q, q, c, c,
  c, w, w, w, w, w, w, c,
  c, w, a, a, a, a, w, c,
  c, w, a, a, a, a, w, c,
  c, c, w, a, a, w, c, c,
  c, c, c, w, w, c, c, c]

# Kép megjelenítése 
sense.set_pixels(kep)

--- /code ---

--- /task ---

--- task ---

Nyomd meg a **Run** (futtatás) gombot a szerkesztő alján, hogy láthasd, ahogy a képed megjelenik a LED-mátrixon.

--- /task ---

--- task ---

**Hibakeresés**

A kódom szintaxishibás ("Syntax error"):

- Ellenőrizd, hogy a kódod megegyezik-e a fenti példákban látható kóddal
- Ellenőrizd, hogy beljebb kezdted-e a kódot a listádban
- Ellenőrizd, hogy a listád `[` és `]` között van-e
- Ellenőrizd, hogy a listában minden színváltozó vesszővel van-e elválasztva

Nem jelenik meg a képem:

- Ellenőrizd, hogy a `sense.set_pixels(kep)` ne legyen beljebb kezdve

--- /task ---



