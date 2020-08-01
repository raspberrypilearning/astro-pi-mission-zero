## Vis luftfugtigheden

Du kan kombinere din fugtlæsning med et billede for også at indikere fugtigheden grafisk. For eksempel kan du vise et hav for høj luftfugtighed og en ørken for lav luftfugtighed:

![Våd og tør](images/wet-dry.png)

\--- opgave \---

I bunden af dit program skal du oprette flere farvevariabler for de vilkårlige farver, du ønsker at anvende på dine billeder. Du har måske allerede defineret nogle af dem i et tidligere trin.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /opgave \---

\--- opgave \---

Ligesom tidligere skal du tegne dine billeder ved først at oprette en liste for hvert af dem og derefter tildele elementerne på listen de farver, du ønsker, dine pixels skal være.

```python
hot = [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g
]


cold = [
  b, b, w, b, b, b, w, b,
  b, b, b, b, b, w, b, b,
  b, w, b, b, b, b, b, w,
  b, b, b, b, w, b, b, b,
  w, b, b, w, b, b, w, b,
  b, b, b, b, b, b, b, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w
]
```

\--- /opgave \---

\--- opgave \---

Tilføj noget kode for at få temperaturen:

```python
temp = sense.temperature
```

\--- /opgave \---

\--- opgave \---

Beslut dig derefter for, hvilket billede du vil vise. I dette eksempel viser vi ` våd ` billede, hvis luftfugtigheden er 20% eller derover, og ` tør ` billede, hvis luftfugtigheden er under 20%.

```python
temp = sense.humidity
if temp >= 40:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /opgave \---

\--- opgave \---

Brug fugtighedsskyderen til at indstille en fugtighed på emulatoren. Kør dit program, og kontroller, at det billede, du har valgt til den målte luftfugtighed, vises korrekt.

\--- /opgave \---

\--- opgave \---

Ændre din kode, så dit program viser astronauterne temperaturen på den måde, du selv har valgt.

\--- /opgave \---