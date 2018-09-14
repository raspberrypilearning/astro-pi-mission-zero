## Esitä kuva

Voit näyttää kuvia Astro Piin LED-matriisissa. Ehkä tervehdyksesi astronauteille voisi sisältää kuvan tai kuvion sekä myös kirjallisen viestin niiden yhteydessä tai niiden sijasta?

![Astronautti](images/astronaut-pic.png)

--- task ---

Luo ohjelman alaosaan tiettyjä värimuuttujia määrittääksesi värit, joilla haluat piirtää kuvan. Voit käyttää niin monta väriä kuin haluat, mutta tässä esimerkissä käytämme vain kahta väriä - valkoista (`w`) ja mustaa (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Huomautus:** Tällä kertaa kannattaa antaa värimuuttujille yksikirjaimisia nimiä, koska se säästää aikaa seuraavassa vaiheessa, jossa tulet kirjoittamaan ne useita kertoja. Lisäksi yksittäiset kirjiamet tekevät helpommaksi nähdä kuvan, jonka piirrät.

--- /task ---

--- task ---

Luo uusien muuttujien alle 64 kohteen luettelo. Jokainen kohde edustaa yhtä pikseliä LED-matriisissa ja vastaa yhtä määrittämistäsi värimuuttujista. Piirrä kuvasi asettamalla muuttuja, jossa haluat sen nimetyn värin esiintyvän. Olemme piirtäneet astronautin käyttämällä mustia (`b`) pikseleinä taustana ja valkoisia (`w`) pikseleitä piirtämään astronautin avaruuspuvun:

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

--- /task ---

--- task ---

Lisää koodirivi esittämään kuvasi LED-näytössä.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Paina **Run** nähdäksesi kuvasi näytössä.

--- /task ---

--- task ---

Haluat ehkä lisätä tietyn koodin sisällyttämään lyhyen odotuksen (vaihtoehtona `sleep`) kuvan näyttämisen jälkeen. Tämä antaa astronauteille aikaa nähdä kuvasi ennen kuin seuraava viestisi osa tulee näkyviin. Lisää ohjelman yläosaan:

```python
from time import sleep
```

Lisää sitten kuvasi esittämän koodin jälkeiselle riville tämä koodi odottamaan kaksi sekuntia:

```python
sleep(2)
```

--- /task ---

--- task ---

Luo oma kuvasi tai kuviosi astronauteille näyttämiseksi!

--- /task ---
