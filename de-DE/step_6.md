## Messen der Temperatur

Der echte Astro Pi misst die Umgebungstemperatur, aber du kannst den Temperaturschieberegler auf dem Sense HAT Emulator bewegen, um Temperaturänderungen zu simulieren und deinen Code zu testen.

![Nachricht über die Temperatur](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

Teil deiner Mission ist es, einen Beitrag zum täglichen Leben der Crew an Bord der ISS zu leisten, und wenn du die Astronauten wissen lässt, dass die Temperatur an Bord der Raumstation in einem normalen Bereich liegt, wird sie das sehr beruhigen.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Füge diesen Code hinzu, um eine Temperaturmessung durchzuführen:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- /task \---

\--- task \---

Die Temperatur wird sehr genau erfasst, d.h. der gespeicherte Wert hat eine große Anzahl von Dezimalstellen. Du kannst den Wert auf eine beliebige Anzahl von Dezimalstellen runden. Im Beispiel haben wir auf eine Dezimalstelle gerundet, aber für eine andere Genauigkeitsstufe kannst du die Zahl `1` zu der Anzahl der Dezimalstellen ändern, die du sehen möchtest.

```python
temp = round( sense.temperature, 1 )
```

\--- /task \---

\--- task \---

Um die aktuelle Temperatur als Laufschrift auf dem Bildschirm anzuzeigen, füge diese Codezeile hinzu:

```python
sense.show_message( str(temp) )
```

The `str()` part converts the humidity from a number into text so that the Astro Pi can display it.

\--- /task \---

\--- task \---

Der Code `str()` wandelt die Temperatur von einer Zahl in Text um, so dass der Astro Pi sie anzeigen kann.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

\--- /task \---

The real Astro Pi will measure the humidity around it, but you can move the humidity slider on the Sense HAT emulator to simulate humidity changes and test your code.

![Humidity slider](images/humidity-slider.png)

**Hinweis:** Du wirst dich vielleicht wundern, warum der Temperaturregler die Temperatur als ganze Zahl anzeigt, aber der Messwert, den du erhältst, eine Dezimalzahl ist. Der Emulator simuliert die geringfügige Ungenauigkeit des realen Sensors.