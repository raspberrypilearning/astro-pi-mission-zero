## Voeg er wat kleur aan toe

De Astro Pi's LEDs kunnen ook kleuren tonen. Je kunt een kleur specificeren door een variabele te definiëren en het een RGB-kleurwaarde toe te kennen.

Je kunt hier leren hoe alle kleuren te definiëren door gebruik te maken van verschillende verhoudingen van rood, groen, en blauw:

[[[generic-theory-colours]]]

--- task ---

Kies een kleur en zoek de RGB-waarde van die kleur. Je kunt een [kleurenkiezer](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} gebruiken om je te helpen.

--- /task ---

--- task ---

Definieer een variabele om je gekozen kleur op te slaan. Bijvoorbeeld, indien je rood hebt gekozen, dan schrijf je deze regel code:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

Je kunt nu je tekst tonen in je gekozen kleur! Om het programma te laten weten dat de gedefinieerde gebruikt moet worden, voeg je een `text_colour` (tekst_kleur) parameter toe aan de code die je tekst toont:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /task ---

![toon de boodschap in kleur](images/show-message-color.gif)

--- task ---

Je kunt ook de achtergrondkleur van het scherm veranderen. Kies een andere kleur en definieer een andere variabele om die kleur op te slaan. Om het programma je gekozen achtergrond te laten gebruiken, voeg je de `back_colour` (achtergrond_kleur) parameter aan je code:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Verander de begroetingstekst en -kleur — welke boodschap zul je naar de astronauten aan boord het ISS sturen?

--- /task ---