## Zobrazenie obrázka

LED matrica počítača Astro Pi môže zobrazovať farby. V tomto kroku zobrazíš obrázky z prírody na LED matrici počítača Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED matrica**</span> je mriežka LED diód, ktoré možno ovládať jednotlivo alebo ako skupinu a vytvárať tak rôzne svetelné efekty. LED matrica LED na module Sense HAT má 64 LED diód zobrazených v mriežke 8 x 8. LED diódy môžu byť naprogramované tak, aby produkovali širokú škálu farieb.
</p>

![Snímka obrazovky okna emulátora zobrazujúca letovú jednotku s LED maticou zobrazujúcou obrázok kvetu.](images/fu-pic.png)

--- task ---

Otvor [úvodný projekt Mission Zero](https://missions.astro-pi.org/sk/mz/code_submissions/new){:target="_blank"}.

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

![Snímka obrazovky emulátora modulu Sense HAT s riadkami úvodného kódu zobrazenými v ľavom paneli.](images/sense-hat-emulator2.png)

--- /task ---

### RGB farby

Farby môžu byť vytvorené pomocou rôznych pomerov červenej, zelenej a modrej. Viac informácií o RGB farbách nájdeš tu:

[[[generic-theory-simple-colours]]]

LED matrica je mriežka 8 x 8. Každá LED dióda na mriežke môže byť nastavená na inú farbu. Tu je zoznam premenných pre 24 rôznych farieb. Každá farba má hodnotu pre červenú, zelenú a modrú:

[[[ambient-colours]]]

### Vyber obrázok

--- task ---

**Vyber:** z možností nižšie vyber obrázok, ktorý sa má zobraziť. Program Python uloží informácie o obrázku do zoznamu. Kód pre každý obrázok obsahuje použité farebné premenné a zoznam.

Budeš musieť **skopírovať** celý kód pre zvolený obrázok a potom ho **prilepiť** do svojho projektu pod riadok s textom `# Pridajte farebné premenné a obrázok`.

--- collapse ---

---
title: Líška
---

![Mriežka s 8 x 8 štvorcami zobrazujúca tvár líšky.](images/fox_mz3.png)

Autor: tím i_pupi, Taliansko

```python
c = (0, 0, 0) # Čierna
a = (255, 255, 255) # Biela
t = (255, 140, 0) # Tmavooranžová
obrazok = [
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
title: Slon
---

![Mriežka s 8 x 8 štvorcami zobrazujúca slona.](images/elephant.png)

Autor: tím ILiFanT, Fínsko

```python
c = (0, 0, 0) # Čierna
b = (105, 105, 105) # Tmavosivá
a = (255, 255, 255) # Biela

obrazok = [
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
title: Kaktus
---

![Mriežka s 8 x 8 štvorcami zobrazujúca kaktus.](images/cactus.png)

Autor: tím 6TETHASI, Holandsko

```python
a = (255, 255, 255) # Biela
c = (0, 0, 0) # Čierna
n = (154, 205, 50) # Žltozelená
q = (255, 255, 0) # Žltá
t = (255, 140, 0) # Tmavooranžová

obrazok = [   
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
title: Krokodíl
---

![Mriežka s 8 x 8 štvorcami zobrazujúcimi krokodíliu hlavu.](images/croc.png)

```python

a = (255, 255, 255) # Biela
c = (0, 0, 0) # Čierna
f = (25, 25, 112) # Polnočná modrá
m = (34, 139, 34) # Lesná zelená

obrazok = [
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
title: Dúha
---

![Mriežka s 8 x 8 štvorcami zobrazujúcimi dúhu.](images/rainbow.png)

Autor: tím camrus_6, Spojené kráľovstvo

```python

c = (100, 149, 237) # Nevädzová modrá
a = (255, 255, 255) # Biela
v = (255, 0, 0) # Červená
t = (255, 140, 0) # Tmavooranžová
q = (255, 255, 0) # Žltá
l = (0, 255, 127) # Jarná zelená
e = (0, 0, 205) # Stredne modrá

duha = [
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
title: Drak
---

![Mriežka s 8 x 8 štvorcami zobrazujúcimi draka.](images/dragon.png)

Autor: tím hwplucyr, Spojené kráľovstvo

```python

b = (105, 105, 105) # Tmavosivá
c = (0, 0, 0) # Čierna
d = (100, 149, 237) # Nevädzová modrá
v = (255, 0, 0) # Červená
z = (153, 50, 204) # Tmavoorchideová

obrazok = [
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

**Nájdite:** riadok s textom `# Zobraziť obrázok` a pridajte riadok kódu na zobrazenie obrázka na matici LED:

```python
a = (255, 255, 255) # Biela
c = (0, 0, 0) # Čierna
f = (25, 25, 112) # Polnočná modrá
m = (34, 139, 34) # Lesná zelená

obrazok = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

# Zobraziť obrázok 
sense.set_pixels(obrazok)

```

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
- Skontrolujte, či sú jednotlivé farebné premenné v zozname oddelené čiarkou

Môj obrázok sa nezobrazuje:

- Skontroluj, či riadok `sense.set_pixels(image)` nie je odsadený

--- /task ---


--- task ---

**Ukladaj si priebeh**

Po zobrazení obrázka si môžeš svoj program uložiť do projektu Mission Starter zadaním názvu tímu, mien členov tímu a kódu triedy, ktorý si dostal/-a. Svoj program môžeš znova načítať na akomkoľvek zariadení s internetovým pripojením zadaním názvu tímu a kódu triedy.

![Tlačidlo Uložiť v Mission Zero](images/mz_savebutton_v2.png)

--- /task --- 
