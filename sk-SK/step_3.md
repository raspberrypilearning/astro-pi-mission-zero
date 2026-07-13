## Zobrazenie obrázka

The image you display will be made from 64 coloured squares called **pixels**. The pixels are arranged in an 8 x 8 grid. Each pixel can be a different colour. By choosing the colours carefully, you can create a picture. Here is an example of a whale made using different shades of blue on a black background.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED matrica**</span> je mriežka LED diód, ktoré možno ovládať jednotlivo alebo ako skupinu a vytvárať tak rôzne svetelné efekty. LED matrica na module Sense HAT má 64 LED diód zobrazených v mriežke 8 x 8. LED diódy môžu byť naprogramované tak, aby produkovali širokú škálu farieb.
</p>

![Snímka obrazovky okna emulátora zobrazujúca letovú jednotku s LED maticou zobrazujúcou obrázok kvetu.](images/whale.png)

Notice that each square is labelled with a code to represent a particular colour. In this image 3 colours are used:
+ Skontroluj, či sa kód zhoduje s kódom v príkladoch vyššie
+ Skontroluj, či máš kód vo svojom zozname odsadený
+ Skontroluj, či je zoznam uzavretý v znakoch `[` a `]`


--- task ---

Otvor [úvodný projekt Mission Zero](https://missions.astro-pi.org/sk/mz/code_submissions/){:target="_blank"}.

Automaticky sa ti pridá niekoľko riadkov kódu.

Tento kód sa pripája k počítaču Astro Pi, zaisťuje, že sa LED displej počítača Astro Pi zobrazuje správnym smerom, a nastavuje snímač farieb. Tento kód tam nechaj, pretože ho budeš potrebovať.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Importujte knižnice
from sense_hat import SenseHat from time import sleep

# Nastavte Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Nastavte snímač farieb
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Snímka obrazovky emulátora modulu Sense HAT s riadkami úvodného kódu zobrazenými v ľavom paneli.](images/sense-hat-emulator3.png)

--- /task ---

### RGB farby

Farby môžu byť vytvorené pomocou rôznych pomerov červenej, zelenej a modrej. Viac informácií o RGB farbách nájdeš tu:

![Three sliders demonstrating RGB colour values](images/rgbsliders.gif)

LED matrica je mriežka 8 x 8. Každá LED dióda na mriežke môže byť nastavená na inú farbu. We can use the letters a to z as the names of variables to represent 24 different colours. Each colour has a value for red, green, and blue.

--- collapse ---

---
title: Ryba
---

![A grid of 24 coloured squared each labelled with a different letter of the alphabet](images/palette.png)

```python
z = (153, 50, 204) # Tmavoorchideová
q = (255, 255, 0) # Žltá
d = (51, 153, 255) # Modrá
c = (0, 0, 0) # Čierna

obrazok = [
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

### Vyber obrázok

--- task ---

**Vyber:** Z možností nižšie vyber obrázok, ktorý sa má zobraziť. Program Python uloží informácie o obrázku do zoznamu. Kód pre každý obrázok obsahuje použité farebné premenné a zoznam.

Budeš musieť **skopírovať** celý kód pre zvolený obrázok a potom ho **prilepiť** do svojho projektu pod riadok s textom `# Pridajte farebné premenné a obrázok`.

--- collapse ---

---
title: Mrož
---

![A grid with 8 x 8 squares showing a whale.](images/whale.png)

Created by Team Naicom, Italy

```python
h = (0, 255, 255) # Azúrová
c = (0, 0, 0) # Čierna
s = (139, 69, 19) # Sedlová hnedá
a = (255, 255, 255) # Biela
r = (184, 134, 11) # Tmavožltá

obrazok = [
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
v = (255, 0, 0) # Červená
m = (34, 139, 34) # Sýtozelená
c = (0, 0, 0) # Čierna
e = (100, 149, 237) # Nevädzová modrá
l = (0, 255, 0) # Zelená

obrazok = [
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
title: Pes
---

![A grid with 8 x 8 squares showing a pig.](images/pig.png)

Created by Gary, United Kingdom

```python
c = (0, 0, 0) # Čierna
r = (184, 134, 11) # Tmavožltá
s = (139, 69, 19) # Sedlová hnedá
y = (255, 20, 147) # Tmavoružová

obrazok = [
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
title: Chameleón
---

![A grid with 8 x 8 squares showing a storm cloud.](images/storm.png)

Created by team hop2p023, Spain

```python

c = (0, 0, 0) # Čierna
s = (139, 69, 19) # Sedlová hnedá
a = (255, 255, 255) # Biela
v = (255, 0, 0) # Červená
t = (255, 140, 0) # Tmavooranžová
q = (255, 255, 0) # Žltá
m = (34, 139, 34) # Sýtozelená
h = (0, 255, 255) # Azúrová
z = (153, 50, 204) # Tmavoorchideová
y = (255, 20, 147) # Tmavoružová

obrazok = [
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
title: Šarkan
---

![A grid with 8 x 8 squares showing a duck.](images/duck.png)

Created by Peter, Ireland

```python

c = (0, 0, 0) # Čierna
m = (34, 139, 34) # Sýtozelená
v = (255, 0, 0) # Červená
q = (255, 255, 0) # Žltá
e = (0, 0, 205) # Stredne modrá
h = (0, 255, 255) # Azúrová

obrazok = [
    h, h, h, h, h, h, h, h, 
    h, h, h, e, e, v, v, h, 
    h, h, h, e, e, v, v, h, 
    h, h, h, q, q, m, m, h, 
    h, h, h, q, q, m, m, h,
    h, h, c, h, h, h, h, h, 
    h, c, h, h, h, h, h, h, 
    c, h, h, h, h, h, h, h]

```

--- /collapse ---

--- collapse ---
---
title: Kuriatko
---

![A grid with 8 x 8 squares showing a Frog.](images/frog.png)

Created by team Jmeno, Czech Republic

```python

v = (255, 0, 0) # Červená
c = (0, 0, 0) # Čierna
b = (105, 105, 105) # Tmavosivá
q = (255, 255, 0) # Žltá
r = (184, 134, 11) # Tmavožltá

obrazok =  [
    c, c, v, v, v, c, c, c,
    c, v, b, b, r, c, c, r,
    c, b, c, b, b, c, r, b,
    q, r, b, b, b, b, b, r,
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

**Nájdite:** riadok s textom `# Zobraziť obrázok` a pridajte riadok kódu na zobrazenie obrázka na LED matrici:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, a, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

# Zobraziť obrázok
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Stlačením tlačidla **Spustiť** v dolnej časti editora zobrazíte obrázok zobrazený na LED matrici.

--- /task ---

--- task ---

**Ladenie**

Môj kód má chybu syntaxe:

- Skontroluj, či sa kód zhoduje s kódom v príkladoch vyššie
- Skontroluj, či máš kód vo svojom zozname odsadený
- Skontroluj, či je zoznam uzavretý v znakoch `[` a `]`
- Skontroluj, či sú jednotlivé farebné premenné v zozname oddelené čiarkou

Môj obrázok sa nezobrazuje:

- Skontroluj, či riadok `sense.set_pixels(image)` nie je odsadený

--- /task ---


--- task ---

**Ukladaj si priebeh**

Po zobrazení obrázka si môžeš svoj program uložiť do projektu Mission Starter zadaním názvu tímu, mien členov tímu a kódu triedy, ktorý si dostal/-a. Svoj program môžeš znova načítať na akomkoľvek zariadení s internetovým pripojením zadaním názvu tímu a kódu triedy.

![Tlačidlo Uložiť v Mission Zero.](images/mz_savebutton_v2.png)

--- /task --- 
