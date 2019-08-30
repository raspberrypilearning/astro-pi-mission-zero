## Messen der Temperatur

Der Temperatursensor im Astro Pi kann die Temperatur der umgebenden Luft messen. Dies ist eine nützliche Funktion, um Daten über die Bedingungen im Weltraum zu sammeln.

![Nachricht über die Temperatur](images/degrees-message.gif)

Der Astro Pi misst die Temperatur auf der Internationalen Raumstation in Grad Celsius (&deg;C). Da die Temperaturen im Weltraum viel stärker variieren als auf der Erde, kann der Astro Pi Temperaturen von -40 °C bis +120° C messen.

Teil deiner Mission ist es, einen Beitrag zum täglichen Leben der Crew an Bord der ISS zu leisten, und wenn du die Astronauten wissen lässt, dass die Temperatur an Bord der Raumstation in einem normalen Bereich liegt, wird sie das sehr beruhigen.

--- collapse ---
---
title: Was ist Temperatur?
---

Die Temperatur ist das Maß dafür, wie heiß etwas ist. Bei einem Arztbesuch wurde bei dir bestimmt schon einmal mit einem Thermometer die Temperatur gemessen.

![Thermometer](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} via Wikimedia Commons*

Um genauer zu sein, ist die Temperatur ein Maß für die Menge an Wärmeenergie einer Substanz. Du weißt, dass ein Eiswürfel fest ist, aber wenn er sich aufwärmt, d.h. Wärmeenergie aus seiner Umgebung aufnimmt, schmilzt er und wird flüssig. Das liegt daran, dass sich bei der Aufnahme oder beim Verlust von genug Wärmeenergie der Zustand einer Substanz verändert, z.B. ein Festkörper wird zu einer Flüssigkeit.

--- /collapse ---

--- task ---

Füge diesen Code hinzu, um eine Temperaturmessung durchzuführen:

```python
temp = sense.temperature
```

Diese Zeile misst die aktuelle Temperatur und speichert den gemessenen Wert in der Variablen `temp`.

--- /task ---

--- task ---

Die Temperatur wird sehr genau erfasst, d.h. der gespeicherte Wert hat eine große Anzahl von Dezimalstellen. Du kannst den Wert auf eine beliebige Anzahl von Dezimalstellen runden. Im Beispiel haben wir auf eine Dezimalstelle gerundet, aber für eine andere Genauigkeitsstufe kannst du die Zahl `1` zu der Anzahl der Dezimalstellen ändern, die du sehen möchtest.

```python
temp = round( sense.temperature, 1 )
```

--- /task ---

--- task ---

Um die aktuelle Temperatur als Laufschrift auf dem Bildschirm anzuzeigen, füge diese Codezeile hinzu:

```python
sense.show_message( str(temp) )
```

Der Code `str()` wandelt die Temperatur von einer Zahl in Text um, so dass der Astro Pi sie anzeigen kann.

--- /task ---

--- task ---

Du kannst die Temperatur auch als Teil einer anderen Nachricht anzeigen, indem du die Teile deiner Nachricht mit einem `+` verbindest.

```python
sense.show_message( "Es hat " + str(temp) + " Grad" )
```

--- /task ---

Der echte Astro Pi misst die Umgebungstemperatur, aber du kannst den Temperaturschieberegler auf dem Sense HAT Emulator bewegen, um Temperaturänderungen zu simulieren und deinen Code zu testen.

![Temperaturschieberegler](images/temperature-slider.png)

**Hinweis:** Du wirst dich vielleicht wundern, warum der Temperaturregler die Temperatur als ganze Zahl anzeigt, aber der Messwert, den du erhältst, eine Dezimalzahl ist. Der Emulator simuliert die geringfügige Ungenauigkeit des realen Sensors. Daher kann die Temperaturmessung, die du siehst, sehr geringfügig größer oder kleiner sein als der Wert, den du mit dem Schieberegler eingestellt hast.