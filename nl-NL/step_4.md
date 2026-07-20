## Een kleur waarnemen

In deze stap stel je de kleur- en helderheidssensor in. Met deze sensor meet je de hoeveelheid rood, groen en blauw licht die de sensor bereikt. Deze waarden worden vervolgens gebruikt om een van de kleuren in de door jouw gekozen afbeelding te wijzigen.

Dit betekent dat het beeld kan veranderen afhankelijk van wat de sensor waarneemt. Een astronaut die bijvoorbeeld een blauw shirt draagt, ziet een andere versie van het beeld dan een astronaut die een rood shirt draagt.

In de walvisafbeelding die we in de vorige stap gebruikten, was de achtergrondkleur zwart. We gebruikten de variabele `c` om de RGB-kleurcode op te slaan:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Gebruik de kleursensor om een van je kleuren te veranderen.

Voeg onder de regels waar je de kleuren definieert de volgende code toe:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

--- /code ---

--- /task ---

Deze code vervangt de RGB-waarden die zijn opgeslagen in `c` door de waarden voor de kleur die door de sensor is gedetecteerd.

Tip: Als je de variabele `c` niet in je eigen afbeelding hebt gebruikt, vervang dan `c` door een van de kleurvariabelen die je wél hebt gebruikt. Hierdoor kan de sensor die kleur veranderen.

--- task ---

**Test:** Verplaats de kleurschuifregelaar naar een kleur van je keuze en voer **** je code uit. De achtergrondkleur zal veranderen. Herhaal deze test met een nieuwe kleur.

**Tip:** Je moet elke keer als je de kleur wijzigt op 'Run' klikken.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Je hebt nu een afbeelding weergegeven, een kleur gedetecteerd en deze in je programma gebruikt, en je code is klaar om in te dienen! 

Je kunt je programma opslaan en indienen via het formulier onderaan de code-editor.
  
Je kunt er echter ook voor kiezen om meer afbeeldingen aan jouw project toe te voegen, of het tot leven te brengen met animatie. De volgende stappen laten zien hoe je dit doet.
</p>

## Animeer je project (optioneel)

Jouw Mission Zero-programma kan tot 30 seconden lang op het Internationale Ruimtestation (ISS) draaien. Je kunt deze tijd gebruiken om een animatie op de LED-matrix weer te geven door te schakelen tussen twee of meer verschillende afbeeldingen.

--- task ---


**Voeg** een tweede afbeelding direct onder je `sense.set_pixels(afbeelding)` regel code toe. Geef het de variabelenaam `afbeelding2` en verander een paar pixels om je animatieframe er anders uit te laten zien. Voeg daarna een korte pauze toe.

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

Helemaal onderaan je codebestand moet je je `for` lus zo instellen dat deze `14` keer herhaalt en afwisselend `afbeelding` en `afbeelding2` weergeeft, met een pauze van 1 seconde tussen elk frame.

**Tip:** Zorg ervoor dat de regels code onder `for i in range(14):` ingesprongen zijn met een spatie, zodat ze **binnen** het lusblok vallen.

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

**Test:** Voer je code opnieuw uit. Je programma laat meteen de kleur zien die de sensor meet, daarna beweegt de kleur heen en weer als een animatie.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Als je meer dan twee frames in je animatie wilt hebben, moet je ervoor zorgen dat het programma niet langer dan 30 seconden duurt. Als je bijvoorbeeld 10 afbeeldingen hebt die elk 1 seconde worden weergegeven, moet je je `for`-lus aanpassen zodat deze 3 keer wordt herhaald (10 * 3 = 30 seconden)
</p>

--- task ---

**Controleer op fouten**

Mijn code bevat een syntaxfout of wisselt niet van frame:
- Controleer of de inspringing van je `for` luscode overeenkomt met de inspringing in het voorbeeld.
- Zorg ervoor dat je je tweede afbeeldingsmatrix de naam `afbeelding2` hebt gegeven en dat deze buiten en vóór het begin van de lus is geplaatst.
- Controleer of je `sleep` tijden precies zijn ingesteld op `1` seconde om te voorkomen dat de strikte uitvoeringslimiet van 30 seconden op het ISS wordt overschreden.

--- /task ---

--- task ---

**Sla je voortgang op**

Je kunt je programma opslaan in het Mission Start-project door je teamnaam, de namen van de teamleden en de klascode die je hebt gekregen in te voeren. Je kunt je programma herladen op elk apparaat met een internetverbinding door je teamnaam en klascode in te voeren.

--- /task ---

--- task ---

--- collapse ---
---
title: Voltooide walvis-codevoorbeeld
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
title: Voltooide walvis-codevoorbeeld (met animatie)
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
