## Zaznajte barve

V tem koraku boste nastavili senzor barve in svetlosti. Z njim boste merili količino rdeče, zelene in modre svetlobe, ki doseže senzor. Te vrednosti boste nato uporabili za spremembo ene od barv na izbrani sliki.

To pomeni, da se slika lahko spreminja glede na to, kaj senzor vidi. Na primer, astronavt v modri majici bi lahko videl drugačno različico slike kot astronavt v rdeči majici.

Na sliki kita, ki smo jo uporabili v prejšnjem koraku, je bila barva ozadja črna. Za shranjevanje barvne kode RGB smo uporabili spremenljivko `c`:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Za spremembo barve uporabite barvni senzor.

Pod vrstice, kjer definirate barve, dodajte naslednjo kodo:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

--- /code ---

--- /task ---

Ta koda nadomesti vrednosti RGB, shranjene v spremenljivki `c` , z vrednostmi za barvo, ki jo zazna senzor.

Nasvet: Če v svoji sliki niste uporabili spremenljivke `c`, zamenjajte `c` z eno od barvnih spremenljivk, ki ste jih uporabili. To bo senzorju omogočilo, da spremeni to barvo.

--- task ---

**Preizkus:** Premaknite barvni drsnik na barvo po vaši izbiri in nato **zaženite** svojo kodo. Vaša barva ozadja se bo spremenila. Ponovno ponovite test z novo barvo.

**Namig:** Vsakič, ko spremenite barvo, boste morali klikniti »Zaženi«.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Zdaj, ko ste prikazali sliko in zaznali barvo ter jo uporabili v svojem programu, je vaša koda pripravljena za oddajo! 

Program lahko shranite in oddate z uporabo obrazca na dnu urejevalnika kode.
  
Vendar pa mu boste morda želeli dodati še več slik ali pa ga poživiti z animacijo. Naslednji koraki vam bodo pokazali, kako to storiti.
</p>

## Animirajte svoj projekt (neobvezno)

Your Mission Zero program can run on the International Space Station (ISS) for up to 30 seconds. You can use this running time to display an animation on the LED matrix by switching between two or more different images.

--- task ---


**Add** a second image right below your `sense.set_pixels(image)` line of code. Give it the variable name `image2` and change a few pixels to make your animation frame look different. Then add a short pause after it.

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

At the very bottom of your code file, set up your `for` loop to repeat `14` times and alternate between displaying `image` and `image2` pausing for 1 second on each frame.

**Tip:** Make sure the lines of code underneath `for i in range(14):` are indented with a space so they sit **inside** the loop block.

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

**Preizkus:** Znova zaženite kodo. Your program will display your sensed color instantly, and then loop back and forth for an animated display.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
If you would like to have more than two frames in your animation, you must make sure that the program will run for no more than 30 seconds. For example, if you have 10 images that each display for 1 second, you must change your `for` loop to repeat 3 times (10 * 3 = 30 seconds)
</p>

--- task ---

**Check for errors**

My code has a syntax error or doesn't change frames:
- Check that your `for` loop code matches the indentation in the example.
- Make sure you named your second image matrix `image2` and that it is placed outside and before the loop begins.
- Check that your `sleep` times are set to exactly `1` second to avoid running past the strict 30-second execution cutoff on the ISS.

--- /task ---

--- task ---

**Shrani svoj napredek**

Svoj program lahko shranite v projekt Mission Starter tako, da vnesete ime svoje ekipe, imena članov ekipe in kodo učilnice, ki ste jo prejeli. Svoj program lahko znova naložite v katero koli napravo z internetno povezavo, tako da vnesete ime ekipe in kodo učilnice.

--- /task ---

--- task ---

--- collapse ---
---
title: Primer dokončane kode s kitom
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
title: Primer dokončane kode z animiranim kitom
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
