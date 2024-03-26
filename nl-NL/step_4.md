## Een kleur waarnemen

In deze stap ga je de kleurhelderheidssensor instellen en deze gebruiken om de hoeveelheid rood, groen en blauw die de sensor bereiken waar te nemen. Deze kleur zal dan worden gebruikt om je afbeelding in te kleuren. Een astronaut die in een blauw shirt naar de sensor loopt, ziet een ander beeld dan een astronaut in een rood shirt.

![afbeelding weergegeven met een roze achtergrond op de LED-matrix](images/colour_background.png)

Welke afbeelding je ook kiest, de achtergrond gebruikt de variabele `c` die is ingesteld op zwart.

--- task ---

Gebruik de kleursensor om je achtergrond in te kleuren.

Voeg code toe voor je afbeeldingenlijst om de kleur van de sensor te krijgen en verander je `c` achtergrondkleurvariabele om de kleur te gebruiken die wordt gedetecteerd door de Sense HAT-kleurensensor in plaats van zwart.

**Tip:**Je hoeft de opmerkingen die beginnen met '#' niet in te typen (ze zijn er om de code uit te leggen).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9-10
---

# Kleurvariabelen en afbeelding toevoegen

c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange y = (255, 20, 147) # DeepPink

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

**Test:** Verplaats de kleurschuifregelaar naar een kleur van je keuze en voer **** je code uit. De achtergrondkleur zal veranderen. Herhaal deze test met een nieuwe kleur.

**Tip:** Je moet elke keer als je de kleur wijzigt op 'Run' klikken.

--- /task ---

## Herhaal je programma

Het Astro Pi Mission Zero-programma mag maximaal 30 seconden draaien. Deze tijd gebruik je om de kleursensor herhaaldelijk te controleren en de afbeelding bij te werken.

Je code gebruikt een `for` lus om 28 keer te worden uitgevoerd. **Elke** keer zal het:
+ de laatste kleur waarnemen
+ de achtergrondkleur van de afbeelding bijwerken
+ pauzeren gedurende een seconde

--- task ---

**Vind** je `rgb = sense.color` code regel.

**Voeg** code hierboven toe om `for` lus in te stellen voor `28` herhalingen.

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

Je moet nu al je code hieronder de `for` lus inspringen zodat deze **in** de `for` lus wordt geplaatst.

**Tip:** Om meerdere lijnen tegelijk te laten inspringen markeer je de regels die je wilt inspringen en druk vervolgens op de <kbd>Tab</kbd> toets op je toetsenbord (meestal boven de <kbd>Caps Lock</kbd> toets op het toetsenbord).

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

Voeg onderaan je code een `sleep` van één seconde toe in je lus:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 4
---

  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Tip:** Zorg ervoor dat deze regel code wordt ingesprongen in je `for` lus.

--- /task ---

--- task ---

**Test:** Voer je code uit en verander de kleurenkiezer meerdere keren terwijl je project wordt uitgevoerd. Controleer of je afbeeldingsupdates de waargenomen kleur bij de volgende keer worden gebruikt.

De afbeelding stopt met bijwerken wanneer de lus klaar is, zodat het programma niet langer dan 30 seconden wordt uitgevoerd.

--- /task ---

--- task ---

**Fouten oplossen (Debuggen)**

Mijn code heeft een syntax fout of wordt niet uitgevoerd zoals verwacht:

- Controleer of je code overeenkomt met de code in de bovenstaande voorbeelden
- Controleer dat je je code in je `for`lus hebt ingesprongen
- Controleer of je lijst is omgeven door `[` en `]`
- Controleer of elke kleurvariabele in de lijst is gescheiden door een komma

Mijn code loopt langer dan 30 seconden:

- Verminder het aantal keren dat je for lus loopt, van 28 tot 25 of zelfs 20 keer.
- Verminder de lengte van de sleep, van 1 seconde naar 0.5 seconde.

--- /task ---

--- task ---

Voeg `sense.clear()` aan het einde van de code toe om de afbeelding aan het einde van de lus te wissen. Dit zal je helpen te zien wanneer je animatie klaar is met draaien.

**Tip:** Zorg ervoor dat je de `sense.clear()` code **niet** laat inspringen, aangezien je wilt dat deze slechts één keer wordt uitgevoerd aan het einde van je animatie.

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

**Test:** Voer je code opnieuw uit. Wanneer je project klaar is met uitvoeren, zal de LED matrix worden leegemaakt, waardoor alle lichtjes op zwart gaan (uit).

--- /task ---

--- task ---

**Fouten oplossen (Debuggen)**

De LED-matrix wordt elke seconde zwart:

- Controleer of je de `sense.clear()` code binnen je `for` lus niet hebt ingesprongen

--- /task ---

--- task ---

Voeg code toe om de LED-matrix te wissen in een kleur naar keuze. Maak een variabele met de naam `x` om je nieuwe kleur op te slaan.

Je kunt je eigen kleur mengen of de waarden uit de lijst met kleuren gebruiken om je nieuwe `x`kleur te maken.

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

**Test:** Voer je code opnieuw uit. Wanneer je project klaar is, wordt de LED-matrix gewist in de door jou gekozen kleur. Je kunt de kleur zo vaak veranderen en testen als je wil.

--- /task ---

--- task ---

--- collapse ---

---
title: Voorbeeld van een voltooide code
---

![Een raster met 8 x 8 vierkanten met een roze bloem op een groene stengel.](images/flower.png)

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
