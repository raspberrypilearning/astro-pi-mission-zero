## Nuskaityti spalvą

Šiame žingsnyje nustatysite spalvų ir ryškumo jutiklį. Šį jutiklį naudosite raudonos, žalios ir mėlynos šviesos, pasiekiančios jutiklį, kiekiui matuoti. Šios vertės bus naudojamos norint pakeisti vieną iš pasirinkto vaizdo spalvų.

Tai reiškia, kad vaizdas gali keistis priklausomai nuo to, ką mato jutiklis. Pavyzdžiui, astronautas, vilkintis mėlynus marškinėlius, matytų kitokią vaizdo versiją nei astronautas, vilkintis raudonus marškinėlius.

Ankstesniame žingsnyje pateiktame banginio paveikslėlyje fono spalva buvo juoda. RGB spalvos kodui saugoti naudojome kintamąjį `c`:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Norėdami pakeisti vieną iš spalvų, naudokite spalvų jutiklį.

Po eilutėmis, kuriose apibrėžiate spalvas, pridėkite šį kodą:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

--- /code ---

--- /task ---

Šis kodas pakeičia RGB reikšmes, saugomas `c` , jutiklio aptiktos spalvos reikšmėmis.

Patarimas: jei savo paveikslėlyje nenaudojote kintamojo `c` , pakeiskite `c` vienu iš spalvų kintamųjų, kuriuos naudojote. Tai leis jutikliui pakeisti tą spalvą.

--- task ---

**Testas:** perkelkite spalvos slankiklį į pasirinktą spalvą ir **paleiskite** savo kodą. Jūsų fono spalva pasikeis. Pakartokite šį testą su nauja spalva.

**Patarimas:** kiekvieną kartą keisdami spalvą turėsite spustelėti „Paleisti“.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Dabar parodėte paveikslėlį, nuskaitėte spalvą ir panaudojote ją savo programoje, todėl jūsų kodas paruoštas pateikimui! 

Programą galite išsaugoti ir pateikti naudodami formą, esančią kodų redagavimo priemonės apačioje.
  
Tačiau, jei norite, prie savo projekto galite pridėti daugiau vaizdų arba jį pagyvinti animuodami. Tolesni veiksmai parodys, kaip tai padaryti.
</p>

## Animuokite savo projektą (nebūtina)

Jūsų „Mission Zero“ programa gali veikti Tarptautinėje kosminėje stotyje (TKS) iki 30 sekundžių. Šį laiką galite naudoti animacijai LED matricoje rodyti, perjungdami du ar daugiau skirtingų paveikslėlių.

--- task ---


**Pridėkite** antrą paveikslėlį iškart po `sense.set_pixels(image)` kodo eilute. Suteikite jam kintamojo pavadinimą `image2` ir pakeiskite kelis pikselius, kad animacijos kadras atrodytų kitaip. Tada po jo pridėkite trumpą pauzę.

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

Pačioje kodo failo apačioje nustatykite savo `for` ciklą taip, kad jis kartotųsi `14` kartų ir kaitaliotų `image` ir `image2` rodymą, tarp kadrų padarydamas 1 sekundės pauzę.

**Patarimas:** įsitikinkite, kad kodo eilutės po `for i in range(14):`  yra su tarpo įtrauka, kad jos būtų ciklo bloko **viduje**.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1)

--- /code ---

--- /task ---

--- task ---

**Testas:** paleiskite savo kodą dar kartą. Jūsų programa akimirksniu parodys jūsų nuskaitytą spalvą, o tada kartos ciklą kaip animuotą vaizdą.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Jei norite, kad animaciją sudarytų daugiau nei du kadrai, turite įsitikinti, kad programa veiks ne ilgiau kaip 30 sekundžių. Pavyzdžiui, jei turite 10 paveikslėlių, kurių kiekvienas rodomas po 1 sekundę, turite pakeisti „for“ ciklą, kad jis kartotųsi 3 kartus (10 * 3 = 30 sekundžių).
</p>

--- task ---

**Patikrinkite, ar nėra klaidų**

Mano kode yra sintaksės klaida arba jis nekeičia kadrų:
- Patikrinkite, ar jūsų `for` ciklo kodas pateiktas su pavyzdyje nurodyta įtrauka.
- Įsitikinkite, kad antrąją vaizdo matricą pavadinote `image2` ir kad ji yra pateikta už ciklo ribų, prieš jam prasidedant.
- Patikrinkite, ar jūsų `pertraukos` laikas nustatytas tiksliai į `1` sekundę, kad neviršytumėte griežtos 30 sekundžių vykdymo ribos TKS.

--- /task ---

--- task ---

**Išsaugokite savo darbą**

Savo programą galite išsaugoti „Mission“ pradiniame projekte įvesdami savo komandos pavadinimą, komandos narių vardus ir jums suteiktą klasės kodą. Programą galite įkelti iš naujo bet kuriame įrenginyje, turinčiame interneto ryšį, įvesdami savo komandos pavadinimą ir klasės kodą.

--- /task ---

--- task ---

--- collapse ---
---
title: Užbaigto banginio kodo pavyzdys
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
title: Užbaigto banginio kodo pavyzdys (su animacija)
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
