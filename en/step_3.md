## Display an image

The Astro Pi's LED matrix can display colours. In this step, you will display images from nature on the Astro Pi's LED matrix. 

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
An <span style="color: #0faeb0">**LED matrix**</span> is a grid of LEDs that can be controlled individually or as a group to create different lighting effects. The LED matrix on the Sense HAT has 64 LEDs displayed in an 8 x 8 grid. The LEDs can be programmed to produce a wide range of colours.
</p>

![A screenshot of the emulator window showing the Flight Unit with the LED matrix displaying a picture of a flower.](images/fu-pic.png)

--- task ---

Open the [Mission Zero starter project](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"}.

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

You will need to **copy** all of the code for your chosen image then **paste** it into your project below the line which says `# Add colour variables and image`. 

--- collapse ---

---
title: Fish
---

![A grid with 8 x 8 squares showing a fish.](images/fish.png)

Created by team chalka, Poland

```python
n = (204, 0, 204) # magenta
y = (255, 255, 0) # yellow
b = (51, 153, 255) # blue
c = (0, 0, 0) # black

image = [
b, b, n, b, b, b, b, b,
b, b, b, n, n, b, b, b,
n, b, y, y, y, y, b, b,
n, n, y, y, y, c, y, b,
n, n, n, y, y, y, y, b,
n, n, y, y, y, y, y, b,
n, b, y, n, n, y, b, b,
b, b, b, n, b, b, b, b,]

```

--- /collapse ---


--- collapse ---

---
title: Walrus
---

![A grid with 8 x 8 squares showing a walrus.](images/walrus.png)

Created by team Walrus, Finland

```python
 k = (0, 255, 255)
 c = (0, 0, 0)
 r = (139, 69, 19)
 w = (255, 255, 255)
 y = (184, 134, 11)   

 image = [
 h, h, h, h, h, h, h, h,
 h, h, r, r, r, h, h, h,
 h, r, r, r, r, r, h, h,
 h, r, c, r, c, r, r, r,
 h, y, y, y, y, y, r, r,
 h, k, w, r, w, r, r, r,
 h, k, w, r, w, r, r, r,
 y, y, r, r, r, r, r, r]

```

--- /collapse ---

--- collapse ---
---
title: Paxi
---

![A grid with 8 x 8 squares showing paxi.](images/paxi.png)

Created by team tony_pi, Italy

```python
p = (255, 0, 0) # Red
d = (34, 139, 34) # ForestGreen
c = (0, 0, 0) # Black 
b = (100, 149, 237) # CornflowerBlue
g = (0, 255, 0) # Green

image = [
  c, p, d, c, c, d, p, c,
	c, c, p, p, p, p, c, c,
	c, p, c, b, g, b, p, c,
	c, p, c, g, g, g, p, c,
	c, p, c, g, c, g, p, c,
	c, c, p, p, p, p, c, c,
	c, c, g, c, c, g, c, c,
	c, d, d, c, c, d, d, c]

```

--- /collapse ---
 
 
--- collapse ---
---
title: Dog
---

![A grid with 8 x 8 squares showing a dog head.](images/dog.png)

Created by team ptpr_07, Spain
```python

c = (0, 0, 0) # Black
d = (86, 71, 0) # Light Brown
o = (123, 61, 0) # Orange Brown
g = (155, 0, 134) # Deep Pink

image = [
    c, d, d, c, c, d, d, c,
    c, d, o, o, o, o, d, c,
    c, d, c, o, o, c, d, c,
    c, o, o, o, o, o, o, c,
    c, o, o, o, o, o, o, c,
    c, o, o, c, c, o, o, c,
    c, c, o, g, g, o, c, c,
    c, c, c, g, g, c, c, c]

```
 
--- /collapse ---
 
--- collapse ---
---
title: Chameleon
---

![A grid with 8 x 8 squares showing a rainbow coloured chameleon.](images/chameleon.png)

Created by team The_ETs, United Kingdom

```python

c = (0, 0, 0) # Black
b = (95, 65, 0) # Brown
w = (255, 255, 255) # white
r = (255, 0, 0) # Red
o = (255, 153, 28) # Orange
y = (255, 255, 0) # Yellow
g = (0, 255, 0) # Green
c = (0, 255, 255) # Cyan
p = (128, 0, 255) # Purple
m = (191, 0, 255) # Magenta

image = [
    w, w, r, r, o, w, w, w,
    w, r, r, o, o, y, w, w,
    r, c, o, o, y, y, g, w,
    r, o, o, y, y, g, g, c,
    b, b, y, b, b, g, b, c,
    w, w, w, w, w, w, w, p,
    w, w, w, w, m, w, w, p,
    w, w, w, w, w, m, p, w]

```

--- /collapse ---

--- collapse ---
---
title: Kite
---

![A grid with 8 x 8 squares showing a kite.](images/kite.png)

Created by team Val, Greece

```python

c = (0, 0, 0) # Black
g = (0, 255, 0) # Green
r = (255, 0, 0) # Red
y = (255, 255, 0) # Yellow
b = (0, 0, 255) # Blue
h = (0, 255, 255) # Cyan

image = [
    h, h, h, h, h, h, h, h, 
    h, h, h, b, b, r, r, h, 
    h, h, h, b, b, r, r, h, 
    h, h, h, y, y, g, g, h, 
    h, h, h, y, y, g, g, h,
    h, h, c, h, h, h, h, h, 
    h, c, h, h, h, h, h, h, 
    c, h, h, h, h, h, h, h]

```

--- /collapse ---

--- collapse ---
---
title: Chicken
---

![A grid with 8 x 8 squares showing a Chicken.](images/chicken.png)

Created by team Slepicky, Czech Republic

```python

w = (255, 255, 255) #  White                                                    			
r = (255, 0, 0) # Red
c = (0, 0, 0) # Black
q = (105, 105, 105) # Light Grey
y = (255, 255, 0) # Yellow
z = (79, 79, 79) # Dark Grey


image =  [
    w, w, r, r, r, w, w, w,
    w, r, q, q, z, w, w, z,
    w, q, c, q, q, w, z, q,
    y, z, q, q, q, q, q, z,
    w, r, q, q, q, q, z, q,
    w, r, q, z, z, z, q, z,
    w, w, w, z, q, y, z, w,
    w, w, w, w, y, y, w, w]

```

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
line_highlights: 18, 19
---
n = (204, 0, 204) # magenta
y = (255, 255, 0) # yellow
b = (51, 153, 255) # blue
c = (0, 0, 0) # black

image = [
  b, b, n, b, b, b, b, b,
  b, b, b, n, n, b, b, b,
  n, b, y, y, y, y, b, b,
  n, n, y, y, y, c, y, b,
  n, n, n, y, y, y, y, b,
  n, n, y, y, y, y, y, b,
  n, b, y, n, n, y, b, b,
  b, b, b, n, b, b, b, b,]

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

- Check that your code matches the code in the examples above
- Check that you have indented the code in your list
- Check that your list is surrounded by `[` and `]`
- Check that each colour variable in the list is separated by a comma

My image does not appear:

- Check that your `sense.set_pixels(image)` is not indented

--- /task ---


--- task --- 

**Save your progress** 

Now that you have displayed an image, you can save your program on the Mission Starter project by entering your team name, team members' names, and the classroom code given to you. You can reload your program on any device with an internet connection by entering your team name and classroom code. 

![Mission Zero Save button](images/mz_savebutton_v2.png)

--- /task --- 
