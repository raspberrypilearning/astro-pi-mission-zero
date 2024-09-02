## Kuva pilt

Astro Pi LED-maatriksid suudavad kuvada ka värve. Selles etapis kuvad Astro Pi LED-maatriksil pilte loodusest.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED-maatriks**</span> on LED-ide võre, mida saab juhtida üksikult või rühmana, et luua erinevaid valgusefekte. Sense HAT-i LED-maatriksil on 64 LED-i, mis kuvatakse 8 x 8 võrena. LED-e saab programmeerida tootma laias valikus värve.
</p>

![Emulaatori akna kuvatõmmis, mis näitab lennuüksust, LED-maatriks kuvamas pilti lillest.](images/fu-pic.png)

--- task ---

Ava [Mission Zero stardiprojekt](http://rpf.io/mzcode){:target="_blank"}.

Näed, et sulle on automaatselt lisatud mõned read koodi.

See kood ühendub Astro Pi-ga ja tagab, et Astro Pi LED-ekraan kuvatakse õigesti ning unstallib värvianduri. Jäta kood sinna, sest sul läheb seda vaja.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Impordi teegid
from sense_hat import SenseHat from time import sleep

# Installi Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Installi värviandur
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Sense HAT-i emulaatori kuvatõmmis algkoodi ridadega, kuvatud vasakus paanis.](images/sense-hat-emulator2.png)

--- /task ---

### RGB värvid

Värve saab luua kasutades erinevaid punase, rohelise ja sinise proportsioone. RGB värvide kohta saad rohkem teada siin:

[[[generic-theory-simple-colours]]]

LED-maatriks on 8 x 8 võre. Iga võre LED-i saab seadistada erinevat värvi. Siin on 24 erineva värvi muutujate loend. Igal värvil on väärtus punase, rohelise ja sinise jaoks:

[[[ambient-colours]]]

### Vali pilt

--- task ---

**Vali:** Vali allolevatest variantidest pilt, mida kuvada. Python salvestab pildi teabe loendisse. Iga pildi kood sisaldab kasutatud värvide muutujaid ja loendit.

Pead **kopeerima** kogu valitud pildi koodi ja seejärel **kleepima** selle oma projekti selle rea alla, mis ütleb `# Lisa värvi muutujad ja pilt`.

--- collapse ---

---
pealkiri: Rebane
---

![8 x 8 ruuduga võre, mis näitab rebase nägu.](images/fox_mz3.png)

Loonud meeskond i_pupi, Itaalia

```python
c = (0, 0, 0) # Black
a = (255, 255, 255) # white
t = (255, 140, 0) # dark orange

image = [
t, a, t, c, c, t, a, t,
t, a, t, c, c, t, a, t,
t, t, t, t, t, t, t, t,
t, a, c, t, t, c, a, t,
t, t, t, t, t, t, t, t,
a, a, a, c, c, a, a, a,
c, a, a, a, a, a, a, c,
c, c, a, a, a, a, c, c]
```

--- /collapse ---


--- collapse ---

---
pealkiri: Elevant
---

![8 x 8 ruuduga võre, millel on kujutatud elevanti.](images/elephant.png)

Loonud meeskond ILiFanT, Soome

```python
c = (0, 0, 0) # Black
b = (105, 105, 105) # dark grey
a = (255, 255, 255) # white

image = [
    c, c, c, c, c, c, c, c,
    c, b, b, b, c, c, c, c,
    c, b, c, b, c, c, b, b,
    c, b, c, c, c, b, b, b,
    c, b, b, c, c, b, c, b,
    c, b, b, b, b, b, b, b,
    c, c, b, b, a, b, b, b,
    c, c, c, c, a, b, b, b]
```

--- /collapse ---

--- collapse ---
---
title: Lill
---

![8 x 8 ruuduga võre, millel on kujutatud kaktus.](images/cactus.png)

Loonud meeskond 6TETHASI, Holland

```python
a = (255, 255, 255) # White
c = (0, 0, 0) # Black
n = (154, 205, 50) # YellowGreen
q = (255, 255, 0) # Yellow
t = (255, 140, 0) # DarkOrange

image = [   
  q, q, c, n, c, c, a, c,
  q, c, c, n, c, a, a, a,
  c, n, c, n, c, c, c, c,
  c, n, n, n, c, n, c, c,
  c, a, n, n, n, n, c, c,
  a, a, a, n, c, a, a, a,
  c, c, c, n, a, a, a, c,
  t, t, t, t, t, t, t, t]

```

--- /collapse ---


--- collapse ---
---
title: Krokodill
---

![8 x 8 ruuduga võre, millel on kujutatud krokodilli pead.](images/croc.png)

```python

a = (255, 255, 255) # White
c = (0, 0, 0) # Black
f = (25, 25, 112) # MidnightBlue
m = (34, 139, 34) # ForestGreen

image = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

```

--- /collapse ---

--- collapse ---
---
pealkiri: Vikerkaar
---

![8 x 8 ruuduga võre, millel on kujutatud vikerkaart.](images/rainbow.png)

Loonud meeskond camrus_6, Ühendkuningriik

```python

c = (100, 149, 237) # CornflowerBlue
a = (255, 255, 255) # White
v = (255, 0, 0) # Red
t = (255, 140, 0) # DarkOrange
q = (255, 255, 0) # Yellow
l = (0, 255, 127) # SpringGreen
e = (0, 0, 205) # MediumBlue

rainbow = [
  c, c, c, c, c, c, c, c, 
  v, v, v, v, c, c, c, c,
  t, t, t, t, v, v, c, c,
  q, q, q, q, t, v, c, c,
  l, l, l, l, q, t, v, c,
  e, e, e, l, q, t, v, c,
  c, c, e, a, a, a, a, c,
  c, a, a, a, a, a, a, a
]

```

--- /collapse ---

--- collapse ---
---
pealkiri: Draakon
---

![8 x 8 ruuduga võre, millel on kujutatud draakonit.](images/dragon.png)

pilt = [ c, a, a, c, a, a, c, c, c, a, c, c, a, c, c, c, c, v, c, c, v, c, c, c, c, v, c, c, v, c, c, c, v, v, v, v, v, c, v, v, v, v, c, c, v, v, v, c, v, v, v, v, v, c, v, v, v, c, v, c, v, c, c, c]

```python

b = (105, 105, 105) # DimGray
c = (0, 0, 0) # Black
d = (100, 149, 237) # CornflowerBlue
v = (255, 0, 0) # Red
z = (153, 50, 204) # DarkOrchid

image = [
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

--- /task ---

--- task ---

**Leia:** rida, mis ütleb `# Kuva pilt` ja lisa koodirida, et kuvada oma pilt LED-maatriksil:

```python
a = (255, 255, 255) # White
c = (0, 0, 0) # Black
f = (25, 25, 112) # MidnightBlue
m = (34, 139, 34) # ForestGreen

image = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

# Display the image 
sense.set_pixels(image)

```

--- /task ---

--- task ---

Vajuta **Käivita** redaktori allosas, et näha oma pilti LED-maatriksil kuvatuna.

--- /task ---

--- task ---

**Silumine**

Minu koodis on süntaksiviga:

- Kontrolli, kas sinu kood ühtib ülaltoodud näidetes oleva koodiga
- Kontrolli, kas oled oma loendis koodi taandanud
- Kontrolli, kas sinu loend on ümbritsetud `[` ja `]`-ga
- Kontrollige, kas iga värvi muutuja on loendis komaga eraldatud

Minu pilt ei ilmu:

- Kontrolli, ega sinu `sense.set_pixels(image)` ei ole taandega

--- /task ---


--- task ---

**Salvesta oma edusammud**

Nüüd, kui oled pildi kuvanud, saad oma programmi salvestada Mission Starter projekti, sisestades oma meeskonna nime, meeskonnaliikmete nimed ja sulle antud klassiruumi koodi. Saad oma programmi uuesti laadida mis tahes internetiühendusega seadmesse, sisestades oma meeskonna nime ja klassiruumi koodi.

![Mission Zero salvestusnupp](images/savebutton.png)

--- /task --- 
