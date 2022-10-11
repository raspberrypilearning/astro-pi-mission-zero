## Prikaže sliko

LED matrika računalnika Astro Pi lahko prikazujejo barve. V tem koraku boste prikazali slike iz narave na LED matriki Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED matrika**</span> je mreža LED diod, ki jih je mogoče nadzorovati posamično ali kot skupino za ustvarjanje različnih svetlobnih učinkov. Matrika LED na Sense HAT ima 64 LED, postavljenih v 8x8 mrežo. Te diode je mogoče programirati za ustvarjanje širokega spektra barv.
</p>

![Posnetek zaslona okna emulatorja, ki prikazuje letalsko enoto z matriko LED, ki prikazuje sliko rože.](images/fu-pic.png)

--- task ---

Odprite začetni projekt [Mission Zero](http://rpf.io/mzcode){:target="_blank"}.

Opazili boste, da je bilo nekaj vrstic kode dodanih samodejno.

Koda se poveže z računalnikom Astro Pi in poskrbi, da sta zaslon LED in senzor svetlobe računalnika Astro Pi nastavljena pravilno. Kodo pustite, ker jo boste potrebovali.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
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

--- /code ---

![Posnetek zaslona emulatorja Sense HAT z vrsticami začetne kode, prikazane v levem podoknu.](images/sense-hat-emulator2.png)

--- /task ---

### RGB barve

Barve lahko ustvarite z različnimi razmerji rdeče, zelene in modre. O barvah RGB si lahko preberete tukaj:

[[[generic-theory-simple-colours]]]

LED matrika je 8x8 mreža. Vsako LED na mreži lahko nastavite na drugo barvo. Tukaj je seznam spremenljivk za 24 različnih barv. Vsaka barva ima vRdečanost za rdečo, zeleno in modro:

[[[ambient-colours]]]

### Izberi sliko

--- task ---

**Izberite:** Med spodnjimi možnostmi izberite sliko za prikaz. Python shrani informacije za sliko na seznam. Koda za vsako sliko v seznamu vsebuje uporabljene barvne spremenljivke.

Vso kodo za izbrano sliko boste morali **kopirati**, nato pa **jo prilepiti** v svoj projekt pod vrstico, ki pravi `# Dodaj barvne spremenljivke in sliko`.

--- collapse ---

---
title: Piščanec
---

![Mreža z 8x8 kvadratki, ki prikazujejo piščanca v jajcu.](images/chick.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Bela
c = (0, 0, 0) # Črna
e = (0, 0, 205) # Modra
q = (255, 255, 0) # Rumena
t = (255, 140, 0) # Temnooranžna
w = (255, 192, 203) # Roza

slika = [
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
title: Roža
---

![Mreža z 8x8 kvardraki, ki prikazujejp rožnato rožo na zelenem steblu.](images/flower.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
c = (0, 0, 0) # Črna
m = (34, 139, 34) # Drevesnozelena
q = (255, 255, 0) # Rumena
t = (255, 140, 0) # Temnooranžna
y = (255, 20, 147) # Temnoroza

slika = [
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
title: Rak
---

![Mreža z 8x8 kvadratki, ki prikazujejo raka.](images/crab.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Bela
c = (0, 0, 0) # Črna
v = (255, 0, 0) # Rdeča

slika = [
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

![Mreža z 8x8 kvadratki, ki prikazujejo krokodiljo glavo.](images/croc.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Bela
c = (0, 0, 0) # Črna
f = (25, 25, 112) # Nočnomodra
m = (34, 139, 34) # Drevesnozelena

slika = [
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
title: Kača
---

![Mreža z 8x8 kvadratki, ki prikazujejo kačo.](images/snake.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
 c = (0, 0, 0) # Črna
 m = (34, 139, 34) # Drevesnozelena
 q = (255, 255, 0) # Rumena
 v = (255, 0, 0) # Rdeča

slika = [
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
title: Žaba
---

![Mreža z 8x8 kvadratki, ki prikazujejo žabo.](images/frog.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
c = (0, 0, 0) # Črna
m = (34, 139, 34) # Drevesnozelena
q = (255, 255, 0) # Rumena
v = (255, 0, 0) # Rdeča

slika = [
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

**Poiščite:** vrstico, ki pravi `# Prikaži sliko` in dodajte vrstico kode za prikaz vaše slike na matriki LED:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 12
---
slika = [
  c, c, c, q, q, q, c, c,
  c, c, t, q, e, q, c, c,
  c, c, c, q, q, q, c, c,
  c, w, w, w, w, w, w, c,
  c, w, a, a, a, a, w, c,
  c, w, a, a, a, a, w, c,
  c, c, w, a, a, w, c, c,
  c, c, c, w, w, c, c, c]

# Prikaži sliko 
sense.set_pixels(slika)


--- /code ---

--- /task ---

--- task ---

Pritisnite **Zaženi (Run)** na dnu urejevalnika, da vidite svojo sliko prikazano na matriki LED.

--- /task ---

--- task ---

**Razhroščevanje**

Moja koda ima sintaktično napako:

- Preverite, ali se vaša koda ujema s kodo v zgornjih primerih
- Preverite, ali ste zamaknili kodo na seznamu
- Preverite, ali je vaš seznam obkrožen z `[` in `]`
- Preverite, ali je vsaka barvna spremenljivka na seznamu ločena z vejico

Moja slika se ne prikaže:

- Preverite, ali vaš `sense.set_pixels(slika)` ni zamaknjen

--- /task ---



