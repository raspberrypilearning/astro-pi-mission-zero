## Mittaa lämpötila

The humidity sensor in the Astro Pi can measure the humidity in the air around it, a useful feature to help you gather data about the conditions in space.

![Viesti lämpötilasta](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

Osa tehtäväänne on edistää ISS:n miehistön jokapäiväistä elämää, joten antamalla heidän tietää, että avaruusaseman lämpötila on tavanomaisella alueella, rauhoittaa heitä.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Add this code to take a humidity reading:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- /task \---

\--- task \---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. Voit pyöristää arvon mihin tahansa desimaaliin. Esimerkissä olemme pyöristäneet yhden desimaalin tarkkuuteen, mutta eri tarkkuustasoa varten muuta numero `1` haluamasi desimaalilukumäärän mukaiseksi.

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

`str()`-osa muuntaa lämpötilan numerosta tekstiksi, jotta Astro Pi voi näyttää sen.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

\--- /task \---

The real Astro Pi will measure the humidity around it, but you can move the humidity slider on the Sense HAT emulator to simulate humidity changes and test your code.

![Humidity slider](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.