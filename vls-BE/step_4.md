## Voeg er wat kleur aan toe

De LED"s van de Astro Pi kunnen ook kleuren weergeven. Je kan een kleur specifiëren door een variabele te maken en er een RGB-kleurwaarde aan toe te wijzen.

![A screenshot of the emulator window showing the Flight Unit with the LED matrix displaying a picture of the Flight Unit itself](images/fu-pic.png)

The LED Matrix is an 8 x 8 grid. You can set each LED on the grid to a different colour to create an image. Python stores this information in a list.

--- task ---

**Choose:** pick an image to display from the options below. You will need to copy the new colour variables and the image list then add them to the end of your project beneath the line which says `# Add colour variables and image`.


**Tip:** If you are not copying one of the images here make sure that you indent the code within the list like in the examples below. Indenting this code tells Python that the indented lines are part of the list. To indent a line, use the `Tab` character on your keyboard (usually above CAPSLOCK on the keyboard) at the start of the line.

--- collapse ---

---
title: Chick in an egg
---

<mark>add image to show output on Sense HAT</mark>

Maak een variabele om je gekozen kleur op te slaan. Als je bijvoorbeeld rood koos, schrijf je deze code-regel:
---
language: python filename: main.py
line_numbers: false
---
a = (255, 255, 255) # White c = (0, 0, 0) # Black e = (0, 0, 205) # MediumBlue q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange w = (255, 192, 203) # Pink


Je kan de tekst nu weergeven in de kleur van jouw keuze! Om het programma te laten weten dat het de kleur die je maakte moet gebruiken, voeg je een `text_colour` parameter toe aan de code die je tekst weergeeft:

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Crab
---

<mark>add image to show output on Sense HAT</mark>

Je kan de achtergrondkleur van het scherm ook aanpassen. Kies een andere kleur en maak een andere variabele om die kleur op te slaan. Om het programma te laten weten dat het de door jouw gekozen achtergondkleur moet gebruiken, voeg je de `back_colour` parameter toe aan je code:
---
language: python filename: main.py
line_numbers: false
---

a = (255, 255, 255) # White c = (0, 0, 0) # Black v = (255, 0, 0) # Red


Verander de begroetingstekst en -kleur — welke boodschap zal je naar de astronauten aan boord het ISS sturen?

--- /code ---

--- /collapse ---


--- collapse ---
---
title: Crocodile
---

<mark>add image to show output on Sense HAT</mark>

--- code ---
---
language: python filename: main.py
line_numbers: false
---

a = (255, 255, 255) # White c = (0, 0, 0) # Black f = (25, 25, 112) # MidnightBlue m = (34, 139, 34) # ForestGreen


image = [ m, m, m, m, m, c, c, c, m, f, m, f, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, a, c, c, c, a, m, m, c, c, c ,c ,c ,c, m, m, c, c, c, a, c, c, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]

--- /code ---


--- /collapse ---

--- collapse ---
---
title: Snake
---

<mark>add image to show output on Sense HAT</mark>

--- code ---
---
language: python filename: main.py
line_numbers: false
---

 c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow v = (255, 0, 0) # Red


image = [ c, c, c, c, c, c, c, m, c, m, m, m, m, m, m, m, c, m, c, c, c, c, c, c, c, m, m, m, m, m, c, c, c, c, c, c, c, m, c, c, q, m, q, m, m, m, c, c, m, m, m, c, c, c, c, c, v, c, c, c, c, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Frog
---

<mark>add image to show output on Sense HAT</mark>

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start:
line_highlights:
---

c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow v = (255, 0, 0) # Red


image = [ c, m, m, m, c, m, m, m, c, m, q, m, c, m, q, m, m, m, m, m, m, m, m, m, m, v, v, v, v, v, v, v, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, m, m, m, c, m ] --- /code ---

--- /collapse ---

--- /task ---

--- task ---

Below your list, add a line of code to display your image on the LED matrix.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 16,17
---
image = [ c, c, c, q, q, q, c, c, c, c, t, q, e, q, c, c, c, c, c, q, q, q, c, c, c, w, w, w, w, w, w, c, c, w, a, a, a, a, w, c, c, w, a, a, a, a, w, c, c, c, w, a, a, w, c, c, c, c, c, w, w, c, c, c]

# Set LED colours
sense.clear(v) sleep(1) sense.clear(m) sleep(1) sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Press **Run** to see your image displayed on the LED matrix.

--- /task ---

--- task ---

My code has a syntax error!

- Check that you code matches the code in the examples above
- Check that you have indented the code in your list
- Check that your list is surrounded by [ and ]
- Check that each colour variable in the list is seperated by a comma.

My image does not appear
- Check that your `sense.set_pixels(image)` is not indented

--- /task ---



