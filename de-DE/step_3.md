## Anzeigen eines Bildes

Das angezeigte Bild wird aus 64 farbigen Quadraten namens **Pixeln** erstellt. Die Pixel sind in einem 8 x 8 Raster angeordnet. Jedes Pixel kann eine andere Farbe haben. Durch die sorgfältige Auswahl der Farben lässt sich ein Bild gestalten. Hier ist ein Beispiel für einen Wal, der aus verschiedenen Blautönen auf schwarzem Hintergrund besteht.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Eine <span style="color: #0faeb0">**LED-Matrix**</span> ist ein Raster von LEDs, die einzeln oder als Gruppe gesteuert werden können, um verschiedene Lichteffekte zu erzeugen. Die LED-Matrix des Sense HAT verfügt über 64 LEDs, die in einem 8 x 8-Raster angeordnet sind. Die LEDs können so programmiert werden, dass sie eine breite Palette von Farben erzeugen.
</p>

![ein 8x8 Bild eines Wales mit Buchstaben, die verschiedene Farben kennzeichnen](images/whale.png)

Beachte, dass jedes Quadrat mit einem Code versehen ist, der eine bestimmte Farbe repräsentiert. In diesem Bild werden 3 Farben verwendet:
+ c = schwarz
+ f = Ozeanblau
+ g = Himmelblau


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

![Drei Schieberegler zur Darstellung der RGB-Farbwerte](images/rgbsliders.gif)

Die LED-Matrix ist ein 8 x 8 Raster. Jede LED am Raster kann auf eine andere Farbe eingestellt werden. Wir können die Buchstaben a bis z als Namen von Variablen verwenden, um 24 verschiedene Farben darzustellen. Jede Farbe hat einen Wert für Rot, Grün und Blau.

--- collapse ---

---
title: Liste der Farbvariablen
---

![Ein Raster aus 24 farbigen Quadraten, von denen jedes mit einem anderen Buchstaben des Alphabets beschriftet ist](images/palette.png)

```python
a = (255, 255, 255) # Weiß
b = (171, 171, 171) # Grau
c = (0, 0, 0) # Schwarz
d = (25, 25, 113) # Marineblau
e = (0, 0, 255) # Reines Blau
f = (36, 128, 200) # Ozeanblau
g = (0, 204, 255) # Himmelblau
h = (86, 255, 255) # Elektrisches Cyan
j = (0, 255, 0) # Reines Grün
k = (46, 139, 33) # Blattgrün
l = (57, 97, 17) # Olivgrün
m = (30, 65, 6) # Waldgrün
n = (126, 88, 25) # Erdbraun
o = (179, 96, 65) # Terrakottabraun
p = (180, 34, 34) # Ziegelrot
q = (255, 0, 0) # Reines Rot
r = (232, 118, 5) # Orange
s = (241, 231, 100) # Hellgelb
t = (255, 255, 0) # Reines Gelb
u = (255, 209, 209) # Hellrosa
v = (255, 177, 177) # Blush Pink
w = (249, 169, 255) # Helles Pink
y = (248, 97, 255) # Magenta
z = (220, 53, 232) # Lila

```

--- /collapse ---

### Wähle ein Bild

--- task ---

**Auswählen:** Wähle ein Bild aus den folgenden Optionen, um es anzuzeigen. Python speichert die Informationen für ein Bild in einer Liste. Der Code für jedes Bild enthält die verwendeten Farbvariablen und die Liste.

Du musst den gesamten Code für dein ausgewähltes Bild **kopieren** und ihn dann in dein Projekt **einfügen**, unterhalb der Zeile mit der Aufschrift `# Farbvariablen und Bild hinzufügen`.

--- collapse ---

---
title: Wal
---

![Ein Raster mit 8 x 8 Quadraten, die einen Wal zeigen.](images/whale.png)

Erstellt vom Team Naicom, Italien

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
title: Zitrone
---

![Ein Raster mit 8 x 8 Quadraten, das eine Zitrone zeigt.](images/lemon.png)

Erstellt von Team g4lemoni, Griechenland

```python
c = (0, 0, 0)       # Black
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
title: Schwein
---

![Ein Raster mit 8 x 8 Quadraten, das ein Schwein zeigt.](images/pig.png)

Erstellt von Gary, Großbritannien

```python
a = (255, 255, 255) # White
v = (255, 177, 177) # Blush Pink
y = (248, 97, 255)  # Magenta
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
title: Sturm
---

![Ein Raster mit 8 x 8 Quadraten, das eine Gewitterwolke darstellt.](images/storm.png)

Erstellt von Team hop2p023, Spanien

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
title: Ente
---

![Ein Raster mit 8 x 8 Quadraten, das eine Ente zeigt.](images/duck.png)

Erstellt von Peter, Irland

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
title: Frosch
---

![Ein Raster mit 8 x 8 Quadraten, das einen Frosch zeigt.](images/frog.png)

Erstellt vom Team Jmeno, Tschechische Republik

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
title: blühender Baum
---

![Ein Raster aus 8 x 8 Quadraten, das einen blühenden Baum zeigt.](images/blossom.png)

Erstellt vom Team Zssh14, Slowakei

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
