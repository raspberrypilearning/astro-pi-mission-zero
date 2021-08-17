## Přidej barvy

LED displej Astro Pi také umí zobrazovat barvy. Barvu můžeš určit vytvořením proměnné, které přiřadíš hodnotu barvy v RGB.

Jak se pomocí různých proporcí červené, zelené a modré dají vytvořit všechny barvy, se dozvíte tady:

[[[generic-theory-colours]]]

--- task ---

Vyber si barvu a zjisti její hodnotu v RGB. S tím ti může pomoci [nástroj pro výběr barvy](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"}.

--- /task ---

--- task ---

Vytvoř proměnnou, do které si svou barvu uložíš. Pokud si vybereš červenou, tvůj řádek s kódem by vypadal takhle:

```python
cervena = (255,0,0)
```

--- /task ---

--- task ---

Teď můžeš zobrazit svůj text v barvě, kterou si vybereš! To tell the program to use the colour you created, add a `text_colour` parameter to the code which displays your text:

```python
cervena = (255,0,0)
sense.show_message("Astro Pi", text_colour=cervena)
```

--- /task ---

![The Trinket Sense HAT emulator running a sample program which scrolls the text \"Astro Pi\" across the LED matrix using red letters](images/M0_2.gif)

--- task ---

Také můžeš změnit barvu pozadí displeje. Vyber si jinou barvu a vytvoř další proměnnou, do které tu barvu uložíš. To tell the program to use your chosen background colour, add the `back_colour` parameter to your code:

```python
cervena = (255,0,0)
zelena = (0,255,0)
sense.show_message("Astro Pi", text_colour=cervena, back_colour=zelena)
```

--- /task ---

--- task ---

Změňte text a barvu pozdravu – jaký vzkaz pošlete astronautům na palubě ISS?

--- /task ---
