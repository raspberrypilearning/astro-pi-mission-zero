## Miss die Luftfeuchtigkeit

Der Feuchtichkeitssensor im Astro Pi misst die Luftfeuchtigkeit in seiner Umgebung. Das ist nützlich, um Daten über die Bedingungen im All zu sammeln.

![Nachricht über die Luftfeuchtigkeit](images/degrees-message.gif)

Der Astro Pi misst die Luftfeuchtigkeit in der ISS in Prozent der maximal möglichen Wasserkonzentration in der Luft.

Teil deiner Mission ist es, einen Beitrag zum täglichen Leben der Crew an Bord der ISS zu leisten, und wenn du die Astronauten wissen lässt, dass die Luftfeuchtigkeit an Bord der Raumstation in einem normalen Bereich liegt, wird sie das sehr beruhigen.

[[[generic-theory-what-is-humidity]]]

--- task ---

Füge diesen Code hinzu, um eine Feuchtemessung durchzuführen:

```python
humid = sense.humidity
```

Diese Zeile misst die aktuelle Luftfeuchtigkeit und speichert den gemessenen Wert in der Variablen `humid`.

--- /task ---

--- task ---

Die Luftfeuchtigkeit wird sehr genau erfasst, d.h. der gespeicherte Wert hat eine große Anzahl von Dezimalstellen. Du kannst den Wert auf eine beliebige Anzahl von Dezimalstellen runden. Im Beispiel haben wir auf eine Dezimalstelle gerundet, aber für eine andere Genauigkeitsstufe kannst du die Zahl `1` zu der Anzahl der Dezimalstellen ändern, die du sehen möchtest.

```python
humid = round( sense.humidity, 1 )
```

--- /task ---

--- task ---

Um die aktuelle Luftfeuchtigkeit als Laufschrift auf dem Bildschirm anzuzeigen, füge diese Codezeile hinzu:

```python
sense.show_message( str(humid) )
```

Der Befehl `str()` wandelt die Luftfeuchtigkeit von einer Zahl in Text um, so dass der Astro Pi sie anzeigen kann.

--- /task ---

--- task ---

Du kannst die Luftfeuchtigkeit auch als Teil einer anderen Nachricht anzeigen, indem du die Teile deiner Nachricht mit einem `+` verbindest.

```python
sense.show_message( "Es hat " + str(humid) + " %" )
```

--- /task ---

Der echte Astro Pi misst die Luftfeuchtigkeit in seiner Umgebung, aber du kannst den Luftfeuchtigkeitsschieberegler auf dem Sense HAT Emulator bewegen, um Luftfeuchtigkeitsänderungen zu simulieren und deinen Code zu testen.

![Feuchtigkeitsregler](images/humidity-slider.png)

**Hinweis:** Du wirst dich vielleicht wundern, warum der Luftfeuchtigkeitsregler die Luftfeuchtigkeit als ganze Zahl anzeigt, aber der Messwert, den du erhältst, eine Dezimalzahl ist. Der Emulator simuliert die geringfügige Ungenauigkeit des realen Sensors. Deshalb kann der Wert, den du siehst, etwas kleiner oder größer sein, als der Wert, den du mit dem Regler eingestellt hast.
