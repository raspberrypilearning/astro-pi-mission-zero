## Măsoară temperatura

Senzorul de temperatură din Astro Pi poate măsura temperatura aerului în jurul acestuia, o funcție utilă care te ajută să obții date despre condițiile din spațiu.

![Mesaj despre temperatură](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

O parte din misiunea ta este să contribui la viața de zi cu zi a echipajului de la bordul ISS, informându-i astfel că temperatura la bordul stației spațiale se află într-un interval normal, fapt ce îi va liniști.

[generic-theory-what-is-humidity]

\--- task \---

Add this code to take a humidity reading:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- /task \---

\--- task \---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. Poți rotunji valoarea la orice număr de zecimale. În exemplul dat, am rotunjit la o zecimală, dar pentru un alt nivel de precizie, schimbă numărul `1` la numărul de zecimale pe care dorești să le vezi.

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

Partea `str()` convertește temperatura dintr-un caracter numeric în caracter text astfel încât Astro Pi să o poată afișa.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

The real Astro Pi will measure the humidity around it, but you can move the humidity slider on the Sense HAT emulator to simulate humidity changes and test your code.

![Humidity slider](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.