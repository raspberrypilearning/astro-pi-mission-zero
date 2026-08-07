## Zobrazenie obrázka

Zobrazený obrázok bude vytvorený zo 64 farebných štvorcov nazývaných **pixely**. Pixely sú usporiadané v mriežke 8 x 8. Každý pixel môže byť inej farby. Starostlivým výberom farieb je možné vytvoriť obrázok. Tu je príklad veľryby vykreslenej v rôznych odtieňoch modrej na čiernom pozadí.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED matrica**</span> je mriežka LED diód, ktoré možno ovládať jednotlivo alebo ako skupinu a vytvárať tak rôzne svetelné efekty. LED matrica na module Sense HAT má 64 LED diód zobrazených v mriežke 8 x 8. LED diódy môžu byť naprogramované tak, aby produkovali širokú škálu farieb.
</p>

![obrázok veľryby s rozmermi 8x8 s písmenami označujúcimi rôzne farby](images/whale.png)

Všimni si, že každý štvorček je označený kódom, ktorý predstavuje konkrétnu farbu. Na tomto obrázku sú použité 3 farby:
+ c = čierna
+ f = morská modrá
+ g = nebeská modrá


--- task ---

Otvor [úvodný projekt Mission Zero](https://missions.astro-pi.org/sk/mz/code_submissions/){:target="_blank"}.

Automaticky sa ti pridá niekoľko riadkov kódu.

Tento kód sa pripája k počítaču Astro Pi, zaisťuje, že sa LED displej počítača Astro Pi zobrazuje správnym smerom, a nastavuje snímač farieb. Tento kód tam nechaj, pretože ho budeš potrebovať.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
---
# Importujte knižnice
from sense_hat import SenseHat
from time import sleep

# Nastavte Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Nastavte snímač farieb
sense.color.gain = 60 # Nastavte citlivosť snímača
sense.color.integration_cycles = 64 # Interval, v ktorom sa bude vykonávať snímanie

--- /code ---

![Snímka obrazovky emulátora modulu Sense HAT s riadkami úvodného kódu zobrazenými v ľavom paneli.](images/sense-hat-emulator3.png)

--- /task ---

### RGB farby

Farby môžu byť vytvorené pomocou rôznych pomerov červenej, zelenej a modrej. Viac informácií o RGB farbách nájdeš tu:

![Tri posuvníky znázorňujúce hodnoty farieb RGB](images/rgbsliders.gif)

LED matrica je mriežka 8 x 8. Každá LED dióda na mriežke môže byť nastavená na inú farbu. Písmená a až z môžeme použiť ako názvy premenných na znázornenie 24 rôznych farieb. Každá farba má hodnotu pre červenú, zelenú a modrú.

--- collapse ---

---
title: Zoznam farebných premenných
---

![Mriežka s 24 farebnými štvorcami, pričom každý je označený iným písmenom abecedy](images/palette.png)

```python
a = (255, 255, 255) # Biela
b = (171, 171, 171) # Sivá
c = (0, 0, 0) # Čierna
d = (25, 25, 113) # Námornícka modrá
e = (0, 0, 255) # Čistá modrá
f = (36, 128, 200) # Morská modrá
g = (0, 204, 255) # Nebeská modrá
h = (86, 255, 255) # Elektrická azúrová
j = (0, 255, 0) # Čistá zelená
k = (46, 139, 33) # Listová zelená
l = (57, 97, 17) # Olivovozelená
m = (30, 65, 6) # Lesná zelená
n = (126, 88, 25) # Zemitá hnedá
o = (179, 96, 65) # Terakotová hnedá
p = (180, 34, 34) # Tehlovočervená
q = (255, 0, 0) # Čistá červená
r = (232, 118, 5) # Oranžová
s = (241, 231, 100) # Svetložltá
t = (255, 255, 0) # Čistá žltá
u = (255, 209, 209) # Svetloružová
v = (255, 177, 177) # Ružová
w = (249, 169, 255) # Bledoružová
y = (248, 97, 255) # Purpurová
z = (220, 53, 232) # Fialová

```

--- /collapse ---

### Vyber obrázok

--- task ---

**Vyber:** Z možností nižšie vyber obrázok, ktorý sa má zobraziť. Program Python uloží informácie o obrázku do zoznamu. Kód pre každý obrázok obsahuje použité farebné premenné a zoznam.

Budeš musieť **skopírovať** celý kód pre zvolený obrázok a potom ho **prilepiť** do svojho projektu pod riadok s textom `# Pridajte farebné premenné a obrázok`.

--- collapse ---

---
title: Veľryba
---

![Mriežka s 8 x 8 štvorcami zobrazujúca veľrybu.](images/whale.png)

Autor: tím Naicom, Taliansko

```python
c = (0, 0, 0)       # Čierna
f = (36, 128, 200)  # Morská modrá
g = (0, 204, 255)   # Nebeská modrá

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
title: Citrón
---

![Mriežka s 8 x 8 štvorcami zobrazujúcimi citrón.](images/lemon.png)

Autor: tím g4lemoni, Grécko

```python
c = (0, 0, 0)       # Čierna
k = (46, 139, 33)   # Listová zelená
t = (255, 255, 0)   # Čistá žltá

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
title: Prasiatko
---

![Mriežka s 8 x 8 štvorcami zobrazujúcimi prasiatko.](images/pig.png)

Autor: Gary, Spojené kráľovstvo

```python
a = (255, 255, 255) # Biela
v = (255, 177, 177) # Ružová
y = (248, 97, 255)  # Purpurová
o = (179, 96, 65)   # Terakotová hnedá
c = (0, 0, 0)       # Čierna

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
title: Búrka
---

![Mriežka s 8 x 8 štvorcami zobrazujúcimi búrkový oblak.](images/storm.png)

Autor: tím hop2p023, Španielsko

```python

c = (0, 0, 0)       # Čierna
f = (36, 128, 200)  # Morská modrá
g = (0, 204, 255)   # Nebeská modrá
t = (255, 255, 0)   # Čistá žltá

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
title: Kačica
---

![Mriežka s 8 x 8 štvorcami zobrazujúcimi kačicu.](images/duck.png)

Autor: Peter, Írsko

```python

c = (0, 0, 0) # Čierna
l = (57, 97, 17)    # Olivovo zelená
m = (30, 65, 6)     # Lesná zelená
r = (232, 118, 5)   # Oranžová
a = (255, 255, 255) # Biela
b = (171, 171, 171) # Sivá

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
title: Žaba
---

![Mriežka s 8 x 8 štvorcami zobrazujúcimi žabu.](images/frog.png)

Autor: tím Jméno, Česká republika

```python

a = (255, 255, 255) # Biela
b = (171, 171, 171) # Sivá
c = (0, 0, 0)       # Čierna
q = (255, 0, 0)     # Čistá červená
j = (0, 255, 0)     # Čistá zelená
k = (46, 139, 33)   # Listová zelená
n = (126, 88, 25)   # Zemitá hnedá

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
title: Kvitnúci strom
---

![Mriežka s 8 x 8 štvorcami zobrazujúca kvitnúci strom.](images/blossom.png)

Autor: tím Zssh14, Slovensko

```python

t = (255, 255, 0)   # Čistá žltá
g = (0, 204, 255)   # Nebeská modrá
w = (249, 169, 255) # Bledoružová
y = (248, 97, 255)  # Purpurová
z = (220, 53, 232)  # Fialová
n = (126, 88, 25)   # Zemitá hnedá
o = (179, 96, 65)   # Terakotová hnedá
k = (46, 139, 33)   # Listová zelená

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

**Nájdi:** riadok s textom `# Zobraziť obrázok` a pridaj riadok kódu na zobrazenie obrázka na LED matrici:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Čierna
f = (36, 128, 200)  # Morská modrá
g = (0, 204, 255)   # Nebeská modrá

image = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, a,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

# Zobrazte obrázok
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Stlačením tlačidla **Spustiť** v dolnej časti editora zobrazíš obrázok zobrazený na LED matrici.

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
