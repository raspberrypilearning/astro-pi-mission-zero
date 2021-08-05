## Voeg wat kleur toe

De LED's van de Astro Pi kunnen ook kleuren weergeven. Je kunt een kleur opgeven door een variabele te maken en deze een RGB-kleurwaarde toe te kennen.

Je kunt hier leren hoe alle kleuren kunnen worden gemaakt met verschillende verhoudingen rood, groen en blauw:

[[[generic-theory-colours]]]

--- task ---

Kies een kleur en ontdek de RGB-waarde van die kleur. Je kunt een [kleurkiezer gebruiken](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} om je te helpen.

--- /task ---

--- task ---

Maak een variabele om de door jou gekozen kleur op te slaan. Als je bijvoorbeeld rood hebt gekozen, schrijf je deze regel code:

```python
rood = (255,0,0)
```

--- /task ---

--- task ---

Je kunt nu je tekst weergeven in de kleur van je keuze! Om het programma te vertellen de door jou gemaakte kleur te gebruiken, voeg je een `text_colour` parameter toe aan de code die je tekst laat zien:

```python
rood = (255,0,0)
sense.show_message("Astro Pi", text_colour=rood)
```

--- /task ---

![The Trinket Sense HAT emulator running a sample program which scrolls the text \"Astro Pi\" across the LED matrix using red letters](images/M0_2.gif)

--- task ---

Je kunt de achtergrondkleur van het display ook wijzigen. Kies een andere kleur en maak een andere variabele om die kleur op te slaan. Om het programma te vertellen de door jou gekozen achtergrondkleur te gebruiken, voeg je de `back_colour` parameter toe aan je code:

```python
rood = (255,0,0)
groen = (0,255,0)
sense.show_message("Astro Pi", text_colour=rood, back_colour=groen)
```

--- /task ---

--- task ---

Verander de tekst en kleur van de begroeting - welke boodschap stuur je naar de astronauten aan boord van het ISS?

--- /task ---
