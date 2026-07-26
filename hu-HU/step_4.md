## Érzékeld a színt

Ebben a lépésben beállítod a szín- és fényerősség-érzékelőt. Ezzel az érzékelővel fogod megmérni az érzékelőhöz érkező vörös, zöld és kék fény erejét. Ezután kapott értékek alapján megváltoztatod valamelyik színt a képeden.

Ez azt jelenti, hogy a kép megváltozhat attól függően, mint lát az érzékelő. Például egy kék inget viselő űrhajós a kép más változatát látná, mint egy vörös inget viselő.

A korábbi bálnás képen a háttér színe fekete volt. A `c` változót használtuk ennek az RGB-értéknek a tárolására:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Használd a színérzékelőt, hogy megváltoztasd az egyik színedet.

A színekez definiáló sorok alá add hozzá az alábbi kódot:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

--- /code ---

--- /task ---

Ez a kód lecseréli a `c` változóban tárolt RGB-értékeket az érzékelőből kiolvasott színértékekkel.

Tipp: Ha nem használtad a `c` változót a képed létrehozására, cseréld le a `c`-t a kódban egy olyan színváltozóra, amelyet használtál. Ez lehetővé teszi, hogy az érzékelő egy másik színt változtasson meg.

--- task ---

**Tesztelés:** Mozgasd a színcsúszkát egy általad választott színre, majd **futtasd** a kódodat. A háttérszín meg fog változni. Ismételd meg a tesztet egy másik színnel.

**Tipp:** Minden egyes alkalommal meg kell nyomnod a Futtatás gombot, ha megváltoztatod a színt.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Most, hogy megjelenítettél egy képet, érzékeltél egy színt és felhasználtad azt a programodban, a kódod készen áll a beküldésre! 

Elmentheted és beküldheted a programodat a kódszerkesztő alján található űrlap segítségével.
  
Azonban esetleg hozzáadhatsz több képet a projektedhez, vagy életre keltheted egy animációval. A következő lépések bemutatják, hogyan teheted meg ezt.
</p>

## Animáld a projektedet (opcionális)

A Mission Zero-programod legfeljebb 30 másodpercig futhat a Nemzetközi Űrállomáson (ISS). Ezt a futási időt felhasználhatod arra, hogy egy animációt jeleníts meg a LED-mátrixon úgy, hogy kettő vagy több kép között váltasz.

--- task ---


**Adj hozzá** egy második képet közvetlenül a `sense.set_pixels(image)` kódsor alá. Add neki a `kep2` változónevet, majd változtass meg néhány pixelt, hogy máshogy nézzen ki az animáció újabb képkockája. Ezután adj hozzá egy rövid várakozást.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# Extra images / frames go here:

image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

A kódfájlod legvégén adj hozzá egy `for` ciklust, hogy `14`-szer váltogass a `kep` és a `kep2` megjelenítése között, és minden képkocka után 1 másodpercet várj.

**Tipp:** Győződj meg róla, hogy a `for i in range(14):` alatti sorok be vannak húzva szóközökkel, hogy a cikluson **belül** legyenek.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1)

--- /code ---

--- /task ---

--- task ---

**Tesztelés:** Futtasd a kódodat még egyszer. A programod azonlla meg fogja jeleníteni az érzékelt színt, aztán váltogatni fog a képek között, így egy animációt hoz létre.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Ha szeretnél kettőnél több képet megjeleníteni, ügyelj arra, hogy a programod ne fusson 30 másodpercnél tovább. Például, ha 10 képed van, és mindegyiket 1 másodpercig jeleníted meg, a "for" ciklusodat át kell írnod, hogy 3-szor fusson le (10 * 3 = 30 másodperc).
</p>

--- task ---

**Keress hibákat**

A kódomban szintaktikai hiba van, vagy nem vált képkockát:
- Ellenőrizd, hogy a `for` ciklusod behúzása ugyanúgy néz ki, mint a példában.
- Győződj meg róla, hogy a második képmátrixodat `kep2`-nek nevezted, és a "for" cikluson kívül, az előtt helyezted el.
- Ellenőrizd, hogy a `sleep` idők pontosan `1` másodpercre vannak állítva, hogy ne lépd túl a szigorú 30 másodperces időkorlátot az ISS-en.

--- /task ---

--- task ---

**Mentsd el a munkádat!**

Elmentheted a programodat a küldetés kezdőprojektjébe, ha megadod a csapatod nevét, a csapattagok nevét és a mentorodtól kapott osztálytermi kódot. Újra betöltheted a programodat bármely internetkapcsolattal rendelkező eszközön, ha megadod a csapatod nevét és az osztálytermi kódot.

--- /task ---

--- task ---

--- collapse ---
---
title: A bálna kész példakódja
---

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
a = (255, 255, 255) # White c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: A bálna kész példakódja (animációval)
---

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
a = (255, 255, 255) # White c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1)

--- /code ---

--- /collapse ---

--- /task ---
