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
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Uvozi knjižnice
from sense_hat import SenseHat from time import sleep

# Nastavi Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Nastavi barvni senzor
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Posnetek zaslona emulatorja Sense HAT z vrsticami začetne kode, prikazane v levem podoknu.](images/sense-hat-emulator2.png)

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
title: Fish
---

![A grid with 8 x 8 squares showing a fish.](images/fish.png)

Created by team chalka, Poland

```python
z = (204, 0, 204) # magenta
q = (255, 255, 0) # yellow
d = (51, 153, 255) # blue
c = (0, 0, 0) # black

image = [
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
title: Walrus
---

![A grid with 8 x 8 squares showing a walrus.](images/walrus.png)

Created by team Walrus, Finland

```python
h = (0, 255, 255)
c = (0, 0, 0)
s = (139, 69, 19)
a = (255, 255, 255)
r = (184, 134, 11)   

image = [
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

![A grid with 8 x 8 squares showing paxi.](images/paxi.png)

Created by team tony_pi, Italy

```python
v = (255, 0, 0) # Red
j = (34, 139, 34) # ForestGreen
c = (0, 0, 0) # Black 
e = (100, 149, 237) # CornflowerBlue
l = (0, 255, 0) # Green

image = [
    c, v, j, c, c, j, v, c,
    c, c, v, v, v, v, c, c,
    c, v, c, e, l, e, v, c,
    c, v, c, l, l, l, v, c,
    c, v, c, l, c, l, v, c,
    c, c, v, v, v, v, c, c,
    c, c, l, c, c, l, c, c,
    c, j, j, c, c, j, j, c]

```

--- /collapse ---


--- collapse ---
---
title: Dog
---

![A grid with 8 x 8 squares showing a dog head.](images/dog.png)

Created by team ptpr_07, Spain
```python

c = (0, 0, 0) # Black
r = (86, 71, 0) # Light Brown
s = (123, 61, 0) # Orange Brown
y = (155, 0, 134) # Deep Pink

image = [
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
title: Chameleon
---

![A grid with 8 x 8 squares showing a rainbow coloured chameleon.](images/chameleon.png)

Created by team The_ETs, United Kingdom

```python

c = (0, 0, 0) # Black
s = (95, 65, 0) # Brown
a = (255, 255, 255) # white
v = (255, 0, 0) # Red
t = (255, 153, 28) # Orange
q = (255, 255, 0) # Yellow
m = (0, 255, 0) # Green
h = (0, 255, 255) # Cyan
z = (128, 0, 255) # Purple
y = (191, 0, 255) # Magenta

image = [
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
title: Kite
---

![A grid with 8 x 8 squares showing a kite.](images/kite.png)

Created by team Val, Greece

```python

c = (0, 0, 0) # Black
m = (0, 255, 0) # Green
v = (255, 0, 0) # Red
q = (255, 255, 0) # Yellow
e = (0, 0, 255) # Blue
h = (0, 255, 255) # Cyan

image = [
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
title: Chicken
---

![A grid with 8 x 8 squares showing a Chicken.](images/chicken.png)

Created by team Slepicky, Czech Republic

```python

w = (255, 255, 255) #  White                                                                
v = (255, 0, 0) # Red
c = (0, 0, 0) # Black
b = (105, 105, 105) # Light Grey
q = (255, 255, 0) # Yellow
k = (79, 79, 79) # Dark Grey


image =  [
    a, a, v, v, v, a, a, a,
    a, v, b, b, k, a, a, k,
    a, b, c, b, b, a, k, b,
    q, k, b, b, b, b, b, k,
    a, v, b, b, b, b, k, b,
    a, v, b, k, k, k, b, k,
    a, a, a, k, b, q, k, a,
    a, a, a, a, q, q, a, a]

```

--- /collapse ---

--- /task ---

--- task ---

**Poiščite:** vrstico, ki pravi `# Prikaži sliko` in dodajte vrstico kode za prikaz vaše slike na matriki LED:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 18, 19
---
z = (204, 0, 204) # magenta q = (255, 255, 0) # yellow d = (51, 153, 255) # blue c = (0, 0, 0) # black

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

# Display the image
sense.set_pixels(image)

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

![Gumb za shranjevanje Mission Zero](images/mz_savebutton_v2.png)

--- /task --- 
