## Sense a colour

In this step, you will set up the colour luminosity sensor and use it to sense the amount of red, green, and blue reaching the sensor. This colour will then be used to colour in your chosen image. An astronaut walking up to the sensor in a blue shirt would see a different image than an astronaut in a red shirt. 

![An image displayed with a pink background on the LED matrix.](images/colour_background.png)

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
line_highlights: 9, 10
---

# Add colour variables and image

a = (255, 255, 255) # White
c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue

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

The Astro Pi Mission Zero program is allowed to run for up to 30 seconds. You can use this time to create an animation on your LED matrix by switching back and forth between two different images!

Your code will use a `for` loop to run 14 times. Because each loop takes 2 seconds (1 second per image), running it 14 times means your animation lasts exactly 28 seconds—perfectly under the 30-second limit!

--- task ---

**Add** a second image right below your first one. Give it the variable name `image1` and change a few pixels to make it look slightly different for your animation.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 11, 12, 13, 14, 15, 16, 17, 18, 19
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

image1 = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, f, f, c,
f, f, c, f, f, f, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

At the bottom of your code, set up your `for` loop to repeat `14` times and add the code to display your animation frame by frame.

**Tip:** Make sure the lines of code underneath `for i in range(14):` are indented so they sit **inside** the loop.

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
  # Display the first image
  sense.set_pixels(image)
  sleep(1)

  # Display the second image
  sense.set_pixels(image1)
  sleep(1)
  
--- /code ---

--- /task ---

--- task ---

Debug My code has a syntax error or doesn't run as expected:

Check that your loop matches the spacing and indentation in the examples.

Check that both image and image1 lists are surrounded by [ and ].

Check that your sleep times are set to exactly 1 second so it doesn't overrun the 30-second limit.

--- /task ---

--- task ---

Save your progress

You can save your program on the Mission Starter project by entering your team name, team members' names, and the classroom code given to you. You can reload your program on any device with an internet connection by entering your team name and classroom code.

--- /task ---

--- collapse ---

title: Completed code example (with Animation)
--- code ---
language: python
filename: main.py
line_numbers: false
Import the libraries
from sense_hat import SenseHat
from time import sleep

Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270)

Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

Add colour variables and image
a = (255, 255, 255) # White
c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue

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

image1 = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, f, f, c,
f, f, c, f, f, f, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14):

Display the first image
sense.set_pixels(image)
sleep(1)

Display the second image
sense.set_pixels(image1)
sleep(1)

--- /code ---

--- /collapse ---

--- /task ---
