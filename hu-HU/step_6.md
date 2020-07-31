## Mérd meg a hőmérsékletet!

The humidity sensor in the Astro Pi can measure the humidity in the air around it, a useful feature to help you gather data about the conditions in space.

![Üzenet a hőmérsékletről](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

A küldetésedhez tartozik a Nemzetközi Űrállomás legénységének napi életéhez való hozzájárulás, úgyhogy, ha tudatod velük, hogy az űrállomáson a hőmérséklet a normális tartományon belül van, azzal megnyugtatod őket.

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

A `str()` rész a hőmérsékletet számból szöveggé alakítja, hogy az Astro Pi meg tudja jeleníteni.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

The real Astro Pi will measure the humidity around it, but you can move the humidity slider on the Sense HAT emulator to simulate humidity changes and test your code.

![Humidity slider](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.