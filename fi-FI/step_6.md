## Mittaa lämpötila

Astro Pin lämpötila-anturi voi mitata sen ympärillä olevan ilman lämpötilaa. Tämä on hyödyllinen ominaisuus, joka auttaa sinua keräämään tietoja olosuhteista avaruudessa.

![Viesti lämpötilasta](images/degrees-message.gif)

Astro Pi mittaa lämpötilaa ISS:ssä celsiusasteina (&deg;C). Koska avaruudessa olevat lämpötilat vaihtelevat paljon enemmän kuin maapallolla, Astro Pi voi mitata lämpötiloja jopa -40 asteen ja +120 asteen välillä.

Osa tehtäväänne on edistää ISS:n miehistön jokapäiväistä elämää, joten antamalla heidän tietää, että avaruusaseman lämpötila on tavanomaisella alueella, rauhoittaa heitä.

--- collapse ---
---
title: Mikä on lämpötila?
---

Lämpötila on mitta siitä, kuinka kuuma jokin on. Sinun kehosi lämpö on ehkä mitattu lämpömittarilla käydessäsi lääkärissä.

![Lämpömittari](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} Wikimedia Commons -sivuston kautta*

Tarkemmin sanottuna lämpötila on aineen lämpöenergian mitattu määrä. Tiedät jääkuution olevan kiinteä, mutta kun se lämpenee eli imee itseensä lämpöenergiaa ympäristöstään, se sulaa ja muuttuu nestemäiseksi. Tämä johtuu siitä, että kun aine imee itseensä tai menettää riittävästi lämpöenergiaa, aine muuttaa olomuotoaan, esim. se muuttuu kiinteästä nestemäiseksi.

--- /collapse ---

--- task ---

Lisää tämä koodi lämpötilan lukemiseksi:

```python
temp = sense.temperature
```

Tämä rivi mittaa nykyisen lämpötilan ja tallentaa mitatun arvon muuttujaan `temp`.

--- /task ---

--- task ---

Lämpötila tallennetaan hyvin tarkkaan, eli tallennetussa arvossa on suuri määrä desimaaleja. Voit pyöristää arvon mihin tahansa desimaaliin. Esimerkissä olemme pyöristäneet yhden desimaalin tarkkuuteen, mutta eri tarkkuustasoa varten muuta numero `1` haluamasi desimaalilukumäärän mukaiseksi.

```python
temp = round( sense.temperature, 1 )
```

--- /task ---

--- task ---

Lisää tämä koodirivi näyttääksesi nykyisen lämpötilan vieritysviestinä näytöllä:

```python
sense.show_message( str(temp) )
```

`str()`-osa muuntaa lämpötilan numerosta tekstiksi, jotta Astro Pi voi näyttää sen.

--- /task ---

--- task ---

Voit myös näyttää lämpötilan osana toista viestiä liittämällä viestisi osat käyttäen merkkiä `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

--- /task ---

Oikea Astro Pi mittaa sen ympärillä olevan lämpötilan, mutta voit liikuttaa lämpötilan liukusäädintä Sense HAT -emulaattorissa simuloidaksesi lämpötilan muutoksia ja testataksesi koodiasi.

![Lämpötilan liukusäädin](images/temperature-slider.png)

**Huomautus:** Saatat ihmetellä, miksi lämpötilan liukusäädin näyttää lämpötilan kokonaislukuna, mutta saamasi arvo on desimaaliluku. Emulaattori simuloi oikean anturin hienoisen epätarkkuuden, joten näkemäsi lämpötilan mittaus voi olla hieman suurempi tai pienempi kuin liukusäätimellä asetettu arvo.