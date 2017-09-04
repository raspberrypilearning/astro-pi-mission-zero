## Add some colour

The Sense HAT's LED matrix can display colours as well as black and white. You can specify a colour by creating a variable and assigning it a RGB colour value.

You can find out how all colours can be made from different amounts of red green and blue here:
[[[generic-theory-colours]]]

+ Choose a colour and find out the colour's RGB value. You could use a [colour picker](https://www.w3schools.com/colors/colors_rgb.asp) to help you.

+ Create a variable to store your chosen colour. For example, if you chose the colour red you would write this line of code:

```python
red = (255,0,0)
```

+ You can now display your text in the colour of your choice! Add a `text_colour` parameter to the code which displays your text to tell the program to use the colour you created:

```python
red = (255,0,0)
sense.show_message("Astro Pi", scroll_speed=0.2, text_colour=red)
```

+ You can also change the background colour of the scrolling text. Pick another colour and create a variable to store that colour. Then add the `back_colour` parameter to tell the program to use your chosen background colour:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```
