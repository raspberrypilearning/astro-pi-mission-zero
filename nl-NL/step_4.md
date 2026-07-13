## Een kleur waarnemen

In this step, you will set up the colour and brightness sensor. In deze stap ga je de kleurhelderheidssensor instellen en deze gebruiken om de hoeveelheid rood, groen en blauw die de sensor bereiken waar te nemen. Deze kleur zal dan worden gebruikt om je afbeelding in te kleuren.

This means that the image can change depending on what the sensor sees. Een astronaut die in een blauw shirt naar de sensor loopt, ziet een ander beeld dan een astronaut in een rood shirt.

In the whale image we used in the previous step, the background colour was black. We used the variable `c` to store its RGB colour code:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0) --- /code ---


--- task ---

Gebruik de kleursensor om je achtergrond in te kleuren.

Underneath the lines where you define the colours, add the following code:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---
# de achtergrondkleur van de afbeelding bijwerken
rgb = sense.color # haal de kleur uit de sensor c = (rgb.red, rgb.green, rgb.blue) # gebruik de waargenomen kleur

This code replaces the RGB values stored in `c` with the values for the colour detected by the sensor.

Welke afbeelding je ook kiest, de achtergrond gebruikt de variabele `c` die is ingesteld op zwart. This will allow the sensor to change that colour instead.

--- task ---

**Test:** Verplaats de kleurschuifregelaar naar een kleur van je keuze en voer **** je code uit. De achtergrondkleur zal veranderen. Herhaal deze test met een nieuwe kleur.

**Tip:** Je moet elke keer als je de kleur wijzigt op 'Run' klikken.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Now you have displayed an image and sensed a colour and used it in your program, and your code is ready for submission! 

You can save and submit your program using the form at the bottom of the code editor.
  
However, you may wish to add more images to your project, or make it come to life with animation. The next steps show you how to do this.
</p>

## Animate your project (optional)

Het Astro Pi Mission Zero-programma mag maximaal 30 seconden draaien. Deze tijd gebruik je om de kleursensor herhaaldelijk te controleren en de afbeelding bij te werken.

--- task ---


**Voeg** code hierboven toe om `for` lus in te stellen voor `28` herhalingen. Give it the variable name `image2` and change a few pixels to make your animation frame look different. Then add a short pause after it.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
---
afbeelding = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

sense.set_pixels(image)

# Extra images / frames go here:

afbeelding = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /code ---

--- /task ---

--- task ---

At the very bottom of your code file, set up your `for` loop to repeat `14` times and alternate between displaying `image` and `image2` pausing for 1 second on each frame.

**Tip:** Zorg ervoor dat deze regel code wordt ingesprongen in je `for` lus.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7, 8
---
images/fish.png

sense.set_pixels(afbeelding) sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  sense.set_pixels(afbeelding) sleep(1)

--- /task ---

--- task ---

**Test:** Voer je code opnieuw uit. Wanneer je project klaar is met uitvoeren, zal de LED matrix worden leegemaakt, waardoor alle lichtjes op zwart gaan (uit).

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
If you would like to have more than two frames in your animation, you must make sure that the program will run for no more than 30 seconds. For example, if you have 10 images that each display for 1 second, you must change your `for` loop to repeat 3 times (10 * 3 = 30 seconds)
</p>

**Test:** Voer je code opnieuw uit.

Mijn code heeft een syntax fout of wordt niet uitgevoerd zoals verwacht:
- Controleer dat je je code in je `for`lus hebt ingesprongen
- Make sure you named your second image matrix `image2` and that it is placed outside and before the loop begins.
- Check that your `sleep` times are set to exactly `1` second to avoid running past the strict 30-second execution cutoff on the ISS.

--- /task ---

--- task ---

**Sla je voortgang op**

Je kunt je programma opslaan in het Mission Start-project door je teamnaam, de namen van de teamleden en de klascode die je hebt gekregen in te voeren. Je kunt je programma herladen op elk apparaat met een internetverbinding door je teamnaam en klascode in te voeren.

--- /task ---

--- collapse ---
---
title: Completed Whale code example
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
z = (153, 50, 204) # Donkerorchidee q = (255, 255, 0) # Geel d = (51, 153, 255) # blauw c = (0, 0, 0) # Zwart

# sense.clear()
for i in range(28): rgb = sense.color # haal de kleur uit de sensor c = (rgb.red, rgb.green, rgb.blue)

afbeelding = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /collapse ---
---
title: Voorbeeld van een voltooide code
---

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Fouten oplossen (Debuggen)
from sense_hat import SenseHat from time import sleep

# Stel de Sense HAT in
sense = SenseHat() sense.set_rotation(270)

# Voeg code toe voor je afbeeldingenlijst om de kleur van de sensor te krijgen en verander je `c` achtergrondkleurvariabele om de kleur te gebruiken die wordt gedetecteerd door de Sense HAT-kleurensensor in plaats van zwart.
for i in range(28): rgb = sense.color # haal de kleur uit de sensor c = (rgb.red, rgb.green, rgb.blue)

# Add colour variables and image
z = (153, 50, 204) # Donkerorchidee q = (255, 255, 0) # Geel d = (51, 153, 255) # blauw c = (0, 0, 0) # Zwart

# de laatste kleur waarnemen
for i in range(28): rgb = sense.color # haal de kleur uit de sensor c = (rgb.red, rgb.green, rgb.blue)

afbeelding = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

sense.set_pixels(afbeelding)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
images/savebutton_nl.png

sense.set_pixels(afbeelding) sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  sense.set_pixels(afbeelding) sleep(1)
