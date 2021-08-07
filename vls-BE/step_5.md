## Laat een beeld zien

Je kan foto's tonen op de LED-matrix van de Astro Pi. Misschien kan je begroeting voor de astronauten een foto of een patroon bevatten, samen met of in plaats van een geschreven boodschap?

![Een screenshot van het emulator-venster dat de vluchteenheid toont met de LED-matrix waarop een foto van de vluchteenheid zelf getoond wordt](images/fu-pic.png)

--- task ---

Onderaan je programma kun je wat kleurvariabelen maken om de kleuren waarmee je je tekening wil maken te definiëren. Je kan zoveel kleuren gebruiken als je wil, maar in dit voorbeeld zullen we maar een paar kleuren gebruiken - rood (`r`), wit (`w`), zwart (`b`), en twee tinten grijs (`g` en `s`). Merk op dat de tinten gemaakt worden door de hoeveelheid licht in alle drie de kanalen te verminderen terwijl de verhoudingen gelijk blijven.

```python
w = (255, 255, 255)
b = (0, 0, 0)
g = (50,50,50)
s = (200,255,200)
r = (255,0,0)
```

**Opmerking:** Deze keer is het een goed idee om de kleurvariabelen namen met één letter te geven, omdat dit tijd zal besparen in de volgende stap, waar je ze vaak zal moeten typen. Bovendien maakt het gebruik van aparte letters het eenvoudiger om de tekening die je maakt te zien.

--- /task ---

--- task ---



Onder je nieuwe variabelen, maak je een lijst van 64 items. Elk item stelt een pixel op de LED-matrix voor en komt overeen met één van de kleurvariabelen die je definieerde. Maak je tekening door een variabele te zetten op de plaats waar je de daaraan toegewezen kleur wil zien verschijnen. We hebben een Astro Pi getekend door de zwarte (`b`) pixels als achtergrond te gebruiken en de grijze (`g`) pixels om de metalen onderdelen van het Astro Pi-omhulsel te tekenen:

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

Misschien wil je een code toevoegen om een korte wachttijd toe te voegen (or `sleep`) nadat de tekening getoond wordt. Dit geeft de astronauten de tijd om je tekening te zien voor het volgende deel van je boodschap verschijnt. Voeg dit bovenaan je programma toe:

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
