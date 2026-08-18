## Taju värvi

Selles etapis seadistate värvi- ja heleduseanduri. Selle anduri abil mõõdad andurile jõudva punase, rohelise ja sinise valguse hulka. Neid väärtusi kasutatakse seejärel teie valitud pildi ühe värvi muutmiseks.

See tähendab, et pilt võib muutuda sõltuvalt sellest, mida andur näeb. Näiteks näeks sinist särki kandev astronaut pildist erinevat versiooni kui punast särki kandev astronaut.

Eelmises etapis kasutatud vaalapildil oli taustavärv must. RGB värvikoodi salvestamiseks kasutasime muutujat `c`:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Värvisensori abil saate ühte oma värvidest muuta.

Värvide defineerimise ridade alla lisa järgmine kood:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4
---
# Tunneta värvi
rgb = sense.color # saa värv andurilt
c = (rgb.red, rgb.green, rgb.blue) # kasuta anduriga määratud värvi

--- /code ---

--- /task ---

See kood asendab `c` salvestatud RGB-väärtused sensori poolt tuvastatud värvi väärtustega.

Näpunäide: Kui sa ei kasutanud oma pildil muutujat `c` , asenda `c` ühe värvimuutujaga, mida sa kasutasid. See võimaldab anduril hoopis seda värvi muuta.

--- task ---

**Test:** Liiguta värviliugur oma valitud värvile ja seejärel **käivita** enda kood. Sinu taustavärv muutub. Korda seda testi uuesti uue värviga.

**Näpunäide:** Iga kord, kui värvi muudad, pead klõpsama käsul "Käivita".

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Nüüd oled pildi kuvanud, värvi tuvastanud ja oma programmis kasutanud ning sinu kood on esitamiseks valmis! 

Saate oma programmi salvestada ja esitada koodiredaktori allosas oleva vormi abil.
  
Siiski võiksite oma projektile lisada rohkem pilte või animatsiooni abil ellu äratada. Järgmised sammud näitavad teile, kuidas seda teha.
</p>

## Animeeri oma projekti (valikuline)

Teie Mission Zero programm saab rahvusvahelises kosmosejaamas (ISS) töötada kuni 30 sekundit. Seda tööaega saab kasutada LED-maatriksil animatsiooni kuvamiseks, vahetades kahe või enama erineva pildi vahel.

--- task ---


**Lisa** teine pilt kohe oma `sense.set_pixels(pilt)` koodirea alla. Anna sellele muutuja nimi `pilt2` ja muuda paar pikslit, et animatsiooniraam teistsugune välja näeks. Seejärel lisage sellele lühike paus.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
pilt = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(pilt)

# Lisapildid/raamid tulevad siia:

pilt2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

Koodifaili kõige lõpus sea oma `for` tsükkel kordama `14` korda ja kuvama vaheldumisi muutujaid `pilt` ja `pilt2`, tehes iga kaadri juures 1-sekundilise pausi.

**Vihje:** Veendu, et koodiread, mis asuvad `for i in range(14):` all, on tühikuga taandatud, nii et need paikneksid **tsükliploki** sees.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
pilt2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Tsükelda 14 korda (14 * 2 sekundit = 28 sekundit animatsiooni kokku)
for i in range(14):
  # Kuva teine pilt
  sense.set_pixels(pilt2)
  sleep(1)

  # Kuva esimene pilt
  sense.set_pixels(pilt)
  sleep(1)
  
--- /code ---

--- /task ---

--- task ---

**Testi:** Käita oma kood uuesti. Teie programm kuvab teie tuvastatud värvi koheselt ja seejärel tsüklib edasi-tagasi animeeritud kuvamiseks.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Kui soovite oma animatsioonis kasutada rohkem kui kahte kaadrit, peate veenduma, et programm ei kesta kauem kui 30 sekundit. Näiteks kui teil on 10 pilti, millest igaüks kuvatakse 1 sekundi jooksul, peate oma `for`-tsüklit muutma nii, et see korduks 3 korda (10 * 3 = 30 sekundit).
</p>

--- task ---

**Kontrolli vigu**

Minu koodis on süntaksiviga või see ei jookse ootuspäraselt:
- Kontrolli, et sinu `for` tsükli kood vastaks näites olevale taandele.
- Veendu, et sa nimetasid oma teise pildimaatriksi `pilt2` ja et see asetseks tsükli algusest väljapoole ja enne seda.
- Kontrolli, et sinu `sleep` ajad oleksid seatud täpselt `1` sekundile, et vältida ISS-i range 30-sekundilise täitmisaja ületamist.

--- /task ---

--- task ---

**Salvesta oma edusammud**

Saad oma programmi salvestada Mission Starter projekti, sisestades oma meeskonna nime, meeskonnaliikmete nimed ja sulle antud klassiruumi koodi. Saad oma programmi uuesti laadida mis tahes internetiühendusega seadmesse, sisestades oma meeskonna nime ja klassiruumi koodi.

--- /task ---

--- task ---

--- collapse ---
---
title: Valmis vaala koodi näide
---

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

# Installi värviandur
sense.color.gain = 60 # Määra anduri tundlikkus
sense.color.integration_cycles = 64 # Intervall, millega näit võetakse

# Lisa värvi muutujad ja pilt
a = (255, 255, 255) # Valge
c = (0, 0, 0)       # Must
f = (36, 128, 200)  # Ookeani sinine
g = (0, 204, 255)   # Taevasinine

# Tunneta värvi
rgb = sense.color # saa värv andurilt
c = (rgb.red, rgb.green, rgb.blue)

pilt = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(pilt)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Valmis vaala koodi näide (animatsiooniga)
---

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

# Installi värviandur
sense.color.gain = 60 # Määra anduri tundlikkus
sense.color.integration_cycles = 64 # Intervall, millega näit võetakse

# Lisa värvi muutujad ja pilt
a = (255, 255, 255) # Valge
c = (0, 0, 0)       # Must
f = (36, 128, 200)  # Ookeani sinine
g = (0, 204, 255)   # Taevasinine

# Tunneta värvi
rgb = sense.color # saa värv andurilt
c = (rgb.red, rgb.green, rgb.blue)

pilt = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(pilt)

# PÕHILISE ESITAMISE NR on nüüdseks tehtud

# Lisapildid/raamid tulevad siia:
pilt2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Tsükelda 14 korda (14 * 2 sekundit = 28 sekundit animatsiooni kokku)
for i in range(14):
  # Kuva teine pilt
  sense.set_pixels(pilt2)
  sleep(1)

  # Kuva esimene pilt
  sense.set_pixels(pilt)
  sleep(1)
  
--- /code ---

--- /collapse ---

--- /task ---

