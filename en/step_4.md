## Sense a colour

In this step, you will set up the colour luminosity sensor and use it to sense the amount of red, green, and blue reaching the sensor. This colour will then be used to colour in your chosen image. An astronaut walking up to the sensor in a blue shirt would see a different image than an astronaut in a red shirt. 

<mark>add an image with a different background colour not black</mark>

--- task ---

Find the `# Set up the colour sensor` comment and below it enter the code to set up the colour sensor.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 2,3
---
# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken
--- /code ---

**Tip:** You don't need to type the comments which start with '#' (they are there to explain the code). 

--- /task ---

Whichever image you chose, the background uses the `c` variable which is set to black. 

--- task ---

Use the colour sensor to colour your background.

Add code to update your `c` background colour variable to use the colour sensed by the Sense HAT colour sensor instead of black.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 2-3
---
# Set LED colours
rgb = sense.color # get the colour from the sensor
c = (rgb.red, rgb.green, rgb.blue)
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

**Test:** Move the colour slider to a colour of your choice and run your code. Your background colour will change. 

Move the colour slider again to a new colour. Run your code again. Your background colour will change to the new colour. 

--- /task ---

## Loop your program

The Astro Pi Mission Zero program needs to run for less than 30 seconds. Your code will run repeatedly and sense the latest colour each time.  

--- task ---

**Find** your `image = [` line of code.

**Add** code above it to set up your `for` loop for `28` repetitions.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---
for i in range(28):
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

--- /task ---

--- task ---

You now need to indent all your code below the `for` loop so that it sits **inside** the `for` loop.

To do this, highlight the code you want to indent and use the <kbd>Tab</kbd> key on your keyboard to indent multiple lines at once.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 2 - 14
---
for i in range(28):
  image = [
    c, c, c, q, q, q, c, c,
    c, c, t, q, e, q, c, c,
    c, c, c, q, q, q, c, c,
    c, w, w, w, w, w, w, c,
    c, w, a, a, a, a, w, c,
    c, w, a, a, a, a, w, c,
    c, c, w, a, a, w, c, c,
    c, c, c, w, w, c, c, c]
    
  # Set LED colours
  rgb = sense.color # read the colour from the sensor
  c = (rgb.red, rgb.green, rgb.blue)
  sense.set_pixels(image)
 
--- /code ---

--- /task ---

--- task ---

At the bottom of your code, add a `sleep` of one second inside your loop:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 5
---
  # Set LED colours
  rgb = sense.color # read the colour from the sensor
  c = (rgb.red, rgb.green, rgb.blue)
  sense.set_pixels(image)
  sleep(1)  
  
--- /code ---

**Tip:** Make sure this line of code is indented within your `for` loop. 

--- /task ---

--- task ---

**Test:** Run your code and change the colour picker several times as your project is running. Check that your image updates to use the sensed colour on its next run of the animation. 

The image will stop updating when the loop finishes so that the program doesn't run for more than 30 seconds. 

--- /task ---

--- task ---

**Debug** 

My code has a syntax error or doesn't run as expected:

- Check that your code matches the code in the examples above
- Check that you have indented the code in your `for` loop
- Check that your list is surrounded by `[` and `]`
- Check that each colour variable in the list is separated by a comma

--- /task ---

--- task ---

Add `sense.clear()` at the end of your code to clear the image at the end of your loop. This will help you see when your animation has finished running. 

**Tip:** Make sure you **do not** indent the `sense.clear()` line of code as you want this to only run once at the end of your animation.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 7
---
  # Set LED colours
  rgb = sense.color # read the colour from the sensor
  c = (rgb.red, rgb.green, rgb.blue)
  sense.set_pixels(image)
  sleep(1) 
  
sense.clear()
  
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code again. When your animation has finished running the LED matrix will clear, turning all the lights black (off).  

--- /task ---

--- task ---

**Debug** 

The LED matrix turns black every second:

- Check that you have not indented the `sense.clear()` code within your `for` loop

--- /task ---

--- task ---

Add code to clear the LED matrix to a colour of your choice. Create a variable called `x` to store your new colour. 

You can mix your own colour or use the values from the list of colours to create your new `x`colour. 

[[[generic-theory-simple-colours]]]
[[[ambient-colours]]]

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 7-8
---
  # Set LED colours
  rgb = sense.color # read the colour from the sensor
  c = (rgb.red, rgb.green, rgb.blue)
  sense.set_pixels(image)
  sleep(1) 

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255
sense.clear(x)
  
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code again. When your animation has finished running the LED matrix will clear to your chosen colour. You can change then test the colour as many times as you want.  

--- /task ---
