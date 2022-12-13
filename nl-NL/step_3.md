## Toon een afbeelding

De LED-matrix van de Astro Pi kan kleuren weergeven. In deze stap zul je afbeeldingen van de natuur weergeven op de LED-matrix van de Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Een <span style="color: #0faeb0">**LED-matrix**</span> is een raster van LED's die afzonderlijk of als groep kunnen worden aangestuurd om verschillende lichteffecten te creëren. De LED-matrix op de Sense HAT heeft 64 LED's die worden weergegeven in een 8 x 8 raster. De LED's kunnen worden geprogrammeerd om een breed scala aan kleuren te produceren.
</p>

![Een screenshot van het emulatorvenster van de Flight Unit met de LED-matrix waarop een afbeelding van een bloem te zien is.](images/fu-pic.png)

--- task ---

Open het [Mission Zero-startproject](https://missions.astro-pi.org/nl-NL/mz/code_submissions/new){:target="_blank"}.

Je zult zien dat er automatisch enkele regels met code voor je zijn toegevoegd.

Deze code maakt verbinding met de Astro Pi en zorgt ervoor dat het LED-display van de Astro Pi op de juiste manier wordt weergegeven en doet de set up van de kleurensensor. Laat de code staan, want je hebt hem nodig.

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

# Stel de Sense HAT in
sense = SenseHat() 
sense.set_rotation(270)

# Stel de kleurensensor in
sense.color.gain = 60 # Stel de gevoeligheid van de sensor in 
sense.color.integration_cycles = 64 # Het interval waarmee de meting wordt uitgevoerd

--- /code ---

![Een schermafbeelding van de Sense HAT emulator met enkele regels startcode weergegeven in het linkervenster.](images/sense-hat-emulator2.png)

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
title: Kip
---

![Een raster met 8 x 8 vierkanten met een kuiken in een ei.](images/chick.png)

--- code ---
---
language: python 
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Wit
c = (0, 0, 0) # Zwart
e = (0, 0, 205) # Middelblauw
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

![Een raster met 8 x 8 vierkanten met een roze bloem op een groene stengel.](images/flower.png)

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
y = (255, 20, 147) # Donkerroze

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

![Een raster met 8 x 8 vierkanten met daarop een krab.](images/crab.png)

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

![Een raster met 8 x 8 vierkanten met een krokodillenkop.](images/croc.png)

--- code ---
---
language: python 
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Wit
c = (0, 0, 0) # Zwart
f = (25, 25, 112) # MidnightBlue
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

![Een raster met 8 x 8 vierkanten met een slang.](images/snake.png)

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

![Een raster met 8 x 8 vierkanten met een kikker.](images/frog.png)

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

**Zoek:** de regel `# Toon de afbeelding` en voeg code toe om je afbeelding op de LED matrix weer te geven:

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

# Geef de afbeelding weer 
sense.set_pixels(afbeelding)

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



