## Detectează o culoare

In this step, you will set up the colour and brightness sensor. You will use this sensor to measure the amount of red, green, and blue light reaching the sensor. These values will then be used to change one of the colours in your chosen image.

This means that the image can change depending on what the sensor sees. For example, an astronaut wearing a blue shirt would see a different version of the image from an astronaut wearing a red shirt.

In the whale image we used in the previous step, the background colour was black. We used the variable `c` to store its RGB colour code:

--- code ---
---
Utilizează senzorul de culoare pentru a colora fundalul.
line_highlights: 9, 10
---
Adaugă cod înainte de lista ta de imagini pentru a obține culoarea de la senzor și a schimba variabila de culoare `c` de fundal pentru a utiliza culoarea simțită de către senzorul de culoare Sense HAT în loc de negru.


--- task ---

Use the colour sensor to change one of your colours.

Underneath the lines where you define the colours, add the following code:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
Repetă programul tău
---
# Adaugă variabile de culoare și imagine
imagine = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

This code replaces the RGB values stored in `c` with the values for the colour detected by the sensor.

Tip: If you didn't use the variable `c` in your own image, replace `c` with one of the colour variables that you did use. This will allow the sensor to change that colour instead.

--- task ---

**Test:** Mută glisorul de culori la o culoare aleasă de tine și apoi **execută** codul tău. Culoarea de fundal se va schimba. Repetați acest test din nou cu o nouă culoare.

**Sfat:** Va trebui să apeși pe 'Rulează' de fiecare dată când schimbi culoarea.

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

# Importă bibliotecile

imagine = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /code ---

--- /task ---

--- task ---

Acum trebuie să indentezi tot codul de sub bucla `for` astfel încât să fie **în interiorul** buclei `for`.

**Sfat:** Pentru a indenta mai multe linii, evidențiază liniile pe care vrei să le indentezi, apoi apasă tasta <kbd>Tab</kbd> de pe tastatură (de obicei deasupra tastei <kbd>Caps Lock</kbd> de pe tastatură).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 5
---
for i in range(28): rgb = sense.color # obține culoarea de la senzor c = (rgb.red, rgb.green, rgb.blue)

imagine = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

# Configurează Sense HAT
# Afișează imaginea

  sense.set_pixels(imagine)

--- /task ---

--- task ---

**Test:** Rulează codul din nou. Your program will display your sensed color instantly, and then loop back and forth for an animated display.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
If you would like to have more than two frames in your animation, you must make sure that the program will run for no more than 30 seconds. For example, if you have 10 images that each display for 1 second, you must change your `for` loop to repeat 3 times (10 * 3 = 30 seconds)
</p>

--- task --- **Check for errors**

# Afișează imaginea
- detecta cea mai recentă culoare
- actualiza culoarea de fundal a imaginii
- face pauză o secundă

--- /task ---

--- task ---

**Salvează-ți progresul**

Poți salva programul tău în proiectul Mission Starter introducând numele echipei, numele membrilor echipei și codul de clasă care ți-a fost dat. Poți reîncărca programul tău pe orice dispozitiv cu o conexiune la internet prin introducerea numelui echipei și a codului de clasă.

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
Codul meu rulează mai mult de 30 de secunde:

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image) --- /code --- --- /collapse --- --- collapse ---
---
title: Exemplu de cod completat
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
sense.set_pixels(imagine) sleep(1)

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
