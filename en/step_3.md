## Display an image

The Astro Pi's LED matrix can display colours. In this step, you will display images from nature on the Astro Pi's LED matrix. 

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
An <span style="color: #0faeb0">**LED matrix**</span> is a grid of LEDs that can be controlled individually or as a group to create different lighting effects. The LED matrix on the Sense HAT has 64 LEDs displayed in an 8 x 8 grid. The LEDs can be programmed to produce a wide range of colours.
</p>

![A screenshot of the emulator window showing the Flight Unit with the LED matrix displaying a picture of a flower.](images/fu-pic.png)

--- task ---

Open the [rpf.io/mzcode](http://rpf.io/mzcode){:target="_blank"} for the Mission Zero project.

You will see that a few lines of code have been added for you automatically.

This code connects to the Astro Pi, makes sure the Astro Pi's LED display is shown the correct way around and sets up the colour sensor. Leave the code there, because you'll need it.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
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

--- /code ---

![A screenshot of the Sense HAT emulator with lines of starter code displayed in the left-hand pane.](images/sense-hat-emulator2.png)

--- /task ---

### RGB Colours 

Colours can be created using different proportions of red, green, and blue. You can find out about RGB colours here:

[[[generic-theory-simple-colours]]]

The LED matrix is an 8 x 8 grid. Each LED on the grid can be set to a different colour. Here is a list of variables for 24 different colours. Each colour has a value for red, green, and blue:

[[[ambient-colours]]]

### Choose an image 

--- task ---

**Choose:** Pick an image to display from the options below. Python stores the information for an image in a list. The code for each image includes the colour variables used and the list.  

You will need to copy all of the code for your chosen image then paste it into your project beneath the line which says `# Add colour variables and image`. 

**Tip:** To indent a line, use the <kbd>Tab</kbd> key on your keyboard (usually above the Caps lock key on the keyboard) at the start of the line. The colour variables use single letters so the code lines up neatly.

--- collapse ---

---
title: Chicken
---

![A grid with 8 x 8 squares showing a chick in an egg.](images/chick.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Add colour variables and image
a = (255, 255, 255) # White
c = (0, 0, 0) # Black
e = (0, 0, 205) # MediumBlue
q = (255, 255, 0) # Yellow
t = (255, 140, 0) # DarkOrange
w = (255, 192, 203) # Pink

image = [
  c, c, c, q, q, q, c, c,
  c, c, t, q, e, q, c, c,
  c, c, c, q, q, q, c, c,
  c, w, w, w, w, w, w, c,
  c, w, a, a, a, a, w, c,
  c, w, a, a, a, a, w, c,
  c, c, w, a, a, w, c, c,
  c, c, c, w, w, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Flower
---

![A grid with 8 x 8 squares showing a pink flower on a green stem.](images/flower.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Add colour variables and image

c = (0, 0, 0) # Black
m = (34, 139, 34) # ForestGreen
q = (255, 255, 0) # Yellow
t = (255, 140, 0) # DarkOrange
y = (255, 20, 147) # DeepPink

image = [
  c, c, y, y, y, y, c, c,
  c, y, y, t, t, y, y, c,
  y, y, t, q, q, t, y, y,
  c, y, y, t, t, y, y, c,
  c, c, y, y, y, y, c, c,
  m, c, c, m, m, c, c, m,
  c, m, m, m, m, m, m, c,
  c, c, c, m, m, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Crab
---

![A grid with 8 x 8 squares showing a crab.](images/crab.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Add colour variables and image
a = (255, 255, 255) # White
c = (0, 0, 0) # Black
v = (255, 0, 0) # Red

image = [
  c, a, a, c, a, a, c, c,
  c, a, c, c, a, c, c, c,
  c, v, c, c, v, c, c, c,
  c, v, c, c, v, c, c, c,
  v, v, v, v, v, c, v, v,
  v, v, c, c, v, v, v, c,
  v, v, v, v, v, c, v, v,
  v, c, v, c, v, c, c, c]
 
--- /code ---

--- /collapse ---
 
 
--- collapse ---
---
title: Crocodile
---

![A grid with 8 x 8 squares showing a crocodile head.](images/croc.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Add colour variables and image
a = (255, 255, 255) # White
c = (0, 0, 0) # Black
f = (25, 25, 112) # MidnightBlue
m = (34, 139, 34) # ForestGreen

image = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

--- /code ---
 
 
--- /collapse ---
 
--- collapse ---
---
title: Snake
---

![A grid with 8 x 8 squares showing a snake.](images/snake.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Add colour variables and image
 c = (0, 0, 0) # Black
 m = (34, 139, 34) # ForestGreen
 q = (255, 255, 0) # Yellow
 v = (255, 0, 0) # Red

image = [
  c, c, c, c, c, c, c, m,
  c, m, m, m, m, m, m, m,
  c, m, c, c, c, c, c, c,
  c, m, m, m, m, m, c, c,
  c, c, c, c, c, m, c, c,
  q, m, q, m, m, m, c, c,
  m, m, m, c, c, c, c, c,
  v, c, c, c, c, c, c, c]
  
--- /code ---

--- /collapse ---

--- collapse ---
---
title: Frog
---

![A grid with 8 x 8 squares showing a frog.](images/frog.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
# Add colour variables and image
c = (0, 0, 0) # Black
m = (34, 139, 34) # ForestGreen
q = (255, 255, 0) # Yellow
v = (255, 0, 0) # Red

image = [
  c, m, m, m, c, m, m, m,
  c, m, q, m, c, m, q, m,
  m, m, m, m, m, m, m, m,
  m, v, v, v, v, v, v, v,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, m, m, m, c, m]

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Find:** the line which says `# Display the image` and add a line of code to display your image on the LED matrix:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 12
---
image = [
  c, c, c, q, q, q, c, c,
  c, c, t, q, e, q, c, c,
  c, c, c, q, q, q, c, c,
  c, w, w, w, w, w, w, c,
  c, w, a, a, a, a, w, c,
  c, w, a, a, a, a, w, c,
  c, c, w, a, a, w, c, c,
  c, c, c, w, w, c, c, c]

# Display the image
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Press **Run** at the bottom of the editor, to see your image displayed on the LED matrix.

--- /task ---

--- task ---

**Debug** 

My code has a syntax error:

- Check that you code matches the code in the examples above
- Check that you have indented the code in your list
- Check that your list is surrounded by `[` and `]`
- Check that each colour variable in the list is separated by a comma

My image does not appear:

- Check that your `sense.set_pixels(image)` is not indented

--- /task ---



