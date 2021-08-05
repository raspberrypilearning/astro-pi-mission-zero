## Zeige eine Nachricht und wähle einen Namen für die neuen Astro Pi Computer

--- task ---

Öffne den [Sense HAT Emulator](https://trinket.io/mission-zero){:target="_blank"} für das Mission Zero Projekt.

Du wirst sehen, dass drei Zeilen Code bereits automatisch erscheinen:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![Sense Hat Emulator](images/sense-hat-emulator2.png)

Dieser Code verbindet sich mit dem Astro Pi und sorgt dafür, dass die LED-Anzeige des Astro Pi korrekt angezeigt wird. Lass den Code so dort stehen, weil du ihn noch brauchen wirst.

--- /task ---

--- task ---

Vielleicht könntest du einen schönen Gruß für die Astronauten hinterlassen, die auf der ISS in der Nähe des Astro Pi arbeiten? Wir lassen nun eine Nachricht über den Bildschirm laufen.

Füge diese Zeile unter dem anderen Code hinzu:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Klicke auf **Run** (Ausführen) und schau wie die Nachricht `Astro Pi` über den LED-Bildschirm läuft.

![Nachrichtencode anzeigen, auf Ausführen klicken](images/show-message-code-annotated.PNG)

--- /task ---

![Lauftext](images/scroll-message.gif)

Um eine andere Nachricht anzuzeigen, kannst du etwas Beliebiges zwischen die Anführungszeichen schreiben (`""`).

--- collapse ---

---
title: Welche Zeichen können verwendet werden?
---

Der Sense HAT kann nur den Zeichensatz Latin 1 anzeigen, sodass nur die folgenden Zeichen verfügbar sind. Andere Zeichen werden als `?` angezeigt.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

Du kannst auch die Geschwindigkeit der Nachricht ändern, mit der sie über den Bildschirm läuft. Füge `scroll_speed` (Laufgeschwindigkeit) zu der Codezeile, die du schon hast, folgendermaßen hinzu:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Die Standardgeschwindigkeit der Nachricht ist `0.1`. Wenn du die Zahl verkleinerst, läuft die Nachricht schneller ab, und wenn du sie vergrößerst, läuft die Nachricht langsamer ab.

--- /task ---

### Wähle einen Namen für die neuen Astro Pi-Computer

--- task --- We will name the Astro Pi computers after two inspirational European scientists. There are hundreds of men and women that have contributed to science and technology, and participants can suggest their own names, or pick from our list of suggestions:


[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"}: [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) [Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel) [Edsgar Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra) [Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr) [Hypatia](https://en.wikipedia.org/wiki/Hypatia) [John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone) [Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie) [Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla) [Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe)

To vote, start your message with the words "My name should be". For example, you want to vote for Ada Lovelace, your code would look like this:

```python
sense.show_message("Mein Name sollte sein Ada Lovelace")
```
--- /task ---



