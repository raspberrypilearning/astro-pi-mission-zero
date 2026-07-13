## Näytä kuva

The image you display will be made from 64 coloured squares called **pixels**. The pixels are arranged in an 8 x 8 grid. Each pixel can be a different colour. By choosing the colours carefully, you can create a picture. Here is an example of a whale made using different shades of blue on a black background.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED-matriisi**</span> on ruudukko LEDejä, joita voidaan ohjata yhdessä tai erikseen erilaisten valotehosteiden luomiseksi. Sense HATin LED-matriisissa on 64 LEDiä 8 x 8 -ruudukossa. LEDit voidaan ohjelmoida tuottamaan laaja valikoima värejä.
</p>

![Ruutukaappaus emulaattorin ikkunasta, jossa näkyy lentoyksikön LED-matriisi näyttämässä kukan kuvaa.](images/whale.png)

Notice that each square is labelled with a code to represent a particular colour. In this image 3 colours are used:
+ Tarkista, että koodisi vastaa yllä olevien esimerkkien koodia
+ Tarkista, että olet sisentänyt koodin luettelossasi
+ Tarkista, että luettelosi ympärillä on `[` ja `]`


--- task ---

Avaa [Mission Zero -aloitusprojekti](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"}.

Näet, että sinua varten on lisätty muutama koodirivi automaattisesti.

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

![Ruutukaappaus Sense Hat -emulaattorista, jossa on aloituskoodirivejä vasemmalla reunalla.](images/sense-hat-emulator3.png)

--- /task ---

### RGB-värit

Värejä voidaan luoda käyttämällä punaista, vihreää ja sinistä eri suhteissa. Voit tutustua RGB-väreihin täältä:

![Three sliders demonstrating RGB colour values](images/rgbsliders.gif)

LED-matriisi on 8 x 8 -ruudukko. Jokainen ruudukon LED-valo voidaan asettaa eri väriin. We can use the letters a to z as the names of variables to represent 24 different colours. Each colour has a value for red, green, and blue.

--- collapse ---

---
title: Kala
---

![A grid of 24 coloured squared each labelled with a different letter of the alphabet](images/palette.png)

```python
z = (153, 50, 204) # DarkOrchid
q = (255, 255, 0) # Keltainen
d = (51, 153, 255) # sininen
c = (0, 0, 0) # Musta

kuva = [
d, d, z, d, d, d, d, d, d, d, d,
d, d, z, z, d, d,
z, d, q, q, q, q, d, d,
z, z, q, q, q, c, q, d,
z, z, z, q, q, q, q, q, d,
z, z, q, q, q, q, q, d,
z, d, q, z, z, q, d, d,
d, d, z, d, d, d, d]

```

--- /collapse ---

### Valitse kuva

--- task ---

**Valitse:** Valitse näytettävä kuva alla olevista vaihtoehdoista. Python tallentaa kuvan tiedot luetteloon. Jokaisen kuvan koodi sisältää käytetyt värimuuttujat ja luettelon.

Sinun on **kopioitava** kaikki valitsemasi kuvan koodi ja sitten **liitettävä** se projektiisi alapuolelle riviä, jolla lukee `# Lisää värimuuttujia ja kuva`.

--- collapse ---

---
title: Mursu
---

![A grid with 8 x 8 squares showing a whale.](images/whale.png)

Created by Team Naicom, Italy

```python
h = (0, 255, 255) # Syaani
c = (0, 0, 0) # Musta
s = (139, 69, 19) # Satulanruskea
a = (255, 255, 255) # Valkoinen
r = (184, 134, 11) # TummaKultapiisku

kuva = [
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

![A grid with 8 x 8 squares showing a lemon.](images/lemon.png)

Created by team g4lemoni, Greece

```python
v = (255, 0, 0) # Punainen
m = (34, 139, 34) # Metsänvihreä
c = (0, 0, 0) # Musta 
e = (100, 149, 237) # Ruiskukansininen
l = (0, 255, 0) # Vihreä

kuva = [
    c, v, m, c, c, m, v, c,
    c, c, v, v, v, v, c, c,
    c, v, c, e, l, e, v, c,
    c, v, c, l, l, l, v, c,
    c, v, c, l, c, l, v, c,
    c, c, v, v, v, v, c, c,
    c, c, l, c, c, l, c, c,
    c, m, m, c, c, m, m, c]

```

--- /collapse ---

--- collapse ---
---
title: Koira
---

![A grid with 8 x 8 squares showing a pig.](images/pig.png)

Created by Gary, United Kingdom

```python
c = (0, 0, 0) # Musta
r = (184, 134, 11) # Tummankultapiisku
s = (139, 69, 19) # Satulanruskea
y = (255, 20, 147) # Syvänvaaleanpunainen

kuva = [
    c, r, r, c, c, r, r, c,
    c, r, s, s, s, r, c,
    c, r, c, s, s, c, r, c,
    c, s, s, s, s, s, s, c,
    c, s, s, s, s, s, s, c,
    c, s, s, c, c, s, s, c,
    c, c, s, y, y, s, c, c,
    c, c, c, y, y, c, c]

```

--- /collapse ---


--- collapse ---
---
title: Kameleontti
---

![A grid with 8 x 8 squares showing a storm cloud.](images/storm.png)

Created by team hop2p023, Spain

```python

c = (0, 0, 0) # Musta
s = (139, 69, 19) # Satulanruskea
a = (255, 255, 255) # Valkoinen
v = (255, 0, 0) # Punainen
t = (255, 140, 0) # Tummanoranssi
q = (255, 255, 0) # Keltainen
m = (34, 139, 34) # Metsänvihreä
h = (0, 255, 255) # Syaani
z = (153, 50, 204) # Tummanorkidea
y = (255, 20, 147) # Syvänvaaleanpunainen

kuva = [
    a, a, v, v, t, a, a,
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
title: Leija
---

![A grid with 8 x 8 squares showing a duck.](images/duck.png)

Created by Peter, Ireland

```python

c = (0, 0, 0) # Musta
m = (34, 139, 34) # Metsänvihreä
v = (255, 0, 0) # Punainen
q = (255, 255, 0) # Keltainen
e = (0, 0, 205) # Keskisininen
h = (0, 255, 255) # Syaani

kuva = [
    h, h, h, h, h, h, h, h, 
    h, h, h, e, e, v, v, h, 
    h, h, h, e, e, v, v, h, 
    h, h, h, q, q, m, m, h, 
    h, h, h, q, q, m, m, h,
    h, h, c, h, h, h, h, h, h, 
    h, c, h, h, h, h, h, h, h, 
    c, h, h, h, h, h, h, h, h]

```

--- /collapse ---

--- collapse ---
---
title: Kana
---

![A grid with 8 x 8 squares showing a Frog.](images/frog.png)

Created by team Jmeno, Czech Republic

```python

v = (255, 0, 0) # Punainen
c = (0, 0, 0) # Musta
b = (105, 105, 105) # Himmeänharmaa
q = (255, 255, 0) # Keltainen
r = (184, 134, 11) # Tummanpiisku

kuva = [
    c, c, v, v, v, c, c, c,
    c, v, b, b, r, c, c, r,
    c, b, c, b, b, c, r, b,
    q, r, b, b, b, b, b, b, r,
    c, v, b, b, b, b, r, b,
    c, v, b, r, r, r, b, r,
    c, c, c, r, b, q, r, c,
    c, c, c, c, q, q, c, c]

```

--- /collapse ---

--- collapse ---
---
line_highlights: 18, 19
---

![A grid with 8 x 8 squares showing a tree in blossom.](images/blossom.png)

Created by team Zssh14, Slovakia

```python

t = (255, 255, 0)   # Pure Yellow
g = (0, 204, 255)   # Sky Blue
w = (249, 169, 255) # Light Pink
y = (248, 97, 255)  # Magenta
z = (220, 53, 232)  # Purple
n = (126, 88, 25)   # Earth Brown
o = (179, 96, 65)   # Terracotta Brown
k = (46, 139, 33)   # Leaf Green

image =  [
t, g, g, w, w, y, g, g,
g, g, w, w, y, y, z, g,
g, w, y, z, y, z, z, z,
w, y, z, z, g, n, w, g,
g, g, o, o, n, w, y, z,
g, g, g, g, n, g, g, g,
g, g, g, o, n, n, g, g,
k, k, o, n, n, n, k, k]

```

--- /collapse ---

--- /task ---

--- task ---

**Etsi:** rivi, jossa lukee `# Näytä kuva` ja lisää koodirivi näyttääksesi kuvasi LED-matriisissa:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, a, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

# Näytä kuva
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

![Mission Zeron Tallennuspainike.](images/mz_savebutton_v2.png)

--- /task --- 
