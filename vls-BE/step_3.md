## Laat een afbeelding zien

De LED matrix van de Astro Pi kan kleuren laten zien. In deze stap zal je natuurafbeeldingen laten zien op de LED matrix van de Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Een <span style="color: #0faeb0">**LED-matrix**</span> is een raster met LEDs die individueel of in groep bestuurd kunnen worden om verschillende lichteffecten te creëeren. De LED matrix op de Sense HAT heeft 64 LEDs die in een raster van 8 x 8 getoond worden. De LEDs kunnen geprogrammeerd worden om een breeder gamma van kleuren te maken.
</p>

![Een screenshot van het emulatorscherm dat de vluchtunit toont met de LED-matrix met een foto van een bloem.](images/fu-pic.png)

--- task ---

Open het [Mission Zero startproject](https://missions.astro-pi.org/nl/mz/code_submissions/){:target="_blank"}.

Je zal zien dat er enkele coderegels automatisch toegevoegd werden.

Deze code maakt verbinding met de Astro Pi, zorgt ervoor dat de LED-display van de Astro Pi op de juiste manier getoond wordt en installeert de kleursensor. Laat de code staan, want je zal ze nodig hebben.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
---
# Importeer de bibliotheken
from sense_hat import SenseHat
from time import sleep

# Installeer de Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Installeer de kleursensor
sense.color.gain = 60 # Stel de gevoeligheid van de sensor in
sense.color.integration_cycles = 64 # Het interval waarin het uitlezen gebeurt

--- /code ---

![Een screenshot van de Sense HAT-emulator met de lijnen van de begincode die getoond wordt aan de linkerkant.](images/sense-hat-emulator3.png)

--- /task ---

### RGB-kleuren

Kleuren kunnen gemaakt worden door het gebruik van rood, groen en blauw in verschillende verhoudingen. Je kan hier meer info over RGB-kleuren vinden:

[[[generic-theory-simple-colours]]]

De LED-matrix is een raster van 8 x 8. Elke LED op het raster kan in een andere kleur ingesteld worden. Hier is een lijst met variabelen voor 24 verschillende kleuren. Elke kleur heeft een waarde voor rood, groen en blauw:

[[[ambient-colours]]]

### Kies een afbeelding

--- task ---

**Kies** Kies een afbeelding om te tonen uit de opties hieronder. Python slaat de informatie voor een afbeelding op in een lijst. De code voor elke afbeelding bevat de kleurvariabelen die gebruikt worden en de lijst.

Je zal alle code moeten **kopieren** voor je gekozen afbeelding en dan **plakken** in je project onder de lijn waar staat `# Voeg kleurvariabelen en afbeelding toe`.

--- collapse ---

---
title: Vis
---

![Een raster van 8 x 8 vierkanten toont een vis.](images/fish.png)

Gemaakt door team chalka, Polen

```python
z = (153, 50, 204) # Donkerorchidee
q = (255, 255, 0) # Geel
d = (51, 153, 255) # Blauw
c = (0, 0, 0) # Zwart

afbeelding= [
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

![Een raster van 8 x 8 vierkanten toont een walrus.](images/walrus.png)

Gemaakt door team Walrus, Finland

```python
h = (0, 255, 255) # Cyaan
c = (0, 0, 0) # Zwart
s = (139, 69, 19) # Zadelbruin
a = (255, 255, 255) # Wit
r = (184, 134, 11) # Donkerguldenroede

afbeelding= [
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

![Een raster met 8 x 8 vierkanten toont Paxi.](images/paxi.png)

Gemaakt door team tony_pi, Italië

```python
v = (255, 0, 0) # Rood
m = (34, 139, 34) # Bosgroen
c = (0, 0, 0) # Zwart 
e = (100, 149, 237) # Korenbloemblauw
l = (0, 255, 0) # Groen

afbeelding= [
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
title: Hond
---

![Een raster met 8 x 8 vierkanten toont een kop van een hond.](images/dog.png)

Gemaakt door team ptpr_07, Spanje

```python

c = (0, 0, 0) # Zwart
r = (184, 134, 11) # Donkerguldenroede
s = (139, 69, 19) # Zadelbruin
y = (255, 20, 147) # Dieproze

afbeelding= [
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

![Een raster met 8 x 8 vierkanten toont een regenboogkleurige kameleon.](images/chameleon.png)

Gemaakt door team The_ETs, Verenigd Koninkrijk

```python

c = (0, 0, 0) # Zwart
s = (139, 69, 19) # Zadelbruin
a = (255, 255, 255) # Wit
v = (255, 0, 0) # Rood
t = (255, 140, 0) # Donkeroranje
q = (255, 255, 0) # Geel
m = (34, 139, 34) # Bosgroen
h = (0, 255, 255) # Cyaan
z = (153, 50, 204) # Donkerorchidee
y = (255, 20, 147) # Dieproze

afbeelding= [
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
title: Vlieger
---

![Een raster met 8 x 8 vierkanten toont een vlieger.](images/kite.png)

Gemaakt door team Val, Griekenland

```python

c = (0, 0, 0) # Zwart
m = (34, 139, 34) # Bosgroen
v = (255, 0, 0) # Rood
q = (255, 255, 0) # Geel
e = (0, 0, 205) # Middenblauw
h = (0, 255, 255) # Cyaan

afbeelding = [
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
title: Kip
---

![Een raster met 8 x 8 vierkanten toont een kip.](images/chicken.png)

Gemaakt door team Slepicky, Tsjechië

```python

v = (255, 0, 0) # Rood
c = (0, 0, 0) # Zwart
b = (105, 105, 105) # Donkergrijs
q = (255, 255, 0) # Geel
r = (184, 134, 11) # Donkerguldenroede

afbeelding =  [
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

**Vind:** de regel die zegt `# Toon de afbeelding` en voeg een codelijn toe om je afbeelding op de LED-matrix weer te geven:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 18, 19
---
z = (153, 50, 204) # Donkerorichidee
q = (255, 255, 0) # Geel
d = (51, 153, 255) # Blauw
c = (0, 0, 0) # Zwart

afbeelding = [
d, d, z, d, d, d, d, d,
d, d, d, z, z, d, d, d,
z, d, q, q, q, q, d, d,
z, z, q, q, q, c, q, d,
z, z, z, q, q, q, q, d,
z, z, q, q, q, q, q, d,
z, d, q, z, z, q, d, d,
d, d, d, z, d, d, d, d]

# Toon de afbeelding 
sense.set_pixels(afbeelding)

--- /code ---

--- /task ---

--- task ---

Druk **Run** onderaan de editor om je afbeelding te zien op de LED-matrix.

--- /task ---

--- task ---

**Fouten oplossen**

Mijn code geeft een foutmelding:

- Controleer dat je code overeenkomt met de code in de voorbeelden hierboven
- Controleer dat je de code gecopieerd hebt in je lijst
- Controleer dat je lijst omgeven wordt door `[` en `]`
- Controleer dat elke kleurvariabele in de lijst gescheiden wordt door een komma

Mijn afbeelding wordt niet getoond:

- Controleer dat je `sense.set_pixels(afbeelding)` niet opgeslagen werd

--- /task ---

--- task ---

**Sla je voortgang op**

Nu dat je een beeld getoond hebt, kan je je programma opslaan op het Mission Starter project door de naam van je team, de namen van de teamleden en de klascode die je ontving in te geven. Je kan je programma nu opnieuw laden op eender welk apparaat met een internetverbinding door je teamnaam en klascode in te geven.

![Knop om Mission Zero op te slaan.](images/savebutton_be.png)

--- /task --- 
