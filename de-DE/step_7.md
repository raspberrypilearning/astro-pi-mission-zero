## Anzeigen der Temperatur

Du kannst deinen Temperaturmesswert mit einem Bild kombinieren, um die Temperatur grafisch darzustellen. Du könntest zum Beispiel für kalte Temperaturen einen Schneesturm und für heiße Temperaturen einen sonnigen Tag anzeigen:

![Heiß und kalt](images/hot-and-cold.png)

--- task ---

Erstelle am unteren Rand deines Programms ein paar Farbvariablen, um die Farben zu definieren, mit denen du dein Bild zeichnen möchtest. Möglicherweise hast du bereits einige von ihnen in einem vorherigen Schritt definiert. In unseren Beispielen verwenden wir weiß (`w`), gelb (`y`), grün (`g`) und schwarz / leer (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

--- /task ---

--- task ---

Zeichne deine Bilder wie zuvor, indem du zunächst eine Liste für jedes Bild erstellst und dann die Listenelemente auf die Farben einstellst, die du für deine Pixel verwenden möchtest.

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

--- /task ---

--- task ---

Füge einen Code hinzu, um die Temperatur zu erhalten:

```python
temp = sense.get_temperature()
```

--- /task ---

--- task ---

Entscheide dich jetzt, welches Bild angezeigt werden soll. In diesem Beispiel zeigen wir das `hot` (heiße) Bild an, wenn der Temperaturmesswert 20 Grad oder mehr beträgt, und das `cold` (kalte) Bild, wenn die Temperatur unter 20 Grad liegt.

```python
temp = sense.get_temperature()
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

--- /task ---

--- task ---

Stell mit dem Temperaturregler eine Temperatur auf dem Emulator ein. Führe dein Programm aus und überprüfe, ob das für diese Temperatur ausgewählte Bild richtig angezeigt wird.

--- /task ---

--- task ---

Ändere deinen Code so, dass dein Programm den Astronauten die Temperatur auf deine ausgesuchte Weise anzeigt.

--- /task ---