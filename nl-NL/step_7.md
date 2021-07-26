## Geef de luchtvochtigheid weer

Je kunt je luchtvochtigheidsmeting combineren met een afbeelding om ook de luchtvochtigheid op een grafische manier aan te geven. Je kunt bijvoorbeeld een oceaan weergeven voor lage luchtvochtigheid en een woestijn voor hoge luchtvochtigheid:

![Nat en droog](images/wet-dry.png)

--- task ---

Maak onder aan het programma meer kleurvariabelen voor alle kleuren die je in je afbeeldingen wilt gebruiken. Mogelijk heb je sommige ervan al in een vorige stap gedefinieerd.

```python
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)
```

--- /task ---

--- task ---

Teken net als eerder je afbeeldingen door eerst een lijst voor elk van deze te maken en vervolgens de lijstitems in te stellen op de kleuren die je wilt dat je pixels zijn.

```python
wet = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


dry = [
  c, c, g, g, c, c, c, c,
  c, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, g, g, g, g, g, c, c,
  c, c, g, g, c, c, c, c,
  y, y, y, y, y, y, y, y,
  y, y, y, y, y, y, y, y
]
```

--- /task ---

--- task ---

Voeg wat code toe om de luchtvochtigheid te krijgen:

```python
humid = sense.humidity
```

--- /task ---

--- task ---

Bepaal nu welke afbeelding moet worden weergegeven. Voor dit voorbeeld zullen we de `wet` (natte) afbeelding weergeven als de luchtvochtigheidswaarde 40 % of meer is, en de `dry` (droge) afbeelding als de luchtvochtigheid lager is dan 40 %.

```python
humid = sense.humidity
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

Gebruik de schuifregelaar voor luchtvochtigheid om een luchtvochtigheid op de emulator in te stellen. Voer je programma uit en controleer of de afbeelding die je voor die luchtvochtigheid hebt geselecteerd correct wordt weergegeven.

--- /task ---

--- task ---

Wijzig je code zodat je programma de luchtvochtigheid op je eigen gekozen manier aan de astronauten weergeeft.

--- /task ---

--- task --- Test your code with a few different humidity settings (using the slider) to make sure it always runs correctly. If you've followed the example above, is an image displayed both when the humidity is set to a value less than 40% and also when it is set to more than 40%?

--- /task ---
