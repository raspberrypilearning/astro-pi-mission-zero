## Farbe ermitteln

In diesem Schritt richtest du den Farbsensor ein und verwendest ihn, um die Menge an Rot, Grün und Blau zu erfassen, die den Sensor erreicht. Diese Farbe wird dann verwendet, um dein ausgewähltes Bild einzufärben. Ein Astronaut, der in einem blauen Hemd auf den Sensor zugeht, würde ein anderes Bild sehen als ein Astronaut in einem roten Hemd.

![image displayed with a pink background on the LED matrix](images/colour_background.png)

Unabhängig davon, welches Bild du wählst, verwendet der Hintergrund die Variable `c`, die auf Schwarz gesetzt ist.

--- task ---

Verwende den Farbsensor, um deinen Hintergrund einzufärben.

Füge Code vor der Liste mit deinem Bild hinzu, um die Farbe vom Sensor zu erhalten und ändere deine `c` Hintergrundfarbenvariable, um die Farbe zu verwenden, die der Sense HAT Farbsensor anstelle von Schwarz erfasst.

**Tipp:** Du musst keine Kommentare eingeben, die mit '#' beginnen (sie sind da, um den Code zu erklären).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9-10
---
# Farbvariablen und Bild hinzufügen

c = (0, 0, 0) # Schwarz m = (34, 139, 34) # Waldgrün q = (255, 255, 0) # Gelb t = (255, 140, 0) # Dunkelorange y = (255, 20, 147) # Dunkelrosa

rgb = sense.color # erhalte die Farbe vom Sensor c = (rgb.red, rgb.green, rgb.blue) # verwende die Farbe

bild = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

**Test:** Bewege den Farbregler auf eine Farbe deiner Wahl und **starte** deinen Code. Deine Hintergrundfarbe ändert sich. Wiederhole diesen Test mit einer neuen Farbe.

**Tipp:** Du musst jedes Mal auf 'Ausführen' klicken, wenn du die Farbe änderst.

--- /task ---

## Mache eine Programmschleife

Das Programm Astro Pi Mission Zero darf bis zu 30 Sekunden laufen. Du wirst diese Zeit nutzen, um den Farbsensor wiederholt abzufragen und das Bild zu aktualisieren.

Ihr Code verwendet eine `-for-` -Schleife, um 28 Mal ausgeführt zu werden. **Jedes** mal wird es:
+ die neueste Farbe ermitteln
+ die Hintergrundfarbe des Bildes aktualisieren
+ eine Sekunde pausieren

--- task ---

**Finde** deine `rgb = sense.color` Codezeile.

Code darüber **hinzufügen** um deine `for` -Schleife für `28` Wiederholungen einzurichten.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 1
---
for i in range(28): rgb = sense.color # holt die Farbe vom Sensor c = (rgb.red, rgb.green, rgb.blue)

bild = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

Du musst jetzt deinen gesamten Code unter der `for` -Schleife einrücken, sodass er **innerhalb** der `for` -Schleife sitzt.

**Tipp:** Um mehrere Zeilen einzurücken, markiere die Zeilen, die du einrücken möchtest, und drücke dann die Taste <kbd>Tab</kbd> auf deiner Tastatur (normalerweise über der Taste <kbd>Caps Lock</kbd> auf der Tastatur).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2 - 17
---
for i in range(28): rgb = sense.color # holt die Farbe vom Sensor c = (rgb.red, rgb.green, rgb.blue)

  bild = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

  # Das Bild anzeigen

  sense.set_pixels(bild)

--- /code ---

--- /task ---

--- task ---

Füge am Ende deines Codes einen `Sleep`Befehl mit einer Sekunde innerhalb deiner Schleife hinzu:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 4
---
  # Das Bild anzeigen

  sense.set_pixels(bild) sleep(1)

--- /code ---

**Tipp:** Stelle sicher, dass diese Codezeile innerhalb deiner `for` Schleife eingerückt ist.

--- /task ---

--- task ---

**Test:** Führe deinen Code aus und ändere die Farbauswahl mehrmals während dein Projekt läuft. Überprüfe, ob dein Bild aktualisiert wird, und die erfasste Farbe beim nächsten Durchlauf verwendet.

Das Bild wird nicht mehr aktualisiert, wenn die Schleife beendet ist, so dass das Programm nicht länger als 30 Sekunden läuft.

--- /task ---

--- task ---

**Fehlersuche**

Mein Code hat einen Syntaxfehler oder läuft nicht wie erwartet:

- Überprüfe, ob dein Code mit dem Code in den obigen Beispielen übereinstimmt
- Überprüfe, ob du den Code in der `for`Schleife richtig eingerückt hast
- Überprüfe, ob deine Liste von `[` und `]`umgeben ist
- Überprüfe, ob die Farbvariablen in der Liste durch Kommas getrennt sind

Mein Code läuft länger als 30 Sekunden:

- Verringere die Anzahl der Durchläufe deiner for-Schleife von 28 auf 25 oder sogar 20.
- Verringern Sie die Schlafdauer von 1 Sekunde auf 0,5 Sekunden.

--- /task ---

--- task ---

Füge `sense.clear()` am Ende deines Codes hinzu, um das Bild am Ende deiner Schleife zu löschen. This will help you see when your animation has finished running.

**Tip:** Make sure you **do not** indent the `sense.clear()` line of code as you want this to only run once at the end of your animation.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 6
---
  # Display the image

  sense.set_pixels(image) sleep(1)

sense.clear()

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code again. When your project has finished running the LED matrix will clear, turning all the lights black (off).

--- /task ---

--- task ---

**Debug**

The LED matrix turns black every second:

- Check that you have not indented the `sense.clear()` code within your `for` loop

--- /task ---

--- task ---

Add code to clear the LED matrix to a colour of your choice. Erstelle eine Variable, um deine gewählte Farbe zu speichern.

You can mix your own colour or use the values from the list of colours to create your new `x`colour.

[[[generic-theory-colours]]]

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 6-7
---
  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code again. When your project has finished running the LED matrix will clear to your chosen colour. You can change then test the colour as many times as you want.

--- /task ---

--- task ---

--- collapse ---

---
title: Completed code example
---

![A grid with 8 x 8 squares showing a pink flower on a green stem.](images/flower.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Import the libraries
from sense_hat import SenseHat from time import sleep

# Set up the Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image

c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange y = (255, 20, 147) # DeepPink

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
