## Bestimme eine Farbe

In diesem Schritt wird der Farb- und Helligkeitssensor eingestellt. Du wirst diesen Sensor verwenden, um die Menge an rotem, grünem und blauem Licht zu messen, die den Sensor erreicht. Diese Werte werden dann verwendet, um eine der Farben in deinem ausgewählten Bild zu ändern.

Das bedeutet, dass sich das Bild je nachdem, was der Sensor sieht, verändern kann. Ein Astronaut, der beispielsweise ein blaues Hemd trägt, würde eine andere Version des Bildes sehen als ein Astronaut, der ein rotes Hemd trägt.

Bei dem Walbild, das wir im vorherigen Schritt verwendet haben, war die Hintergrundfarbe schwarz. Wir haben die Variable `c` verwendet, um seinen RGB-Farbcode zu speichern:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Verwende den Farbsensor, um eine deiner Farben zu ändern.

Füge unterhalb der Zeilen, in denen du die Farben definierst, den folgenden Code ein:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

--- /code ---

--- /task ---

Dieser Code ersetzt die in `c` gespeicherten RGB-Werte durch die vom Sensor erfassten Werte für die Farbe.

Tipp: Falls du die Variable `c` in deinem Bild nicht verwendet hast, ersetze `c` durch die Farbvariable, die du verwendest hast. Dadurch kann der Sensor diese Farbe ändern.

--- task ---

**Test:** Bewege den Farbregler auf eine Farbe deiner Wahl und **starte** deinen Code. Deine Hintergrundfarbe ändert sich. Wiederhole diesen Test mit einer neuen Farbe.

**Tipp:** Du musst jedes Mal auf 'Ausführen' klicken, wenn du die Farbe änderst.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Du hast nun ein Bild angezeigt, eine Farbe erkannt und diese in deinem Programm verwendet – dein Code ist bereit zur Abgabe! 

Du kannst dein Programm mithilfe des Formulars am unteren Rand des Code-Editors speichern und absenden.
  
Vielleicht möchtest du deinem Projekt aber auch weitere Bilder hinzufügen oder es mit Animationen zum Leben erwecken. Die nächsten Schritte zeigen dir, wie das geht.
</p>

## Animiere dein Projekt (optional)

Dein Mission Zero Programm kann bis zu 30 Sekunden auf der Internationalen Raumstation (ISS) laufen. Mit dieser Laufzeit kannst du eine Animation auf der LED-Matrix anzeigen, indem du zwischen zwei oder mehr verschiedenen Bildern wechselst.

--- task ---


**Füge** ein zweites Bild direkt unterhalb deiner `sense.set_pixels(image)` Codezeile hinzu. Gib der Variable den Namen `bild2` und ändere ein paar Pixel, damit dein Animationsbild anders aussieht. Füge anschließend eine kurze Pause ein.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# Extra images / frames go here:

image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

Richte ganz unten in deiner Codedatei deine `for` Schleife so ein, dass sie `14` Mal wiederholt wird und abwechselnd `bild` und `bild2` angezeigt wird, wobei sie jeweils 1 Sekunde pausieren.

**Tipp:** Stelle sicher, dass die Codezeilen unterhalb von `for i in range(14):` mit einem Leerzeichen eingerückt sind, sodass sie sich **innerhalb** des Schleifenblocks befinden.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1)

--- /code ---

--- /task ---

--- task ---

**Test:** Führe deinen Code erneut aus. Dein Programm zeigt die erfasste Farbe sofort an und läuft dann in einer Schleife um eine Animation zu zeigen.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Wenn deine Animation mehr als zwei Einzelbilder enthalten soll, musst du sicherstellen, dass das Programm nicht länger als 30 Sekunden läuft. Wenn du beispielsweise 10 Bilder hast, die jeweils 1 Sekunde lang angezeigt werden, musst du deine `for`-Schleife so ändern, dass sie 3 Mal wiederholt wird (10 * 3 = 30 Sekunden)
</p>

--- task ---

**Auf Fehler prüfen**

Mein Code enthält einen Syntaxfehler oder ändert die Frames nicht:
- Prüfe, ob dein `for` Schleifencode der Einrückung im Beispiel entspricht.
- Stelle sicher, dass deine zweite Bildmatrix `bild2` genannt hast und dass sie außerhalb und vor Beginn der Schleife platziert wird.
- Überprüfe, ob deine `Schlafzeiten` genau auf`1` Sekunde eingestellt sind, um ein Überschreiten des strikten 30-Sekunden-Ausführungslimits auf der ISS zu vermeiden.

--- /task ---

--- task ---

**Speichere deinen Fortschritt**

Du kannst dein Programm im Mission Starter-Projekt speichern, indem du deinen Teamnamen, die Namen der Teammitglieder und den dir zugewiesenen Klassen-Code eingibst. Du kannst dein Programm auf jedem Gerät mit Internetverbindung neu laden, indem du deinen Teamnamen und deinen Klassen-Code eingibst.

--- /task ---

--- task ---

--- collapse ---
---
title: Vollständiges Wal-Code-Beispiel
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
a = (255, 255, 255) # White c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Vollständiges Wal-Code-Beispiel (mit Animation)
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
a = (255, 255, 255) # White c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1)

--- /code ---

--- /collapse ---

--- /task ---
