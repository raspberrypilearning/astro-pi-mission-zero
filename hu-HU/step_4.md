## Érzékeld a színt

Ebben a lépésben be fogod állítani a színfényerősség-érzékelőt, és arra fogod használni, hogy érzékeld a vörös, zöld és kék fény erejét, amely eléri az érzékelőt. Ezután ezt a színt fogod használni a kiválaszott képed kiszínezésére. Ha egy kék inget viselő űrhajós áll az érzékelő elé, más képet fog látni, mint egy vörös inget viselő.

![megjelenített kép rózsaszín háttérrel a LED-mátrixon](images/colour_background.png)

Bármelyik képet választottad is, a háttér a `c` változót használja, amely feketére van állítva.

--- task ---

Használd a színérzékelőt, hogy kiszínezd a hátteret.

Adj hozzá kódot a képet meghatározó lista elé, hogy kiolvasd a SenseHAT színérzékelőből a színt, majd a `c` változót állítsd be erre a színre fekete helyett.

**Tipp:** Nem kell begépelned a megjegyzéseket, amelyek "#" karakterrel kezdődnek (ezek csak azért vannak ott, hogy elmagyarázzák kódot).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9-10
---

# Adj hozzá színváltozókat és képet

c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange y = (255, 20, 147) # DeepPink

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

**Tesztelés:** Mozgasd a színcsúszkát egy általad választott színre, majd **futtasd** a kódodat. A háttérszín meg fog változni. Ismételd meg a tesztet egy másik színnel.

**Tipp:** Minden egyes alkalommal meg kell nyomnod a Futtatás gombot, ha megváltoztatod a színt.

--- /task ---

## Készíts egy ciklust

Az Astro Pi Mission Zero program legfeljebb 30 másodpercig futhat. Ezt az időt arra fogod használni, hogy ismételten leolvasd az érzékelőt és frissítsd a képet.

A kódod egy `for` ciklust fog használni, hogy 28-szor lefusson. Így **minden** alkalommal:
+ kiolvassa a legfrissebb színt
+ frissíti a kép háttérszínét
+ várakozik egy másodpercig

--- task ---

**Keresd meg** a kódodban az `rgb = sense.color` sort.

**Add hozzá** a kódot egy sorral feljebb, hogy elkezdj egy `for` ciklust, amely `28` alkalommal ismétlődik.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 1
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

Most be kell húznod az összes kódot a `for` ciklus alatt, hogy a `for` cikluson **belül** legyen.

**Tipp:** Ha egyszerre több sort akarsz behúzni, jelöld ki az összeset, majd nyomd le a <kbd>Tab</kbd> billentyűt (általában a <kbd>Caps Lock</kbd> billentyű felett található).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2 - 17
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

  # Display the image

  sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

A kódod alján adj hozzá egy 1 másodperces `sleep` (alvás) parancsot a cikluson belül:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 4
---

  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Tipp:** Ellenőrizd, hogy ez a kód be van-e húzva, hogy a `for` cikluson belül legyen.

--- /task ---

--- task ---

**Tesztelés:** Futtasd a kódodat, és többször változtasd meg a színt, miközben fut a projekt. Figyled, hogy frissül-e a kép az érzékelt színnel a következő futásnál.

A kép frissítése leáll, miután befejeződik a ciklus, hogy a program ne fusson 30 másodpercnél tovább.

--- /task ---

--- task ---

**Hibakeresés**

A kódomban szintaktikai hiba van, vagy nem úgy fut, ahogy kéne:

- Ellenőrizd, hogy a kódod megegyezik-e a fenti példákban látható kóddal
- Ellenőrizd, hogy beljebb kezdted-e a kódot a `for` ciklusban
- Ellenőrizd, hogy a listád `[` és `]` között van-e
- Ellenőrizd, hogy a listában minden színváltozó vesszővel van-e elválasztva

A kódom 30 másodpercnél tovább fut:

- Csökkentsd a ciklus ismétléseinek számát 28-ról 25-re vagy akár 20-ra.
- Csökkentsd a várakozást 1 másodpercről fél (`0.5`) másodpercre.

--- /task ---

--- task ---

Add hozzá a `sense.clear()` parancsot a kódod végére, hogy a kép kitörlődjön a ciklus végén. Így könnyebben láthatod, mikor fejeződött be az animáció.

**Tipp:** Ellenőrizd, hogy a kód **nincs** behúzva, mert a `sense.clear()` sort csak egyszer szeretnéd futtatni, az animáció végén.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 6
---

  # Display the image

  sense.set_pixels(image) sleep(1)

sense.clear()

--- /code ---

--- /task ---

--- task ---

**Tesztelés:** Futtasd a kódodat még egyszer. Miután a projekt futása befejeződik, a LED-mátrix alaphelyzetbe áll, minden lámpa színe fekete lesz (kikapcsolt).

--- /task ---

--- task ---

**Hibakeresés**

A LED-mátrix minden másodpercben feketére vált:

- Ellenőrizd, hogy a `sense.clear()` kód ne legyen behúzva a `for` ciklusba

--- /task ---

--- task ---

Adj hozzá kódot, hogy a LED-mátrix az általad választott színre váltson. Készíts egy `x` változót, amely az új színt tárolja.

Kikeverheted a színt, vagy a listán levő színek közül választhatsz egyet, hogy létrehozd az új `x` színt.

\[[[generic-theory-simple-colours]]\] \[[[ambient-colours\]]]

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 6-7
---

  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /task ---

--- task ---

**Tesztelés:** Futtasd a kódodat még egyszer. Miután a projekt futása befejeződik, a LED-mátrix minden lámpája az általad választott színre vált. Akárhányszor megváltoztathatod a színt, és újra tesztelheted a kódot.

--- /task ---

--- task ---

--- collapse ---

---
title: Kész példakód
---

![Egy 8*8-as rács, amely egy zöld szárú rózsaszín virág képét mutatja.](images/flower.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Import the libraries
from sense_hat import SenseHat from time import sleep

# Set up the Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image

c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange y = (255, 20, 147) # DeepPink

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
