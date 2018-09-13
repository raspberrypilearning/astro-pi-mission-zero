## Mittaa lämpötila

Astro Pi:n lämpötila-anturi voi mitata sen ympärillä olevan ilman lämpötilaa; hyödyllinen ominaisuus auttaen sinua keräämään tietoja olosuhteista avaruudessa.

![Viesti lämpötilasta](images/degrees-message.gif)

Astro Pi mittaa lämpötilaa ISS:ssä celsiusasteina (&deg;C). Koska avaruudessa olevat lämpötilat vaihtelevat paljon enemmän kuin maapallolla, Astro Pi voi mitata lämpötiloja jopa -40 asteen ja +120 asteen välillä.

Osa tehtäväänne on edistää ISS:n miehistön jokapäiväistä elämää, joten antamalla heidän tietää, että avaruusaseman lämpötila on tavanomaisella alueella, rauhoittaa heitä.

--- collapse ---
---
title: Mikä on lämpötila?
---
Lämpötila mittaa tietyn kuumuuden. Sinun kehosi lämpö on ehkä mitattu lämpömittarilla käydessäsi lääkärissä.

![Lämpömittari](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} Wikimedia Commons -sivuston kautta*

Tarkemmin sanottuna lämpötila on aineen lämpöenergian mitattu määrä. Tiedät, että jääkuutio on kiinteä, mutta kun se lämpenee, eli kun se absorboi lämpöenergiaa sen ympäristöstä, se sulaa ja tulee nestemäiseksi. Tämä johtuu siitä, että kun aine imeytyy tai menettää riittävästi lämpöenergiaa, aine muuttaa tilaansa, esim. se muuttuu kiinteästä nestemäiseksi.

--- /collapse ---

--- task ---

Lisää tämä koodi lämpötilan lukeman ottamiseksi:

```python
temp = sense.get_temperature()
```

Tämä rivi mittaa nykyisen lämpötilan ja tallentaa mitatun arvon muuttujalle `temp`.

--- /task ---

--- task ---

Lämpötila tallennetaan hyvin tarkkaan merkiten sitä, että tallenntussa arvossa on suuri määrä desimaaleja. Voit pyöristää arvon mihin tahansa desimaaliin. Esimerkissä olemme pyöristäneet arvon yhden desimaalin tarkkuudella, mutta eri tarkkuustasoja varten muuta numero `1` desimaaliin, jonka haluat nähdä.

```python
temp = round( sense.get_temperature(), 1 )
```

--- /task ---

--- task ---

Olemassa olevan lämpötilan esittämiseksi vieritysviestinä näytössä lisää koodin tämä rivi:

```python
sense.show_message( str(temp) )
```

`str()` -osa muuntaa lämpötilan numerosta tekstiin niin, että Astro Pi voi näyttää sen.

--- /task ---

--- task ---

Voit myös näyttää lämpötilan osana toista viestiä liittämällä viestisi osat näin: `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

--- /task ---

Reaalitilan Astro Pi mittaa sen ympärillä olevan lämpötilan, mutta voit siirtää Sense HAT -emulaattorin lämpötilan liukusäädintä simuloimaan lämpötilan muutoksia ja testaamaan koodisi.

![Lämpötilan liukusäädin](images/temperature-slider.png)

**Huomautus:** Saatat ihmetellä, miksi lämpötilan liukusäädin näyttää lämpötilan kokonaislukuna, mutta lukema on desimaali. Emulaattori simuloi reaalianturin hienoisen epätarkkuuden, joten näkemän lämpötilan mittaus voi olla hieman suurempi tai pienempi kuin liukusäätimellä asetettu arvo.