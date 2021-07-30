## Anzeigen eines Bildes

Auf der LED-Matrix des Astro Pi kannst du auch Bilder anzeigen. Vielleicht könnte dein Gruß an die Astronauten zusätzlich, oder statt einer schriftlichen Nachricht, ein Bild oder ein Muster enthalten?

![Astronaut](images/astronaut-pic.png)

--- task ---

Erstelle am unteren Rand deines Programms ein paar Farbvariablen, um die Farben zu definieren, mit denen du dein Bild zeichnen möchtest. Du kannst so viele Farben verwenden, wie du möchtest, aber in diesem Beispiel bleiben wir bei zwei Farben — weiß (`w`) und schwarz (`s`). Beachte, dass die Schattierungen durch die Reduzierung der Lichtmenge in allen drei Kanälen erzielt werden, während die Proportionen gleich bleiben.

```python
w = (255, 255, 255)
s = (0, 0, 0)
```

**Hinweis:** Es ist hier sinnvoll den Farbvariablen Namen aus nur einem Buchstaben zu geben, denn das spart Zeit im nächsten Schritt, wo du sie mehrmals tippen musst. Darüber hinaus erleichtert die Verwendung einzelner Buchstaben das Erkennen des gezeichneten Bildes.

--- /task ---

--- task ---



Erstelle unter deinen neuen Variablen eine Liste von 64 Elementen. Jedes Element repräsentiert ein Pixel in der LED-Matrix und entspricht einer der von dir definierten Farbvariablen. Zeichne dein Bild, indem du eine Variable dort einfügst, wo die zugewiesene Farbe angezeigt werden soll. Wir haben einen Astronauten gezeichnet, indem wir die schwarzen (`s`) Pixel als Hintergrund und die weißen (`w`) Pixel für den Raumanzug des Astronauten benutzt haben:

```python
 bild = [
    s, s, w, w, w, w, s, s,
    s, w, s, s, s, s, w, s,
    s, w, s, w, w, s, w, s,
    s, w, s, s, s, s, w, s,
    s, s, w, w, w, w, s, s,
    s, s, w, w, w, w, s, s,
    s, w, w, w, w, w, w, s,
    s, w, w, w, w, w, w, s
]
```
--- /task ---

--- task ---

Füge eine Codezeile hinzu, um dein Bild auf dem LED-Bildschirm anzuzeigen.

```python
sense.set_pixels(bild)
```

--- /task ---

--- task ---

Klicke auf **Run** (Ausführen), um dein Bild angezeigt zu sehen.

--- /task ---

--- task ---

Vielleicht möchtest du Code hinzufügen, um eine kurze Pause (oder `sleep` (Schlaf)) einzubauen nachdem das Bild angezeigt wird. Dies wird den Astronauten Zeit geben, dein Bild zu betrachten, bevor der nächste Teil deiner Nachricht erscheint. Füge oben in deinem Programm Folgendes hinzu:

```python
from time import sleep
```

Füge dann in der Zeile unter deinem Bild diesen Code hinzu, um zwei Sekunden zu warten:

```python
sleep(2)
```

--- /task ---

--- task ---

Erstelle dein eigenes Bild oder Muster, um es den Astronauten zu zeigen!

--- /task ---
