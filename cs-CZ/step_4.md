## Přidej barvy

LED displej Astro Pi také umí zobrazovat barvy. Barvu můžeš určit vytvořením proměnné, které přiřadíš hodnotu barvy v RGB.

Tady se dozvíš, jak se pomocí různých poměrů červené, zelené a modré dají vytvořit všechny barvy:

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

Teď můžeš zobrazit svůj text v barvě, kterou si vybereš! Pokud chceš programu říct, aby použil tvoji barvu, přidej do řádku s kódem, který zobrazuje tvůj text, parametr `text_colour`:

```python
cervena = (255,0,0)
sense.show_message("Astro Pi", text_colour=cervena)
```

--- /task ---

![The Trinket Sense HAT emulator running a sample program which scrolls the text \"Astro Pi\" across the LED matrix using red letters](images/M0_2.gif)

--- task ---

Také můžeš změnit barvu pozadí displeje. Vyber si jinou barvu a vytvoř další proměnnou, do které tu barvu uložíš. Pokud chceš programu říct, aby použil tvoji barvu pozadí, přidej do kódu parametr `back_colour`:

```python
cervena = (255,0,0)
zelena = (0,255,0)
sense.show_message("Astro Pi", text_colour=cervena, back_colour=zelena)
```

--- /task ---

--- task ---

Změň text a barvu pozdravu. Jaký vzkaz pošleš astronautům na palubě ISS?

--- /task ---
