## Laat een boodschap zien en kies een naam voor de nieuwe Astro Pi-computers

The Astro Pi's LED matrix can display colours. In this step, you will specify a colour to be displayed by creating a variable and assigning it an RGB colour value.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
An <span style="color: #0faeb0">**LED matrix**</span> is a grid of LEDs that can be controlled individually or as a group to create different lighting effects. The LED matrix on the Sense HAT has 64 LEDs displayed in an 8 x 8 grid. The LEDs can be programmed to produce a wide range of colours.
</p>

Je zult zien dat drie lijnen code automatisch voor je werden toegevoegd:

You will see that four lines of code have been added for you automatically:

Deze code maakt verbinding met de Astro Pi en zorgt ervoor de het LED-scherm van de Astro Pi op de juiste manier weergegeven wordt. Laat de code staan, want je zal ze nodig hebben.
---
language: python filename: main.py line_numbers: false line_number_start: 1
title: Welke tekens kunnen worden gebruikt?
---
# Import the libraries
from sense_hat import SenseHat from time import sleep

# Set up the SenseHAT
Misschien kan je een leuke begroeting achterlaten voor de astronauten die in de buurt van de Astro Pi op het ISS werken? Laten we een boodschap over het scherm laten rollen.

![A screenshot of the Trinket Sense HAT emulator with three lines of starter code displayed in the left hand pane.](images/sense-hat-emulator2.png)

This code connects to the Astro Pi and makes sure the Astro Pi's LED display is shown the correct way around. Leave the code there, because you'll need it.

--- /task ---

Druk op de **Run** knop en zie de boodschap `Astro Pi` over het LED-scherm rollen.

[[[generic-theory-simple-colours]]]

--- task ---

Om een andere boodschap te tonen, kan je wat je maar wil schrijven tussen de aanhalingstekens (`""`).

--- collapse ---

--- /task ---

--- task ---

Create a variable to store your chosen colour. For example, if you picked red, you would write this line of code:

Je kan de weergavesnelheid van de boodschap die over het scherm rolt ook aanpassen. Voeg een `scroll_speed` toe aan de codelijn die je al hebt, op deze manier:
---
De startsnelheid van de boodschap is `0.1`. Als je het getal kleiner maakt, zal de boodschap sneller bewegen en het getal vergroten zal de boodschap trager doen bewegen.
line_highlights: 2
---
# Add colour variables and image
v = (255, 0, 0) # Red --- /code ---

--- /task ---

--- task ---

Om te stemmen, begin je je boodschap met de woorden "My name should be" (in het Engels). Bijvoorbeeld, als je wil stemmen van Ada Lovelace, zal je code er als volgt uitzien:

Als je wil stemmen, moet je boodschpa beginnen met deze woorden, anders kunnen we je deelname niet registreren.
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 5
---
# Add colour variables and image
v = (255, 0, 0) # Red

# Set LED colours
sense.clear(v) --- /code ---

--- /task ---

--- task ---

**Test:** Run your code by .... <mark> add details of how to run code in the new editor here </mark>. The LED matrix on your Sense HAT will light in your chosen colour.

<mark>update image </mark>

![The Trinket Sense HAT emulator running a sample program which scrolls the text \"Astro Pi\" across the LED matrix using red letters.](images/M0_2.gif)

--- /task ---

--- task ---

**Choose** a second colour to display on the Sense HAT LED matrix and set up the colour variable below your first colour variable.

[[[ambient-colours]]]

For example, if you picked forest green, your code would look like this:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3
---
# Add colour variables and image
v = (255, 0, 0) # Red m = (34, 139, 34) # ForestGreen

# Set LED colours
sense.clear(v) --- /code ---

--- /task ---

--- task ---

You can use `sense.clear()` to show another colour of your choice. To see both colours, you will need to pause in between the `sense.clear()` code so that you have time to see them:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7, 8, 9
---
# Add colour variables and image
v = (255, 0, 0) # Red m = (34, 139, 34) # ForestGreen

# Set LED colours
sense.clear(v) sleep(1) sense.clear(m) sleep(1) --- /code ---

--- /task ---

--- task ---

**Test:** Run your code by .... <mark> add details of how to run code in the new editor here </mark>. The LED matrix on your Sense HAT will light your first colour for one second, then change to your second colour.

<mark>update image </mark>

![The Trinket Sense HAT emulator running a sample program which scrolls the text \"Astro Pi\" across the LED matrix using red letters.](images/M0_2.gif)

--- /task ---

--- task ---

**Debug**

My code doesn't run:
- `NameError:` &mdash; have you checked that your colour variable is spelled correctly in `sense.clear()`and that it matches the variable earlier in your code?
- `SyntaxError bad input:` Make sure that your code matches the code above. It is important to use `,` and `.` when needed.

My Sense HAT only shows my second colour:
- Make sure you have added `sleep(1)` to pause your code for 1 second between changes.

--- /task ---

