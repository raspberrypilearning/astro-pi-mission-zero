## Kuva pilt

Astro Pi LED-maatriksid suudavad kuvada ka värve. Selles etapis kuvad Astro Pi LED-maatriksil pilte loodusest.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED-maatriks**</span> on LED-ide võre, mida saab juhtida üksikult või rühmana, et luua erinevaid valgusefekte. Sense HAT-i LED-maatriksil on 64 LED-i, mis kuvatakse 8 x 8 võrena. LED-e saab programmeerida tootma laias valikus värve.
</p>

![Emulaatori akna kuvatõmmis, mis näitab lennuüksust, LED-maatriks kuvamas pilti lillest.](images/fu-pic.png)

--- task ---

Ava [Mission Zero stardiprojekt](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"}.

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

![Sense HAT-i emulaatori kuvatõmmis algkoodi ridadega, kuvatud vasakus paanis.](images/sense-hat-emulator3.png)

--- /task ---

### RGB värvid

Värve saab luua kasutades erinevaid punase, rohelise ja sinise proportsioone. RGB värvide kohta saad rohkem teada siin:

[[[generic-theory-simple-colours]]]

LED-maatriks on 8x8-ruudustik. Iga võre LED-i saab seadistada erinevat värvi. Siin on 24 erineva värvi muutujate loend. Igal värvil on väärtus punase, rohelise ja sinise jaoks:

[[[ambient-colours]]]

### Vali pilt

--- task ---

**Vali:** Vali allolevatest variantidest pilt, mida kuvada. Python salvestab pildi teabe loendisse. Iga pildi kood sisaldab kasutatud värvide muutujaid ja loendit.

Pead **kopeerima** kogu valitud pildi koodi ja seejärel **kleepima** selle oma projekti selle rea alla, mis ütleb `# Lisa värvi muutujad ja pilt`.

--- collapse ---

---
title: Rebane
---

![8 x 8 ruuduga võre, mis näitab rebase nägu.](images/fish.png)

Loonud meeskond i_pupi, Itaalia

```python
c = (0, 0, 0) # Must
a = (255, 255, 255) # Valge
t = (255, 140, 0) # Tumeoranž

pilt = [
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
title: Elevant
---

![8 x 8 ruuduga võre, millel on kujutatud elevanti.](images/walrus.png)

Loonud meeskond ILiFanT, Soome

```python
c = (0, 0, 0) # Must
b = (105, 105, 105) # Tumehall
a = (255, 255, 255) # Valge

pilt = [
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
title: Paxi
---

![8 x 8 ruuduga võre, millel on kujutatud kaktus.](images/paxi.png)

Loonud meeskond 6TETHASI, Holland

```python
a = (255, 255, 255) # Valge
c = (0, 0, 0) # Must
n = (154, 205, 50) # Kollakasroheline
q = (255, 255, 0) # Kollane
t = (255, 140, 0) # Tumeoranž

pilt = [   
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

![8 x 8 ruuduga võre, millel on kujutatud krokodilli pead.](images/dog.png)

Created by team ptpr_07, Spain

```python

a = (255, 255, 255) # Valge
c = (0, 0, 0) # Must
f = (25, 25, 112) # MidnightBlue
m = (34, 139, 34) # Metsaroheline

pilt = [
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
title: Vikerkaar
---

![A grid with 8 x 8 squares showing a rainbow-coloured chameleon.](images/chameleon.png)

Created by team The_ETs, United Kingdom

```python

c = (100, 149, 237) # Rukkilillesinine
a = (255, 255, 255) # Valge
v = (255, 0, 0) # Punane
t = (255, 140, 0) # Tumeoranž
q = (255, 255, 0) # Kollane
l = (0, 255, 127) # Kevadroheline
e = (0, 0, 205) # MediumBlue

vikerkaar = [
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
title: Draakon
---

![A grid with 8 x 8 squares showing a kite.](images/kite.png)

Created by team Val, Greece

```python

b = (105, 105, 105) # Tuhmhall
c = (0, 0, 0) # Must
d = (100, 149, 237) # Rukkilillesinine
v = (255, 0, 0) # Punane
z = (153, 50, 204) # Tume orhidee

pilt = [
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

![A grid with 8 x 8 squares showing a chicken.](images/chicken.png)

Created by team Slepicky, Czechia

```python

a = (255, 255, 255) # Valge
c = (0, 0, 0) # Must
f = (25, 25, 112) # MidnightBlue
m = (34, 139, 34) # Metsaroheline

pilt = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

# Kuva pilt
sense.set_pixels(pilt)

```

--- /collapse ---

--- /task ---

--- task ---

**Find:** the line that says `# Display the image` and add a line of code to display your image on the LED matrix:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 18, 19
---
z = (153, 50, 204) # DarkOrchid q = (255, 255, 0) # Yellow d = (51, 153, 255) # blue c = (0, 0, 0) # Black

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

# Kuva pilt
sense.set_pixels(image)

--- /code ---

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

![The Mission Zero Save button.](images/mz_savebutton_v2.png)

--- /task --- 
