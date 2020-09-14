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

Kosteus tallennetaan hyvin tarkkaan, eli tallennetussa arvossa on suuri määrä desimaaleja. Voit pyöristää arvon mihin tahansa desimaaliin. Esimerkissä olemme pyöristäneet yhden desimaalin tarkkuuteen, mutta eri tarkkuustasoa varten muuta numero `1` haluamasi desimaalilukumäärän mukaiseksi.

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

**Huomautus:** Saatat ihmetellä, miksi kosteuden liukusäädin näyttää kosteuden kokonaislukuna, mutta saamasi lukema on desimaaliluku. Emulaattori simuloi oikean anturin hienoisen epätarkkuuden, joten näkemäsi kosteuden mittaus voi olla hieman suurempi tai pienempi kuin liukusäätimellä asetettu arvo.