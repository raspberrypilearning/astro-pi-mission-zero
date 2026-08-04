## Taju värvi

Selles etapis seadistate värvi- ja heleduseanduri. Selle anduri abil mõõdad andurile jõudva punase, rohelise ja sinise valguse hulka. Neid väärtusi kasutatakse seejärel teie valitud pildi ühe värvi muutmiseks.

See tähendab, et pilt võib muutuda sõltuvalt sellest, mida andur näeb. Näiteks näeks sinist särki kandev astronaut pildist erinevat versiooni kui punast särki kandev astronaut.

Eelmises etapis kasutatud vaalapildil oli taustavärv must. RGB värvikoodi salvestamiseks kasutasime muutujat `c`:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Värvisensori abil saate ühte oma värvidest muuta.

Värvide defineerimise ridade alla lisa järgmine kood:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

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


**Lisa** teine pilt kohe oma `sense.set_pixels(image)` koodirea alla. Anna sellele muutuja nimi `image2` ja muuda paar pikslit, et animatsiooniraam teistsugune välja näeks. Seejärel lisage sellele lühike paus.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# Extra images / frames go here:

image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

Koodifaili kõige lõpus sea oma `` tsükkel kordama `14` korda ja kuvama vaheldumisi `pilti` ja `pilti2` , tehes iga kaadri juures 1-sekundilise pausi.

**Vihje:** Veendu, et vahemikus (14):</code> olevad koodiread `i jaoks vahemikus <code> on tühikuga taandatud, nii et need paikneksid <strong x-id="1">tsükliploki</strong> sees.</p>

<p spaces-before="0">--- code ---</p>

<hr />

<p spaces-before="0">language: python
filename: main.py
line_numbers: false
line_number_start: 1</p>

<h2 spaces-before="0">line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22</h2>

<p spaces-before="0">image2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]</p>

<p spaces-before="0">sleep(1)</p>

<h1 spaces-before="0">Loop 14 times (14 * 2 seconds = 28 seconds total animation)</h1>

<p spaces-before="0">for i in range(14):
  # Display the second image
  sense.set_pixels(image2)
  sleep(1)</p>

<p spaces-before="2"># Display the first image
  sense.set_pixels(image)
  sleep(1)</p>

<p spaces-before="0">--- /code ---</p>

<p spaces-before="0">--- /task ---</p>

<p spaces-before="0">--- task ---</p>

<p spaces-before="0"><strong x-id="1">Testi:</strong> Käita oma kood uuesti. Teie programm kuvab teie tuvastatud värvi koheselt ja seejärel tsüklib edasi-tagasi animeeritud kuvamiseks.</p>

<p spaces-before="0">--- /task ---</p>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Kui soovite oma animatsioonis kasutada rohkem kui kahte kaadrit, peate veenduma, et programm ei kesta kauem kui 30 sekundit. Näiteks kui teil on 10 pilti, millest igaüks kuvatakse 1 sekundi jooksul, peate oma `for`-tsüklit muutma nii, et see korduks 3 korda (10 * 3 = 30 sekundit).
</p>

<p spaces-before="0">--- task ---</p>

<p spaces-before="0"><strong x-id="1">Kontrolli vigu</strong></p>

<p spaces-before="0">Minu koodis on süntaksiviga või see ei jookse ootuspäraselt:</p>

<ul>
<li>Kontrolli, et sinu <code>for` tsükli kood vastaks näites olevale taandele.</li>
- Veendu, et sa nimetasid oma teise pildimaatriksi `pilt2` ja et see asetseks tsükli algusest väljapoole ja enne seda.
- Kontrolli, et sinu `une-` ajad oleksid seatud täpselt `1` sekundile, et vältida ISS-i range 30-sekundilise täitmisaja ületamist.</ul>

--- /task ---

--- task ---

**Salvesta oma edusammud**

Saad oma programmi salvestada Mission Starter projekti, sisestades oma meeskonna nime, meeskonnaliikmete nimed ja sulle antud klassiruumi koodi. Saad oma programmi uuesti laadida mis tahes internetiühendusega seadmesse, sisestades oma meeskonna nime ja klassiruumi koodi.

--- /task ---

--- task ---

--- collapse ---
---
pealkiri: Valmis vaala koodi näide
---

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Import the libraries
from sense_hat import SenseHat from time import sleep

# Set up the Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image
a = (255, 255, 255) # White c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

--- /code ---

--- /collapse ---

--- collapse ---
---
pealkiri: Valmis vaala koodi näide (animatsiooniga)
---

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Import the libraries
from sense_hat import SenseHat from time import sleep

# Set up the Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image
a = (255, 255, 255) # White c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1)

--- /code ---

--- /collapse ---

--- /task ---
