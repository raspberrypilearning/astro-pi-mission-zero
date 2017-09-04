## Display an image

You can display a picture on the Sense HAT's LED matrix.

![Astronaut](images/astronaut-pic.png)

+ Create colour variables to define the colours you want to use in your picture. You can use as many colours as you like, but for this example we'll stick to only two - white (`w`) and black (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

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
