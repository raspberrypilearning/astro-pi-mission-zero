## Sense a colour

In this step, you will set up the colour luminosity sensor and use it to sense the amount of red, green, and blue reaching the sensor. This colour will then be used to colour in your chosen image. An astronaut walking up to the sensor in a blue shirt would see a different image than an astronaut in a red shirt. 

This tutorial uses the variable c (initially set to black) to store the color detected by the color sensor.

--- task ---

Use the colour sensor to change one of your colours.

Add this code before your image list to get the colour from the sensor and change your `c` variable to use the colour sensed by the Sense HAT colour sensor instead of black.

**Tip:** You don't need to type the comments that start with '#' (they are there to explain the code). 

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 8, 9, 10,
---
# Add colour variables and image
a = (255, 255, 255) # White
c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor
c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(image)
--- /code ---

--- /task ---

--- task ---

**Test:** Move the colour slider to a colour of your choice and then **run** your code. Your background colour will change. Repeat this test again with a new colour.

**Tip:** You will need to click 'Run' every time you change the colour.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Now you have displayed an image and sensed a colour and used it in your program, and your code is ready for submission! You can save and submit your program using the form at the bottom of the code editor.
  
However, you may wish to add more images to your project, or make it come to life with animation.
</p>

## Animate your project (Optional)

The Astro Pi Mission Zero program is allowed to run for up to 30 seconds. You can use this time to create an animation on your LED matrix by switching back and forth between two different images.

--- task ---

**Add** a second image right below your `sense.set_pixels(image)` line of code. Give it the variable name `image2` and change a few pixels to make your animation frame look different. Then add a short pause after it.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
image = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# Extra images / frames go here:

image2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

At the very bottom of your code file, set up your `for` loop to repeat `14` times and alternate between displaying `image` and `image2` pausing for 1 second on each frame.

**Tip:** Make sure the lines of code underneath `for i in range(14):` are indented with a space so they sit **inside** the loop block.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
image2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14):
  # Display the second image
  sense.set_pixels(image2)
  sleep(1)

  # Display the first image
  sense.set_pixels(image)
  sleep(1)
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code again. Your program will display your sensed color instantly, and then loop back and forth for an animated display.

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

**Save your progress**

You can save your program on the Mission Starter project by entering your team name, team members' names, and the classroom code given to you. You can reload your program on any device with an internet connection by entering your team name and classroom code.

--- /task ---

--- task ---
--- collapse ---
---
title: Completed Whale code example (with Animation)
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image
a = (255, 255, 255) # White
c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor
c = (rgb.red, rgb.green, rgb.blue)

image = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
image2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14):
  # Display the second image
  sense.set_pixels(image2)
  sleep(1)

  # Display the first image
  sense.set_pixels(image)
  sleep(1)
--- /code ---

--- /collapse ---
--- collapse ---
---
title: Completed Storm code example (with Animation)
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue
t = (255, 255, 0)   # Pure Yellow

rgb = sense.color # get the colour from the sensor
t = (rgb.red, rgb.green, rgb.blue)
image = [
c, c, c, c, c, c, c, c,
c, c, f, f, f, f, c, c,
c, f, f, f, f, f, f, c,
c, g, c, g, c, c, c, c,
c, c, c, c, c, g, c, c,
c, c, c, c, c, c, c, c,
c, c, g, c, c, c, c, c,
c, g, c, c, c, c, c, c]

sense.set_pixels(image)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
image2 = [
c, c, c, c, c, c, c, c,
c, c, f, f, f, f, c, c,
c, f, f, f, f, f, f, c,
c, c, c, c, c, c, c, c,
c, g, c, g, c, c, c, c,
c, c, c, c, c, g, c, c,
c, c, c, c, c, c, c, c,
c, c, g, c, c, c, c, c]

image3 = [
c, c, c, c, c, c, c, c,
c, c, f, f, f, f, c, c,
c, f, f, f, f, f, f, c,
c, c, g, c, c, c, c, c,
c, c, c, c, c, c, c, c,
c, g, c, g, c, c, c, c,
c, c, c, c, c, g, c, c,
c, c, c, c, c, c, c, c]

image3l = [
c, c, c, c, c, c, c, c,
c, c, f, f, f, f, c, c,
c, f, f, f, f, f, f, c,
c, c, g, c, t, c, c, c,
c, c, c, t, t, c, c, c,
c, g, t, t, c, c, c, c,
c, c, t, c, c, g, c, c,
c, c, c, c, c, c, c, c]

image4 = [
c, c, c, c, c, c, c, c,
c, c, f, f, f, f, c, c,
c, f, f, f, f, f, f, c,
c, c, c, c, c, c, c, c,
c, c, g, c, c, c, c, c,
c, c, c, c, c, c, c, c,
c, g, c, g, c, c, c, c,
c, c, c, c, c, g, c, c]

image5 = [
c, c, c, c, c, c, c, c,
c, c, f, f, f, f, c, c,
c, f, f, f, f, f, f, c,
c, c, c, c, c, g, c, c,
c, c, c, c, c, c, c, c,
c, c, g, c, c, c, c, c,
c, c, c, c, c, c, c, c,
c, g, c, g, c, c, c, c]

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(15):
  # Display the second image
  sense.set_pixels(image)
  sleep(0.3)

  # Display the first image
  sense.set_pixels(image2)
  sleep(0.3)
  sense.set_pixels(image3)
  sleep(0.3)
  sense.set_pixels(image3l)
  sleep(0.2)
  sense.set_pixels(image4)
  sleep(0.3)
  sense.set_pixels(image5)
  sleep(0.3)
--- /collapse ---
--- /task ---
