## Näytä lämpötila

Voit yhdistää lämpötilalukemasi kuvaan myös lämpötilan osoittamiseksi graafisella tavalla. Esimerkiksi saatat näyttää lumimyrskyn kylmille lämpötiloille ja aurinkoisen päivän kuumille lämpötiloille:

![Kuuma ja kylmä](images/hot-and-cold.png)

--- task ---

Luo ohjelman alaosaan tiettyjä värimuuttujia määrittääksesi värit, joilla haluat piirtää kuvan. Olet ehkä jo määritellyt joitakin niistä edellisessä vaiheessa. Esimerkkeissämme käytämme valkoista (`w`), keltaista (`y`), vihreää (`g`) ja mustaa / tyhjää (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

--- /task ---

--- task ---

Aivan kuten aiemmin, piirrä kuvat luoden ensin listan jokaisesta niistä ja asettaen sitten listan kohteet väreihin, joissa haluat pikselisi esitettäväksi.

```python
kuuma = [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g
]


kylmä = [
  b, b, w, b, b, b, w, b,
  b, b, b, b, b, w, b, b,
  b, w, b, b, b, b, b, w,
  b, b, b, b, w, b, b, b,
  w, b, b, w, b, b, w, b,
  b, b, b, b, b, b, b, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w
]
```

--- /task ---

--- task ---

Lisää tietty koodi lämpötilan saamiseksi:

```python
temp = sense.get_temperature()
```

--- /task ---

--- task ---

Päätä nyt, minkä kuvan haluat esitettäväksi. Tässä esimerkissä näytämme kuvan `hot`, jos lämpötilan lukema on 20 astetta tai sen yli ja, jos lämpötila lukema on alle 20 astetta, näytämme kuvan `cold`.

```python
temp = sense.get_temperature()
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

--- /task ---

--- task ---

Käytä lämpötilan liukusäädintä asettaaksesi lämpötilan emulaattoriin. Aja ohjelma ja tarkista, että kyseiselle lämpötilalle valittu kuva näytetään oikein.

--- /task ---

--- task ---

Muuta koodisi niin, että ohjelma näyttää lämpötilan astronauteille omalla valitsemallasi tavalla.

--- /task ---