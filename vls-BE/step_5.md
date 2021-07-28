## Laat een beeld zien

Je kan foto's tonen op de LED-matrix van de Astro Pi. Misschien kan je begroeting voor de astronauten een foto of een patroon bevatten, samen met of in plaats van een geschreven boodschap?

![Astronaut](images/astronaut-pic.png)

--- task ---

Onderaan je programma kun je wat kleurvariabelen maken om de kleuren waarmee je je tekening wil maken te definiëren. Je kan zoveel kleuren gebruiken als je wil, maar in dit voorbeeld zullen we maar een paar kleuren gebruiken - rood (`r`), wit (`w`), zwart (`b`), en twee tinten grijs (`g` en `s`). Merk op dat de tinten gemaakt worden door de hoeveelheid licht in alle drie de kanalen te verminderen terwijl de verhoudingen gelijk blijven.

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Note:** This time, it's a good idea to give the colour variables single-letter names, because that will save time in the next step, where you are going to be typing them out many times. Moreover, using single letters will make it easier to see the picture you'll draw.

--- /task ---

--- task ---



Below your new variables, create a list of 64 items. Each item represents one pixel on the LED matrix, and corresponds to one of the colour variables you defined. Draw your picture by putting a variable where you want its assigned colour to appear. We have drawn an Astro Pi by using the black (`b`) pixels as the background and the grey (`g`) pixels to draw the metal parts of the Astro Pi flight case:

```python
 picture = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
```
--- /task ---

--- task ---

Voeg een codelijn toe om je tekening te tonen op het led-kleurenbeeldscherm.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Druk op **Run** om je tekening te zien verschijnen.

--- /task ---

--- task ---

You might want to add some code to include a short wait (or `sleep`) after the picture is displayed. This will give the astronauts time to see your picture before the next part of your message appears. At the top of your program, add:

```python
from time import sleep
```

Daarna, op de lijn na degene die jouw tekening toont, voeg je deze code toe om twee seconden te wachten:

```python
sleep(2)
```

--- /task ---

--- task ---

Definieer je eigen tekening of patroon om aan de astronauten te laten zien!

--- /task ---
