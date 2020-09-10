## Laat de vochtigheid zien

Je kan je vochtigheidsmeting combineren met een foto om de vochtigheid ook op een grafische manier te laten zien. Je kan bijvoorbeeld een oceaan tonen voor hoge vochtigheid en een woestijn voor lage luchtvochtigheid:

![Nat en droog](images/wet-dry.png)

\--- task \---

Onderaan je programma, kun je meer kleurvariabelen definiëren voor kleuren die je wil gebruiken in je tekeningen. Misschien heb je al sommige gedefinieerd in een vorige stap.

```python
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)
```

\--- /task \---

\--- task \---

Net zoals eerder, teken je tekeningen door eerst een lijst aan te maken voor elk van hen, en zet dan de items met de kleuren op de lijst die je voor je pixels wilt gebruiken.

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

\--- /task \---

\--- task \---

Voeg code toe om de vochtigheid te verkrijgen:

```python
humid = sense.humidity
```

\--- /task \---

\--- task \---

Beslis nu welke tekening je wilt tonen. In dit voorbeeld zullen we de `wet`(nat) tekening laten zien als de vochtigheidsmeting 40% of hoger is en de `dry` (droog) tekening als de vochtigheid lager is dan 40%.

```python
humid = sense.humidity
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

\--- /task \---

\--- task \---

Gebruik de vochtigheid-schuifknop om een vochtigheid op de emulator in te stellen. Start je programma en controleer dat de tekening die je koos voor die vochtigheid juist weergegeven wordt.

\--- /task \---

\--- task \---

Verander je code zodat je programma de vochtigheid weergeeft aan de astronauten op de door jou gekozen manier.

\--- /task \---