## Mittaa ilmankosteus

Astro Pi: n kosteusanturi voi mitata ympäröivän ilman kosteutta, mikä on hyödyllinen ominaisuus, jonka avulla voit kerätä tietoja avaruusolosuhteista.

![Viesti kosteudesta](images/degrees-message.gif)

Astro Pi mittaa ISS:n kosteuden prosentteina veden pitoisuudesta ilmassa.

Osa tehtäväänne on edistää ISS:n miehistön jokapäiväistä elämää, joten antamalla heidän tietää, että avaruusaseman ilmankosteus on tavanomaisella alueella, rauhoittaa heitä.

[[[generic-theory-what-is-humidity]]]

--- task ---

Lisää tämä koodi kosteuden lukemiseksi:

```python
humid = sense.humidity
```

Tämä viiva mittaa nykyisen kosteuden ja tallentaa mitatun arvon muuttujaan `humid`.

--- /task ---

--- task ---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. You can round the value to any number of decimal places. In the example we have rounded to one decimal place, but for a different level of precision, change the number `1` to the number of decimal places you would like to see.

```python
humid = round( sense.humidity, 1 )
```

--- /task ---

--- task ---

Lisää tämä koodirivi näyttääksesi nykyisen kosteuden vieritysviestinä näytöllä:

```python
sense.show_message( str(humid) )
```

`str()`-osa muuntaa kosteuden numerosta tekstiksi, jotta Astro Pi voi näyttää sen.

--- /task ---

--- task ---

Voit myös näyttää kosteuden osana toista viestiä liittämällä viestisi osat käyttäen merkkiä `+`.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

--- /task ---

Oikea Astro Pi mittaa sen ympärillä olevan kosteuden, mutta voit liikuttaa kosteuden liukusäädintä Sense HAT -emulaattorissa simuloidaksesi kosteuden muutoksia ja testataksesi koodiasi.

![Kosteuden liukusäädin](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.
