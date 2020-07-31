## Meet de temperatuur

De temperatuursensor op de Astro Pi kan de temperatuur meten van de lucht eromheen, een nuttige eigenschap om je te helpen met het verzamelen van gegevens over de condities in de ruimte.

![Boodschap over de temperatuur](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

Een deel van je missie is het bijdragen tot het dagelijkse leven van de bemanning aan boord het ISS, dus hun laten weten dat de temperatuur aan boord het ruimtestation binnen de normale parameters ligt zal hun geruststellen.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Add this code to take a humidity reading:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- /task \---

\--- task \---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. Je kunt de waarde afronden tot een aantal decimale cijfers. In het voorbeeld hebben wij het cijfer afgerond tot een decimaal, maar voor een ander niveau van nauwkeurigheid, verander het nummer `1` tot het nummer van decimale cijfers die je wenst te zien.

```python
temp = round( sense.temperature, 1 )
```

\--- /task \---

\--- task \---

To display the current humidity as a scrolling message on the display, add this line of code:

```python
sense.show_message( str(temp) )
```

The `str()` part converts the humidity from a number into text so that the Astro Pi can display it.

\--- /task \---

\--- task \---

Het `str()` deel zet de temperatuur om van een nummer naar tekst zodat de Astro Pi het kan laten zien.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

The real Astro Pi will measure the humidity around it, but you can move the humidity slider on the Sense HAT emulator to simulate humidity changes and test your code.

![Humidity slider](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.