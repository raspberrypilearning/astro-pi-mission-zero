## Zeige eine Nachricht und wähle einen Namen für die neuen Astro Pi Computer

The Astro Pi's LED matrix can display colours. In this step, you will specify a colour to be displayed by creating a variable and assigning it an RGB colour value.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
An <span style="color: #0faeb0">**LED matrix**</span> is a grid of LEDs that can be controlled individually or as a group to create different lighting effects. The LED matrix on the SenseHAT has 64 LEDs displayed in an 8 x 8 grid. The LEDs can be programmed to produce a wide range of colours.
</p>

Du wirst sehen, dass drei Zeilen Code bereits automatisch erscheinen:

Füge diese Zeile unter dem anderen Code hinzu:

--- /collapse ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
title: Welche Zeichen können verwendet werden?
---
# Import the libraries
from sense_hat import SenseHat sense = SenseHat() sense.set_rotation(270)

# Set up the SenseHAT
sense.show_message("Astro Pi", scroll_speed=0.05)

![Ein Screenshot des Trinket Sense Hat-Emulators mit drei Zeilen Anfangscode, der im linken Bereich angezeigt wird.](images/sense-hat-emulator2.png)

Dieser Code verbindet sich mit dem Astro Pi und sorgt dafür, dass die LED-Anzeige des Astro Pi korrekt angezeigt wird. Lass den Code so dort stehen, weil du ihn noch brauchen wirst.

--- /task ---

Klicke auf **Run** (Ausführen) und schau wie die Nachricht `Astro Pi` über den LED-Bildschirm läuft.

[[[generic-theory-simple-colours]]]

--- task ---

Um eine andere Nachricht anzuzeigen, kannst du etwas Beliebiges zwischen die Anführungszeichen schreiben (`""`).

--- collapse ---

--- /task ---

--- task ---

Create a variable to store your chosen colour. For example, if you picked red, you would write this line of code:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start:
line_highlights: 2
---
# Add colour variables and image
v = (255, 0, 0) # Red --- /code ---

--- /task ---

--- task ---

You can now make your Sense HAT display the colour you picked, using the LED matrix.

Wenn du mitwählen willst, *muss* deine Nachricht mit diesen Worten beginnen, da wir deine Stimme sonst nicht zählen können.
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

<mark>images/M0_1.gif </mark>

![Der Trinket Sense HAT-Emulator, der ein Beispielprogramm ausführt, das den Text "Astro PI" in weißen Buchstaben über die LED-Matrix laufen lässt](images/M0_2.gif)

--- /task ---

--- task ---

**Choose:** a second colour to display on the Sense HAT LED matrix and set up the colour variable below your first colour variable.

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

You can use `sense.clear()` to show another colour of your choice. To see both colours you will need to pause inbetween the `sense.clear()` code so that you have time to see them:

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

