## Voeg er wat kleur aan toe

The Astro Pi's LEDs can also display colours. You can specify a colour by creating a variable and assigning it an RGB colour value.

Je kunt hier leren hoe alle kleuren te definiëren door gebruik te maken van verschillende verhoudingen van rood, groen, en blauw:

[[[generic-theory-colours]]]

--- task ---

Kies een kleur en zoek de RGB-waarde van die kleur. Je kunt een [kleurenkiezer](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} gebruiken om je te helpen.

--- /task ---

--- task ---

Definieer een variabele om je gekozen kleur op te slaan. Als je bijvoorbeeld rood koos, schrijf je deze code-regel:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

Je kan de tekst nu weergeven in de kleur van jouw keuze! Om het programma te laten weten dat het de kleur die je maakte moet gebruiken, voeg je een `text_colour` parameter toe aan de code die je tekst weergeeft:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /task ---

![toon de boodschap in kleur](images/show-message-color.gif)

--- task ---

Je kan de achtergrondkleur van het scherm ook aanpassen. Kies een andere kleur en maak een andere variabele om die kleur op te slaan. Om het programma te laten weten dat het de door jouw gekozen achtergondkleur moet gebruiken, voeg je de `back_colour` parameter toe aan je code:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Verander de begroetingstekst en -kleur — welke boodschap zul je naar de astronauten aan boord het ISS sturen?

--- /task ---
