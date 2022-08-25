## Add some colour

The Astro Pi's LED matrix can display colours. You can specify a colour by creating a variable and assigning it an RGB colour value.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
An <span style="color: #0faeb0">**LED matrix**</span> is a grid of LEDs that can be controlled individually or as a group to create different lighting effects. The LED matrix on the SenseHAT has 64 LEDs displayed in an 8 x 8 grid. The LEDs can be programmed to produce a wide range of colours.
</p>

--- task ---
<mark>change link to emulator</mark>
Open the [Sense HAT emulator](https://trinket.io/mission-zero){:target="_blank"} for the Mission Zero project.

You will see that four lines of code have been added for you automatically:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
---
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)
--- /code ---

![A screenshot of the Trinket Sense Hat emulator with three lines of starter code displayed in the left hand pane.](images/sense-hat-emulator2.png)

This code connects to the Astro Pi and makes sure the Astro Pi's LED display is shown the correct way around. Leave the code there, because you'll need it.

--- /task ---

You can learn how all colours can be created using different proportions of red, green, and blue here:

[[[generic-theory-simple-colours]]]

--- task ---

Choose a colour you would like to display on the LED matrix:

[[[ambient-colours]]]

--- /task ---

--- task ---

Create a variable to store your chosen colour. For example, if you picked red, you would write this line of code:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 12
---
red = (255, 0, 0)
--- /code ---

--- /task ---

--- task ---

You can now make your Sense HAT display the colour you picked, using the LED matrix.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3
---
red = (255, 0, 0)

sense.clear(red)
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code by .... <mark> add details of how to run code in the new editor here </mark>. The LED matrix on your Sense HAT will light in your chosen colour. 

<mark>update image </mark>

![The Trinket Sense HAT emulator running a sample program which scrolls the text \"Astro Pi\" across the LED matrix using red letters](images/M0_2.gif)

--- /task ---

--- task ---

**Choose:** a second colour to display on the Sense HAT LED matrix and set up the colour variable below your first colour variable. 

[[[ambient-colours]]]

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 2
---
red = (255, 0, 0)
green = (0, 255, 0)

sense.clear(red)
--- /code ---

--- /task ---

--- task ---

You can use `sense.clear()` to show another colour of your choice. To see both colours you will need to pause inbetween the `sense.clear()` code so that you have time to see them:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 2,5,6
---

--- /code ---
red = (255, 0, 0)
green = (0, 255, 0)

sense.clear(red)
sleep(1)
sense.clear(green)

--- /task ---

--- task ---

**Test:** Run your code by .... <mark> add details of how to run code in the new editor here </mark>. The LED matrix on your Sense HAT will light your first colour for one second then change to your second colour. 

<mark>update image </mark>

![The Trinket Sense HAT emulator running a sample program which scrolls the text \"Astro Pi\" across the LED matrix using red letters](images/M0_2.gif)

--- /task ---

--- task ---

**Debug:**

My code doesn't run:
- `NameError:` - have you checked that your colour variable is spelled correctly in `sense.clear()`and that it matches the variable earlier in your code? 
- `SyntaxError bad input:` Make sure that your code matches the code above. It is important to use `,` and `.` when needed. 

My Sense HAT only shows my second colour:
- Make sure you have added `sleep(1)` to pause your code for 1 second between changes. 

--- /task ---

