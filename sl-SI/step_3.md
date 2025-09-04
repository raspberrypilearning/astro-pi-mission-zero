## Prikažite sliko

LED matrika računalnika Astro Pi lahko prikazuje barve. V tem koraku boste prikazali slike iz narave na LED matriki Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED matrika**</span> je mreža LED diod, ki jih je mogoče nadzorovati posamično ali kot skupino za ustvarjanje različnih svetlobnih učinkov. Matrika LED na Sense HAT ima 64 LED, postavljenih v 8x8 mrežo. Te diode je mogoče programirati za ustvarjanje širokega spektra barv.
</p>

![Posnetek zaslona okna emulatorja, ki prikazuje letalsko enoto z matriko LED, ki prikazuje sliko rože.](images/fu-pic.png)

--- task ---

Odprite začetni projekt [Mission Zero](https://missions.astro-pi.org/sl/mz/code_submissions/){:target="_blank"}.

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

![Posnetek zaslona emulatorja Sense HAT z vrsticami začetne kode, prikazane v levem podoknu.](images/sense-hat-emulator3.png)

--- /task ---

### RGB barve

Barve lahko ustvarite z različnimi razmerji rdeče, zelene in modre. O barvah RGB si lahko preberete tukaj:

[[[generic-theory-simple-colours]]]

LED matrika je 8x8 mreža. Vsako LED na mreži lahko nastavite na drugo barvo. Tukaj je seznam spremenljivk za 24 različnih barv. Vsaka barva ima vrednost za rdečo, zeleno in modro:

[[[ambient-colours]]]

### Izberi sliko

--- task ---

**Izberite:** Med spodnjimi možnostmi izberite sliko za prikaz. Python shrani informacije za sliko na seznam. Koda za vsako sliko v seznamu vsebuje uporabljene barvne spremenljivke.

Vso kodo za izbrano sliko boste morali **kopirati**, nato pa **jo prilepiti** v svoj projekt pod vrstico, ki pravi `# Dodaj barvne spremenljivke in sliko`.

--- collapse ---

---
title: Riba
---

![Mreža z 8x8 kvadratki, ki prikazujejo ribo.](images/fish.png)

Ustvarila ekipa chalka, Poljska

```python
z = (153, 50, 204) # Svetlo vijolična
q = (255, 255, 0) # Rumena
d = (51, 153, 255) # Modra
c = (0, 0, 0) # Črna

slika = [
d, d, z, d, d, d, d, d,
d, d, d, z, z, d, d, d,
z, d, q, q, q, q, d, d,
z, z, q, q, q, c, q, d,
z, z, z, q, q, q, q, d,
z, z, q, q, q, q, q, d,
z, d, q, z, z, q, d, d,
d, d, d, z, d, d, d, d]

```

--- /collapse ---


--- collapse ---

---
title: Mrož
---

![Mreža z 8x8 kvadratki, ki prikazujejo mroža.](images/walrus.png)

Ustvarila ekipa Mrož, Finska

```python
h = (0, 255, 255) # Cian
c = (0, 0, 0) # Črna
s = (139, 69, 19) # Rjava
a = (255, 255, 255) # Bela
r = (184, 134, 11) # Temno zlata

slika = [
h, h, h, h, h, h, h, h,
h, h, s, s, s, h, h, h,
h, s, s, s, s, s, h, h,
h, s, c, s, c, s, s, s,
h, r, r, r, r, r, s, s,
h, h, a, s, a, s, s, s,
h, h, a, s, a, s, s, s,
r, r, s, s, s, s, s, s]

```

--- /collapse ---

--- collapse ---
---
title: Paxi
---

![Mreža z 8x8 kvadratki, ki prikazujejo Paxija.](images/paxi.png)

Ustvarila ekipa tony_pi, Italija

```python
v = (255, 0, 0) # Rdeča
m = (34, 139, 34) # Drevesno zelena
c = (0, 0, 0) # Črna
e = (100, 149, 237) # Sinje modra
l = (0, 255, 0) # Zelena

slika = [
    c, v, m, c, c, m, v, c,
    c, c, v, v, v, v, c, c,
    c, v, c, e, l, e, v, c,
    c, v, c, l, l, l, v, c,
    c, v, c, l, c, l, v, c,
    c, c, v, v, v, v, c, c,
    c, c, l, c, c, l, c, c,
    c, m, m, c, c, m, m, c]

```

--- /collapse ---


--- collapse ---
---
title: Pes
---

![Mreža z 8x8 kvadratki, ki prikazujejo glavo psa.](images/dog.png)

Ustvarila ekipa ptpr_07, Španija

```python

c = (0, 0, 0) # Črna
r = (184, 134, 11) # Temno zlata
s = (139, 69, 19) # Rjava
y = (255, 20, 147) # Temno roza

slika = [
    c, r, r, c, c, r, r, c,
    c, r, s, s, s, s, r, c,
    c, r, c, s, s, c, r, c,
    c, s, s, s, s, s, s, c,
    c, s, s, s, s, s, s, c,
    c, s, s, c, c, s, s, c,
    c, c, s, y, y, s, c, c,
    c, c, c, y, y, c, c, c]


```

--- /collapse ---

--- collapse ---
---
title: Kameleon
---

![Mreža z 8x8 kvadratki, ki prikazujejo mavrično obarvanega kameleona.](images/chameleon.png)

Ustvarila ekipa The_ETs, Združeno kraljestvo

```python

c = (0, 0, 0) # Črna
s = (139, 69, 19) # Rjava
a = (255, 255, 255) # Bela
v = (255, 0, 0) # Rdeča
t = (255, 140, 0) # Temno oranžna
q = (255, 255, 0) # Rumena
m = (34, 139, 34) # Drevesno zelena
h = (0, 255, 255) # Cian
z = (153, 50, 204) # Svetlo vijolična
y = (255, 20, 147) # Temno roza

slika = [
    a, a, v, v, t, a, a, a,
    a, v, v, t, t, q, a, a,
    v, c, t, t, q, q, m, a,
    v, t, t, q, q, m, m, h,
    s, s, q, s, s, m, s, h,
    a, a, a, a, a, a, a, z,
    a, a, a, a, y, a, a, z,
    a, a, a, a, a, y, z, a]

```

--- /collapse ---

--- collapse ---
---
title: Zmaj
---

![Mreža z 8x8 kvadratki, ki prikazujejo zmaja.](images/kite.png)

Ustvarila ekipa Val, Grčija

```python

c = (0, 0, 0) # Črna
m = (34, 139, 34) # Drevesno zelena
v = (255, 0, 0) # Rdeča
q = (255, 255, 0) # Rumena
e = (0, 0, 205) # Modra
h = (0, 255, 255) # Cian

slika = [
    h, h, h, h, h, h, h, h, 
    h, h, h, e, e, v, v, h, 
    h, h, h, e, e, v, v, h, 
    h, h, h, q, q, m, m, h, 
    h, h, h, q, q, m, m, h,
    h, h, c, h, h, h, h, h, 
    h, c, h, h, h, h, h, h, 
    c, h, h, h, h, h, h, h]

```

--- /collapse ---

--- collapse ---
---
title: Piščanec
---

![Mreža z 8x8 kvadratki, ki prikazujejo piščanca.](images/chicken.png)

Ustvarila ekipa Slepicky, Češka

```python

v = (255, 0, 0) # Rdeča
c = (0, 0, 0) # Črna
b = (105, 105, 105) # Temno siva
q = (255, 255, 0) # Rumena
r = (184, 134, 11) # Temno zlata

slika =  [
    c, c, v, v, v, c, c, c,
    c, v, b, b, r, c, c, r,
    c, b, c, b, b, c, r, b,
    q, r, b, b, b, b, b, r,
    c, v, b, b, b, b, r, b,
    c, v, b, r, r, r, b, r,
    c, c, c, r, b, q, r, c,
    c, c, c, c, q, q, c, c]

```

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
line_highlights: 18, 19
---
z = (153, 50, 204) # Svetlo vijolična
q = (255, 255, 0) # Rumena
d = (51, 153, 255) # Modra
c = (0, 0, 0) # Črna

slika = [
d, d, z, d, d, d, d, d,
d, d, d, z, z, d, d, d,
z, d, q, q, q, q, d, d,
z, z, q, q, q, c, q, d,
z, z, z, q, q, q, q, d,
z, z, q, q, q, q, q, d,
z, d, q, z, z, q, d, d,
d, d, d, z, d, d, d, d]

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


--- task ---

**Shrani svoj napredek**

Zdaj, ko ste prikazali sliko, lahko shranite svoj program v projekt Mission Starter tako, da vnesete ime svoje ekipe, imena članov ekipe in kodo učilnice, ki ste jo prejeli. Svoj program lahko znova naložite v katero koli napravo z internetno povezavo, tako da vnesete ime ekipe in kodo učilnice.

![Gumb za shranjevanje Mission Zero.](images/savebutton_sl.png)

--- /task --- 
