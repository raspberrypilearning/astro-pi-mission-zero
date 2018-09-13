## Näytä viesti

--- task ---

Avaa [Sense HAT emulator](https://trinket.io/mission-zero){:target="_blank"} Mission Zero -hanketta varten.

Näet, että kolme koodiriviä on lisätty automaattisesti sinua varten:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![sense hat -emulaattori](images/sense-hat-emulator2.png)

Tämän koodin kytkennän kohteena on Astro Pi, ja se varmistaa, että Astro Pi LED -näyttö on esitetty oikein. Jätä koodi sinne. koska tulet tarvitsemaan sitä.

--- /task ---

--- task ---

Ehkä voisit jättää mukavan tervehdyksen ISS:n astronauteille, jotka työskentelevät lähellä Astro Piä? Selataanpa viestiä näytöllä.

Lisää tämä rivi toisen koodin alapuolelle:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Paina **Run** (Suorita) -painiketta ja katsele, kun viesti `Astro Pi` vierittyy LED-näytön poikkii.

![näytä viestikoodin aja-klikkaus](images/show-message-code-annotated.PNG)

--- /task ---

![Vieritysviesti](images/scroll-message.gif)

Erilaisen viestin näyttämiseksi voit kirjoittaa sen lainausmerkkien (`""`) väliin.

--- collapse ---
---
title: Mitä merkkejä voidaan käyttää?
---
Sense HAT voi esittää Latin 1 -merkistön merkiten sitä, että vain seuraavat merkiit ovat saatavana. Muut merkit näytetään muodossa `?`.

    +-*/!"#$><0123456789.=)(
    
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    abcdefghijklmnopqrstuvwxyz
    
    ?,;:|@%[&_']~
    

--- /collapse ---

--- task ---

Voit myös muuttaa näytön poikki vierivän viestin nopeutta. Lisää `scroll_speed` jo olemassa olevan koodisi riviin tällä tavalla:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Viestin oletusnopeus on `0.1`. Numeron tekeminen pienemmäksi saa viestin vierittymään nopeammin, ja sen tekeminen suuremmaksi saa viestin vierittymään hitaammin.

--- /task ---