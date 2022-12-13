## Kuva pilt

Astro Pi LED-maatriksid suudavad kuvada ka värve. Selles etapis kuvad Astro Pi LED-maatriksil pilte loodusest.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED-maatriks**</span> on LED-ide võre, mida saab juhtida üksikult või rühmana, et luua erinevaid valgusefekte. Sense HAT-i LED-maatriksil on 64 LED-i, mis kuvatakse 8 x 8 võrena. LED-e saab programmeerida tootma laias valikus värve.
</p>

![Emulaatori akna kuvatõmmis, mis näitab lennuüksust, LED-maatriks kuvamas pilti lillest.](images/fu-pic.png)

--- task ---

Ava [Mission Zero stardiprojekt](https://missions.astro-pi.org/cs/et/code_submissions/new){:target="_blank"}.

Näed, et sulle on automaatselt lisatud mõned read koodi.

See kood ühendub Astro Pi-ga ja tagab, et Astro Pi LED-ekraan kuvatakse õigesti ning unstallib värvianduri. Jäta kood sinna, sest sul läheb seda vaja.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
---
# Impordi teegid
from sense_hat import SenseHat
from time import sleep

# Installi Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Installi värviandur
sense.color.gain = 60 # Määra anduri tundlikkus
sense.color.integration_cycles = 64 # Intervall, millal näit võetakse

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
title: Kana
---

![8 x 8 ruuduga võre, mis näitab tibu munas.](images/chick.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # White
c = (0, 0, 0) # Black
e = (0, 0, 205) # MediumBlue
q = (255, 255, 0) # Yellow
t = (255, 140, 0) # DarkOrange
w = (255, 192, 203) # Pink

pilt = [
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
title: Lill
---

![8 x 8 ruuduga võre, millel on roosa lill rohelisel varrel.](images/flower.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
c = (0, 0, 0) # Black
m = (34, 139, 34) # ForestGreen
q = (255, 255, 0) # Yellow
t = (255, 140, 0) # DarkOrange
y = (255, 20, 147) # DeepPink

pilt = [
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
title: Krabi
---

![8 x 8 ruuduga võre, millel on kujutatud krabi.](images/crab.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # White
c = (0, 0, 0) # Black
v = (255, 0, 0) # Red

pilt = [
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
title: Krokodill
---

![8 x 8 ruuduga võre, millel on kujutatud krokodilli pead.](images/croc.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # White
c = (0, 0, 0) # Black
f = (25, 25, 112) # MidnightBlue
m = (34, 139, 34) # ForestGreen

pilt = [
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
title: Madu
---

![8 x 8 ruuduga võre, millel on kujutatud madu.](images/snake.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
 c = (0, 0, 0) # Black
 m = (34, 139, 34) # ForestGreen
 q = (255, 255, 0) # Yellow
 v = (255, 0, 0) # Red

pilt = [
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
title: Konn
---

![8 x 8 ruuduga võre, millel on kujutatud konn.](images/frog.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
c = (0, 0, 0) # Black
m = (34, 139, 34) # ForestGreen
q = (255, 255, 0) # Yellow
v = (255, 0, 0) # Red

pilt = [
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

**Leia:** rida, mis ütleb `# Kuva pilt` ja lisa koodirida, et kuvada oma pilt LED-maatriksil:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 12
---
pilt = [
  c, c, c, q, q, q, c, c,
  c, c, t, q, e, q, c, c,
  c, c, c, q, q, q, c, c,
  c, w, w, w, w, w, w, c,
  c, w, a, a, a, a, w, c,
  c, w, a, a, a, a, w, c,
  c, c, w, a, a, w, c, c,
  c, c, c, w, w, c, c, c]

# Kuva pilt 
sense.set_pixels(pilt)

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

- Kontrolli, ega sinu `sense.set_pixels(pilt)` ei ole taandega

--- /task ---



