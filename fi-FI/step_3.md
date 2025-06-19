## Näytä kuva

Astro Pin LED-matriisi voi näyttää värejä. Tässä vaiheessa näytät luontokuvia Astro Pin LED-matriisilla.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED-matriisi**</span> on ruudukko LEDejä, joita voidaan ohjata yhdessä tai erikseen erilaisten valotehosteiden luomiseksi. Sense HATin LED-matriisissa on 64 LEDiä 8 x 8 -ruudukossa. LEDit voidaan ohjelmoida tuottamaan laaja valikoima värejä.
</p>

![Ruutukaappaus emulaattorin ikkunasta, jossa näkyy lentoyksikön LED-matriisi näyttämässä kukan kuvaa.](images/fu-pic.png)

--- task ---

Avaa [Mission Zero -aloitusprojekti](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"}.

Näet, että muutama koodirivi on lisätty sinulle automaattisesti.

Tämä koodi ottaa yhteyden Astro Pihin, varmistaa Astro Pin LED-näytön olevan oikein päin ja määrittää värianturin. Jätä koodi sinne, koska tulet tarvitsemaan sitä.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Tuo kirjastot
from sense_hat import SenseHat from time import sleep

# Määritä Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Määritä värianturi
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Ruutukaappaus Sense Hat -emulaattorista, jossa on aloituskoodirivejä vasemmalla reunalla.](images/sense-hat-emulator2.png)

--- /task ---

### RGB-värit

Värejä voidaan luoda käyttämällä punaista, vihreää ja sinistä eri suhteissa. Voit tutustua RGB-väreihin täältä:

[[[generic-theory-simple-colours]]]

The LED matrix is an 8 x 8 grid. Jokainen ruudukon LED-valo voidaan asettaa eri väriin. Tässä on luettelo muuttujista 24 eri värille. Jokaisella värillä on arvo punaiselle, vihreälle ja siniselle:

[[[ambient-colours]]]

### Valitse kuva

--- task ---

**Valitse:** Valitse näytettävä kuva alla olevista vaihtoehdoista. Python tallentaa kuvan tiedot luetteloon. Jokaisen kuvan koodi sisältää käytetyt värimuuttujat ja luettelon.

Sinun on **kopioitava** kaikki valitsemasi kuvan koodi ja sitten **liitettävä** se projektiisi alapuolelle riviä, jolla lukee `# Lisää värimuuttujia ja kuva`.

--- collapse ---

---
title: Fish
---

![A grid with 8 x 8 squares showing a fish.](images/fish.png)

Created by team chalka, Poland

```python
z = (204, 0, 204) # magenta
q = (255, 255, 0) # yellow
d = (51, 153, 255) # blue
c = (0, 0, 0) # black

image = [
d, d, z, d, d, d, d, d,
d, d, d, z, z, d, d, d,
z, d, q, q, q, q, d, d,
z, z, q, q, q, c, q, d,
z, z, z, q, q, q, q, d,
z, z, q, q, q, q, q, d,
z, d, q, z, z, q, d, d,
d, d, d, z, d, d, d, d]

```

--- /collapse ---


--- collapse ---

---
title: Walrus
---

![A grid with 8 x 8 squares showing a walrus.](images/walrus.png)

Created by team Walrus, Finland

```python
h = (0, 255, 255)
c = (0, 0, 0)
s = (139, 69, 19)
a = (255, 255, 255)
r = (184, 134, 11)   

image = [
h, h, h, h, h, h, h, h,
h, h, s, s, s, h, h, h,
h, s, s, s, s, s, h, h,
h, s, c, s, c, s, s, s,
h, r, r, r, r, r, s, s,
h, h, a, s, a, s, s, s,
h, h, a, s, a, s, s, s,
r, r, s, s, s, s, s, s]

```

--- /collapse ---

--- collapse ---
---
title: Paxi
---

![A grid with 8 x 8 squares showing paxi.](images/paxi.png)

Created by team tony_pi, Italy

```python
v = (255, 0, 0) # Red
j = (34, 139, 34) # ForestGreen
c = (0, 0, 0) # Black 
e = (100, 149, 237) # CornflowerBlue
l = (0, 255, 0) # Green

image = [
    c, v, j, c, c, j, v, c,
    c, c, v, v, v, v, c, c,
    c, v, c, e, l, e, v, c,
    c, v, c, l, l, l, v, c,
    c, v, c, l, c, l, v, c,
    c, c, v, v, v, v, c, c,
    c, c, l, c, c, l, c, c,
    c, j, j, c, c, j, j, c]

```

--- /collapse ---


--- collapse ---
---
title: Dog
---

![A grid with 8 x 8 squares showing a dog head.](images/dog.png)

Created by team ptpr_07, Spain
```python

c = (0, 0, 0) # Black
r = (86, 71, 0) # Light Brown
s = (123, 61, 0) # Orange Brown
y = (155, 0, 134) # Deep Pink

image = [
    c, r, r, c, c, r, r, c,
    c, r, s, s, s, s, r, c,
    c, r, c, s, s, c, r, c,
    c, s, s, s, s, s, s, c,
    c, s, s, s, s, s, s, c,
    c, s, s, c, c, s, s, c,
    c, c, s, y, y, s, c, c,
    c, c, c, y, y, c, c, c]


```

--- /collapse ---

--- collapse ---
---
title: Chameleon
---

![A grid with 8 x 8 squares showing a rainbow coloured chameleon.](images/chameleon.png)

Created by team The_ETs, United Kingdom

```python

c = (0, 0, 0) # Black
s = (95, 65, 0) # Brown
a = (255, 255, 255) # white
v = (255, 0, 0) # Red
t = (255, 153, 28) # Orange
q = (255, 255, 0) # Yellow
m = (0, 255, 0) # Green
h = (0, 255, 255) # Cyan
z = (128, 0, 255) # Purple
y = (191, 0, 255) # Magenta

image = [
    a, a, v, v, t, a, a, a,
    a, v, v, t, t, q, a, a,
    v, c, t, t, q, q, m, a,
    v, t, t, q, q, m, m, h,
    s, s, q, s, s, m, s, h,
    a, a, a, a, a, a, a, z,
    a, a, a, a, y, a, a, z,
    a, a, a, a, a, y, z, a]

```

--- /collapse ---

--- collapse ---
---
title: Lohikäärme
---

![A grid with 8 x 8 squares showing a kite.](images/kite.png)

Created by team Val, Greece

```python

b = (105, 105, 105) # DimGray
c = (0, 0, 0) # Musta
d = (100, 149, 237) # Ruiskukansininen
v = (255, 0, 0) # Punainen
z = (153, 50, 204) # Tummanorkidea

kuva = [
    c, c, v, c, v, c, c, c,
    c, z, z, z, z, v, c, c,
    z, b, z, b, z, c, c, c,
    z, z, z, z, z, v, c, c,
    c, c, d, d, d, c, c, z,
    c, z, d, z, z, z, z, c,
    c, c, d, d, z, c, c, c,
    c, c, z, c, z, c, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Chicken
---

![A grid with 8 x 8 squares showing a Chicken.](images/chicken.png)

Created by team Slepicky, Czech Republic

```python

a = (255, 255, 255) # Valkoinen
c = (0, 0, 0) # Musta
f = (25, 25, 112) # Yönsininen
m = (34, 139, 34) # Metsänvihreä

kuva = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

# Näytä kuva
sense.set_pixels(kuva)

```

--- /collapse ---

--- /task ---

--- task ---

**Etsi:** rivi, jossa lukee `# Näytä kuva` ja lisää koodirivi näyttääksesi kuvasi LED-matriisissa:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 18, 19
---
Kuvani ei näy:

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

# Display the image
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Paina **Aja** editorin alaosassa nähdäksesi kuvasi LED-matriisissa.

--- /task ---

--- task ---

**Vianselvitys**

Koodissani on syntaksivirhe:

- Tarkista, että koodisi vastaa yllä olevien esimerkkien koodia
- Tarkista, että olet sisentänyt koodin luettelossasi
- Tarkista, että luettelosi ympärillä on `[` ja `]`
- Tarkista, että jokainen värimuuttuja luettelossa on erotettu pilkulla

Kuvani ei näy:

- Tarkista, että `sense.set_pixels(kuva)` ei ole sisennetty

--- /task ---


--- task ---

**Tallenna kehityksesi**

Nyt kun olet näyttänyt kuvan, voit tallentaa ohjelmasi tehtävän aloitusprojektissa syöttämällä joukkueesi nimen, joukkueen jäsenten nimet ja saamasi luokkahuonekoodin. Voit ladata ohjelman uudelleen millä tahansa laitteella, jossa on Internet-yhteys, syöttämällä joukkuenimen ja luokkahuonekoodin.

![Mission Zeron Tallennuspainike](images/mz_savebutton_v2.png)

--- /task --- 
