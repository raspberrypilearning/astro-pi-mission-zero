## Afișează temperatura

You could combine your humidity reading with a picture to also indicate the humidity in a graphical way. For example, you might display an ocean for high humidity, and a desert for low humidity:

![Cald și rece](images/wet-dry.png)

\--- task \---

În partea de jos a programului tău, creează mai multe variabile pentru orice culori pe care vrei sa le folosești în imaginile tale. Este posibil să fi definit deja unele dintre ele într-un pas anterior.

```python
a = (255, 255, 255)
g = (255, 255, 0)
v = (0, 255, 0)
n = (0, 0, 0)
```

\--- /task \---

\--- task \---

La fel ca mai devreme, desenează imaginile tale, creând mai întâi o listă pentru fiecare dintre ele, apoi setând elementele listei la culorile pe care dorești să le aibă pixelii.

```python
cald = [
  n, n, n, n, n, g, g, n,
  n, n, n, n, g, g, g, g,
  n, n, n, n, n, g, g, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  v, v, v, v, v, v, v, v,
  v, v, v, v, v, v, v, v
]


rece = [
  n, n, a, n, n, n, a, n,
  n, n, n, n, n, a, n, n,
  n, a, n, n, n, n, n, a,
  n, n, n, n, a, n, n, n,
  a, n, n, a, n, n, a, n,
  n, n, n, n, n, n, n, n,
  a, a, a, a, a, a, a, a,
  a, a, a, a, a, a, a, a
]
```

\--- /task \---

\--- task \---

Adaugă cod pentru a obține temperatura:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Acum decide ce imagine vrei să se afișeze. For this example, we will display the `wet` image if the humidity reading is 20% or above, and the `dry` image if the humidity is below 20%.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(cald)
else:
    sense.set_pixels(rece)
```

\--- /task \---

\--- task \---

Use the humidity slider to set a humidity on the emulator. Run your program and check that the image you've selected for that humidity is correctly displayed.

\--- /task \---

\--- task \---

Modifică codul astfel încât programul să afișeze temperatura pentru astronauți în modul ales de tine.

\--- /task \---