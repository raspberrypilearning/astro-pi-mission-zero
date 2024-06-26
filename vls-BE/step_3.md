## Laat een afbeelding zien

De LED matrix van de Astro Pi kan kleuren laten zien. In deze stap zal je natuurafbeeldingen laten zien op de LED matrix van de Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Een <span style="color: #0faeb0">**LED-matrix**</span> is een raster met LEDs die individueel of in groep bestuurd kunnen worden om verschillende lichteffecten te creëeren. De LED matrix op de Sense HAT heeft 64 LEDs die in een raster van 8 x 8 getoond worden. De LEDs kunnen geprogrammeerd worden om een breeder gamma van kleuren te maken.
</p>

![Een screenshot van het emulatorscherm dat de vluchtunit toont met de LED-matrix met een foto van een bloem.](images/fu-pic.png)

--- task ---

Open het [Mission Zero startproject](https://missions.astro-pi.org/nl-BE/mz/code_submissions/new){:target="_blank"}.

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

![Een screenshot van de Sense HAT-emulator met de lijnen van de begincode die getoond wordt aande linkerkant.](images/sense-hat-emulator2.png)

--- /task ---

### RGB-kleuren

Kleuren kunnen gemaakt worden door het gebruik van rood, groen en blauw in verschillende verhoudingen. Je kan hier meer info over RGB-kleuren vinden:

[[[generic-theory-simple-colours]]]

De LED-matrix is een raster van 8 x 8. Elke LED op het raster kan in een ander kleur ingesteld worden. Hier is een lijst met variabelen voor 24 verschillende kleuren. Elke kleur heeft een waarde voor rood, groen en blauw:

[[[ambient-colours]]]

### Kies een afbeelding

--- task ---

**Kies** Kies een afbeelding om te tonen uit de opties hieronder. Python slaat de informatie voor een afbeelding op in een lijst. De code voor elke afbeelding bevat de kleurvariabelen die gebruikt worden en de lijst.

Je zal alle code moeten **kopieren** voor je gekozen afbeelding en dan **plakken** in je project onder de lijn waar staat `# Voeg kleurvariabelen en afbeelding toe`.

--- collapse ---

---
title: Kip
---

![Een raster met 8 x 8 vierkanten dat een kip in een ei toont.](images/chick.png)


--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Wit
c = (0, 0, 0) # Zwart
e = (0, 0, 205) # Middenblauw
q = (255, 255, 0) # Geel
t = (255, 140, 0) # Donkeroranje
w = (255, 192, 203) # Roze

afbeelding = [
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
title: Bloem
---

![Een raster met 8 x 8 vierkanten dat een roze bloem op een groene stengel toont.](images/flower.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
c = (0, 0, 0) # Zwart
m = (34, 139, 34) # Bosgroen
q = (255, 255, 0) # Geel
t = (255, 140, 0) # Donkeroranje
y = (255, 20, 147) # Dieproze

afbeelding = [
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
title: Krab
---

![Een raster met 8 x 8 vierkanten dat een krab toont.](images/crab.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Wit
c = (0, 0, 0) # Zwart
v = (255, 0, 0) # Rood

afbeelding = [
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

![Een raster met 8 x 8 vierkanten dat een krokodil toont.](images/croc.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Wit
c = (0, 0, 0) # Zwart
f = (25, 25, 112) # Middernachtblauw
m = (34, 139, 34) # Bosgroen

afbeelding = [
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
title: Slang
---

![Een raster met 8 x 8 vierkanten dat een slang toont.](images/snake.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
 c = (0, 0, 0) # Zwart
 m = (34, 139, 34) # Bosgroen
 q = (255, 255, 0) # Geel
 v = (255, 0, 0) # Rood

afbeelding = [
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
title: Kikker
---

![Een raster met 8 x 8 vierkanten dat een kikker toont.](images/frog.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
c = (0, 0, 0) # Zwart
m = (34, 139, 34) # Bosgroen
q = (255, 255, 0) # Geel
v = (255, 0, 0) # Rood

afbeelding = [
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

**Vind:** de lijn waar staat `# Toon de afbeelding` en voeg een coderegel toe om je afbeelding op de LED matrix te tonen:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 12
---
afbeelding = [
  c, c, c, q, q, q, c, c,
  c, c, t, q, e, q, c, c,
  c, c, c, q, q, q, c, c,
  c, w, w, w, w, w, w, c,
  c, w, a, a, a, a, w, c,
  c, w, a, a, a, a, w, c,
  c, c, w, a, a, w, c, c,
  c, c, c, w, w, c, c, c]

# Toon de afbeelding 
sense.set_pixels(afbeelding)

--- /code ---

--- /task ---

--- task ---

Druk **Start** onderaan de editor om je afbeelding te zien op de LED-matrix.

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



