## Prikažite temperaturo

You could combine your humidity reading with a picture to also indicate the humidity in a graphical way. For example, you might display an ocean for high humidity, and a desert for low humidity:

![Vroče in hladno](images/wet-dry.png)

\--- task \---

Na dnu svojega programa določite več barvnih spremenljivk za barve, ki jih želite uporabiti v svojih slikah. Nekatere izmed njih ste morda določili že pri prejšnjem koraku.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Tako kot prej svoje slike ustvarite tako, da za vsako od njih ustvarite seznam in nato elementom seznama določite barve, ki jih želite uporabiti pri prikazu slikovnih pik.

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

Za temperaturo dodajte kodo:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Zdaj se odločite, katero sliko želite uporabiti. For this example, we will display the `wet` image if the humidity reading is 20% or above, and the `dry` image if the humidity is below 20%.

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

Svojo kodo spremenite tako, da bo vaš program astronavtom temperaturo prikazal na želen način.

\--- /task \---