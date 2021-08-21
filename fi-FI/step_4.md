## Lisää jonkun verran väriä

Astro Pin LEDit voivat näyttää myös värejä. Voit määrittää värin luomalla muuttujan ja antamalla sille RGB-väriarvon.

Täältä voit oppia, kuinka kaikki värit voidaan luoda käyttämällä punaisen, vihreän ja sinisen eri mittasuhteita:

[[[generic-theory-colours]]]

--- tehtävä ---

Valitse väri ja selvitä värin RGB-arvo. Voit käyttää [värinvalitsinta](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} auttamaan sinua.

--- /task ---

--- task ---

Luo muuttuja tallentaaksesi valitsemasi värin. For example, if you picked red, you would write this line of code:

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

![The Trinket Sense HAT emulator running a sample program which scrolls the text \"Astro Pi\" across the LED matrix using red letters](images/M0_2.gif)

--- task ---

You can also change the background colour of the display. Pick another colour, and create another variable to store that colour. To tell the program to use your chosen background colour, add the `back_colour` parameter to your code:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Muuta tervehdystekstiä ja väriä — minkä viestin sinä lähetät ISS:n astronauteille?

--- /task ---
