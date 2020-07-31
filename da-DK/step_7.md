## Vis temperaturen

You could combine your humidity reading with a picture to also indicate the humidity in a graphical way. For example, you might display an ocean for high humidity, and a desert for low humidity:

![Varmt og koldt](images/wet-dry.png)

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

Beslut dig derefter for, hvilket billede du vil vise. For this example, we will display the `wet` image if the humidity reading is 20% or above, and the `dry` image if the humidity is below 20%.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /opgave \---

\--- opgave \---

Use the humidity slider to set a humidity on the emulator. Run your program and check that the image you've selected for that humidity is correctly displayed.

\--- /opgave \---

\--- opgave \---

Ændre din kode, så dit program viser astronauterne temperaturen på den måde, du selv har valgt.

\--- /opgave \---