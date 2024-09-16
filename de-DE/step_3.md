## Anzeigen eines Bildes

Die LED-Matrix des Astro Pi kann Farben darstellen. In diesem Schritt zeigst du Bilder aus der Natur auf der LED-Matrix des Astro Pi an.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Eine <span style="color: #0faeb0">**LED-Matrix**</span> ist ein Raster von LEDs, die einzeln oder als Gruppe gesteuert werden können, um verschiedene Lichteffekte zu erzeugen. Die LED-Matrix des Sense HAT verfügt über 64 LEDs, die in einem 8 x 8-Raster angeordnet sind. Die LEDs können so programmiert werden, dass sie eine breite Palette von Farben erzeugen.
</p>

![Ein Screenshot des Emulatorfensters, das die Flugeinheit mit der LED-Matrix zeigt, die ein Bild einer Blume anzeigt.](images/fu-pic.png)

--- task ---

Öffne das [Mission Zero-Starterprojekt](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"}.

Du wirst sehen, dass einige Zeilen Code bereits automatisch erscheinen.

Dieser Code verbindet sich mit dem Astro Pi, stellt sicher, dass die LED-Anzeige des Astro Pi richtig herum angezeigt wird und richtet den Farbsensor ein. Lass den Code so dort stehen, weil du ihn noch brauchen wirst.

--- code ---
---
language: python 
filename: main.py 
line_numbers: false 
line_number_start: 1
line_highlights:
---
# Bibliotheken importieren
from sense_hat import SenseHat 
from time import sleep

# Einrichten des Sense HAT
sense = SenseHat() 
sense.set_rotation(270)

# Farbsensor einrichten
sense.color.gain = 60 # Stelle die Empfindlichkeit des Sensors ein 
sense.color.integration_cycles = 64 # Das Intervall in dem gemessen wird

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
title: Fuchs
---

![Ein Raster mit 8 x 8 Quadraten, die ein Fuchsgesicht zeigen.](images/fox_mz3.png)

Erstellt vom Team i_pupi, Italien

```python
c = (0, 0, 0) # Schwarz
a = (255, 255, 255) # Weiß
t = (255, 140, 0) # Dunkelorange

bild = [
t, a, t, c, c, t, a, t,
t, a, t, c, c, t, a, t,
t, t, t, t, t, t, t, t,
t, a, c, t, t, c, a, t,
t, t, t, t, t, t, t, t,
a, a, a, c, c, a, a, a,
c, a, a, a, a, a, a, c,
c, c, a, a, a, a, c, c]
```

--- /collapse ---

--- collapse ---

---
title: Elefant
---

![Ein Raster mit 8 x 8 Quadraten, die einen Elefanten zeigen.](images/elephant.png)

Erstellt vom Team ILiFanT, Finnland

```python
c = (0, 0, 0) # Schwarz
b = (105, 105, 105) # Dunkelgrau
a = (255, 255, 255) # Weiß

bild = [
    c, c, c, c, c, c, c, c,
    c, b, b, b, c, c, c, c,
    c, b, c, b, c, c, b, b,
    c, b, c, c, c, b, b, b,
    c, b, b, c, c, b, c, b,
    c, b, b, b, b, b, b, b,
    c, c, b, b, a, b, b, b,
    c, c, c, c, a, b, b, b]
```

--- /collapse ---

--- collapse ---
---
title: Kaktus
---

![Ein Raster mit 8 x 8 Quadraten, die einen Kaktus zeigen.](images/cactus.png)

Erstellt vom Team 6TETHASI, Niederlande

```python
a = (255, 255, 255) # Weiß
c = (0, 0, 0) # Schwarz
n = (154, 205, 50) # Gelbgrün
q = (255, 255, 0) # Gelb
t = (255, 140, 0) # Dunkelorange

bild = [   
  q, q, c, n, c, c, a, c,
  q, c, c, n, c, a, a, a,
  c, n, c, n, c, c, c, c,
  c, n, n, n, c, n, c, c,
  c, a, n, n, n, n, c, c,
  a, a, a, n, c, a, a, a,
  c, c, c, n, a, a, a, c,
  t, t, t, t, t, t, t, t]

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

bild = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

```

--- /collapse ---

--- collapse ---
---
title: Regenbogen
---

![Ein Raster mit 8 x 8 Quadraten, die einen Regenbogen zeigen.](images/rainbow.png)

Erstellt von Team camrus_6, Vereinigtes Königreich

```python

c = (100, 149, 237) # Kornblumenblau
a = (255, 255, 255) # Weiß
v = (255, 0, 0) # Rot
t = (255, 140, 0) # Dunkelorange
q = (255, 255, 0) # Gelb
l = (0, 255, 127) # Frühlingsgrün
e = (0, 0, 205) # Mittelblau

regenbogen = [
  c, c, c, c, c, c, c, c, 
  v, v, v, v, c, c, c, c,
  t, t, t, t, v, v, c, c,
  q, q, q, q, t, v, c, c,
  l, l, l, l, q, t, v, c,
  e, e, e, l, q, t, v, c,
  c, c, e, a, a, a, a, c,
  c, a, a, a, a, a, a, a
]

```

--- /collapse ---

--- collapse ---
---
title: Drache
---

![Ein Raster mit 8 x 8 Quadraten, die einen Drachen zeigen.](images/dragon.png)

Erstellt vom Team hwplucyr, Vereinigtes Königreich

```python

b = (105, 105, 105) # Mittelgrau
c = (0, 0, 0) # Schwarz
d = (100, 149, 237) # Kornblumenblau
v = (255, 0, 0) # Rot
z = (153, 50, 204) # Dunkle Orchidee

bild = [
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
a = (255, 255, 255) # Weiß
c = (0, 0, 0) # Schwarz
f = (25, 25, 112) # Mitternachtsblau
m = (34, 139, 34) # Waldgrün

bild = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

# Das Bild anzeigen
sense.set_pixels(bild)

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

- Überzeuge dich, dass dein `sense.set_pixels(bild)` nicht eingerückt ist

--- /task ---


--- task ---

**Speichere deinen Fortschritt**

Nachdem du nun ein Bild angezeigt hast, kannst du dein Programm im Mission Starter-Projekt speichern, indem du deinen Teamnamen, die Namen der Teammitglieder und den dir zugewiesenen Klassen-Code eingibst. Du kannst dein Programm auf jedem Gerät mit Internetverbindung neu laden, indem du deinen Teamnamen und deinen Klassen-Code eingibst.

![Mission Zero Speichern-Button](images/savebutton_de.png)

--- /task --- 
