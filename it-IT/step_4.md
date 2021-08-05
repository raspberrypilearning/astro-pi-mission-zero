## Aggiungi un po’ di colore

I LED dell’Astro Pi possono anche visualizzare i colori. Potete specificare un colore creando una variabile e assegnando ad essa un valore di colore RGB.

Potete imparare come si possono creare tutti i colori usando diverse proporzioni di rosso, verde e blu qui:

[[[generic-theory-colours]]]

--- task ---

Scegliete un colore e scoprite qual è il suo valore RGB. Se volete, potete usare un [selettore dei colori](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} per sceglierlo.

--- /task ---

--- task ---

Create una variabile in cui memorizzare il colore che avete scelto. Ad esempio, se avete scelto il rosso dovreste scrivere questa riga di codice:

```python
rosso = (255,0,0)
```

--- /task ---

--- task ---

Potete ora visualizzare il vostro messaggio nel colore che preferite! Per dire al programma di usare il colore che avete creato, aggiungete il parametro `text_colour` al codice che visualizza il vostro testo:

```python
rosso = (255,0,0)
sense.show_message("Astro Pi", text_colour=rosso)
```

--- /task ---

![The Trinket Sense HAT emulator running a sample program which scrolls the text "Astro Pi" across the LED matrix using red letters](images/M0_4.gif)

--- task ---

Potete anche cambiare il colore di sfondo del display. Scegliete un altro colore e create un’altra variabile per memorizzare tale colore. Per dire al programma di usare il colore di sfondo che avete scelto, aggiungete al codice il parametro `back_colour`:

```python
rosso = (255,0,0)
verde = (0,255,0)
sense.show_message("Astro Pi", text_colour=rosso, back_colour=verde)
```

--- /task ---

--- task ---

Modificate il testo e il colore del messaggio di saluto: quale messaggio volete inviare agli astronauti a bordo della ISS?

--- /task ---
