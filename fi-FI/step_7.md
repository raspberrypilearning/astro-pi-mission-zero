## Reagoi ilmankosteuteen

Voit yhdistää ilmankosteuden lukemasi kuvaan näyttääksesi ilmankosteuden myös graafisella tavalla. Esimerkiksi voit näyttää valtameren korkealle kosteudelle ja aavikon matalalle kosteudelle:

![Märkä ja kuiva](images/wet-dry.png)

--- task ---

Lisää ohjelman loppuun uusia värimuuttujia kaikille väreille, joita haluat käyttää kuvissasi. Olet ehkä jo määritellyt joitakin niistä edellisessä vaiheessa.

```python
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)
```

--- /task ---

--- task ---

Aivan kuten aiemminkin, piirrä kuvat luomalla ensin listan jokaista varten, ja sitten täyttämällä listan kohdat väreillä, joilla haluat pikselisi esitettävän.

```python
wet = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


dry = [
  c, c, g, g, c, c, c, c,
  c, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, g, g, g, g, g, c, c,
  c, c, g, g, c, c, c, c,
  y, y, y, y, y, y, y, y,
  y, y, y, y, y, y, y, y
]
```

--- /task ---

--- task ---

Lisää koodia ilmankosteuden saamiseksi:

```python
humid = sense.get_humidity()
```

--- /task ---

--- task ---

Päätä nyt, minkä kuvan haluat esitettäväksi. Tässä esimerkissä näytämme kuvan `wet`, jos ilmankosteuslukema on 40% tai sen yli, ja kuvan `dry`, jos ilmankosteuslukema on alle 40%.

```python
humid = sense.get_humidity()
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

Aseta ilmankosteus emulaattoriin käyttäen ilmankosteuden liukusäädintä. Suorita ohjelma ja tarkista, että kyseiselle ilmankosteudelle valittu kuva näytetään oikein.

--- /task ---

--- task ---

Muuta koodiasi niin, että ohjelma näyttää kosteuden astronauteille omalla valitsemallasi tavalla.

--- /task ---

--- task --- Testaa koodiasi muutamilla erilaisilla ilmankosteusarvoilla (liukusäädintä käyttäen) varmistaaksesi, että se toimii aina oikein. Jos olet seurannut yllä olevaa esimerkkiä, onko kuva näkyvissä silloin, kun ilmankosteuden arvo on alle 40 %, sekä silloin, kun se on yli 40 %?

--- /task ---
