## Näytä kuva

Voit näyttää kuvia Astro Pin LED-matriisissa. Ehkä tervehdyksesi astronauteille voisi sisältää kuvan tai kuvion kirjallisen viestin yhteydessä tai sen sijasta?

![Ruutukaappaus emulaattori-ikkunasta, jossa näkyy lentoyksikön LED-matriisi näyttämässä omaa kuvaansa lentoyksiköstä](images/fu-pic.png)

--- task ---

Luo ohjelman loppuun värimuuttujia määrittämään värit, joilla haluat piirtää kuvan. Voit käyttää niin monta väriä kuin haluat, mutta tässä esimerkissä käytämme vain muutamia värejä — punainen (`r`), valkoinen (`w`), musta (`b`), ja kaksi harmaan sävyä (`g` ja `s`). Huomaa, että sävyt saavutetaan vähentämällä valon määrää kaikissa kolmessa kanavassa ja pitämällä mittasuhteet samoina.

```python
w = (255, 255, 255)
b = (0, 0, 0)
g = (50,50,50)
s = (200,255,200)
r = (255,0,0)
```

**Huomautus:** Tällä kertaa kannattaa antaa värimuuttujille yksikirjaimisia nimiä, koska se säästää aikaa seuraavassa vaiheessa, jossa tulet kirjoittamaan ne useita kertoja. Lisäksi yksittäiset kirjaimet helpottavat piirtämäsi kuvan hahmottamista.

--- /task ---

--- task ---



Luo 64-kohtainen lista uusien muuttujien alle. Jokainen kohde edustaa yhtä pikseliä LED-matriisissa ja vastaa yhtä määrittämääsi värimuuttujaa. Piirrä kuvasi asettamalla muuttuja sinne, missä haluat sille nimetyn värin esiintyvän. Olemme piirtäneet Astro Pin käyttämällä mustia (`b`) pikseleitä taustana ja harmaita (`g`) pikseleitä Astro Pin lentokotelon metalliosina:

```python
 picture = [
    g, b, b, b, b, b, b, g,
    b, g, g, g, g, g, g, b,
    b, g, b, b, g, w, g, g,
    b, g, b, b, g, g, g, g,
    b, g, g, g, s, s, g, g,
    b, g, r, g, g, g, g, g,
    b, g, g, g, g, g, g, b,
    g, b, b, b, b, b, b, g
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

Paina **Run** (Suorita) nähdäksesi kuvasi näytössä.

--- /task ---

--- task ---

Haluat ehkä lisätä koodia lyhyttä viivettä varten (eli `sleep`-käsky) kuvan näyttämisen jälkeen. Tämä antaa astronauteille aikaa nähdä kuvasi ennen kuin seuraava viestisi osa tulee näkyviin. Lisää ohjelmasi alkuun:

```python
from time import sleep
```

Lisää sitten kuvasi näyttävää koodia seuraavalle riville tämä koodi kahden sekunnin viivettä varten:

```python
sleep(2)
```

--- /task ---

--- task ---

Luo oma kuva tai kuvio näytettäväksi astronauteille!

--- /task ---
