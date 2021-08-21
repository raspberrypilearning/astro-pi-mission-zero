## Mittaa ilmankosteus

Astro Pin ilmankosteusanturi voi mitata ympäröivän ilman kosteutta, mikä on hyödyllinen ominaisuus, jonka avulla voit kerätä tietoja avaruusolosuhteista.

![Trinket Sense HAT -emulaattori ajamassa esimerkkiohjelmaa, joka vierittää ilmankosteuden arvoa LED-matriisin läpi valkoisin kirjaimin](images/M0_3.gif)

Astro Pi mittaa ISS:n ilmankosteuden prosentteina veden pitoisuudesta ilmassa.

Osa tehtäväänne on edistää ISS:n miehistön jokapäiväistä elämää, joten antamalla heidän tietää, että avaruusaseman ilmankosteus on tavanomaisella alueella, rauhoittaa heitä.

[[[generic-theory-what-is-humidity]]]

--- task ---

Lisää tämä koodi ilmankosteuden arvon lukemiseksi:

```python
humid = sense.get_humidity()
```

Tämä rivi mittaa nykyisen ilmankosteuden, ja tallentaa mitatun arvon muuttujaan `humid`.

--- /task ---

--- task ---

Ilmankosteus tallennetaan hyvin tarkkaan, eli tallennetussa arvossa on suuri määrä desimaaleja. Voit pyöristää arvon mihin tahansa desimaaliin. Esimerkissä olemme pyöristäneet yhden desimaalin tarkkuuteen, mutta eri tarkkuustasoa varten muuta numero `1` haluamasi desimaalilukumäärän mukaiseksi.

```python
humid = round(sense.get_humidity(), 1)
```

--- /task ---

--- task ---

Lisää tämä koodirivi näyttääksesi nykyisen ilmankosteuden vierivänä viestinä näytöllä:

```python
sense.show_message(str(humid))
```

`str()`-osa muuntaa ilmankosteuden numerosta tekstiksi, jotta Astro Pi voi näyttää sen.

--- /task ---

--- task ---

Voit myös näyttää ilmankosteuden osana toista viestiä liittämällä viestisi osat yhteen käyttäen merkkiä `+`.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

--- /task ---

Oikea Astro Pi mittaa sen ympärillä olevan ilmankosteuden, mutta voit liikuttaa kosteuden liukusäädintä Sense HAT -emulaattorissa simuloidaksesi kosteuden muutoksia ja testataksesi koodiasi.

![Merkitty ruutukaappaus Sense HAT -emulaattorista, jossa on koodi-ikkuna vasemmalla ja emulaattori oikealla. Liukusäädin, jota käytetään ilmankosteuden muuttamiseen, on ympyröitynä oikeassa yläkulmassa](images/humidity-slider.png)

**Huomautus:** Saatat ihmetellä, miksi ilmankosteuden liukusäädin näyttää ilmankosteuden kokonaislukuna, mutta saamasi lukema on desimaaliluku. Emulaattori simuloi oikean anturin hienoisen epätarkkuuden, joten näkemäsi ilmankosteuden mittaus voi olla hieman suurempi tai pienempi kuin liukusäätimellä asetettu arvo.
