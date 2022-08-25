## Ajouter de la couleur

In this step, you will display images on the Astro Pi's LED matrix.

![A screenshot of the emulator window showing the Flight Unit with the LED matrix displaying a picture of the Flight Unit itself](images/fu-pic.png)

The LED Matrix is an 8 x 8 grid. You can set each LED on the grid to a different colour to create an image. Python stores this information in a list.

--- task ---

**Choose:** pick an image to display from the options below. You will need to copy the new colour variables and the image list then add them to the end of your project beneath the line which says `# Add colour variables and image`.


**Tip:** If you are not copying one of the images here make sure that you indent the code within the list like in the examples below. Indenting this code tells Python that the indented lines are part of the list. To indent a line, use the `Tab` character on your keyboard (usually above CAPSLOCK on the keyboard) at the start of the line.

--- collapse ---

---
title: Chicken
---

![A grid with 8x8 squares showing a chick in an egg.](images/chick.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
a = (255, 255, 255) # White c = (0, 0, 0) # Black e = (0, 0, 205) # MediumBlue q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange w = (255, 192, 203) # Pink


image = [ c, c, c, q, q, q, c, c, c, c, t, q, e, q, c, c, c, c, c, q, q, q, c, c, c, w, w, w, w, w, w, c, c, w, a, a, a, a, w, c, c, w, a, a, a, a, w, c, c, c, w, a, a, w, c, c, c, c, c, w, w, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Crab
---

![A grid with 8x8 squares showing a crab.](images/crab.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---

a = (255, 255, 255) # White c = (0, 0, 0) # Black v = (255, 0, 0) # Red


image = [ c, a, a, c, a, a, c, c, c, a, c, c, a, c, c, c, c, v, c, c, v, c, c, c, c, v, c, c, v, c, c, c, v, v, v, v, v, c, v, v, v, v, c, c, v, v, v, c, v, v, v, v, v, c, v, v, v, c, v, c, v, c, c, c]

--- /code ---

--- /collapse ---


--- collapse ---
---
title: Crocodile
---

![A grid with 8x8 squares showing a crocodile head.](images/croc.png)

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

![A grid with 8x8 squares showing a snake.](images/snake.png)

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

![A grid with 8x8 squares showing a frog.](images/frog.png)

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



