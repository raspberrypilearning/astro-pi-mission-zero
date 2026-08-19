## Sajūtiet krāsu

Šajā solī jūs iestatīsiet krāsu un spilgtuma sensoru. Jūs izmantosiet šo sensoru, lai mērītu sarkanās, zaļās un zilās gaismas daudzumu, kas sasniedz sensoru. Šīs vērtības pēc tam tiks izmantotas, lai mainītu vienu no krāsām jūsu izvēlētajā attēlā.

Tas nozīmē, ka attēls var mainīties atkarībā no tā, ko redz sensors. Piemēram, astronauts zilā kreklā redzētu atšķirīgu attēla versiju nekā astronauts sarkanā kreklā.

Iepriekšējā solī izmantotajā vaļa attēlā fona krāsa bija melna. Mēs izmantojām mainīgo `c` , lai saglabātu tā RGB krāsu kodu:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Izmantojiet krāsu sensoru, lai mainītu vienu no krāsām.

Zem rindām, kur definējat krāsas, pievienojiet šādu kodu:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

--- /code ---

--- /task ---

Šis kods aizvieto RGB vērtības, kas saglabātas `c` , ar sensora noteiktajām krāsas vērtībām.

Padoms: ja savā attēlā neizmantojāt mainīgo `c` , nomainiet `c` ar vienu no izmantotajiem krāsu mainīgajiem. Tas ļaus sensoram mainīt šo krāsu.

--- task ---

**Pārbaude:** Pārvietojiet krāsas slīdni uz izvēlēto krāsu un pēc tam **palaidiet** savu kodu. Jūsu fona krāsa mainīsies. Atkārtojiet šo testu vēlreiz ar jaunu krāsu.

**Padoms:** katru reizi, kad maināt krāsu, būs jānoklikšķina uz “Palaist”.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Tagad esat parādījis attēlu, noteicis krāsas sajūtu un izmantojis to savā programmā, un jūsu kods ir gatavs iesniegšanai! 

Programmu var saglabāt un iesniegt, izmantojot veidlapu koda redaktora apakšdaļā.
  
Tomēr jūs varētu vēlēties savam projektam pievienot vairāk attēlu vai atdzīvināt to ar animācijas palīdzību. Nākamās darbības parādīs, kā to izdarīt.
</p>

## Animējiet savu projektu (pēc izvēles)

Jūsu programma “Mission Zero” var darboties Starptautiskajā kosmosa stacijā (SKS) līdz 30 sekundēm. Šo darbības laiku var izmantot, lai LED matricā parādītu animāciju, pārslēdzoties starp diviem vai vairākiem dažādiem attēliem.

--- task ---


**Pievienojiet** otru attēlu tieši zem jūsu `sense.set_pixels(image)` koda rindiņas. Piešķiriet tam mainīgā nosaukumu `image2` un nomainiet dažus pikseļus, lai animācijas rāmis izskatītos citādi. Pēc tam pievienojiet īsu pauzi.

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

Koda faila pašā apakšā iestatiet savu `for` ciklu, lai tas atkārtotu `14` reizes un pārmaiņus parādītu `image` un `image2`, katrā kadrā ieturot 1 sekundes pauzi.

**Padoms:** pārliecinieties, ka koda rindas zem `for i in range(14):` ir ievilktas ar atstarpi, lai tās atrastos **cikla bloka** iekšpusē.

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

**Pārbaude:** palaidiet savu kodu vēlreiz. Jūsu programma acumirklī parādīs jūsu uztverto krāsu un pēc tam cikliski darbosies animētā attēlojumā.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Ja vēlaties, lai animācijā būtu vairāk nekā divi kadri, pārliecinieties, ka programma darbosies ne ilgāk kā 30 sekundes. Piemēram, ja jums ir 10 attēli, katrs no kuriem tiek parādīts 1 sekundi, jums ir jāmaina `for` cikls, lai tas atkārtotos 3 reizes (10 * 3 = 30 sekundes)
</p>

--- task ---

**Pārbaudiet, vai nav kļūdu**

Manā kodā ir sintakses kļūda vai tas nemaina kadrus:
- Pārliecinieties, vai jūsu `priekš` cikla kods atbilst piemērā norādītajai atkāpei.
- Pārliecinieties, ka jūsu otrās attēlu matricas nosaukums ir `image2` un ka tā ir novietota ārpus cikla un pirms tā sākuma.
- Pārliecinieties, vai jūsu `miega` laiki ir iestatīti precīzi uz `1` sekundi, lai izvairītos no stingrā 30 sekunžu izpildes ierobežojuma pārsniegšanas SKS.

--- /task ---

--- task ---

**Saglabājiet savu progresu**

Jūs varat saglabāt savu programmu Mission Starter projektā, ievadot savas komandas nosaukumu, komandas dalībnieku vārdus un jums piešķirto klases kodu. Programmu var atkārtoti ielādēt jebkurā ierīcē ar interneta pieslēgumu, ievadot komandas nosaukumu un klases kodu.

--- /task ---

--- task ---

--- collapse ---
---
title: Pabeigts vaļa koda piemērs
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
title: Pabeigts vaļa koda piemērs (ar animāciju)
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
