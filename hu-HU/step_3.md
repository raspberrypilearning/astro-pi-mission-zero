## Jeleníts meg egy képet

Az Astro Pi LED-mátrixa színeket is meg tud jeleníteni. Ebben a lépésben a természetről szóló képeket fogsz megjeleníteni az Astro Pi LED-mátrixán.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A <span style="color: #0faeb0">**LED mátrix**</span> egy LED-ekből álló rács, amely egyenként vagy csoportosan vezérelhető, hogy létrehozz különféle fényhatásokat. A Sense HAT LED-mátrixa 64 LED-ből áll egy 8*8-as rácson elhelyezve. A LED-eket be lehet programozni, hogy a színek széles skáláját mustassák.
</p>

![Képernyőkép az emulátorról, amely a Repülési Egységet mutatja, a LED-mátrixon egy virágnak a képével.](images/fu-pic.png)

--- task ---

Nyisd meg a [Mission Zero kezdőprojektet](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"}.

Látni fogod, hogy néhány kódsort már automatikusan hozzáadtunk neked.

Ez a kód az Astro Pi-hoz kapcsolódik, és biztosítja, hogy az Astro Pi LED kijelzője a helyes irányba mutat, majd beállítja a színérzékelőt. Hagyd meg a kódot, mert szükséged lesz rá!

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Importáld a könyvtárakat
from sense_hat import SenseHat from time import sleep

# Állítsd be a SenseHAT-et
sense = SenseHat() sense.set_rotation(270)

# Állítsd be a színérzékelőt
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Képernyőkép a Sense Hat emulátorról a kezdőkóddal a bal oldali panelen.](images/sense-hat-emulator3.png)

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
title: Róka
---

![Egy 8*8-as rács, amely egy róka képét mutatja.](images/fish.png)

Készítette: team i_pupi csapat, Olaszország

```python
c = (0, 0, 0) # Black (fekete)
a = (255, 255, 255) # White (fehér)
t = (255, 140, 0) # Sötét narancssárga

kep = [
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
title: Elefánt
---

![Egy 8*8-as rács, amely egy elefánt képét mutatja.](images/walrus.png)

Készítette: ILiFanT csapat, Finnország

```python
c = (0, 0, 0) # Black (fekete)
b = (105, 105, 105) # Sötétszürke
a = (255, 255, 255) # White (fehér)

kep = [
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
title: Paxi
---

![Egy 8*8-as rács, amely egy kaktusz képét mutatja.](images/paxi.png)

Készítette: 6TETHASI csapat, Hollandia

```python
a = (255, 255, 255) # White (fehér)
c = (0, 0, 0) # Black (fekete)
n = (154, 205, 50) # YellowGreen (sárgászöld)
q = (255, 255, 0) # Yellow (sárga)
t = (255, 140, 0) # DarkOrange (narancssárga)

image = [   
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
title: Krokodil
---

![Egy 8*8-as rács, amely egy tojás és egy krokodil képét mutatja.](images/dog.png)

Készítette: ptpr_07 csapat, Spanyolország

```python

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


```

--- /collapse ---

--- collapse ---
---
title: Szivárvány
---

![Egy 8*8-as rács, amely egy szivárványszínű kaméleon képét mutatja.](images/chameleon.png)

Készítette: The_ETs csapat, Egyesült Királyság

```python

c = (100, 149, 237) # CornflowerBlue (búzavirágkék)
a = (255, 255, 255) # White (fehér)
v = (255, 0, 0) # Red (piros)
t = (255, 140, 0) # DarkOrange (narancssárga)
q = (255, 255, 0) # Yellow (sárga)
l = (0, 255, 127) # SpringGreen (élénkzöld)
e = (0, 0, 205) # MediumBlue (kék)

szivarvany = [
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
title: Sárkány
---

![Egy 8*8-as rács, amely egy papírsárkány képét mutatja.](images/kite.png)

Készítette: Val csapat, Görögország

```python

b = (105, 105, 105) # DimGray (sötétszürke)
c = (0, 0, 0) # Black (fekete)
d = (100, 149, 237) # CornflowerBlue (búzavirágkék)
v = (255, 0, 0) # Red (piros)
z = (153, 50, 204) # DarkOrchid (lila)

kep = [
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
title: Csirke
---

![Egy 8*8-as rács, amely egy csirke képét mutatja.](images/chicken.png)

Készítette: Slepicky csapat, Csehország

```python

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

# Kép megjelenítése 
sense.set_pixels(kep)

```

--- /collapse ---

--- /task ---

--- task ---

**Keresd meg** a sort, ahol ez áll `# Kép megjelenítése`, és add hozzá ezt a sort, amely megjeleníti a képet a LED-mátrixon:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 18, 19
---
Nem jelenik meg a képem:

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

# A kép megjelenítése
sense.set_pixels(image)

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


--- task ---

**Mentsd el a munkádat!**

Most, hogy megjeenítettél egy képet, elmentheted a programodat a küldetés kezdőprojektjébe, ha megadod a csapatod nevét, a csapattagok nevét és a mentorodtól kapott osztálytermi kódot. Újra betöltheted a programodat bármely internetkapcsolattal rendelkező eszközön, ha megadod a csapatod nevét és az osztálytermi kódot.

![A Mission Zero mentés gombja.](images/mz_savebutton_v2.png)

--- /task --- 
