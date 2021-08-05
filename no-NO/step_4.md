## Legge til farge

Astro Pi-lysdiodene kan også vise farger. Du kan angi en farge ved å opprette en variabel og tildele den en RGB-fargeverdi.

Du kan lære hvordan alle farger kan lages ved å bruke ulike deler av rød, grønn og blå her:

[[[generic-theory-colours]]]

--- task ---

Velg en farge, og finn fargens RGB-verdi. Du kan bruke en [fargevelger](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} som hjelp.

--- /task ---

--- task ---

Lag en variabel for å lagre den valgte fargen. Hvis du for eksempel valgte rød, skriver du denne kodelinjen:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

Nå kan du vise teksten i fargen du valgte! For å fortelle programmet at det skal bruke fargen du lagde, legger du til en `text_colour`-parameter i koden som viser teksten:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /task ---

![The Trinket Sense HAT emulator running a sample program which scrolls the text \"Astro Pi\" across the LED matrix using red letters](images/M0_2.gif)

--- task ---

Du kan også endre bakgrunnsfargen på skjermen. Velg en annen farge, og opprett en annen variabel for å lagre den fargen. For å fortelle programmet at det skal bruke den valgte bakgrunnsfargen, legger du til `back_colour`-parameteren i koden:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Endre teksten og fargen - hvilken melding vil dere sende til astronautene om bord på ISS?

--- /task ---
