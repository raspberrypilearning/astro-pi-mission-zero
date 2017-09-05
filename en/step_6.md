## Display an image

You can display a picture on the Sense HAT's LED matrix.

![Astronaut](images/astronaut-pic.png)

+ Create colour variables to define the colours you want to use in your picture. You can use as many colours as you like, but for this example we'll stick to only two - white (`w`) and black (`b`).

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

+ Perhaps your greeting for the Astronauts could include a picture or a pattern you want to show them, as well as or instead a written message?
