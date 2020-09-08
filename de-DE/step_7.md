## Zeige die Luftfeuchtigkeit an

Du kannst deinen Feuchtigkeitsmesswert auch mit einem Bild kombinieren, um die Luftfeuchtigkeit auch grafisch anzuzeigen. Beispielsweise könntest du einen Ozean für hohe Luftfeuchtigkeit und eine Wüste für niedrige Luftfeuchtigkeit anzeigen:

![Nass und trocken](images/wet-dry.png)

--- task ---

Erstelle am unteren Rand deines Programms ein paar Farbvariablen, um die Farben zu definieren, mit denen du dein Bild zeichnen möchtest. Möglicherweise hast du bereits einige von ihnen in einem vorherigen Schritt definiert.

```python
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)
```

--- /task ---

--- task ---

Zeichne deine Bilder wie zuvor, indem du zunächst eine Liste für jedes Bild erstellst und dann die Listenelemente auf die Farben einstellst, die du für deine Pixel verwenden möchtest.

```python
nass = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


trocken = [
  c, c, g, g, c, c, c, c,
  c, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, g, g, g, g, g, c, c,
  c, c, g, g, c, c, c, c,
  y, y, y, y, y, y, y, y,
  y, y, y, y, y, y, y, y
]
```

--- /task ---

--- task ---

Füge Code hinzu, um die Luftfeuchtigkeit zu ermitteln:

```python
humid = sense.humidity
```

--- /task ---

--- task ---

Entscheide dich jetzt, welches Bild angezeigt werden soll. In diesem Beispiel wird das Bild `nass` angezeigt, wenn der Feuchtigkeitswert 40% oder mehr beträgt und das `Trocken-`Bild, wenn die Luftfeuchtigkeit unter 40% liegt.

```python
humid = sense.humidity
if humid >= 40:
    sense.set_pixels(nass)
else:
    sense.set_pixels(trocken)
```

--- /task ---

--- task ---

Verwende den Feuchtigkeitsregler, um eine Luftfeuchtigkeit am Emulator einzustellen. Führe dein Programm aus und überprüfe, ob das für diese Luftfeuchtigkeit ausgewählte Bild richtig angezeigt wird.

--- /task ---

--- task ---

Ändere deinen Code so, dass dein Programm den Astronauten die Luftfeuchtigkeit auf die von dir gewählte Weise anzeigt.

--- /task ---