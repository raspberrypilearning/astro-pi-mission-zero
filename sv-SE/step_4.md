## Känn en färg

I det här steget kommer du att ställa in färgljussensorn och använda den för att känna av mängden rött, grönt och blått som når sensorn. Denna färg kommer sedan att användas för att färglägga din valda bild. En astronaut som går upp till sensorn i en blå skjorta skulle se en annan bild än en astronaut i en röd skjorta.

![image displayed with a pink background on the LED matrix](images/colour_background.png)

Vilken bild du än väljer använder bakgrunden variabeln `c` som är inställd på svart.

--- task ---

Använd färgsensorn för att färga din bakgrund.

Lägg till kod före din bildlista för att få färgen från sensorn och ändra din `c` bakgrundsfärgvariabel för att använda färgen som avkänns av Sense HAT-färgsensorn istället för svart.

**Tips:** Du behöver inte skriva kommentarerna som börjar med '#' (de är till för att förklara koden).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9-10
---
# Lägg till färgvariabler och bild

c = (0, 0, 0) # Svart m = (34, 139, 34) # Skogsgrön q = (255, 255, 0) # Gul t = (255, 140, 0) # MörkOrange y = (255, 20, 147) # DjupRosa

rgb = sense.color # hämta färgen från sensorn c = (rgb.red, rgb.green, rgb.blue) # använd den avlästa färgen

image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

**Test:** Flytta färgreglaget till en färg som du väljer och sedan **kör** din kod. Din bakgrundsfärg kommer att ändras. Upprepa detta test igen med en ny färg.

**Tips:** Du måste klicka på "Kör" varje gång du ändrar färg.

--- /task ---

## Loopa ditt program

Astro Pi Mission Zero-programmet får köras i upp till 30 sekunder. Du kommer att använda denna tid för att upprepade gånger kontrollera färgsensorn och uppdatera bilden.

Din kod kommer att använda en `for` loop för att köra 28 gånger. **Varje** gång kommer den att:
+ känna den senaste färgen
+ uppdatera bildens bakgrundsfärg
+ pausa i en sekund

--- task ---

**Find** your `rgb = sense.color` line of code.

**Add** code above it to set up your `for` loop for `28` repetitions.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 1
---
for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

You now need to indent all your code below the `for` loop so that it sits **inside** the `for` loop.

**Tip:** To indent multiple lines, highlight the lines you want to indent then press the <kbd>Tab</kbd> key on your keyboard (usually above the <kbd>Caps Lock</kbd> key on the keyboard).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2 - 17
---
for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

  # Display the image

  sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

At the bottom of your code, add a `sleep` of one second inside your loop:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 4
---
  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Tip:** Make sure this line of code is indented within your `for` loop.

--- /task ---

--- task ---

**Test:** Run your code and change the colour picker several times as your project is running. Check that your image updates to use the sensed colour on its next run.

The image will stop updating when the loop finishes so that the program doesn't run for more than 30 seconds.

--- /task ---

--- task ---

**Debug**

My code has a syntax error or doesn't run as expected:

- Check that your code matches the code in the examples above
- Check that you have indented the code in your `for` loop
- Check that your list is surrounded by `[` and `]`
- Check that each colour variable in the list is separated by a comma

My code runs for longer than 30 seconds:

- Decrease the number of times your for loop runs, from 28 to 25 or even 20.
- Decrease the length of the sleep, from 1 second to 0.5 seconds.

--- /task ---

--- task ---

Add `sense.clear()` at the end of your code to clear the image at the end of your loop. This will help you see when your animation has finished running.

**Tip:** Make sure you **do not** indent the `sense.clear()` line of code as you want this to only run once at the end of your animation.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 6
---
  # Display the image

  sense.set_pixels(image) sleep(1)

sense.clear()

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code again. When your project has finished running the LED matrix will clear, turning all the lights black (off).

--- /task ---

--- task ---

**Debug**

The LED matrix turns black every second:

- Check that you have not indented the `sense.clear()` code within your `for` loop

--- /task ---

--- task ---

Add code to clear the LED matrix to a colour of your choice. Create a variable called `x` to store your new colour.

You can mix your own colour or use the values from the list of colours to create your new `x`colour.

\[[[generic-theory-simple-colours]]\] \[[[ambient-colours\]]]

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 6-7
---
  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code again. When your project has finished running the LED matrix will clear to your chosen colour. You can change then test the colour as many times as you want.

--- /task ---

--- task ---

--- collapse ---

---
title: Completed code example
---

![A grid with 8 x 8 squares showing a pink flower on a green stem.](images/flower.png)

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

c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange y = (255, 20, 147) # DeepPink

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
