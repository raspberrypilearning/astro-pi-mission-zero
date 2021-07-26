## Dodajte barve

The Astro Pi's LEDs can also display colours. You can specify a colour by creating a variable and assigning it an RGB colour value.

O tem, kako lahko s pomočjo različnih razmerij rdeče, zelene in modre ustvarite različne barve, se lahko poučite tukaj:

[[[generic-theory-colours]]]

--- task ---

Choose a colour, and find out that colour's RGB value. You could use a [colour picker](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} to help you.

--- /task ---

--- task ---

Create a variable to store your chosen colour. For example, if you picked red, you would write this line of code:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

You can now display your text in the colour of your choice! To tell the program to use the colour you created, add a `text_colour` parameter to the code which displays your text:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /task ---

![Prikaži sporočilo v barvah](images/show-message-color.gif)

--- task ---

You can also change the background colour of the display. Pick another colour, and create another variable to store that colour. To tell the program to use your chosen background colour, add the `back_colour` parameter to your code:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Spremenite besedilo in barvo pozdravnega sporočila — kakšno sporočilo boste poslali astronavtom na postaji ISS?

--- /task ---
