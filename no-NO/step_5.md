## Vise et bilde

You can display pictures on the Astro Pi's LED matrix. Perhaps your greeting for the astronauts could include a picture or a pattern, as well as or instead of a written message?

![Astronaut](images/astronaut-pic.png)

--- task ---

At the bottom of your program, create some colour variables to define the colours with which you want to draw your picture. You can use as many colours as you like, but in this example we'll use only a few colours — red (`r`), white (`w`), black (`b`), and two shades of grey (`g` and `s`). Notice that the shades are achieved by reducing the amount of light in all three channels while keeping the proportions the same.

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Note:** This time, it's a good idea to give the colour variables single-letter names, because that will save time in the next step, where you are going to be typing them out many times. Moreover, using single letters will make it easier to see the picture you'll draw.

--- /task ---

--- task ---



Below your new variables, create a list of 64 items. Each item represents one pixel on the LED matrix, and corresponds to one of the colour variables you defined. Draw your picture by putting a variable where you want its assigned colour to appear. We have drawn an Astro Pi by using the black (`b`) pixels as the background and the grey (`g`) pixels to draw the metal parts of the Astro Pi flight case:

```python
 picture = [
b, b, w, w, w, w, b, b,
b, w, b, b, b, b, w, b,
b, w, b, w, w, b, w, b,
b, w, b, b, b, b, w, b,
b, b, w, w, w, w, b, b,
b, b, w, w, w, w, b, b,
b, w, w, w, w, w, w, b,
b, w, w, w, w, w, w, b
]
```
--- /task ---

--- task ---

Legg til en kodelinje for å vise bildet på LED-skjermen.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Trykk **Run** (Kjør) for å se bildet på skjermen.

--- /task ---

--- task ---

You might want to add some code to include a short wait (or `sleep`) after the picture is displayed. This will give the astronauts time to see your picture before the next part of your message appears. At the top of your program, add:

```python
from time import sleep
```

På linjen etter den som viser bildet, legger dere til denne koden for å få et opphold på to sekunder:

```python
sleep(2)
```

--- /task ---

--- task ---

Lag et eget bilde eller mønster for å vise til astronautene!

--- /task ---
