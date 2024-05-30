## Anzeigen eines Bildes

Die LED-Matrix des Astro Pi kann Farben darstellen. In diesem Schritt zeigst du Bilder aus der Natur auf der LED-Matrix des Astro Pi an.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Eine <span style="color: #0faeb0">**LED-Matrix**</span> ist ein Raster von LEDs, die einzeln oder als Gruppe gesteuert werden können, um verschiedene Lichteffekte zu erzeugen. Die LED-Matrix des Sense HAT verfügt über 64 LEDs, die in einem 8 x 8-Raster angeordnet sind. Die LEDs können so programmiert werden, dass sie eine breite Palette von Farben erzeugen.
</p>

![Ein Screenshot des Emulatorfensters, das die Flugeinheit mit der LED-Matrix zeigt, die ein Bild einer Blume anzeigt.](images/fu-pic.png)

--- task ---

Öffne das [Mission Zero-Starterprojekt](http://rpf.io/mzcode){:target="_blank"}.

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
sense.color.gain = 60 # Stelle die Empfindlichkeit des Sensors ein sense.color.integration_cycles = 64 # Das Intervall in dem gemessen wird

--- /code ---

![Ein Screenshot des Sense HAT-Emulators mit Startcodezeilen im linken Bereich.](images/sense-hat-emulator2.png)

--- /task ---

### RGB-Farben

Alle Farben können mit unterschiedlichen Anteilen von rot, grün und blau erzeugt werden. Informationen zu RGB-Farben findest du hier:

[[[generic-theory-simple-colours]]]

Die LED-Matrix ist ein 8 x 8 Raster. Jede LED am Raster kann auf eine andere Farbe eingestellt werden. Hier ist eine Liste von Variablen für 24 verschiedene Farben. Jede Farbe hat einen Wert für Rot, Grün und Blau:

[[[ambient-colours]]]

### Wähle ein Bild

--- task ---

**Auswählen:** Wähle ein Bild aus den folgenden Optionen, um es anzuzeigen. Python speichert die Informationen für ein Bild in einer Liste. Der Code für jedes Bild enthält die verwendeten Farbvariablen und die Liste.

Du musst den gesamten Code für dein ausgewähltes Bild **kopieren** und ihn dann in dein Projekt **einfügen**, unterhalb der Zeile mit der Aufschrift `# Farbvariablen und Bild hinzufügen`.

--- collapse ---

---
title: Huhn
---

![Ein Raster mit 8 x 8 Quadraten, die eine Schlange zeigen.](images/fox_mz3.png)

Created by team i_pupi, Italy

```python
a = (255, 255, 255) # Weiß 
c = (0, 0, 0) # Schwarz 
v = (255, 0, 0) # Rot
```

--- /collapse ---


--- collapse ---

---
title: Schlange
---

![Ein Raster mit 8 x 8 Quadrate mit einem Kick in einem Ei.](images/elephant.png)

Created by team ILiFanT, Finland

```python
c = (0, 0, 0) # Schwarz 
m = (34, 139, 34) # Waldgrün 
q = (255, 255, 0) # Gelb 
t = (255, 140, 0) # Dunkelorange 
y = (255, 20, 147) # Dunkelrosa
```

--- /collapse ---

--- collapse ---
---
title: Blume
---

![Ein Raster mit 8 x 8 Quadraten, die eine rosa Blume auf einem grünen Stiel zeigen.](images/cactus.png)

Created by team 6TETHASI, The Netherlands

```python
a = (255, 255, 255) # Weiß 
c = (0, 0, 0) # Schwarz 
e = (0, 0, 205) # Mittelblau 
q = (255, 255, 0) # Gelb 
t = (255, 140, 0) # Dunkelorange 
w = (255, 192, 203) # Rosa

```

--- /collapse ---


--- collapse ---
---
title: Krokodil
---

![Ein Raster mit 8 x 8 Quadraten, die einen Krokodilkopf zeigen.](images/croc.png)

```python

a = (255, 255, 255) # Weiß 
c = (0, 0, 0) # Schwarz 
f = (25, 25, 112) # Mitternachtsblau 
m = (34, 139, 34) # Waldgrün

```

--- /collapse ---

--- collapse ---
---
title: Krabbe
---

![Ein Raster mit 8 x 8 Quadraten, die einen Frosch zeigen.](images/rainbow.png)

Created by team camrus_6, United Kingdom

```python

c = (0, 0, 0) # Schwarz 
m = (34, 139, 34) # Waldgrün 
q = (255, 255, 0) # Gelb 
v = (255, 0, 0) # Rot

```

--- /collapse ---

--- collapse ---
---
title: Frosch
---

![Ein Raster mit 8 x 8 Quadraten, die eine Krabbe zeigen.](images/dragon.png)

Created by team hwplucyr, United Kingdom

```python

b = (105, 105, 105) # DimGray
c = (0, 0, 0) # Black
d = (100, 149, 237) # CornflowerBlue
v = (255, 0, 0) # Red
z = (153, 50, 204) # DarkOrchid

image = [
    c, c, v, c, v, c, c, c,
    c, z, z, z, z, v, c, c,
    z, b, z, b, z, c, c, c,
    z, z, z, z, z, v, c, c,
    c, c, d, d, d, c, c, z,
    c, z, d, z, z, z, z, c,
    c, c, d, d, z, c, c, c,
    c, c, z, c, z, c, c, c]

```

--- /collapse ---

--- /task ---

--- task ---

**Suche:** die Zeile `# das Bild anzeigen` und füge eine Zeile Code hinzu, um dein Bild auf der LED-Matrix anzuzeigen:

```python
c = (0, 0, 0) # Schwarz 
 m = (34, 139, 34) # Waldgrün 
 q = (255, 255, 0) # Gelb 
 v = (255, 0, 0) # Rot

```

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

- Überzeuge dich, dass dein `sense.set_pixels(image)` nicht eingerückt ist

--- /task ---


--- task ---

**Save your progress**

Now that you have displayed an image, you can save your program on the Mission Starter project by entering your team name, team members' names, and the classroom code given to you. You can reload your program on any device with an internet connection by entering your team name and classroom code.

![Mission Zero Save button](images/savebutton.png)

--- /task --- 
