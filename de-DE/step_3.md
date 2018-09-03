## Anzeigen einer Nachricht

\--- task \---

Öffne den [ Sense HAT Emulator](https://trinket.io/mission-zero){:target="_ blank"} für das Mission Zero Projekt.

Du wirst sehen, dass drei Zeilen Code bereits automatisch erscheinen:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![Sense Hat Emulator](images/sense-hat-emulator2.png)

Dieser Code verbindet sich mit dem Astro Pi und sorgt dafür, dass die LED-Anzeige des Astro Pi korrekt angezeigt wird. Lass den Code so dort stehen, weil du ihn noch brauchen wirst.

\--- /task \---

\--- task \---

Vielleicht könntest du einen schönen Gruß für die Astronauten hinterlassen, die auf der ISS in der Nähe des Astro Pi arbeiten? Wir lassen nun eine Nachricht über den Bildschirm laufen.

Füge diese Zeile unter dem anderen Code hinzu:

```python
sense.show_message("Astro Pi")
```

\--- /task \---

\--- task \---

Klicke auf **Run** (Ausführen) und schau wie die Nachricht `Astro Pi` über den LED-Bildschirm läuft.

![Nachrichtencode anzeigen, Auf Ausführen klicken](images/show-message-code-annotated.PNG)

\--- /task \---

![Lauftext](images/scroll-message.gif)

Um eine andere Nachricht anzuzeigen, kannst du beliebig zwischen den Anführungszeichen schreiben (`""`).

\--- collapse \---

* * *

## title: Welche Zeichen können verwendet werden?

Der Sense HAT kann nur den Zeichensatz Latin 1 anzeigen, sodass nur die folgenden Zeichen verfügbar sind. Andere Zeichen werden als `?` angezeigt.

    +-*/!"#$><0123456789.=)(
    
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    abcdefghijklmnopqrstuvwxyz
    
    ?,;:|@%[&_']\~
    

\--- /collapse \---

\--- task \---

Du kannst auch die Geschwindigkeit der Nachricht ändern, die über den Bildschirm läuft. Füge `scroll_speed` (Laufgeschwindigkeit) zu der Codezeile, die du schon hast, folgendermaßen hinzu:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Die Standardgeschwindigkeit der Nachricht ist `0.1`. Wenn du die Zahl verkleinerst, läuft die Nachricht schneller ab, und wenn du sie vergrößerst, läuft die Nachricht langsamer ab.

\--- /task \---