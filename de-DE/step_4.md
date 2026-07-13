## Bestimme eine Farbe

In this step, you will set up the colour and brightness sensor. In diesem Schritt richtest du den Farbsensor ein und verwendest ihn, um die Menge an Rot, Grün und Blau zu erfassen, die den Sensor erreicht. Diese Farbe wird dann verwendet, um dein ausgewähltes Bild einzufärben.

This means that the image can change depending on what the sensor sees. Ein Astronaut, der in einem blauen Hemd auf den Sensor zugeht, würde ein anderes Bild sehen als ein Astronaut in einem roten Hemd.

In the whale image we used in the previous step, the background colour was black. Erstelle eine Variable namens `x`, um deine gewählte Farbe zu speichern.

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0) --- /code ---


--- task ---

Verwende den Farbsensor, um deinen Hintergrund einzufärben.

Underneath the lines where you define the colours, add the following code:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---
# die Hintergrundfarbe des Bildes aktualisieren
rgb = sense.color # Hole die Farbe vom Sensor c = (rgb.red, rgb.green, rgb.blue) # Verwende die ermittelte Farbe

This code replaces the RGB values stored in `c` with the values for the colour detected by the sensor.

Unabhängig davon, welches Bild du wählst, verwendet der Hintergrund die Variable `c`, die auf Schwarz gesetzt ist. This will allow the sensor to change that colour instead.

--- task ---

**Test:** Bewege den Farbregler auf eine Farbe deiner Wahl und **starte** deinen Code. Deine Hintergrundfarbe ändert sich. Wiederhole diesen Test mit einer neuen Farbe.

**Tipp:** Du musst jedes Mal auf 'Ausführen' klicken, wenn du die Farbe änderst.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Now you have displayed an image and sensed a colour and used it in your program, and your code is ready for submission! 

You can save and submit your program using the form at the bottom of the code editor.
  
However, you may wish to add more images to your project, or make it come to life with animation. The next steps show you how to do this.
</p>

## Animate your project (optional)

Das Programm Astro Pi Mission Zero darf bis zu 30 Sekunden laufen. Du wirst diese Zeit nutzen, um den Farbsensor wiederholt abzufragen und das Bild zu aktualisieren.

--- task ---


**Tipp:** Stelle sicher, dass diese Codezeile innerhalb deiner `for`-Schleife eingerückt ist. Give it the variable name `image2` and change a few pixels to make your animation frame look different. Then add a short pause after it.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
---
bild = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

sense.set_pixels(image)

# Extra images / frames go here:

bild = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /code ---

--- /task ---

--- task ---

At the very bottom of your code file, set up your `for` loop to repeat `14` times and alternate between displaying `image` and `image2` pausing for 1 second on each frame.

**Tipp:** Um mehrere Zeilen einzurücken, markiere die Zeilen, die du einrücken möchtest, und drücke dann die Taste <kbd>Tab</kbd> auf deiner Tastatur (normalerweise über der Taste <kbd>Caps Lock</kbd> auf der Tastatur).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7, 8
---
images/fish.png

sense.set_pixels(bild) sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  sense.set_pixels(bild) sleep(1)

--- /task ---

--- task ---

**Test:** Führe deinen Code erneut aus. Wenn dein Projekt fertig ist, wird die LED-Matrix gelöscht, wobei alle Lichter schwarz (aus) sind.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
If you would like to have more than two frames in your animation, you must make sure that the program will run for no more than 30 seconds. For example, if you have 10 images that each display for 1 second, you must change your `for` loop to repeat 3 times (10 * 3 = 30 seconds)
</p>

**Jedes** mal wird es:

Mein Code hat einen Syntaxfehler oder läuft nicht wie erwartet:
- Überprüfe, ob dein Code mit dem Code in den obigen Beispielen übereinstimmt
- Make sure you named your second image matrix `image2` and that it is placed outside and before the loop begins.
- Check that your `sleep` times are set to exactly `1` second to avoid running past the strict 30-second execution cutoff on the ISS.

--- /task ---

--- task ---

**Speichere deinen Fortschritt**

Du kannst dein Programm im Mission Starter-Projekt speichern, indem du deinen Teamnamen, die Namen der Teammitglieder und den dir zugewiesenen Klassen-Code eingibst. Du kannst dein Programm auf jedem Gerät mit Internetverbindung neu laden, indem du deinen Teamnamen und deinen Klassen-Code eingibst.

--- /task ---

--- collapse ---
---
title: Vollständiges Code-Beispiel
---

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
z = (153, 50, 204) # Dunkle Orchidee q = (255, 255, 0) # Gelb d = (51, 153, 255) # Blau c = (0, 0, 0) # Schwarz

# sense.clear()
for i in range(28): rgb = sense.color # Hole die Farbe vom Sensor c = (rgb.red, rgb.green, rgb.blue)

bild = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /collapse ---
---
title: Completed Whale code example (with Animation)
---

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Bibliotheken importieren
from sense_hat import SenseHat from time import sleep

# Füge Code vor der Liste mit deinem Bild hinzu, um die Farbe vom Sensor zu erhalten und ändere deine `c` Hintergrundfarbenvariable, um die Farbe zu verwenden, die der Sense HAT Farbsensor anstelle von Schwarz erfasst.
sense = SenseHat() sense.set_rotation(270)

# for i in range(28): rgb = sense.color # Hole die Farbe vom Sensor c = (rgb.red, rgb.green, rgb.blue)
sense.color.gain = 60 # Empfindlichkeit des Sensors einstellen sense.color.integration_cycles = 64 # Das Intervall, in dem die Messung durchgeführt wird

# Add colour variables and image
z = (153, 50, 204) # Dunkle Orchidee q = (255, 255, 0) # Gelb d = (51, 153, 255) # Blau c = (0, 0, 0) # Schwarz

# die neueste Farbe ermitteln
for i in range(28): rgb = sense.color # Hole die Farbe vom Sensor c = (rgb.red, rgb.green, rgb.blue)

bild = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

sense.set_pixels(bild)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
images/savebutton_de.png

sense.set_pixels(bild) sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  sense.set_pixels(bild) sleep(1)
