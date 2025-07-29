## Toon een afbeelding

De LED-matrix van de Astro Pi kan kleuren weergeven. In deze stap zul je afbeeldingen van de natuur weergeven op de LED-matrix van de Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Een <span style="color: #0faeb0">**LED-matrix**</span> is een raster van LED's die afzonderlijk of als groep kunnen worden aangestuurd om verschillende lichteffecten te creëren. De LED-matrix op de Sense HAT heeft 64 LED's die worden weergegeven in een 8 x 8 raster. De LED's kunnen worden geprogrammeerd om een breed scala aan kleuren te produceren.
</p>

![Een screenshot van het emulatorvenster van de Flight Unit met de LED-matrix waarop een afbeelding van een bloem te zien is.](images/fu-pic.png)

--- task ---

Open het [Mission Zero-startproject](https://missions.astro-pi.org/nl/mz/code_submissions/new){:target="_blank"}.

Je zult zien dat er automatisch enkele regels met code voor je zijn toegevoegd.

Deze code maakt verbinding met de Astro Pi en zorgt ervoor dat het LED-display van de Astro Pi op de juiste manier wordt weergegeven en doet de set up van de kleurensensor. Laat de code staan, want je hebt hem nodig.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Importeer de bibliotheken
from sense_hat import SenseHat from time import sleep

# Stel de Sense HAT in
sense = SenseHat() sense.set_rotation(270)

# Stel de kleurensensor in
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Een schermafbeelding van de Sense HAT emulator met enkele regels startcode weergegeven in het linkervenster.](images/sense-hat-emulator3.png)

--- /task ---

### RGB-kleuren

Kleuren kunnen worden gemaakt met verschillende verhoudingen van rood, groen en blauw. Meer informatie over de RGB kleuren vind je hier:

[[[generic-theory-simple-colours]]]

De LED-matrix is een 8 x 8 raster. Elke LED op het raster kan op een andere kleur worden ingesteld. Hier is een lijst met variabelen voor 24 verschillende kleuren. Elke kleur heeft een waarde voor rood, groen en blauw:

[[[ambient-colours]]]

### Kies een afbeelding

--- task ---

**Kies:** Kies een afbeelding om weer te geven uit de onderstaande opties. Python slaat de informatie voor een afbeelding op in een lijst. De code voor elke afbeelding bevat de gebruikte kleurvariabelen en de lijst.

Je moet alle code **kopiëren** voor je gekozen afbeelding en **plak** het in je project onder de regel `# Voeg kleurvariablen en afbeelding toe`.

--- collapse ---

---
title: Vis
---

![Een raster met 8 x 8 vierkanten met daarop een vis.](images/fish.png)

Gemaakt door team Chalka, Polen

```python
z = (153, 50, 204) # Donker orchidee 
q = (255, 255, 0) # Geel
d = (51, 153, 255) # blauw
c = (0, 0, 0) # Zwart

afbeelding = [
d, d, z, d, d, d, d, d,
d, d, d, z, z, d, d, d,
z, d, q, q, q, q, d, d,
z, z, q, q, q, c, q, d,
z, z, z, q, q, q, q, d,
z, z, q, q, q, q, q, q, d,
z, d, q, z, z, q, d, d,
d, d, d, z, d, d, d, d]

```

--- /collapse ---


--- collapse ---

---
title: Walrus
---

![Een raster van 8 x 8 vierkanten met daarop een walrus.](images/walrus.png)

Gemaakt door team Walrus, Finland

```python
h = (0, 255, 255) # Cyaan
c = (0, 0, 0) # Zwart
s = (139, 69, 19) # Zadelbruin
a = (255, 255, 255) # Wit
r = (184, 134, 11) # Donkergoudenroede

afbeelding = [
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

![Een raster van 8 x 8 vierkanten met Paxi.](images/paxi.png)

Gemaakt door team tony_pi, Italië

```python
v = (255, 0, 0) # Rood
m = (34, 139, 34) # Bosgroen
c = (0, 0, 0) # Zwart 
e = (100, 149, 237) # Korenbloemblauw
l = (0, 255, 0) # Groen

afbeelding = [
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

![A grid with 8 x 8 squares showing a dog head.](images/dog.png)

Created by team ptpr_07, Spain

```python

c = (0, 0, 0) # Black
r = (184, 134, 11) # DarkGoldenrod
s = (139, 69, 19) # SaddleBrown
y = (255, 20, 147) # DeepPink

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

![A grid with 8 x 8 squares showing a rainbow-coloured chameleon.](images/chameleon.png)

Created by team The_ETs, United Kingdom

```python

c = (0, 0, 0) # Black
s = (139, 69, 19) # SaddleBrown
a = (255, 255, 255) # White
v = (255, 0, 0) # Red
t = (255, 140, 0) # DarkOrange
q = (255, 255, 0) # Yellow
m = (34, 139, 34) # ForestGreen
h = (0, 255, 255) # Cyan
z = (153, 50, 204) # DarkOrchid
y = (255, 20, 147) # DeepPink

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
m = (34, 139, 34) # ForestGreen
v = (255, 0, 0) # Red
q = (255, 255, 0) # Yellow
e = (0, 0, 205) # MediumBlue
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

![A grid with 8 x 8 squares showing a chicken.](images/chicken.png)

Created by team Slepicky, Czechia

```python

v = (255, 0, 0) # Red
c = (0, 0, 0) # Black
b = (105, 105, 105) # DimGray
q = (255, 255, 0) # Yellow
r = (184, 134, 11) # DarkGoldenrod

image =  [
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

**Find:** the line that says `# Display the image` and add a line of code to display your image on the LED matrix:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 18, 19
---
z = (153, 50, 204) # DarkOrchid q = (255, 255, 0) # Yellow d = (51, 153, 255) # blue c = (0, 0, 0) # Black

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

# Geef de afbeelding weer
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Druk op de **Run** knop onderaan de editor, en zie je bericht weergegeven op de LED matrix.

--- /task ---

--- task ---

**Fouten oplossen (Debuggen)**

Mijn code heeft een syntax fout:

- Controleer of je code overeenkomt met de code in de bovenstaande voorbeelden
- Controleer of je de code in je lijst hebt ingesprongen
- Controleer of je lijst is omgeven door `[` en `]`
- Controleer of elke kleurvariabele in de lijst is gescheiden door een komma

Mijn afbeelding verschijnt niet:

- Controleer of je `sense.set_pixels(afbeelding)` niet ingesprongen is

--- /task ---


--- task ---

**Sla je voortgang op**

Nu je een afbeelding hebt weergegeven, kun je je programma opslaan in het Mission Start-project door je teamnaam, de namen van de teamleden en de klascode die je hebt gekregen in te voeren. Je kunt je programma herladen op elk apparaat met een internetverbinding door je teamnaam en klascode in te voeren.

![Mission Zero Save-knop](images/mz_savebutton_v2.png)

--- /task --- 
