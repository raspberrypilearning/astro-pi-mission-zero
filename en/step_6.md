## Display an image

You can display a picture on the Astro Pi's LED matrix.

![Astronaut](images/astronaut-pic.png)

+ At the bottom of your code, create some colour variables to define the colours you want to use in your picture. You can use as many colours as you like, but for this example we'll stick to only two - white (`w`) and black (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

This time, we have given the colour variables single letter names because you are going to be typing them out a lot in the next step and single letters make it easier to see the picture you will develop.

+ Underneath that, create a list of 64 letters. Each letter represents one pixel on the LED matrix, and corresponds to one of the colours you defined.

Draw your picture by putting a letter to represent where you want a colour to appear. We have drawn an astronaut by using the black (`b`) pixels as the background and white (`w`) pixels to draw the astronaut's space suit.

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

+ Add a line of code to display your picture on the LED display.

```python
sense.set_pixels(picture)
```

+ Press **Run** to see your picture displayed.

+ You might want to add some code for a short wait (or `sleep`) after the picture is displayed so that the astronauts have time to see it before the next part of your message. At the start of your program, add

```python
from time import sleep
```

Then, on the line after you display your picture, add this code to wait for 2 seconds:

```python
sleep(2)
```

+ Perhaps your greeting for the astronauts could include a picture or a pattern you want to show them, as well as or instead of a written message?
