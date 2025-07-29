## Bestimme eine Farbe

In diesem Schritt richtest du den Farbsensor ein und verwendest ihn, um die Menge an Rot, Grün und Blau zu erfassen, die den Sensor erreicht. Diese Farbe wird dann verwendet, um dein ausgewähltes Bild einzufärben. Ein Astronaut, der in einem blauen Hemd auf den Sensor zugeht, würde ein anderes Bild sehen als ein Astronaut in einem roten Hemd.

![Bild, das mit einem rosa Hintergrund auf der LED-Matrix angezeigt wird](images/colour_background.png)

Unabhängig davon, welches Bild du wählst, verwendet der Hintergrund die Variable `c`, die auf Schwarz gesetzt ist.

--- task ---

Verwende den Farbsensor, um deinen Hintergrund einzufärben.

Füge Code vor der Liste mit deinem Bild hinzu, um die Farbe vom Sensor zu erhalten und ändere deine `c` Hintergrundfarbenvariable, um die Farbe zu verwenden, die der Sense HAT Farbsensor anstelle von Schwarz erfasst.

**Tipp:** Du musst keine Kommentare eingeben, die mit '#' beginnen (sie sind da, um den Code zu erklären).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9, 10
---

# Add colour variables and image

z = (153, 50, 204) # DarkOrchid q = (255, 255, 0) # Yellow d = (51, 153, 255) # blue c = (0, 0, 0) # Black

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


--- /code ---

--- /task ---

--- task ---

**Test:** Bewege den Farbregler auf eine Farbe deiner Wahl und **starte** deinen Code. Deine Hintergrundfarbe ändert sich. Wiederhole diesen Test mit einer neuen Farbe.

**Tipp:** Du musst jedes Mal auf 'Ausführen' klicken, wenn du die Farbe änderst.

--- /task ---

## Mache eine Programmschleife

Das Programm Astro Pi Mission Zero darf bis zu 30 Sekunden laufen. Du wirst diese Zeit nutzen, um den Farbsensor wiederholt abzufragen und das Bild zu aktualisieren.

Ihr Code verwendet eine `for`-Schleife, um 28 Mal ausgeführt zu werden. **Jedes** mal wird es:
+ die neueste Farbe ermitteln
+ die Hintergrundfarbe des Bildes aktualisieren
+ eine Sekunde pausieren

--- task ---

**Finde** deine `rgb = sense.color` Codezeile.

Code darüber **hinzufügen** um deine `for`-Schleife für `28` Wiederholungen einzurichten.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


--- /code ---

--- /task ---

--- task ---

Du musst jetzt deinen gesamten Code unter der `for`-Schleife einrücken, sodass er **innerhalb** der `for`-Schleife sitzt.

**Tipp:** Um mehrere Zeilen einzurücken, markiere die Zeilen, die du einrücken möchtest, und drücke dann die Taste <kbd>Tab</kbd> auf deiner Tastatur (normalerweise über der Taste <kbd>Caps Lock</kbd> auf der Tastatur).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


  # Display the image

  sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Füge am Ende deines Codes einen `Sleep` Befehl mit einer Sekunde innerhalb deiner Schleife hinzu:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 5
---

  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Tipp:** Stelle sicher, dass diese Codezeile innerhalb deiner `for`-Schleife eingerückt ist.

--- /task ---

--- task ---

**Test:** Führe deinen Code aus und ändere die Farbauswahl mehrmals während dein Projekt läuft. Überprüfe, ob dein Bild aktualisiert wird, und die erfasste Farbe beim nächsten Durchlauf verwendet.

Das Bild wird nicht mehr aktualisiert, wenn die Schleife beendet ist, so dass das Programm nicht länger als 30 Sekunden läuft.

--- /task ---

--- task ---

**Fehlersuche**

Mein Code hat einen Syntaxfehler oder läuft nicht wie erwartet:

- Überprüfe, ob dein Code mit dem Code in den obigen Beispielen übereinstimmt
- Überprüfe, ob du den Code in der `for`-Schleife richtig eingerückt hast
- Überprüfe, ob deine Liste von `[` und `]`umgeben ist
- Überprüfe, ob die Farbvariablen in der Liste durch Kommas getrennt sind

Mein Code läuft länger als 30 Sekunden:

- Verringere die Anzahl der Durchläufe deiner for-Schleife von 28 auf 25 oder sogar 20.
- Verringern Sie die Schlafdauer von 1 Sekunde auf 0,5 Sekunden.

--- /task ---

--- task ---

Füge `sense.clear()` am Ende deines Codes hinzu, um das Bild am Ende deiner Schleife zu löschen. Damit siehst du, wenn deine Animation beendet ist.

**Tipp:** Stelle sicher, dass du die Codezeile **sense.clear()** `nicht` einrückst, da diese nur einmal am Ende deiner Animation ausgeführt werden soll.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7
---

  # Display the image

  sense.set_pixels(image) sleep(1)

sense.clear()

--- /code ---

--- /task ---

--- task ---

**Test:** Führe deinen Code erneut aus. Wenn dein Projekt fertig ist, wird die LED-Matrix gelöscht, wobei alle Lichter schwarz (aus) sind.

--- /task ---

--- task ---

**Fehlersuche**

Die LED-Matrix wird jede Sekunde schwarz:

- Stelle sicher, dass du den Code `sense.clear()` in deiner `for`-Schleife nicht eingerückt hast

--- /task ---

--- task ---

Füge Code hinzu, um die LED-Matrix auf eine Farbe deiner Wahl zu löschen. Erstelle eine Variable namens `x`, um deine gewählte Farbe zu speichern.

Du kannst deine eigene Farbe mischen oder die Werte aus der Farbliste verwenden, um deine neue `x`-Farbe zu erstellen.

\[[[generic-theory-simple-colours]]\] \[[[ambient-colours\]]]

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7, 8
---

  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /task ---

--- task ---

**Test:** Führe deinen Code erneut aus. Wenn dein Projekt fertig ist, leuchtet die LED-Matrix in der von dir gewählten Farbe. Du kannst die Farbe beliebig oft ändern und dann testen.

--- /task ---


--- task ---

**Speichere deinen Fortschritt**

Du kannst dein Programm im Mission Starter-Projekt speichern, indem du deinen Teamnamen, die Namen der Teammitglieder und den dir zugewiesenen Klassen-Code eingibst. Du kannst dein Programm auf jedem Gerät mit Internetverbindung neu laden, indem du deinen Teamnamen und deinen Klassen-Code eingibst.

![Screenshot der Schaltfläche „Speichern“ von Mission Zero](images/mz_savebutton_v2.png)

--- /task ---


--- task ---

--- collapse ---

---
title: Vollständiges Code-Beispiel
---

![A grid with 8 x 8 squares showing a fish.](images/fish.png)

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

z = (153, 50, 204) # DarkOrchid q = (255, 255, 0) # Yellow d = (51, 153, 255) # blue c = (0, 0, 0) # Black

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 and 255 sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
