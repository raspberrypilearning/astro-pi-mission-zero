## Näytä kuva

Astro Pin LED-matriisi voi näyttää värejä. Tässä vaiheessa näytät luontokuvia Astro Pin LED-matriisilla.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED-matriisi**</span> on ruudukko LEDejä, joita voidaan ohjata yhdessä tai erikseen erilaisten valotehosteiden luomiseksi. Sense HATin LED-matriisissa on 64 LEDiä 8 x 8 -ruudukossa. LEDit voidaan ohjelmoida tuottamaan laaja valikoima värejä.
</p>

![Ruutukaappaus emulaattorin ikkunasta, jossa näkyy lentoyksikön LED-matriisi näyttämässä kukan kuvaa.](images/fu-pic.png)

--- task ---

Avaa [Mission Zero -aloitusprojekti](https://missions.astro-pi.org/fi/mz/code_submissions/new){:target="_blank"}.

Näet, että muutama koodirivi on lisätty sinulle automaattisesti.

Tämä koodi ottaa yhteyden Astro Pihin, varmistaa Astro Pin LED-näytön olevan oikein päin ja määrittää värianturin. Jätä koodi sinne, koska tulet tarvitsemaan sitä.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
---
# Tuo kirjastot
from sense_hat import SenseHat
from time import sleep

# Määritä Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Määritä värianturi
sense.color.gain = 60 # Määritä anturin herkkyys
sense.color.integration_cycles = 64 # Aikaväli lukeman ottamiseksi

--- /code ---

![Ruutukaappaus Sense Hat -emulaattorista, jossa on aloituskoodirivejä vasemmalla reunalla.](images/sense-hat-emulator2.png)

--- /task ---

### RGB-värit

Värejä voidaan luoda käyttämällä punaista, vihreää ja sinistä eri suhteissa. Voit tutustua RGB-väreihin täältä:

[[[generic-theory-simple-colours]]]

LED-matriisi on 8 x 8 -ruudukko. Jokainen ruudukon LED-valo voidaan asettaa eri väriin. Tässä on luettelo muuttujista 24 eri värille. Jokaisella värillä on arvo punaiselle, vihreälle ja siniselle:

[[[ambient-colours]]]

### Valitse kuva

--- task ---

**Valitse:** Valitse näytettävä kuva alla olevista vaihtoehdoista. Python tallentaa kuvan tiedot luetteloon. Jokaisen kuvan koodi sisältää käytetyt värimuuttujat ja luettelon.

Sinun on **kopioitava** kaikki valitsemasi kuvan koodi ja sitten **liitettävä** se projektiisi alapuolelle riviä, jolla lukee `# Lisää värimuuttujia ja kuva`.

--- collapse ---

---
title: Kana
---

![8 x 8 neliön ruudukko esittämässä kananpoikasta munassa.](images/chick.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Valkoinen
c = (0, 0, 0) # Musta
e = (0, 0, 205) # Tummansininen
q = (255, 255, 0) # Keltainen
t = (255, 140, 0) # Tummanoranssi
w = (255, 192, 203) # Vaaleanpunainen

kuva = [
  c, c, c, q, q, q, c, c,
  c, c, t, q, e, q, c, c,
  c, c, c, q, q, q, c, c,
  c, w, w, w, w, w, w, c,
  c, w, a, a, a, a, w, c,
  c, w, a, a, a, a, w, c,
  c, c, w, a, a, w, c, c,
  c, c, c, w, w, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Kukka
---

![8 x 8 neliön ruudukko esittämässä vaaleanpunaista kukkaa vihreässä varressa.](images/flower.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
c = (0, 0, 0) # Musta
m = (34, 139, 34) # Metsänvihreä
q = (255, 255, 0) # Keltainen
t = (255, 140, 0) # Tummanoranssi
y = (255, 20, 147) # Tummanvaaleanpunainen

kuva = [
  c, c, y, y, y, y, c, c,
  c, y, y, t, t, y, y, c,
  y, y, t, q, q, t, y, y,
  c, y, y, t, t, y, y, c,
  c, c, y, y, y, y, c, c,
  m, c, c, m, m, c, c, m,
  c, m, m, m, m, m, m, c,
  c, c, c, m, m, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Rapu
---

![8 x 8 neliön ruudukko esittämässä rapua.](images/crab.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Valkoinen
c = (0, 0, 0) # Musta
v = (255, 0, 0) # Punainen

kuva = [
  c, a, a, c, a, a, c, c,
  c, a, c, c, a, c, c, c,
  c, v, c, c, v, c, c, c,
  c, v, c, c, v, c, c, c,
  v, v, v, v, v, c, v, v,
  v, v, c, c, v, v, v, c,
  v, v, v, v, v, c, v, v,
  v, c, v, c, v, c, c, c]
 

--- /code ---

--- /collapse ---


--- collapse ---
---
title: Krokotiili
---

![8 x 8 neliön ruudukko esittämässä krokotiilin päätä.](images/croc.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
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

--- /code ---


--- /collapse ---

--- collapse ---
---
title: Käärme
---

![8 x 8 neliön ruudukko esittämässä käärmettä.](images/snake.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
 c = (0, 0, 0) # Musta
 m = (34, 139, 34) # Metsänvihreä
 q = (255, 255, 0) # Keltainen
 v = (255, 0, 0) # Punainen

kuva = [
  c, c, c, c, c, c, c, m,
  c, m, m, m, m, m, m, m,
  c, m, c, c, c, c, c, c,
  c, m, m, m, m, m, c, c,
  c, c, c, c, c, m, c, c,
  q, m, q, m, m, m, c, c,
  m, m, m, c, c, c, c, c,
  v, c, c, c, c, c, c, c]
  
--- /code ---

--- /collapse ---

--- collapse ---
---
title: Sammakko
---

![8 x 8 neliön ruudukko esittämässä sammakkoa.](images/frog.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
c = (0, 0, 0) # Musta
m = (34, 139, 34) # Metsänvihreä
q = (255, 255, 0) # Keltainen
v = (255, 0, 0) # Punainen

kuva = [
  c, m, m, m, c, m, m, m,
  c, m, q, m, c, m, q, m,
  m, m, m, m, m, m, m, m,
  m, v, v, v, v, v, v, v,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, m, m, m, c, m]

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Etsi:** rivi, jossa lukee `# Näytä kuva` ja lisää koodirivi näyttääksesi kuvasi LED-matriisissa:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 12
---
kuva = [
  c, c, c, q, q, q, c, c,
  c, c, t, q, e, q, c, c,
  c, c, c, q, q, q, c, c,
  c, w, w, w, w, w, w, c,
  c, w, a, a, a, a, w, c,
  c, w, a, a, a, a, w, c,
  c, c, w, a, a, w, c, c,
  c, c, c, w, w, c, c, c]

# Näytä kuva 
sense.set_pixels(kuva)

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



