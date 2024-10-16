## Taju värvi

Selles etapis installid värvide helenduse anduri ja kasutad seda andurini jõudva punase, rohelise ja sinise koguse tuvastamiseks. Seda värvi kasutatakse seejärel sinu valitud pildi värvimiseks. Anduri juurde kõndiv sinises särgis astronaut näeks teistsugust pilti kui punases särgis astronaut.

![LED-maatriksil kuvatav roosa taustaga pilt](images/colour_background.png)

Mis tahes pildi sa valid, taust kasutab `c` muutujat, mis on seadistatud mustana.

--- task ---

Kasuta oma tausta värvimiseks värviandurit.

Andurilt värvi saamiseks lisa pildiloendi ette kood ja muuda oma `c` taustavärvi muutujat, et musta asemel kasutaks Sense HAT värvianduri tajutavat värvi.

**Näpunäide:** Sa ei pea sisestama "#"-ga algavaid kommentaare (need on koodi selgitamiseks).

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 9, 10
---

# Lisa värvi muutujad ja pilt

a = (255, 255, 255) # Valge
c = (0, 0, 0) # Must
f = (25, 25, 112) # MidnightBlue
m = (34, 139, 34) # Metsaroheline

rgb = sense.color # saa värv andurilt
c = (rgb.red, rgb.green, rgb.blue) # kasuta anduriga määratud värvi

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

--- /task ---

--- task ---

**Test:** Liiguta värviliugur oma valitud värvile ja seejärel **käivita** enda kood. Sinu taustavärv muutub. Korda seda testi uuesti uue värviga.

**Näpunäide:** Iga kord, kui värvi muudad, pead klõpsama käsul "Käivita".

--- /task ---

## Silmusta oma programm

Astro Pi Mission Zero programmil on lubatud jooksutada kuni 30 sekundit. Kasutad seda aega värvianduri korduvaks kontrollimiseks ja pildi värskendamiseks.

Sinu kood kasutab `for` tsüklit 28 korda käitamiseks. **Iga** kord see:
+ tajub uusimat värvi
+ värskendab pildi taustavärvi
+ peatub üheks sekundiks

--- task ---

**Leia** oma `rgb = sense.color` koodirida.

**Lisa** kood selle ette, et installida oma `for` tsükkel `28` korduseks.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 2
---

for i in range(28):
rgb = sense.color # saa värv andurilt
c = (rgb.red, rgb.green, rgb.blue)

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

--- /task ---

--- task ---

Nüüd pead taandama kogu koodi `for` tsükli alla, nii et see paigutuks `for` tsükli **sisse**.

**Näpunäide:** Mitme rea taandamiseks tõsta esile read, mida soovid taandada, seejärel vajuta oma klaviatuuril <kbd>Tab</kbd> klahvi (reeglina klaviatuuril <kbd>Caps Lock</kbd> klahvi kohal).

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
---

for i in range(28):
  rgb = sense.color # saa värv andurilt
  c = (rgb.red, rgb.green, rgb.blue)

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
 
--- /code ---

--- /task ---

--- task ---

Lisa koodi allossa oma tsüklisse ühe sekundi pikkune `sleep`:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 5
---
  
  # Kuva pilt

  sense.set_pixels(pilt)
  sleep(1)  
  
--- /code ---

**Näpunäide:** Veendu, et see koodirida oleks sinu `for` tsüklisse taandatud.

--- /task ---

--- task ---

**Test:** Käita oma kood ja muuda projekti jooksutamise ajal korduvalt värvivalijat. Kontrolli, kas sinu pilti värskendatakse, et kasutada tajutud värvi järgmisel käitamisel.

Pildi värskendamine lõpetatakse, kui tsükkel lõpeb, nii et programm ei jookse kauem kui 30 sekundit.

--- /task ---

--- task ---

**Silumine**

Minu koodis on süntaksiviga või see ei jookse ootuspäraselt:

- Kontrolli, kas sinu kood ühtib ülaltoodud näidetes oleva koodiga
- Kontrolli, kas oled oma `for` tsüklis koodi taandanud
- Kontrolli, kas sinu loend on ümbritsetud `[` ja `]`-ga
- Kontrolli, kas iga värvi muutuja on loendis komaga eraldatud

Minu kood jookseb kauem kui 30 sekundit:

- Vähenda for-tsükli käitamise kordade arvu 28-lt 25-le või isegi 20-le.
- Vähenda sleep-i pikkust 1 sekundilt 0,5 sekundini.

--- /task ---

--- task ---

Lisa oma koodi lõppu `sense.clear()`, et oma tsükli lõpus olev pilt tühjendada. See aitab sul näha, millal sinu animatsioon on ära jooksutanud.

**Näpunäide:** Veendu, et sa **ei** taanda `sense.clear()` koodirida, kuna sinu eesmärgiks on see käitada vaid korra, animatsiooni lõpus.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 7
---
  
  # Kuva pilt

  sense.set_pixels(pilt)
  sleep(1) 
  
sense.clear()
  
--- /code ---

--- /task ---

--- task ---

**Testi:** Käita oma kood uuesti. Kui sinu projekt on ära jooksutanud, tühjeneb LED-maatriks, muutes kõik tuled mustaks (lülitab need välja).

--- /task ---

--- task ---

**Silumine**

LED-maatriks muutub iga sekundi järel mustaks:

- Kontrolli, et sa pole oma `for` tsüklis `sense.clear()` koodi taandanud

--- /task ---

--- task ---

Lisa kood LED-maatriksi tühjendamiseks enda valitud värvile. Uue värvi salvestamiseks loo muutuja nimega `x`.

Saad oma värvi ise kokku segada või kasutada värvide loendis olevaid väärtusi, et luua uus `x`värv.

[[[generic-theory-simple-colours]]]
[[[ambient-colours]]]

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 7, 8
---
  
  # Kuva pilt

  sense.set_pixels(pilt)
  sleep(1) 

x = (178, 34, 34)  # vali oma punase, rohelise ja sinise väärtused vahemikus 0–255
sense.clear(x)
  
--- /code ---

--- /task ---

--- task ---

**Testi:** Käita oma kood uuesti. Kui sinu projekt on ära jooksutanud, tühjeneb LED-maatriks sinu valitud värviks. Saad värvi muuta ja katsetada nii mitu korda kui soovid.

--- /task ---

--- task ---

**Salvesta oma edusammud**

Saad oma programmi salvestada Mission Starter projekti, sisestades oma meeskonna nime, meeskonnaliikmete nimed ja sulle antud klassiruumi koodi. Saad oma programmi uuesti laadida mis tahes internetiühendusega seadmesse, sisestades oma meeskonna nime ja klassiruumi koodi.

![Mission Zero salvestamisnupu ekraanipilt](images/savebutton_ee.png)

--- /task ---

--- task ---

--- collapse ---

---
title: Valmis koodi näide
---

![8 x 8 ruuduga võre, millel on kujutatud krokodilli.](images/croc.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Impordi teegid
from sense_hat import SenseHat
from time import sleep

# Installi Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# SInstalli värviandur
sense.color.gain = 60 # Määra anduri tundlikkus
sense.color.integration_cycles = 64 # Intervall, millal näit võetakse

# Lisa värvi muutujad ja pilt

a = (255, 255, 255) # Valge
c = (0, 0, 0) # Must
f = (25, 25, 112) # MidnightBlue
m = (34, 139, 34) # Metsaroheline

for i in range(28):
  rgb = sense.color # saa värv andurilt
  c = (rgb.red, rgb.green, rgb.blue)

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
  sleep(1)

x = (178, 34, 34)  # vali oma punase, rohelise ja sinise väärtused vahemikus 0–255
sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
