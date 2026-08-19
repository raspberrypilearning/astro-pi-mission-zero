## Jeleníts meg egy képet

Az általad megjelenített kép 64 színes négyzetből, azaz **pixelből** fog állni. A pixelek egy 8 x 8-as rácsban vannak elrendezve. Minden pixel más színű lehet. A színek gondos kiválasztásával egy képet alkothatsz. Példaként itt egy bálna képe különféle kék árnyalatok felhasználásával fekete háttéren.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A <span style="color: #0faeb0">**LED mátrix**</span> egy LED-ekből álló rács, amely egyenként vagy csoportosan vezérelhető, hogy létrehozz különféle fényhatásokat. A Sense HAT LED-mátrixa 64 LED-ből áll egy 8*8-as rácson elhelyezve. A LED-eket be lehet programozni, hogy a színek széles skáláját mustassák.
</p>

![egy bálna 8x8-as képe, amelyen betűk jelölik a különböző színeket](images/whale.png)

Figyeld meg, hogy mindegyik négyzet meg van jelölve egy kóddal, amely egy bizonyos színt jelképez. Ezen a képen 3 színt használtunk:
+ c = Fekete
+ f = Óceánkék
+ g = Égkék


--- task ---

Nyisd meg a [Mission Zero kezdőprojektet](https://missions.astro-pi.org/hu/mz/code_submissions/){:target="_blank"}.

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
# Importáld a könyvtárakat
from sense_hat import SenseHat
from time import sleep

# Állítsd be a SenseHAT-et
sense = SenseHat()
sense.set_rotation(270)

# Állítsd be a színérzékelőt
sense.color.gain = 60 # Az érzékelő érzékenységének beállítása
sense.color.integration_cycles = 64 # Az egyes leolvasások között eltelt idő

--- /code ---

![Képernyőkép a Sense Hat emulátorról a kezdőkóddal a bal oldali panelen.](images/sense-hat-emulator3.png)

--- /task ---

### RGB-színek

Bármilyen színt létrehozhatsz a vörös, a zöld és a kék különböző arányainak használatával. Itt többet tudhatsz meg az RGB-színekről:

![Három csúszka az RGB színértékek bemutatására](images/rgbsliders.gif)

A LED-mátrix egy 8*8-as rács. A rácson mindegyik LED más színre állítható be. Az a-tól z-ig terjedő betűket használhatjuk változónévként 24 különböző szín jelképezésére. Mindegyik szín egy vörös, zöld és kék értékkel rendelkezik.

--- collapse ---

---
title: Színváltozók listája
---

![24 színes négyzetből álló rács, amelyek mindegyike az ábécé más betűjével van jelölve](images/palette.png)

```python
a = (255, 255, 255) # White (fehér)
b = (171, 171, 171) # Grey (szürke)
c = (0, 0, 0)       # Black (fekete)
d = (25, 25, 113)   # Navy Blue (sötétkék)
e = (0, 0, 255)     # Pure Blue (tiszta kék)
f = (36, 128, 200)  # Ocean Blue (óceánkék)
g = (0, 204, 255)   # Sky Blue (égkék)
h = (86, 255, 255)  # Electric Cyan (ciánkék)
j = (0, 255, 0)     # Pure Green (tiszta zöld)
k = (46, 139, 33)   # Leaf Green (levélzöld)
l = (57, 97, 17)    # Olive Green (olajzöld)
m = (30, 65, 6)     # Forest Green (sötétzöld)
n = (126, 88, 25)   # Earth Brown (barna)
o = (179, 96, 65)   # Terracotta Brown (világosbarna)
p = (180, 34, 34)   # Brick Red (sötétvörös)
q = (255, 0, 0)     # Pure Red (tiszta vörös)
r = (232, 118, 5)   # Orange (narancs)
s = (241, 231, 100) # Pale Yellow (halványsárga)
t = (255, 255, 0)   # Pure Yellow (sárga)
u = (255, 209, 209) # Pale Pink (halvány rózsaszín)
v = (255, 177, 177) # Blush Pink (rózsaszín)
w = (249, 169, 255) # Light Pink (világoslila)
y = (248, 97, 255)  # Magenta (lila)
z = (220, 53, 232)  # Purple (sötétlila)

```

--- /collapse ---

### Válassz egy képet

--- task ---

**Válassz:** Az alábbi képek között keress egyet, amely tetszik. A Python a kép információit egy listában tárolja. Mindegyik kép kódja tartalmazza a felhasznált színváltozókat és a listát.

Ki kell **másolnod** a választott képed kódját, aztán **beillesztened** a projektedbe a `Színváltozók és kép hozzáadása` sor alá.

--- collapse ---

---
title: Bálna
---

![Egy 8 x 8-as rács, amely egy bálna képét mutatja.](images/whale.png)

Készítette: Naicom csapat, Olaszország

```python
c = (0, 0, 0)       # Black (fekete)
f = (36, 128, 200)  # Ocean Blue (óceánkék)
g = (0, 204, 255)   # Sky Blue (égkék)

kep = [
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
title: Citrom
---

![Egy 8 x 8-as rács, amely egy citrom képét mutatja.](images/lemon.png)

Készítette: g4lemoni csapat, Görögország

```python
c = (0, 0, 0)       # Black (fekete)
k = (46, 139, 33)   # Leaf Green (levélzöld)
t = (255, 255, 0)   # Pure Yellow (sárga)

kep = [
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
title: Disznó
---

![Egy 8 x 8-as rács, amely egy disznó képét mutatja.](images/pig.png)

Készítette: Gary, Egyesült Királyság

```python
a = (255, 255, 255) # White (fehér)
v = (255, 177, 177) # Blush Pink (rózsaszín)
y = (248, 97, 255)  # Magenta (lila)
o = (179, 96, 65)   # Terracotta Brown (világosbarna)
c = (0, 0, 0)       # Black (fekete)

kep = [
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
title: Vihar
---

![Egy 8 x 8-as rács, amely egy viharfelhő képét mutatja.](images/storm.png)

Készítette: hop2p023 csapat, Spanyolország

```python

c = (0, 0, 0)       # Black (fekete)
f = (36, 128, 200)  # Ocean Blue (óceánkék)
g = (0, 204, 255)   # Sky Blue (égkék)
t = (255, 255, 0)   # Pure Yellow (sárga)

kep = [
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
title: Kacsa
---

![Egy 8 x 8-as rács, amely egy kacsa képét mutatja.](images/duck.png)

Készítette: Peter, Írország

```python

c = (0, 0, 0) # Black (fekete)
l = (57, 97, 17)    # Olive Green (olajzöld)
m = (30, 65, 6)     # Forest Green (sötétzöld)
r = (232, 118, 5)   # Orange (narancs)
a = (255, 255, 255) # White (fehér)
b = (171, 171, 171) # Grey (szürke)

kep = [
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
title: Béka
---

![Egy 8 x 8-as rács, amely egy béka képét mutatja.](images/frog.png)

Készítette: Jmeno csapat, Csehország

```python

a = (255, 255, 255) # White (fehér)
b = (171, 171, 171) # Grey (szürke)
c = (0, 0, 0)       # Black (fekete)
q = (255, 0, 0)     # Pure Red (tiszta vörös)
j = (0, 255, 0)     # Pure Green (tiszta zöld)
k = (46, 139, 33)   # Leaf Green (levélzöld)
n = (126, 88, 25)   # Earth Brown (barna)

kep = [
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
title: Virágzó fa
---

![Egy 8 x 8-as rács, amely egy virágzó fa képét mutatja.](images/blossom.png)

Készítette: Zssh14 csapat, Szlovákia

```python

t = (255, 255, 0)   # Pure Yellow (sárga)
g = (0, 204, 255)   # Sky Blue (égkék)
w = (249, 169, 255) # Light Pink (világoslila)
y = (248, 97, 255)  # Magenta (lila)
z = (220, 53, 232)  # Purple (sötétlila)
n = (126, 88, 25)   # Earth Brown (barna)
o = (179, 96, 65)   # Terracotta Brown (világosbarna)
k = (46, 139, 33)   # Leaf Green (levélzöld)

kep =  [
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

**Keresd meg** a sort, ahol ez áll `# Kép megjelenítése`, és add hozzá ezt a sort, amely megjeleníti a képet a LED-mátrixon:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Black (fekete)
f = (36, 128, 200)  # Ocean Blue (óceánkék)
g = (0, 204, 255)   # Sky Blue (égkék)

kep = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, a,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

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


--- task --- 

**Mentsd el a munkádat!**

Most, hogy megjeenítettél egy képet, elmentheted a programodat a küldetés kezdőprojektjébe, ha megadod a csapatod nevét, a csapattagok nevét és a mentorodtól kapott osztálytermi kódot. Újra betöltheted a programodat bármely internetkapcsolattal rendelkező eszközön, ha megadod a csapatod nevét és az osztálytermi kódot.

![A Mission Zero mentés gombja.](images/mz_savebutton_v2.png)

--- /task --- 

