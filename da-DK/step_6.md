## Mål temperaturen

Temperatursensoren i Astro Pi kan måle temperaturen i luften omkring den og er en nyttig funktion, der kan hjælpe dig med at indsamle data om forholdene i rummet.

![Besked om temperaturen](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

En del af din mission går ud på at bidrage til besætningens dagligdag ombord på ISS, så det vil berolige dem at få at vide, at temperaturen ombord på rumstationen ligger inden for normalområdet.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Add this code to take a humidity reading:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- /task \---

\--- task \---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. Du kan afrunde værdien til et vilkårligt antal decimaler. I eksemplet har vi afrundet til én decimal, men for at få en anden grad af præcision skal du ændre tallet `1` til det antal decimaler, du gerne vil se.

```python
temp = round( sense.temperature, 1 )
```

\--- /opgave \---

\--- opgave \---

To display the current humidity as a scrolling message on the display, add this line of code:

```python
sense.show_message( str(temp) )
```

The `str()` part converts the humidity from a number into text so that the Astro Pi can display it.

\--- /task \---

\--- task \---

Delen `str()` konverterer temperaturen fra et tal til tekst, så Astro Pi kan vise den.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /opgave \---

The real Astro Pi will measure the humidity around it, but you can move the humidity slider on the Sense HAT emulator to simulate humidity changes and test your code.

![Humidity slider](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.