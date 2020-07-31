## Måle temperaturen

Temperaturføleren i Astro Pi kan måle temperaturen på luften rundt den, en nyttig funksjon som hjelper deg med å samle data om forholdene i rommet.

![Melding om temperaturen](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

En del av oppdraget deres er å bidra til dagliglivet til mannskapet ombord på ISS, så når de får vite at temperaturen om bord på romstasjonen ligger innenfor et normalt område, vil de bli beroliget.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Add this code to take a humidity reading:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- /task \---

\--- task \---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. You can round the value to any number of decimal places. In the example we have rounded to one decimal place, but for a different level of precision, change the number `1` to the number of decimal places you would like to see.

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

`str()`-delen omdanner temperaturen fra tall til tekst slik at Astro Pi kan vise den.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

The real Astro Pi will measure the humidity around it, but you can move the humidity slider on the Sense HAT emulator to simulate humidity changes and test your code.

![Humidity slider](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.