## Mõõda õhutemperatuur

Astro Pi´l asuv õhutemperatuuri sensor mõõdab ümbritseva õhu temperatuuri, mis on vajalik kosmoses valitsevate tingimuste kohta andmete kogumiseks.

![Sõnum õhutemperatuuri kohta](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

Osa sinu ülesandest on panustada rahvusvahelise kosmosejaama meeskonna igapäeva ellu, seetõttu nende teavitamine sellest, et õhutemperatuur kosmosejaama pardal on normaalses vahemikus annab neile suuremat kindlust.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Add this code to take a humidity reading:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- / ülesanne \---

\--- task \---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. Sina võid väärtuse ümardada mistahes kümnendkohtadega arvuks. Meie ümardasime näite ühe kümnendkohaga arvuks, aga teistsuguse täpsuse saavutamiseks muuda numbrit `1` selliseks kümnendkoha arvuks, mida soovid näha.

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

\--- / ülesanne \---

\--- task \---

See `str()` osa konverteerib õhutemperatuuri numbri tekstiks selle jaoks, et seda saaks kuvada Astro Pi´l.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

\--- /task \---

The real Astro Pi will measure the humidity around it, but you can move the humidity slider on the Sense HAT emulator to simulate humidity changes and test your code.

![Humidity slider](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.