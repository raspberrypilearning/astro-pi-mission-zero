## Vis luftfugtigheden

You could combine your humidity reading with a picture to also indicate the humidity in a graphical way. For example, you might display an ocean for high humidity, and a desert for low humidity:

![Våd og tør](images/wet-dry.png)

--- task ---

At the bottom of your program, create more colour variables for any colours you want to use in your pictures. You may already have defined some of them in a previous step.

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

--- opgave ---

Brug fugtighedsskyderen til at indstille en fugtighed på emulatoren. Kør dit program og kontroller, at det billede, du har valgt til den målte luftfugtighed, vises korrekt.

--- /opgave ---

--- opgave ---

Ændre din kode, så dit program viser astronauterne temperaturen på den måde, du selv har valgt.

--- /opgave ---

--- opgave --- Test din kode med et par forskellige fugtighedsindstillinger (ved hjælp af skyderen) for at sikre, at den altid kører korrekt. Hvis du har fulgt eksemplet ovenfor, vises der så et billede både, når luftfugtigheden er indstillet til en værdi mindre end 40% og også når, den er indstillet til mere end 40%?

--- /opgave ---
