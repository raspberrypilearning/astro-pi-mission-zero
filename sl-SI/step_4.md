## Zaznajte barve

V tem koraku boste nastavili senzor barve in svetlosti. Z njim boste merili količino rdeče, zelene in modre svetlobe, ki doseže senzor. Te vrednosti boste nato uporabili za spremembo ene od barv na izbrani sliki.

To pomeni, da se slika lahko spreminja glede na to, kaj senzor vidi. Na primer, astronavt v modri majici bi lahko videl drugačno različico slike kot astronavt v rdeči majici.

Na sliki kita, ki smo jo uporabili v prejšnjem koraku, je bila barva ozadja črna. Za shranjevanje barvne kode RGB smo uporabili spremenljivko `c`:

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

Za spremembo barve uporabite barvni senzor.

Pod vrstice, kjer definirate barve, dodajte naslednjo kodo:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4
---
# Zazna barvo
rgb = sense.color # Prebere barvo iz senzorja
c = (rgb.red, rgb.green, rgb.blue) # Uporabi zaznano barvo

--- /code ---

--- /task ---

Ta koda nadomesti vrednosti RGB, shranjene v spremenljivki `c` , z vrednostmi za barvo, ki jo zazna senzor.

Nasvet: Če v svoji sliki niste uporabili spremenljivke `c`, zamenjajte `c` z eno od barvnih spremenljivk, ki ste jih uporabili. To bo senzorju omogočilo, da spremeni to barvo.

--- task ---

**Preizkus:** Premaknite barvni drsnik na barvo po vaši izbiri in nato **zaženite** svojo kodo. Vaša barva ozadja se bo spremenila. Ponovno ponovite test z novo barvo.

**Namig:** Vsakič, ko spremenite barvo, boste morali klikniti »Zaženi«.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Zdaj, ko ste prikazali sliko in zaznali barvo ter jo uporabili v svojem programu, je vaša koda pripravljena za oddajo! 

Program lahko shranite in oddate z uporabo obrazca na dnu urejevalnika kode.
  
Vendar pa mu boste morda želeli dodati še več slik ali pa ga poživiti z animacijo. Naslednji koraki vam bodo pokazali, kako to storiti.
</p>

## Animirajte svoj projekt (neobvezno)

Vaš program za Mission Zero se lahko na Mednarodni vesoljski postaji (ISS) izvaja do 30 sekund. Med tem časom lahko na LED matriki z menjavanjem dveh ali več različnih sličic prikazujete animacijo.

--- task ---


**Dodajte** drugo sliko tik pod vrstico `sense.set_pixels(slika)`. Spremenljivki dajte ime `slika2` in spremenite nekaj slikovnih pik, da bo vaša sličica videti drugačen. Nato dodajte kratek premor.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
slika = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(slika)

# Dodatne sličice gredo sem:

slika2 = [
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

Čisto na dnu datoteke s kodo ustvarite zanko `for`, ki se ponovi `14`-krat in izmenično prikazuje `slika` in `slika2`, pri čemer se po vsaki sličici ustavi za eno sekundo.

**Nasvet:** Prepričajte se, da so vrstice kode pod `for i in range(14):` zamaknjene s presledki, tako da se nahajajo **znotraj** bloka zanke.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
slika2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Ponovi 14-krat (14 * 2 sekundi = 28 sekund animacije)
for i in range(14):
  # Prikaže drugo sliko
  sense.set_pixels(slika2)
  sleep(1)

  # Prikaže prvo sliko
  sense.set_pixels(slika)
  sleep(1)
  
--- /code ---

--- /task ---

--- task ---

**Preizkus:** Znova zaženite kodo. Vaš program bo takoj prikazal zaznano barvo in se nato v zanki preklapljal med sličicama.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Če želite v animaciji imeti več kot dve sličici, morate zagotoviti, da program ne bo deloval več kot 30 sekund. Na primer, če imate 10 slik, kjer se vsaka prikazuje 1 sekundo, morate zanko `for` spremeniti tako, da se ponovi 3-krat (10 * 3 = 30 sekund)
</p>

--- task ---

**Preverite napake**

Moja koda ima sintaktično napako ali pa ne spreminja sličic:
- Preverite, ali se zamik v vaši kodi zanke `for` ujema z zamikom v primeru.
- Prepričajte se, da ste drugo slikovno spremenljivko poimenovali `slika2` ter je postavljena zunaj in pred začetkom zanke.
- Preverite, ali so vaši časi premora (`sleep`) nastavljeni na natančno `1` sekundo, da se izognete prekoračitvi stroge 30-sekundne omejitve izvajanja na ISS.

--- /task ---

--- task ---

**Shrani svoj napredek**

Svoj program lahko shranite v projekt Mission Starter tako, da vnesete ime svoje ekipe, imena članov ekipe in kodo učilnice, ki ste jo prejeli. Svoj program lahko znova naložite v katero koli napravo z internetno povezavo, tako da vnesete ime ekipe in kodo učilnice.

--- /task ---

--- task ---

--- collapse ---
---
title: Primer dokončane kode s kitom
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Uvozi knjižnice
from sense_hat import SenseHat
from time import sleep

# Nastavi Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Nastavi barvni senzor
sense.color.gain = 60 # Nastavi občutljivost senzorja
sense.color.integration_cycles = 64 # Interval, v katerem bo opravljeno branje

# Doda barvne spremenljivke in sliko
a = (255, 255, 255) # Bela
c = (0, 0, 0)       # Črna
f = (36, 128, 200)  # Oceansko modra
g = (0, 204, 255)   # Nebesno modra

# Zazna barvo
rgb = sense.color # Prebere barvo iz senzorja
c = (rgb.red, rgb.green, rgb.blue)

slika = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(slika)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Primer dokončane kode z animiranim kitom
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Uvozi knjižnice
from sense_hat import SenseHat
from time import sleep

# Nastavi Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Nastavi barvni senzor
sense.color.gain = 60 # Nastavi občutljivost senzorja
sense.color.integration_cycles = 64 # Interval, v katerem bo opravljeno branje

# Doda barvne spremenljivke in sliko
a = (255, 255, 255) # Bela
c = (0, 0, 0)       # Črna
f = (36, 128, 200)  # Oceansko modra
g = (0, 204, 255)   # Nebesno modra

# Zazna barvo
rgb = sense.color # Prebere barvo iz senzorja
c = (rgb.red, rgb.green, rgb.blue)

slika = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(slika)

# OSNOVNA ODDAJA je zdaj končana

# Dodatne sličice gredo sem:
slika2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Ponovi 14-krat (14 * 2 sekundi = 28 sekund animacije)
for i in range(14):
  # Prikaže drugo sliko
  sense.set_pixels(slika2)
  sleep(1)

  # Prikaže prvo sliko
  sense.set_pixels(slika)
  sleep(1)
  
--- /code ---

--- /collapse ---

--- /task ---

