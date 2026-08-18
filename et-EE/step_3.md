## Kuva pilt

Kuvatav pilt koosneb 64 värvilisest ruudust, mida nimetatakse **piksliteks**. Pikslid on paigutatud 8 x 8 ruudustikku. Iga piksel võib olla erinevat värvi. Värve hoolikalt valides saate luua soovitud pildi. Siin on näide vaalast, mis on valmistatud mustal taustal erinevate sinise varjundite abil.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED-maatriks**</span> on LED-ide võre, mida saab juhtida üksikult või rühmana, et luua erinevaid valgusefekte. Sense HAT-i LED-maatriksil on 64 LED-i, mis kuvatakse 8 x 8 võrena. LED-e saab programmeerida tootma laias valikus värve.
</p>

![8x8 vaala pilt, millel on tähed, mis tähistavad erinevaid värve](images/whale.png)

Pane tähele, et iga ruut on tähistatud koodiga, mis tähistab konkreetset värvi. Sellel pildil on kasutatud kolme värvi:
+ c = must
+ f = ookeanisinine
+ g = taevasinine


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

![Kolm liugurit, mis näitavad RGB värviväärtusi](images/rgbsliders.gif)

LED-maatriks on 8x8-ruudustik. Iga võre LED-i saab seadistada erinevat värvi. Muutujate nimedena saame kasutada tähti a kuni z, mis tähistavad 24 erinevat värvi. Igal värvil on väärtus punase, rohelise ja sinise jaoks.

--- collapse ---

---
title: Värvimuutujate loend
---

![24 värvilisest ruudust koosnev ruudustik, millest igaüks on tähistatud erineva tähestiku tähega](images/palette.png)

```python
a = (255, 255, 255) # Valge
b = (171, 171, 171) # Hall
c = (0, 0, 0) # Must
d = (25, 25, 113) # Tumesinine
e = (0, 0, 255) # Puhas sinine
f = (36, 128, 200) # Ookeanisinine
g = (0, 204, 255) # Taevasinine
h = (86, 255, 255) # Elektriline tsüaansinine
j = (0, 255, 0) # Puhas roheline
k = (46, 139, 33) # Leheroheline
l = (57, 97, 17) # Oliivroheline
m = (30, 65, 6) # Metsaroheline
n = (126, 88, 25) # Maapruun
o = (179, 96, 65) # Terrakotapruun
p = (180, 34, 34) # Telliskivipunane
q = (255, 0, 0) # Puhas punane
r = (232, 118, 5) # Oranž
s = (241, 231, 100) # Kahvatukollane
t = (255, 255, 0) # Puhas kollane
u = (255, 209, 209) # Kahvaturoosa
v = (255, 177, 177) # Punakasroosa
w = (249, 169, 255) # Heleroosa
y = (248, 97, 255) # Magenta
z = (220, 53, 232) # Lilla

```

--- /collapse ---

### Vali pilt

--- task ---

**Vali:** Vali allolevatest variantidest pilt, mida kuvada. Python salvestab pildi teabe loendisse. Iga pildi kood sisaldab kasutatud värvide muutujaid ja loendit.

Pead **kopeerima** kogu valitud pildi koodi ja seejärel **kleepima** selle oma projekti selle rea alla, mis ütleb `# Lisa värvi muutujad ja pilt`.

--- collapse ---

---
title: Vaal
---

![8 x 8 ruuduga ruudustik, mis kujutab vaala.](images/whale.png)

Loonud Team Naicom, Itaalia

```python
c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue

image = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, a,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

```

--- /collapse ---


--- collapse ---

---
title: Sidrun
---

![Ruudustik 8 x 8 ruutudega, millel on kujutatud sidrun.](images/lemon.png)

Loonud meeskond g4lemoni, Kreeka

```python
c = (0, 0, 0)       # Black
k = (46, 139, 33)   # Leaf Green
t = (255, 255, 0)   # Pure Yellow

image = [
c, c, c, k, k, c, c, c,
c, c, k, c, k, c, c, c,
c, k, c, t, t, c, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, c, t, t, c, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Siga
---

![8 x 8 ruuduga ruudustik, millel on kujutatud siga.](images/pig.png)

Loonud Gary, Ühendkuningriik

```python
a = (255, 255, 255) # White
v = (255, 177, 177) # Blush Pink
y = (248, 97, 255)  # Magenta
o = (179, 96, 65)   # Terracotta Brown
c = (0, 0, 0)       # Black

image = [
a, a, y, a, a, y, a, a,
a, y, y, y, y, y, y, a,
a, y, c, y, c, y, y, y,
v, v, v, v, v, y, y, y,
v, o, v, o, v, y, y, y,
v, v, v, v, v, y, y, y,
a, y, y, y, y, y, y, y,
a, a, y, a, a, a, y, a]

```

--- /collapse ---


--- collapse ---
---
title: Torm
---

![8 x 8 ruuduga ruudustik, mis kujutab tormipilve.](images/storm.png)

Loonud meeskond hop2p023, Hispaania

```python

c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue
t = (255, 255, 0)   # Pure Yellow

image = [
c, c, c, c, c, c, c, c,
c, c, f, f, f, f, c, c,
c, f, f, f, f, f, f, c,
c, g, c, g, t, g, c, c,
c, c, c, t, t, c, c, c,
c, c, t, t, c, c, c, c,
c, c, g, c, c, c, c, g,
c, g, c, c, c, c, c, c]


```

--- /collapse ---

--- collapse ---
---
title: Part
---

![8 x 8 ruuduga ruudustik, millel on kujutatud parti.](images/duck.png)

Loonud Peter, Iirimaa

```python

c = (0, 0, 0) # Black
l = (57, 97, 17)    # Olive Green
m = (30, 65, 6)     # Forest Green
r = (232, 118, 5)   # Orange
a = (255, 255, 255) # White
b = (171, 171, 171) # Grey

image = [
c, l, l, c, c, c, c, c,
r, r, m, c, c, c, c, c,
c, l, l, c, c, c, c, c,
c, a, a, l, a, a, c, c,
c, l, l, a, a, a, b, a,
c, a, a, b, b, b, a, a,
c, c, a, a, a, a, c, c,
c, c, c, r, c, r, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Konn
---

![8 x 8 ruuduga ruudustik, millel on kujutatud konna.](images/frog.png)

Loodud meeskond Jmeno, Tšehhi Vabariik

```python

a = (255, 255, 255) # White
b = (171, 171, 171) # Grey
c = (0, 0, 0)       # Black
q = (255, 0, 0)     # Pure Red
j = (0, 255, 0)     # Pure Green
k = (46, 139, 33)   # Leaf Green
n = (126, 88, 25)   # Earth Brown

image = [
a, a, a, a, a, a, a, a,
a, a, a, a, a, b, a, b,
a, a, a, a, a, a, c, a,
a, a, c, a, c, a, q, a,
a, a, j, j, j, q, a, a,
a, j, j, k, q, a, a, a,
j, k, j, k, k, a, a, a,
k, k, k, j, k, n, n, n]

```

--- /collapse ---

--- collapse ---
---
title: Õitepuu
---

![8 x 8 ruuduga ruudustik, mis kujutab õitsvat puud.](images/blossom.png)

Loonud meeskond Zssh14, Slovakkia

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

**Leia:** rida, mis ütleb `# Kuva pilt` ja lisa koodirida, et kuvada oma pilt LED-maatriksil:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, a, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

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

![Mission Zero salvestusnupp.](images/mz_savebutton_v2.png)

--- /task --- 
