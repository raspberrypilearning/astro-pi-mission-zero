## Näytä lämpötila

You could combine your humidity reading with a picture to also indicate the humidity in a graphical way. For example, you might display an ocean for high humidity, and a desert for low humidity:

![Kuuma ja kylmä](images/wet-dry.png)

\--- task \---

Lisää ohjelman loppuun uusia värimuuttujia kaikille väreille, joita haluat käyttää kuvissasi. Olet ehkä jo määritellyt joitakin niistä edellisessä vaiheessa.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Aivan kuten aiemminkin, piirrä kuvat luomalla ensin listan jokaista varten, ja sitten täyttämällä listan kohdat väreillä, joilla haluat pikselisi esitettävän.

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

Lisää koodi lämpötilan saamiseksi:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Päätä nyt, minkä kuvan haluat esitettäväksi. For this example, we will display the `wet` image if the humidity reading is 20% or above, and the `dry` image if the humidity is below 20%.

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

Muuta koodiasi niin, että ohjelma näyttää lämpötilan astronauteille omalla valitsemallasi tavalla.

\--- /task \---