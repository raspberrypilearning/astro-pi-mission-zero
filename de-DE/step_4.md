## Füge etwas Farbe hinzu

Die LEDs des Astro Pi können auch Farben anzeigen. Du kannst eine Farbe bestimmen, indem du eine Variable erstellst und ihr einen RGB-Farbwert zuweist.

Du kannst hier lernen, wie alle Farben mit unterschiedlichen Anteilen von rot, grün und blau erzeugt werden können:

[[[generic-theory-colours]]]

--- task ---

Wähle eine Farbe und ermittle den RGB-Wert dieser Farbe. Du könntest zur Hilfe einen [Farbwähler](https://www.w3schools.com/colors/colors_rgb.asp){:target="_ blank"} verwenden.

--- /task ---

--- task ---

Erstelle eine Variable, um deine gewählte Farbe zu speichern. Wenn du beispielsweise rot gewählt hast, würdest du diese Codezeile schreiben:

```python
rot = (255,0,0)
```

--- /task ---

--- task ---

Du kannst nun deinen Text in der Farbe deiner Wahl anzeigen! Um dem Programm mitzuteilen, dass es die von dir erstellte Farbe verwenden soll, füge einen `text_colour` (Textfarbe) Parameter zum Code, der deinen Text anzeigt, hinzu:

```python
rot = (255,0,0)
sense.show_message ("Astro Pi", text_colour = rot)
```

--- /task ---

![Zeige die Nachricht in Farbe an](images/show-message-color.gif)

--- task ---

Du kannst auch die Hintergrundfarbe des Displays ändern. Wähle eine andere Farbe und erstelle eine weitere Variable, um diese Farbe zu speichern. Um dem Programm zu sagen, dass es die gewählte Hintergrundfarbe verwenden soll, füge den Parameter `back_colour` (Hintergrundfarbe) zu deinem Code hinzu:

```python
rot = (255,0,0)
gruen = (0,255,0)
sense.show_message("Astro Pi", text_colour=rot, back_colour=gruen)
```

--- /task ---

--- task ---

Ändere den Begrüßungstext und die Farbe — welche Nachricht wirst du an die Astronauten an Bord der ISS schicken?

--- /task ---