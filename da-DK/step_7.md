## Vis luftfugtigheden

Du kan kombinere din fugtlæsning med et billede for også at indikere fugtigheden grafisk. For eksempel kan du vise et hav for høj luftfugtighed og en ørken for lav luftfugtighed:

![Våd og tør](images/wet-dry.png)

--- task ---

I bunden af dit program skal du oprette flere farvevariabler for de vilkårlige farver, du ønsker at anvende på dine billeder. Du har måske allerede defineret nogle af dem i et tidligere trin.

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

Ligesom tidligere skal du tegne dine billeder ved først at oprette en liste for hvert af dem og derefter tildele elementerne på listen de farver, du ønsker, dine pixels skal være.

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

Tilføj noget kode for at få luftfugtigheden:

```python
humid = sense.humidity
```

--- /task ---

--- task ---

Beslut dig derefter for, hvilket billede du vil vise. I dette eksempel viser vi `våd (wet)` billede, hvis luftfugtigheden er 40% eller derover og `tør (dry)` billede, hvis luftfugtigheden er under 40%.

```python
humid = sense.humidity
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

Brug fugtighedsskyderen til at indstille en fugtighed på emulatoren. Kør dit program, og kontroller, at det billede, du har valgt til den målte luftfugtighed, vises korrekt.

--- /task ---

--- task ---

Ændre din kode, så dit program viser astronauterne temperaturen på den måde, du selv har valgt.

--- /task ---