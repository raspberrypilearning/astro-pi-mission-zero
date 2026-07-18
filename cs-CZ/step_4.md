## Získej hodnoty ze senzoru

V tomto kroku nastavíš senzor barev a svítivosti. Tento senzor použiješ k měření množství červeného, zeleného a modrého světla, které na něho dopadá. These values will then be used to change one of the colours in your chosen image.

This means that the image can change depending on what the sensor sees. For example, an astronaut wearing a blue shirt would see a different version of the image from an astronaut wearing a red shirt.

In the whale image we used in the previous step, the background colour was black. We used the variable `c` to store its RGB colour code:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Use the colour sensor to change one of your colours.

Underneath the lines where you define the colours, add the following code:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

--- /code ---

--- /task ---

This code replaces the RGB values stored in `c` with the values for the colour detected by the sensor.

Tip: If you didn't use the variable `c` in your own image, replace `c` with one of the colour variables that you did use. This will allow the sensor to change that colour instead.

--- task ---

**Test:** Pomocí nástroje pro výběr barvy si zvol barvu, která se ti líbí, a pak svůj kód **spusť**. Barva tvého pozadí se změní. Opakuj tento test s novou barvou.

**Tip:** Po každé změně barvy musíš kliknout na tlačítko „Spustit“.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Now you have displayed an image and sensed a colour and used it in your program, and your code is ready for submission! 

You can save and submit your program using the form at the bottom of the code editor.
  
However, you may wish to add more images to your project, or make it come to life with animation. The next steps show you how to do this.
</p>

## Animate your project (optional)

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

**Test:** Spusť svůj kód znovu. Your program will display your sensed color instantly, and then loop back and forth for an animated display.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
If you would like to have more than two frames in your animation, you must make sure that the program will run for no more than 30 seconds. For example, if you have 10 images that each display for 1 second, you must change your `for` loop to repeat 3 times (10 * 3 = 30 seconds)
</p>

--- task ---

**Check for errors**

Můj kód má chyby v syntaxi nebo nemění snímky:
- Check that your `for` loop code matches the indentation in the example.
- Make sure you named your second image matrix `image2` and that it is placed outside and before the loop begins.
- Check that your `sleep` times are set to exactly `1` second to avoid running past the strict 30-second execution cutoff on the ISS.

--- /task ---

--- task ---

**Ulož si svůj postup**

Svůj program můžeš uložit do startovacího projektu výzvy zadáním názvu týmu, jmen členů týmu a kódu třídy, který ti byl přidělen. Program můžeš načíst na jakémkoli zařízení s připojením k internetu tak, že zadáš název týmu a kód třídy.

--- /task ---

--- task ---

--- collapse ---
---
title: Příklad dokončeného kódu s velrybou
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
title: Příklad dokončeného kódu s velrybou (včetně animace)
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
