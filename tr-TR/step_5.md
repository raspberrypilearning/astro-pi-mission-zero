## Display an image

You can display pictures on the Astro Pi's LED matrix. Perhaps your greeting for the astronauts could include a picture or a pattern, as well as or instead of a written message?

![Astronaut](images/astronaut-pic.png)

\--- task \---

At the bottom of your program, create some colour variables to define the colours with which you want to to draw your picture. You can use as many colours as you like, but in this example we'll stick to only two — white (`w`) and black (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Note:** This time, it's a good idea to give the colour variables single-letter names, because that will save time in the next step, where you are going to be typing them out many times. Moreover, using single letters will make it easier to see the picture you'll draw.

\--- /task \---

\--- task \---

Below your new variables, create a list of 64 items. Each item represents one pixel on the LED matrix, and corresponds to one of the colour variables you defined. Draw your picture by putting a variable where you want its assigned colour to appear. We have drawn an astronaut by using the black (`b`) pixels as the background and the white (`w`) pixels to draw the astronaut's space suit:

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

\--- /görev \---

\--- task \---

Add a line of code to display your picture on the LED display.

```python
sense.set_pixels(picture)
```

\--- /görev \---

\--- task \---

Press **Run** to see your picture displayed.

\--- /görev \---

\--- task \---

You might want to add some code to include a short wait (or `sleep`) after the picture is displayed. This will give the astronauts time to see your picture before the next part of your message appears. At the top of your program, add:

```python
from time import sleep
```

Then, on the line after the one that displays your picture, add this code to wait for two seconds:

```python
sleep(2)
```

\--- /görev \---

\--- task \---

Create your own picture or pattern to display to the astronauts!

\--- /görev \---