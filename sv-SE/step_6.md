## Mäta temperaturen

Temperatursensorn i Astro Pi kan mäta den omgivande luftens temperatur, en användbar funktion som hjälper dig att samla data om förhållandena i rymden.

![Meddelande om temperaturen](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

En del av ditt uppdrag är att bidra till det dagliga livet för besättningen ombord på ISS, så att låta dem veta att temperaturen ombord på rymdstationen är inom ett normalt område kommer att lugna dem.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Add this code to take a humidity reading:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- /task \---

\--- task \---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. Du kan avrunda värdet till valfritt antal decimaler. I exemplet har vi avrundat till en decimal, men för en annan precision, ändra siffran ` 1 ` till antalet decimaler du vill se.

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

Delen med `str()` konverterar temperaturen från ett tal till text så att Astro Pi kan visa den.

```python
sense.show_message ("Det är" + str (humid) + "%")
```

\--- /task \---

The real Astro Pi will measure the humidity around it, but you can move the humidity slider on the Sense HAT emulator to simulate humidity changes and test your code.

![Humidity slider](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.