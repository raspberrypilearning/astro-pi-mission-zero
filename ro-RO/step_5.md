## Afișează o imagine

You can display pictures on the Astro Pi's LED matrix. Perhaps your greeting for the astronauts could include a picture or a pattern, as well as or instead of a written message?

![Astronaut](images/astronaut-pic.png)

--- task ---

At the bottom of your program, create some colour variables to define the colours with which you want to draw your picture. You can use as many colours as you like, but in this example we'll use only a few colours — red (`r`), white (`w`), black (`b`), and two shades of grey (`g` and `s`). Notice that the shades are achieved by reducing the amount of light in all three channels while keeping the proportions the same.

```python
a = (255, 255, 255)
n = (0, 0, 0)
```

**Note:** This time, it's a good idea to give the colour variables single-letter names, because that will save time in the next step, where you are going to be typing them out many times. Moreover, using single letters will make it easier to see the picture you'll draw.

--- /task ---

--- task ---



Below your new variables, create a list of 64 items. Each item represents one pixel on the LED matrix, and corresponds to one of the colour variables you defined. Draw your picture by putting a variable where you want its assigned colour to appear. We have drawn an Astro Pi by using the black (`b`) pixels as the background and the grey (`g`) pixels to draw the metal parts of the Astro Pi flight case:

```python
 imagine = [
    n, n, a, a, a, a, n, n,
    n, a, n, n, n, n, a, n,
    n, a, n, a, a, n, a, n,
    n, a, n, n, n, n, a, n,
    n, n, a, a, a, a, n, n,
    n, n, a, a, a, a, n, n,
    n, a, a, a, a, a, a, n,
    n, a, a, a, a, a, a, n
]
```
--- /task ---

--- task ---

Adaugă o linie de cod pentru a afișa imaginea ta pe afișajul cu LED-uri.

```python
sense.set_pixels(imagine)
```

--- /task ---

--- task ---

Apasă **Run** pentru a vedea afișată imaginea ta.

--- /task ---

--- task ---

You might want to add some code to include a short wait (or `sleep`) after the picture is displayed. This will give the astronauts time to see your picture before the next part of your message appears. At the top of your program, add:

```python
from time import sleep
```

Apoi, pe linia după cea care afișează imaginea, adaugă acest cod pentru a aștepta două secunde:

```python
sleep(2)
```

--- /task ---

--- task ---

Creează propria ta imagine sau model pentru a le afișa astronauților!

--- /task ---
