## Přidejte barvy

LED displej Astra Pi také umí zobrazovat barvy. Barvu můžete určit vytvořením proměnné, které přiřadíte hodnotu barvy v RGB.

Jak se pomocí různých proporcí červené, zelené a modré dají vytvořit všechny barvy, se dozvíte tady:

[[[generic-theory-colours]]]

--- task ---

Vyberte si barvu a zjistěte její hodnotu v RGB. Pomůže vám s tím [vybírátko barev](https://www.w3schools.com/colors/colors_rgb.asp) {:target="_blank"}.

--- /task ---

--- task ---

Vytvoře proměnnou, do které si svou barvu uložíte. Například když jste si vybrali červenou, můžete napsat tuto řádku kódu:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

Teď můžete zobrazit svůj text v barvě, kterou jste si vybrali! Abyste programu řekli, jakou barvu jste vytvořili, přidejte do kódu, který zobrazuje váš text, `text_colour`:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /task ---

![barva zobrazené zprávy](images/show-message-color.gif)

--- task ---

Můžete také změnit barvu pozadí displeje. Vyberte si jinou barvu a vytvořte další proměnnou, do které ji uložíte. Abyste programu řekli, aby použil barvu pozadí, kterou jste si vybrali, přidejte do svého kódu parametr `back_colour`:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Změňte text a barvu pozdravu – jaký vzkaz pošlete astronautům na palubě ISS?

--- /task ---