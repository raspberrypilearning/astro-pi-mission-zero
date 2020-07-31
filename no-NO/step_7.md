## Vise temperaturen

You could combine your humidity reading with a picture to also indicate the humidity in a graphical way. For example, you might display an ocean for high humidity, and a desert for low humidity:

![Varmt og kaldt](images/wet-dry.png)

\--- task \---

På slutten av programmet kan dere opprette flere fargevariabler for fargene dere vil bruke i bildene. Dere har kanskje allerede definert noen av dem i et tidligere trinn.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Som tidligere begynner dere med å opprette en liste for hver av dem, og deretter angir dere farger for punktene på listen slik dere vil at bildene skal være.

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

\--- /task \---

\--- task \---

Legg til kode for å få temperaturen:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Nå bestemmer dere hvilket bilde som skal vises. For this example, we will display the `wet` image if the humidity reading is 20% or above, and the `dry` image if the humidity is below 20%.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /task \---

\--- task \---

Use the humidity slider to set a humidity on the emulator. Run your program and check that the image you've selected for that humidity is correctly displayed.

\--- /task \---

\--- task \---

Endre koden slik at programmet viser temperaturen til astronautene slik dere har valgt.

\--- /task \---