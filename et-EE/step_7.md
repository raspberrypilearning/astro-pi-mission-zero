## Õhutemperatuuri kuvamine

You could combine your humidity reading with a picture to also indicate the humidity in a graphical way. For example, you might display an ocean for high humidity, and a desert for low humidity:

![Kuum ja külm](images/wet-dry.png)

\--- task \---

Oma programmi lõpus lisa rohkem värvimuutujaid värvide jaoks, mida tahad oma piltidel kasutada. Võimalik, et oled mõned juba eelmises etapis määranud.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Täpselt samamoodi kui varem, oma piltide joonistamiseks tee kõigepealt iga pildi jaoks loetelu ja seejärel vastavalt soovitud pikslite värvidele määra loetelu ühikutele värvid.

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

Õhutemperatuuri saamiseks lisa kood:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Nüüd otsusta, millist pilti kuvada. For this example, we will display the `wet` image if the humidity reading is 20% or above, and the `dry` image if the humidity is below 20%.

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

Muuda oma koodi, et sinu programm kuvaks õhutemperatuuri astronautidele sinu poolt valitud viisil.

\--- /task \---