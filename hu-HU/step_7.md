## Jelenítsd meg a hőmérsékletet!

You could combine your humidity reading with a picture to also indicate the humidity in a graphical way. For example, you might display an ocean for high humidity, and a desert for low humidity:

![Hideg és meleg](images/wet-dry.png)

\--- task \---

A programod végén hozz létre még több színváltozót azokra a színekre, amelyeket használni szeretnél a képeidben. Lehetséges, hogy van olyan, amit már egy előző lépésben meghatároztál.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Akárcsak korábban, a képeid megrajzolásához hozz létre egy listát mindegyiknek, majd állítsd be a listaelemeket azokra a színekre, amelyekre szeretnéd a pixeleidet beszínezni.

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

Add hozzá a kódot, hogy megkapd a hőmérsékletet:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Most döntsd el, melyik képet szeretnéd megjeleníteni. For this example, we will display the `wet` image if the humidity reading is 40% or above, and the `dry` image if the humidity is below 40%.

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

Változtasd meg a kódot, hogy a programod az általad választott módon jelenítse meg a hőmérsékletet az űrhajósok számára.

\--- /task \---