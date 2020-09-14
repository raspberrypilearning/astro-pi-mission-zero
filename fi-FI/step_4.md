## Lisää jonkun verran väriä

Astro Pin LEDit voivat näyttää myös värejä. Voit määrittää värin luomalla muuttujan ja antamalla sille RGB-väriarvon.

Täältä voit oppia, kuinka kaikki värit voidaan luoda käyttämällä punaisen, vihreän ja sinisen eri mittasuhteita:

[[[generic-theory-colours]]]

--- task ---

Valitse väri ja selvitä värin RGB-arvo. Voit käyttää [värinvalitsinta](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} auttamaan sinua.

--- /task ---

--- task ---

Luo muuttuja tallentaaksesi valitsemasi värin. Jos esimerkiksi valitsit punaisen, kirjoitat tämän koodirivin:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

Voit nyt näyttää tekstin haluamallasi värillä! Käskeäksesi ohjelman käyttämään valitsemaasi väriä, lisää parametri `text_colour` koodiin, joka näyttää tekstisi:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /task ---

![näytä viesti värillisenä](images/show-message-color.gif)

--- task ---

Voit myös vaihtaa näytön taustaväriä. Valitse toinen väri ja luo toinen muuttuja tallentamaan kyseinen väri. Käskeäksesi ohjelman käyttämään valitsemaasi taustaväriä, lisää parametri `back_colour` koodiisi:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Muuta tervehdystekstiä ja väriä — minkä viestin sinä lähetät ISS:n astronauteille?

--- /task ---