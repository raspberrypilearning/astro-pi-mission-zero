## Érzékeld a színt

In this step, you will set up the colour and brightness sensor. You will use this sensor to measure the amount of red, green, and blue light reaching the sensor. These values will then be used to change one of the colours in your chosen image.

This means that the image can change depending on what the sensor sees. For example, an astronaut wearing a blue shirt would see a different version of the image from an astronaut wearing a red shirt.

In the whale image we used in the previous step, the background colour was black. We used the variable `c` to store its RGB colour code:

--- code ---
---
Használd a színérzékelőt, hogy kiszínezd a hátteret.
line_highlights: 9, 10
---
Adj hozzá kódot a képet meghatározó lista elé, hogy kiolvasd a SenseHAT színérzékelőből a színt, majd a `c` változót állítsd be erre a színre fekete helyett.


--- task ---

Use the colour sensor to change one of your colours.

Underneath the lines where you define the colours, add the following code:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
Készíts egy ciklust
---
# Színváltozók és kép hozzáadása
kep = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

This code replaces the RGB values stored in `c` with the values for the colour detected by the sensor.

Tip: If you didn't use the variable `c` in your own image, replace `c` with one of the colour variables that you did use. This will allow the sensor to change that colour instead.

--- task ---

**Tesztelés:** Mozgasd a színcsúszkát egy általad választott színre, majd **futtasd** a kódodat. A háttérszín meg fog változni. Ismételd meg a tesztet egy másik színnel.

**Tipp:** Minden egyes alkalommal meg kell nyomnod a Futtatás gombot, ha megváltoztatod a színt.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Now you have displayed an image and sensed a colour and used it in your program, and your code is ready for submission! 

You can save and submit your program using the form at the bottom of the code editor.
  
However, you may wish to add more images to your project, or make it come to life with animation. The next steps show you how to do this.
</p>

## line_highlights: 2

Your Mission Zero program can run on the International Space Station (ISS) for up to 30 seconds. You can use this running time to display an animation on the LED matrix by switching between two or more different images.

--- task ---


**Add** a second image right below your `sense.set_pixels(image)` line of code. Give it the variable name `image2` and change a few pixels to make your animation frame look different. Then add a short pause after it.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
---
image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# Programkönyvtárak importálása

kep = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /code ---

--- /task ---

--- task ---

Most be kell húznod az összes kódot a `for` ciklus alatt, hogy a `for` cikluson **belül** legyen.

**Tipp:** Ha egyszerre több sort akarsz behúzni, jelöld ki az összeset, majd nyomd le a <kbd>Tab</kbd> billentyűt (általában a <kbd>Caps Lock</kbd> billentyű felett található).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 5
---
for i in range(28): rgb = sense.color # szín lekérése az érzékelőtől c = (rgb.red, rgb.green, rgb.blue)

kep = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

# Sense HAT beállítása
# Kép megjelenítése

  sense.set_pixels(kep)

--- /task ---

--- task ---

**Tesztelés:** Futtasd a kódodat még egyszer. Your program will display your sensed color instantly, and then loop back and forth for an animated display.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
If you would like to have more than two frames in your animation, you must make sure that the program will run for no more than 30 seconds. For example, if you have 10 images that each display for 1 second, you must change your `for` loop to repeat 3 times (10 * 3 = 30 seconds)
</p>

--- task --- **Check for errors**

# Kép megjelenítése
- kiolvassa a legfrissebb színt
- frissíti a kép háttérszínét
- várakozik egy másodpercig

--- /task ---

--- task ---

**Mentsd el a munkádat!**

Elmentheted a programodat a küldetés kezdőprojektjébe, ha megadod a csapatod nevét, a csapattagok nevét és a mentorodtól kapott osztálytermi kódot. Újra betöltheted a programodat bármely internetkapcsolattal rendelkező eszközön, ha megadod a csapatod nevét és az osztálytermi kódot.

--- /task ---

--- task --- --- collapse ---
---
line_highlights: 7
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
A kódom 30 másodpercnél tovább fut:

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image) --- /code --- --- /collapse --- --- collapse ---
---
title: Kész példakód
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
sense.set_pixels(kep) sleep(1)

# Add colour variables and image
sense.clear()

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

  # Display the first image sense.set_pixels(image) sleep(1) --- /code --- --- /collapse --- --- /task ---
