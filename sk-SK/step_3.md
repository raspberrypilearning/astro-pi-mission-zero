## Zobraziť obrázok

Matrica LED Astro Pi môže zobrazovať farby. V tomto kroku zobrazíte obrázky z prírody na LED matrici Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED matrica**</span> je mriežka LED diód, ktoré možno ovládať jednotlivo alebo ako skupinu a vytvárať tak rôzne svetelné efekty. Matrica LED na Sense HAT má 64 LED zobrazených v mriežke 8 x 8. LED diódy môžu byť naprogramované tak, aby produkovali širokú škálu farieb.
</p>

![Snímka obrazovky okna emulátora zobrazujúca letovú jednotku s maticou LED zobrazujúcou obrázok kvetu.](images/fu-pic.png)

--- task ---

Otvorte [úvodný projekt Mission Zero](http://rpf.io/mzcode){:target="_blank"}.

Uvidíte, že sa vám automaticky pridalo niekoľko riadkov kódu.

Tento kód sa pripája k počítaču Astro Pi, zaisťuje, že sa LED displej Astro Pi zobrazuje správnym smerom a nastavuje snímač farieb. Tento kód nechajte na mieste, pretože ho budete potrebovať.

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
sense.color.integration_cycles = 64 # Interval, v ktorom sa bude realizovať snímanie

--- /code ---

![Snímka obrazovky emulátora Sense HAT s riadkami štartovacieho kódu zobrazenými v ľavom paneli.](images/sense-hat-emulator2.png)

--- /task ---

### RGB farby

Farby môžu byť vytvorené pomocou rôznych pomerov červenej, zelenej a modrej. O farbách RGB sa môžete dozvedieť tu:

[[[generic-theory-simple-colours]]]

Matrica LED je mriežka 8 x 8. Každá LED na mriežke môže byť nastavená na inú farbu. Tu je zoznam premenných pre 24 rôznych farieb. Každá farba má hodnotu pre červenú, zelenú a modrú:

[[[ambient-colours]]]

### Vyberte obrázok

--- task ---

**Vyberte:** z možností nižšie vyberte obrázok, ktorý sa má zobraziť. Program Python uloží informácie o obrázku do zoznamu. Kód pre každý obrázok obsahuje použité farebné premenné a zoznam.

Budete musieť **skopírovať** celý kód pre zvolený obrázok a potom ho **prilepiť** do svojho projektu pod riadok ktorý znie `# Pridajte farebné premenné a obrázok`.

--- collapse ---

---
title: Kuriatko
---

![Mriežka s 8 x 8 štvorcami zobrazujúca kuriatko vo vajci.](images/chick.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Biela
c = (0, 0, 0) # Čierna
e = (0, 0, 205) # StČervenáne modrá
q = (255, 255, 0) # Žltá
t = (255, 140, 0) # Tmavo oranžová
w = (255, 192, 203) # Ružová

obrazok = [
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
title: Kvet
---

![Mriežka s 8 x 8 štvorcami zobrazujúca ružový kvet na zelenej stonke.](images/flower.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
c = (0, 0, 0) # Čierna
m = (34, 139, 34) # Lesná zelená
q = (255, 255, 0) # Žltá
t = (255, 140, 0) # Tmavo oranžová
y = (255, 20, 147) # Tmavo ružová

obrazok = [
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
title: Krab
---

![Mriežka s 8 x 8 štvorcami zobrazujúcimi kraba.](images/crab.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Biela
c = (0, 0, 0) # Čierna
v = (255, 0, 0) # Červená

obrazok = [
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
title: Krokodíl
---

![Mriežka s 8 x 8 štvorcami zobrazujúcimi krokodíliu hlavu.](images/croc.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
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

--- /code ---


--- /collapse ---

--- collapse ---
---
title: Had
---

![Mriežka s 8 x 8 štvorcami zobrazujúcimi hada.](images/snake.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
 c = (0, 0, 0) # Čierna
 m = (34, 139, 34) # Lesná zelená
 q = (255, 255, 0) # Žltá
 v = (255, 0, 0) # Červená

obrazok = [
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
title: Žaba
---

![Mriežka s 8 x 8 štvorcami zobrazujúcimi žabu.](images/frog.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
c = (0, 0, 0) # Čierna
m = (34, 139, 34) # Lesná zelená
q = (255, 255, 0) # Žltá
v = (255, 0, 0) # Červená

obrazok = [
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

**Nájdite:** riadok s textom `# Zobraziť obrázok` a pridajte riadok kódu na zobrazenie obrázka na matici LED:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 12
---

obrazok = [
  c, c, c, q, q, q, c, c,
  c, c, t, q, e, q, c, c,
  c, c, c, q, q, q, c, c,
  c, w, w, w, w, w, w, c,
  c, w, a, a, a, a, w, c,
  c, w, a, a, a, a, w, c,
  c, c, w, a, a, w, c, c,
  c, c, c, w, w, c, c, c]

# Zobrazte obrázok 
sense.set_pixels(obrazok)

--- /code ---

--- /task ---

--- task ---

Stlačením tlačidla **Spustiť** v dolnej časti editora zobrazíte obrázok zobrazený na matici LED.

--- /task ---

--- task ---

**Ladenie**

Môj kód má chybu syntaxe:

- Skontrolujte, či sa váš kód zhoduje s kódom v príkladoch vyššie
- Skontrolujte, či ste odsadili kód vo svojom zozname
- Skontrolujte, či je váš zoznam obklopený znakmi `[` a `]`
- Skontrolujte, či sú jednotlivé farebné premenné v zozname oddelené čiarkou

Môj obrázok sa nezobrazuje:

- Skontrolujte, či váš `sense.set_pixels(obrazok)` nie je odsadený

--- /task ---



