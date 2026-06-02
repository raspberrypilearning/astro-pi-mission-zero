## Sense a colour

In this step, you will set up the colour luminosity sensor and use it to sense the amount of red, green, and blue reaching the sensor. This colour will then be used to colour in your chosen image. An astronaut walking up to the sensor in a blue shirt would see a different image than an astronaut in a red shirt. 

Whichever image you chose, the background uses the `c` variable, which is set to black.

--- task ---

Use the colour sensor to colour your background.

Add code before your image list to get the colour from the sensor and change your `c` background colour variable to use the colour sensed by the Sense HAT colour sensor instead of black.

**Tip:** You don't need to type the comments that start with '#' (they are there to explain the code). 

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 8, 9, 21
---
# Add colour variables and image

z = (153, 50, 204) # DarkOrchid
q = (255, 255, 0) # Yellow
d = (51, 153, 255) # blue

rgb = sense.color # get the colour from the sensor
c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [
  d, d, z, d, d, d, d, d,
  d, d, d, z, z, d, d, d,
  z, d, q, q, q, q, d, d,
  z, z, q, q, q, c, q, d,
  z, z, z, q, q, q, q, d,
  z, z, q, q, q, q, q, d,
  z, d, q, z, z, q, d, d,
  d, d, d, z, d, d, d, d
]

sense.set_pixels(image)
--- /code ---

--- /task ---

--- task ---

**Test:** Move the colour slider to a colour of your choice and then **run** your code. Your background colour will change. Repeat this test again with a new colour.

**Tip:** You will need to click 'Run' every time you change the colour.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Now you have sensed a colour and used it in your program, and your code is ready for submission! You can save and submit your program using the form at the bottom of the code editor.
  
However, you may wish to add more images to your project, or make it come to life with animation!
</p>

## Animate your project (Optional)

The Astro Pi Mission Zero program is allowed to run for up to 30 seconds. You can use this time to create a moving animation on your LED matrix by switching back and forth between two different images!

Your code will use a `for` loop to run 14 times. Because each loop takes 2 seconds (1 second per image frame), running it 14 times keeps your animation safely under the 30-second limit.

--- task ---

**Add** a second image right below your `sense.set_pixels(image)` line of code. Give it the variable name `image2` and shift a few pixels over to make your animation frame look different. Then add a short pause after it.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 13
---
sense.set_pixels(image)

# Extra images / frames go here:
image2 = [
  d, d, d, z, d, d, d, d,
  d, d, d, d, z, z, d, d,
  d, z, d, q, q, q, q, d,
  d, z, z, q, q, q, c, q,
  d, z, z, z, q, q, q, q,
  d, z, z, q, q, q, q, q,
  d, z, d, q, z, z, q, d,
  d, d, d, d, z, d, d, d
]

sleep(1)
--- /code ---

--- /task ---

--- task ---

At the very bottom of your code file, set up your `for` loop to repeat `14` times and alternate between displaying `image2` and `image`.

**Tip:** Make sure the lines of code underneath `for i in range(14):` are indented with spaces so they sit **inside** the loop block.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 2, 4, 5, 7, 8
---
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

**Test:** Run your code again. Your program will light up with your sensed color instantly, and then loop smoothly back and forth for an animated display!

--- /task ---

--- task ---

**Debug**

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
title: Completed code example (with Animation)
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

z = (153, 50, 204) # DarkOrchid
q = (255, 255, 0) # Yellow
d = (51, 153, 255) # blue

rgb = sense.color # get the colour from the sensor
c = (rgb.red, rgb.green, rgb.blue)

image = [
  d, d, z, d, d, d, d, d,
  d, d, d, z, z, d, d, d,
  z, d, q, q, q, q, d, d,
  z, z, q, q, q, c, q, d,
  z, z, z, q, q, q, q, d,
  z, z, q, q, q, q, q, d,
  z, d, q, z, z, q, d, d,
  d, d, d, z, d, d, d, d
]

sense.set_pixels(image)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
image2 = [
  d, d, d, z, d, d, d, d,
  d, d, d, d, z, z, d, d,
  d, z, d, q, q, q, q, d,
  d, z, z, q, q, q, c, q,
  d, z, z, z, q, q, q, q,
  d, z, z, q, q, q, q, q,
  d, z, d, q, z, z, q, d,
  d, d, d, d, z, d, d, d
]

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
--- /task ---
