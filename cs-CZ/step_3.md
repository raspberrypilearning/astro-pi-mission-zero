## Zobraz obrázek

LED obrazovka počítače Astro Pi umí zobrazovat barvy. V tomto kroku zobrazíš obrázky přírody na LED obrazovce počítače Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED matice**</span> je mřížka osazená LED diodami, které můžeš ovládat jednotlivě nebo jako skupinu, a můžeš tak docílit různých světelných efektů. LED matice na desce Sense HAT má 64 LED diod v mřížce o velikosti 8 × 8. Tyto LED diody můžeš naprogramovat tak, aby vyprodukovaly širokou škálu barev.
</p>

![Snímek obrazovky emulátoru, který zobrazuje letovou jednotku s LED maticí zobrazující obrázek kytičky.](images/fu-pic.png)

--- task ---

Otevři [startovací projekt výzvy Mission Zero](http://rpf.io/mzcode){:target="_blank"}.

Uvidíš pár řádků kódu, které tam už budou automaticky přichystané.

Tento kód slouží k připojení k počítači Astro Pi a zajistí, že se jeho LED displej bude zobrazovat správně, a také nastavuje senzor barev. Ten kód tam nech, protože ho budeš potřebovat.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Importuj knihovny
from sense_hat import SenseHat from time import sleep

# Nastav Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Nastav senzor barev
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Snímek obrazovky emulátoru Sense HAT s několika řádky startovacího kódu zobrazeným v levém panelu.](images/sense-hat-emulator2.png)

--- /task ---

### Barvy RGB

Barvy se dají vytvořit pomocí různých poměrů červené, zelené a modré. O barvách RGB se můžeš dozvědět zde:

[[[generic-theory-simple-colours]]]

LED matice je mřížka o velikost 8 × 8. Každou LED diodu na mřížce lze nastavit na jinou barvu. Tady je seznam proměnných pro 24 různých barev. Každá barva obsahuje hodnotu pro červenou, zelenou a modrou:

[[[ambient-colours]]]

### Vyber obrázek

--- task ---

**Vyber:** Zvol si obrázek, který chceš zobrazit, z příkladů uvedených níže. Python ukládá informaci o obrázku do seznamu. Kód každého obrázku obsahuje proměnné použitých barev a samotný seznam.

Budeš muset **zkopírovat** celý kód tebou zvoleného obrázku a **vložit** ho do svého projektu pod řádek, na kterém je napsáno `# Přidej proměnné s barvami a obrázek`.

--- collapse ---

---
title: Fox
---

![A grid with 8 x 8 squares showing a fox face.](images/fox_mz3.png)

Created by team i_pupi, Italy

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
title: Elephant
---

![A grid with 8 x 8 squares showing an elephant.](images/elephant.png)

Created by team ILiFanT, Finland

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
title: Cactus
---

![A grid with 8 x 8 squares showing a cactus.](images/cactus.png)

Created by team 6TETHASI, The Netherlands

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
title: Krokodýl
---

![Mřížka o velikosti 8 × 8, na které je hlava krokodýla.](images/croc.png)

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
title: Rainbow
---

![A grid with 8 x 8 squares showing a rainbow.](images/rainbow.png)

Created by team camrus_6, United Kingdom

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
title: Dragon
---

![A grid with 8 x 8 squares showing a dragon.](images/dragon.png)

Created by team hwplucyr, United Kingdom

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

**Najdi:** řádek, na kterém je napsáno `# Zobraz obrázek` a přidej řádek kódu, který zobrazí tvůj obrázek na LED matici:

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

Klepni na tlačítko **Spustit** v dolní části editoru a tvůj obrázek se zobrazí na LED matici.

--- /task ---

--- task ---

**Ladění**

Můj kód má chyby v syntaxi:

- Zkontroluj si, jestli tvůj kód odpovídá kódu v příkladech uvedených výše.
- Zkontroluj si, jestli je tvůj kód seznamu správně odsazený.
- Zkontroluj si, jestli je tvůj seznam ohraničený závorkami `[` a `]`.
- Zkontroluj si, jestli je každá proměnná s barvou oddělená čárkou.

Neukazuje se mi obrázek:

- Zkontroluj si, jestli řádek `sense.set_pixels(image)` není odsazený.

--- /task ---


--- task ---

**Save your progress**

Now that you have displayed an image, you can save your program on the Mission Starter project by entering your team name, team members' names, and the classroom code given to you. You can reload your program on any device with an internet connection by entering your team name and classroom code.

![Mission Zero Save button](images/savebutton.png)

--- /task --- 
