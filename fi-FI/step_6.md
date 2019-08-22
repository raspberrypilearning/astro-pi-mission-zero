## Mittaa lämpötila

Astro Pin lämpötila-anturi voi mitata sen ympärillä olevan ilman lämpötilaa. Tämä on hyödyllinen ominaisuus, joka auttaa sinua keräämään tietoja olosuhteista avaruudessa.

![Viesti lämpötilasta](images/degrees-message.gif)

Astro Pi mittaa lämpötilaa ISS:ssä celsiusasteina (&deg;C). Koska avaruudessa olevat lämpötilat vaihtelevat paljon enemmän kuin maapallolla, Astro Pi voi mitata lämpötiloja jopa -40 asteen ja +120 asteen välillä.

Osa tehtäväänne on edistää ISS:n miehistön jokapäiväistä elämää, joten antamalla heidän tietää, että avaruusaseman lämpötila on tavanomaisella alueella, rauhoittaa heitä.

## \--- collapse \---

## title: Mikä on lämpötila?

Lämpötila on mitta siitä, kuinka kuuma jokin on. Sinun kehosi lämpö on ehkä mitattu lämpömittarilla käydessäsi lääkärissä.

![Lämpömittari](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} Wikimedia Commons -sivuston kautta*

Tarkemmin sanottuna lämpötila on aineen lämpöenergian mitattu määrä. Tiedät, että jääkuutio on kiinteä, mutta kun se lämpenee, eli kun se imee itseensä lämpöenergiaa sen ympäristöstä, se sulaa ja tulee nestemäiseksi. Tämä johtuu siitä, että kun aine imee itseensä tai menettää riittävästi lämpöenergiaa, aine muuttaa olomuotoaan, esim. se muuttuu kiinteästä nestemäiseksi.

\--- /collapse \---

\--- task \---

Lisää tämä koodi lämpötilan lukeman ottamiseksi:

```python
temp = sense.temperature
```

Tämä rivi mittaa nykyisen lämpötilan ja tallentaa mitatun arvon muuttujalle `temp`.

\--- /task \---

\--- task \---

Lämpötila tallennetaan hyvin tarkkaan merkiten sitä, että tallennetussa arvossa on suuri määrä desimaaleja. Voit pyöristää arvon mihin tahansa desimaaliin. Esimerkissä olemme pyöristäneet arvon yhden desimaalin tarkkuudella, mutta eri tarkkuustasoja varten muuta numero `1` desimaaliin, jonka haluat nähdä.

```python
temp = round( sense.temperature, 1 )
```

\--- /task \---

\--- task \---

Jos haluat näyttää nykyisen lämpötilan vieritysviestinä näytöllä, lisää tämä koodirivi:

```python
sense.show_message( str(temp) )
```

`str()` -osa muuntaa lämpötilan numerosta tekstiksi, jotta Astro Pi voi näyttää sen.

\--- /task \---

\--- task \---

Voit myös näyttää lämpötilan osana toista viestiä liittämällä viestisi osat `+` merkillä.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

Oikea Astro Pi mittaa sen ympärillä olevan lämpötilan, mutta voit siirtää Sense HAT -emulaattorin lämpötilan liukusäädintä simuloimaan lämpötilan muutoksia ja testaamaan koodiasi.

![Lämpötilan liukusäädin](images/temperature-slider.png)

**Huomautus:** Saatat ihmetellä, miksi lämpötilan liukusäädin näyttää lämpötilan kokonaislukuna, mutta lukema on desimaali. Emulaattori simuloi oikean anturin hienoisen epätarkkuuden, joten näkemäsi lämpötilan mittaus voi olla hieman suurempi tai pienempi kuin liukusäätimellä asetettu arvo.