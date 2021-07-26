## Lägg till lite färg

The Astro Pi's LEDs can also display colours. You can specify a colour by creating a variable and assigning it an RGB colour value.

Du kan lära dig hur alla färger kan skapas med olika proportioner av rött, grönt och blått här:

[[[generic-theory-colours]]]

--- uppgift ---

Choose a colour, and find out that colour's RGB value. You could use a [colour picker](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} to help you.

--- /uppgift ---

--- uppgift ---

Create a variable to store your chosen colour. For example, if you picked red, you would write this line of code:

```python
red = (255,0,0)
```

--- /uppgift ---

--- uppgift ---

You can now display your text in the colour of your choice! To tell the program to use the colour you created, add a `text_colour` parameter to the code which displays your text:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /uppgift ---

![visa meddelande i färg](images/show-message-color.gif)

--- uppgift ---

You can also change the background colour of the display. Pick another colour, and create another variable to store that colour. To tell the program to use your chosen background colour, add the `back_colour` parameter to your code:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /uppgift ---

--- uppgift ---

Ändra hälsningstexten och färgen - vilket meddelande vill du skicka till astronauterna ombord på ISS?

--- /uppgift ---
