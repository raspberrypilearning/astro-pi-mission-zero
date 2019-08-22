## Näytä kuva

Voit näyttää kuvia Astro Pin LED-matriisissa. Ehkä tervehdyksesi astronauteille voisi sisältää kuvan tai kuvion kirjallisen viestin yhteydessä tai sen sijasta?

![Astronautti](images/astronaut-pic.png)

\--- task \---

Luo ohjelman loppuun värimuuttujia määrittämään värit, joilla haluat piirtää kuvan. Voit käyttää niin montaa väriä kuin haluat, mutta tässä esimerkissä käytämme vain kahta väriä — valkoista (`w`) ja mustaa (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Huomautus:** Tällä kertaa kannattaa antaa värimuuttujille yksikirjaimisia nimiä, koska se säästää aikaa seuraavassa vaiheessa, jossa tulet kirjoittamaan ne useita kertoja. Lisäksi yksittäiset kirjaimet helpottavat piirtämäsi kuvan näkemistä.

\--- /task \---

\--- task \---

Luo 64-kohtainen lista uusien muuttujien alle. Jokainen kohde edustaa yhtä pikseliä LED-matriisissa ja vastaa yhtä määrittämistäsi värimuuttujista. Piirrä kuvasi asettamalla muuttuja sinne, missä haluat sille nimetyn värin esiintyvän. Olemme piirtäneet astronautin käyttämällä mustia (`b`) pikseleitä taustana ja valkoisia (`w`) pikseleitä piirtämään astronautin avaruuspuvun:

```python
picture = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
```

\--- /task \---

\--- task \---

Lisää koodirivi esittämään kuvasi LED-näytössä.

```python
sense.set_pixels(picture)
```

\--- /task \---

\--- task \---

Paina **Run** (Suorita) nähdäksesi kuvasi näytössä.

\--- /task \---

\--- task \---

Haluat ehkä lisätä koodia lyhyttä viivettä varten (eli `sleep`-käsky) kuvan näyttämisen jälkeen. Tämä antaa astronauteille aikaa nähdä kuvasi ennen kuin seuraava viestisi osa tulee näkyviin. Lisää ohjelman yläosaan:

```python
from time import sleep
```

Lisää sitten kuvasi näyttävää koodia seuraavalle riville tämä koodi kahden sekunnin viivettä varten:

```python
sleep(2)
```

\--- /task \---

\--- task \---

Luo oma kuva tai kuvio näytettäväksi astronauteille!

\--- /task \---