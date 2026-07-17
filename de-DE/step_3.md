## Anzeigen eines Bildes

The image you display will be made from 64 coloured squares called **pixels**. The pixels are arranged in an 8 x 8 grid. Each pixel can be a different colour. By choosing the colours carefully, you can create a picture. Here is an example of a whale made using different shades of blue on a black background.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Eine <span style="color: #0faeb0">**LED-Matrix**</span> ist ein Raster von LEDs, die einzeln oder als Gruppe gesteuert werden können, um verschiedene Lichteffekte zu erzeugen. Die LED-Matrix des Sense HAT verfügt über 64 LEDs, die in einem 8 x 8-Raster angeordnet sind. Die LEDs können so programmiert werden, dass sie eine breite Palette von Farben erzeugen.
</p>

![an 8x8 image of a whale with letters labelling different colours](images/whale.png)

Notice that each square is labelled with a code to represent a particular colour. In this image 3 colours are used:
+ c = black
+ f = Ocean blue
+ g = Sky blue


--- task ---

Öffne das [Mission Zero-Starterprojekt](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"}.

Du wirst sehen, dass einige Zeilen Code bereits automatisch erscheinen.

Dieser Code verbindet sich mit dem Astro Pi, stellt sicher, dass die LED-Anzeige des Astro Pi richtig herum angezeigt wird und richtet den Farbsensor ein. Lass den Code so dort stehen, weil du ihn noch brauchen wirst.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Bibliotheken importieren
from sense_hat import SenseHat from time import sleep

# Einrichten des Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Farbsensor einrichten
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Ein Screenshot des Sense HAT-Emulators mit Startcodezeilen im linken Bereich.](images/sense-hat-emulator3.png)

--- /task ---

### RGB-Farben

Alle Farben können mit unterschiedlichen Anteilen von rot, grün und blau erzeugt werden. Informationen zu RGB-Farben findest du hier:

![Three sliders demonstrating RGB colour values](images/rgbsliders.gif)

Die LED-Matrix ist ein 8 x 8 Raster. Jede LED am Raster kann auf eine andere Farbe eingestellt werden. We can use the letters a to z as the names of variables to represent 24 different colours. Each colour has a value for red, green, and blue.

--- collapse ---

---
title: List of Colour Variables
---

![A grid of 24 coloured squared each labelled with a different letter of the alphabet](images/palette.png)

```python
a = (255, 255, 255) # White
b = (171, 171, 171) # Grey
c = (0, 0, 0)       # Black
d = (25, 25, 113)   # Navy Blue
e = (0, 0, 255)     # Pure Blue
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue
h = (86, 255, 255)  # Electric Cyan
j = (0, 255, 0)     # Pure Green
k = (46, 139, 33)   # Leaf Green
l = (57, 97, 17)    # Olive Green
m = (30, 65, 6)     # Forest Green
n = (126, 88, 25)   # Earth Brown
o = (179, 96, 65)   # Terracotta Brown
p = (180, 34, 34)   # Brick Red
q = (255, 0, 0)     # Pure Red
r = (232, 118, 5)   # Orange
s = (241, 231, 100) # Pale Yellow
t = (255, 255, 0)   # Pure Yellow
u = (255, 209, 209) # Pale Pink
v = (255, 177, 177) # Blush Pink
w = (249, 169, 255) # Light Pink
y = (248, 97, 255)  # Magenta
z = (220, 53, 232)  # Purple

```

--- /collapse ---

### Wähle ein Bild

--- task ---

**Auswählen:** Wähle ein Bild aus den folgenden Optionen, um es anzuzeigen. Python speichert die Informationen für ein Bild in einer Liste. Der Code für jedes Bild enthält die verwendeten Farbvariablen und die Liste.

Du musst den gesamten Code für dein ausgewähltes Bild **kopieren** und ihn dann in dein Projekt **einfügen**, unterhalb der Zeile mit der Aufschrift `# Farbvariablen und Bild hinzufügen`.

--- collapse ---

---
title: Whale
---

![A grid with 8 x 8 squares showing a whale.](images/whale.png)

Created by Team Naicom, Italy

```python
c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue

image = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, a,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

```

--- /collapse ---


--- collapse ---

---
title: Lemon
---

![A grid with 8 x 8 squares showing a lemon.](images/lemon.png)

Created by team g4lemoni, Greece

```python
a = (255, 255, 255) # White
k = (46, 139, 33)   # Leaf Green
t = (255, 255, 0)   # Pure Yellow

image = [
c, c, c, k, k, c, c, c,
c, c, k, c, k, c, c, c,
c, k, c, t, t, c, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, c, t, t, c, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Pig
---

![A grid with 8 x 8 squares showing a pig.](images/pig.png)

Created by Gary, United Kingdom

```python
a = (255, 255, 255) # White
u = (255, 209, 209) # Pale Pink
v = (255, 177, 177) # Blush Pink
o = (179, 96, 65)   # Terracotta Brown
c = (0, 0, 0)       # Black

image = [
a, a, y, a, a, y, a, a,
a, y, y, y, y, y, y, a,
a, y, c, y, c, y, y, y,
v, v, v, v, v, y, y, y,
v, o, v, o, v, y, y, y,
v, v, v, v, v, y, y, y,
a, y, y, y, y, y, y, y,
a, a, y, a, a, a, y, a]

```

--- /collapse ---


--- collapse ---
---
title: Storm
---

![A grid with 8 x 8 squares showing a storm cloud.](images/storm.png)

Created by team hop2p023, Spain

```python

c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue
t = (255, 255, 0)   # Pure Yellow

image = [
c, c, c, c, c, c, c, c,
c, c, f, f, f, f, c, c,
c, f, f, f, f, f, f, c,
c, g, c, g, t, g, c, c,
c, c, c, t, t, c, c, c,
c, c, t, t, c, c, c, c,
c, c, g, c, c, c, c, g,
c, g, c, c, c, c, c, c]


```

--- /collapse ---

--- collapse ---
---
title: Duck
---

![A grid with 8 x 8 squares showing a duck.](images/duck.png)

Created by Peter, Ireland

```python

c = (0, 0, 0) # Black
l = (57, 97, 17)    # Olive Green
m = (30, 65, 6)     # Forest Green
r = (232, 118, 5)   # Orange
a = (255, 255, 255) # White
b = (171, 171, 171) # Grey

image = [
c, l, l, c, c, c, c, c,
r, r, m, c, c, c, c, c,
c, l, l, c, c, c, c, c,
c, a, a, l, a, a, c, c,
c, l, l, a, a, a, b, a,
c, a, a, b, b, b, a, a,
c, c, a, a, a, a, c, c,
c, c, c, r, c, r, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Frog
---

![A grid with 8 x 8 squares showing a Frog.](images/frog.png)

Created by team Jmeno, Czech Republic

```python

a = (255, 255, 255) # White
b = (171, 171, 171) # Grey
c = (0, 0, 0)       # Black
q = (255, 0, 0)     # Pure Red
j = (0, 255, 0)     # Pure Green
k = (46, 139, 33)   # Leaf Green
n = (126, 88, 25)   # Earth Brown

image = [
a, a, a, a, a, a, a, a,
a, a, a, a, a, b, a, b,
a, a, a, a, a, a, c, a,
a, a, c, a, c, a, q, a,
a, a, j, j, j, q, a, a,
a, j, j, k, q, a, a, a,
j, k, j, k, k, a, a, a,
k, k, k, j, k, n, n, n]

```

--- /collapse ---

--- collapse ---
---
title: Blossom Tree
---

![A grid with 8 x 8 squares showing a tree in blossom.](images/blossom.png)

Created by team Zssh14, Slovakia

```python

t = (255, 255, 0)   # Pure Yellow
g = (0, 204, 255)   # Sky Blue
w = (249, 169, 255) # Light Pink
y = (248, 97, 255)  # Magenta
z = (220, 53, 232)  # Purple
n = (126, 88, 25)   # Earth Brown
o = (179, 96, 65)   # Terracotta Brown
k = (46, 139, 33)   # Leaf Green

image =  [
t, g, g, w, w, y, g, g,
g, g, w, w, y, y, z, g,
g, w, y, z, y, z, z, z,
w, y, z, z, g, n, w, g,
g, g, o, o, n, w, y, z,
g, g, g, g, n, g, g, g,
g, g, g, o, n, n, g, g,
k, k, o, n, n, n, k, k]

```

--- /collapse ---

--- /task ---

--- task ---

**Suche:** die Zeile `# das Bild anzeigen` und füge eine Zeile Code hinzu, um dein Bild auf der LED-Matrix anzuzeigen:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, a, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

# Das Bild anzeigen
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Drücke **Ausführen** am unteren Rand des Editors, um dein Bild auf der LED-Matrix anzuzeigen.

--- /task ---

--- task ---

**Fehlersuche**

Mein Code hat einen Syntaxfehler:

- Überprüfe, ob dein Code mit dem Code in den obigen Beispielen übereinstimmt
- Überprüfe, ob du den Code richtig eingerückt hast
- Überprüfe, ob deine Liste von `[` und `]`umgeben ist
- Überprüfe, ob die Farbvariablen in der Liste durch ein Kommas getrennt sind

Mein Bild wird nicht angezeigt:

- Überzeuge dich, dass dein `sense.set_pixels(bild)` nicht eingerückt ist

--- /task ---


--- task ---

**Speichere deinen Fortschritt**

Nachdem du nun ein Bild angezeigt hast, kannst du dein Programm im Mission Starter-Projekt speichern, indem du deinen Teamnamen, die Namen der Teammitglieder und den dir zugewiesenen Klassen-Code eingibst. Du kannst dein Programm auf jedem Gerät mit Internetverbindung neu laden, indem du deinen Teamnamen und deinen Klassen-Code eingibst.

![Mission Zero Speichern-Button](images/mz_savebutton_v2.png)

--- /task --- 
