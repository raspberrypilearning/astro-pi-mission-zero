## Miss die Luftfeuchtigkeit

Der Feuchtichkeitssensor im Astro Pi misst die Luftfeuchtigkeit in seiner Umgebung. Das ist nützlich, um Daten über die Bedingungen im All zu sammeln.

![Der Trinket Sense HAT-Emulator, der ein Beispielprogramm ausführt, das den Wert der Luftfeuchtigkeit in weißen Buchstaben über die LED-Matrix laufen lässt](images/M0_3.gif)

Der Astro Pi misst die Luftfeuchtigkeit in der ISS in Prozent der maximal möglichen Wasserkonzentration in der Luft.

Teil deiner Mission ist es, einen Beitrag zum täglichen Leben der Crew an Bord der ISS zu leisten, und wenn du die Astronauten wissen lässt, dass die Luftfeuchtigkeit an Bord der Raumstation in einem normalen Bereich liegt, wird sie das sehr beruhigen.

[[[generic-theory-what-is-humidity]]]

--- task ---

Füge diesen Code hinzu, um eine Feuchtigkeitsmessung durchzuführen:

```python
humid = sense.get_humidity()
```

Diese Zeile misst die aktuelle Luftfeuchtigkeit und speichert den gemessenen Wert in der Variablen `humid`.

--- /task ---

--- task ---

Die Luftfeuchtigkeit wird sehr genau erfasst, d.h. der gespeicherte Wert hat eine große Anzahl von Dezimalstellen. Du kannst den Wert auf eine beliebige Anzahl von Dezimalstellen runden. Im Beispiel haben wir auf eine Dezimalstelle gerundet, aber für eine andere Genauigkeitsstufe kannst du die Zahl `1` zu der Anzahl der Dezimalstellen ändern, die du sehen möchtest.

```python
humid = round(sense.get_humidity(), 1)
```

--- /task ---

--- task ---

Um die aktuelle Luftfeuchtigkeit als Laufschrift auf dem Bildschirm anzuzeigen, füge diese Codezeile hinzu:

```python
sense.show_message(str(humid))
```

Der Befehl `str()` wandelt die Luftfeuchtigkeit von einer Zahl in Text um, so dass der Astro Pi sie anzeigen kann.

--- /task ---

--- task ---

Du kannst die Luftfeuchtigkeit auch als Teil einer anderen Nachricht anzeigen, indem du die Teile deiner Nachricht mit einem `+` verbindest.

```python
sense.show_message( "Feuchte= " + str(humid) + " %" )
```

--- /task ---

Der echte Astro Pi misst die Luftfeuchtigkeit in seiner Umgebung, aber du kannst den Schieberegler für Luftfeuchtigkeit auf dem Sense HAT Emulator bewegen, um Änderungen der Luftfeuchtigkeit zu simulieren und deinen Code zu testen.

![Ein beschrifteter Screenshot des Sense HAT-Emulators mit dem Codefenster links und dem Emulator rechts. Der Schieberegler zum Einstellen der Luftfeuchtigkeit ist in der oberen rechten Ecke eingekreist](images/humidity-slider.png)

**Hinweis:** Du wirst dich vielleicht wundern, warum der Luftfeuchtigkeitsregler die Luftfeuchtigkeit als ganze Zahl anzeigt, aber der Messwert, den du erhältst, eine Dezimalzahl ist. Der Emulator simuliert die geringfügige Ungenauigkeit des realen Sensors. Deshalb kann der Wert, den du siehst, etwas kleiner oder größer sein, als der Wert, den du mit dem Regler eingestellt hast.
