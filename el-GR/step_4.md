## Προσθήκη χρώματος

The Astro Pi's LEDs can also display colours. You can specify a colour by creating a variable and assigning it an RGB colour value.

Μπορείτε να μάθετε πώς να δημιουργείτε όλα τα χρώματα χρησιμοποιώντας διαφορετικές αναλογίες κόκκινου, πράσινου και μπλε εδώ:

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

![εμφάνιση μηνύματος με χρώμα](images/show-message-color.gif)

--- task ---

You can also change the background colour of the display. Pick another colour, and create another variable to store that colour. To tell the program to use your chosen background colour, add the `back_colour` parameter to your code:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Αλλάξτε το κείμενο και το χρώμα του χαιρετισμού — τι μήνυμα θα στείλετε στους αστροναύτες που βρίσκονται στον Διεθνή Διαστημικό Σταθμό;

--- /task ---
