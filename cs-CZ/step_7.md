## Zobrazte teplotu

You could combine your humidity reading with a picture to also indicate the humidity in a graphical way. For example, you might display an ocean for high humidity, and a desert for low humidity:

![Teplo a zima](images/wet-dry.png)

\--- task \---

Na konci programu vytvořte ještě několik proměnných s barvami, jaké budete chtít použít v obrázcích. Možná jste některé z nich definovali už v předchozím kroku.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Stejně jako předtím nakreslete obrázky tak, že pro každý z nich vytvoříte seznam a potom položky tohoto seznamu nastavíte na barvy, které mají mít jednotlivé pixely.

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

Přidejte kód pro získání teploty:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Teď rozhodněte, který obrázek se zobrazí. For this example, we will display the `wet` image if the humidity reading is 20% or above, and the `dry` image if the humidity is below 20%.

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

Změňte kód tak, aby váš program ukazoval astronautům teplotu tak, jak chcete vy.

\--- /task \---