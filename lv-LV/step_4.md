## Sajūtiet krāsu

Šajā solī jūs iestatīsiet krāsu un spilgtuma sensoru. Jūs izmantosiet šo sensoru, lai mērītu sarkanās, zaļās un zilās gaismas daudzumu, kas sasniedz sensoru. Šīs vērtības pēc tam tiks izmantotas, lai mainītu vienu no krāsām jūsu izvēlētajā attēlā.

Tas nozīmē, ka attēls var mainīties atkarībā no tā, ko redz sensors. Piemēram, astronauts zilā kreklā redzētu atšķirīgu attēla versiju nekā astronauts sarkanā kreklā.

Iepriekšējā solī izmantotajā vaļa attēlā fona krāsa bija melna. Mēs izmantojām mainīgo `c` , lai saglabātu tā RGB krāsu kodu:

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

Izmantojiet krāsu sensoru, lai mainītu vienu no krāsām.

Zem rindām, kur definējat krāsas, pievienojiet šādu kodu:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4
---
# Sajūtiet krāsu
rgb = sense.color # iegūt krāsu no sensora
c = (rgb.red, rgb.green, rgb.blue) # izmantojiet uztverto krāsu

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


**Pievienojiet** otru attēlu tieši zem jūsu `sense.set_pixels(attelu)` koda rindiņas. Piešķiriet tam mainīgā nosaukumu `attelu2` un nomainiet dažus pikseļus, lai animācijas rāmis izskatītos citādi. Pēc tam pievienojiet īsu pauzi.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
attelu = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(attelu)

# Papildu attēli/rāmji nonāk šeit:

attelu2 = [
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

Koda faila pašā apakšā iestatiet savu `ciklu` , lai tas atkārtotu `14` reizes un pārmaiņus parādītu `attelu` un `attelu2` , katrā kadrā apturot 1 sekundes pauzi.

**Padoms:** pārliecinieties, ka koda rindas zem `for i in range(14):` , ir atkāptas ar atstarpi, lai tās atrastos **cikla bloka** iekšpusē.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
attelu2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Cikls 14 reizes (14 * 2 sekundes = 28 sekundes kopā animācijas)
for i in range(14):
  # Parādiet otro attēlu
  sense.set_pixels(attelu2)
  sleep(1)

  # Parādiet pirmo attēlu
  sense.set_pixels(attelu)
  sleep(1)
  
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
- Pārliecinieties, ka jūsu otrās attēlu matricas nosaukums ir `attelu2` un ka tā ir novietota ārpus cikla un pirms tā sākuma.
- Pārliecinieties, vai jūsu `miega` laiki ir iestatīti precīzi uz `1` sekundi, lai izvairītos no stingrā 30 sekunžu izpildes ierobežojuma pārsniegšanas SKS.

--- /task ---

--- task ---

**Saglabājiet savu progresu**

Jūs varat saglabāt savu programmu Mission Starter projektā, ievadot savas komandas nosaukumu, komandas dalībnieku vārdus un jums piešķirto klases kodu. Programmu var atkārtoti ielādēt jebkurā ierīcē ar interneta pieslēgumu, ievadot komandas nosaukumu un klases kodu.

--- /task ---

--- task ---

--- collapse ---
---
nosaukums: Pabeigts vaļa koda piemērs
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importējiet bibliotēkas
from sense_hat import SenseHat
from time import sleep

# Iestatiet Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Krāsu sensora iestatīšana
sense.color.gain = 60 # Iestatiet sensitīvu jutību
sense.color.integration_cycles = 64 # Intervāls, kurā tiks veikts nolasījums

# Pievienojiet krāsu mainīgos un attēlu
a = (255, 255, 255) # Baltā
c = (0, 0, 0)       # Melns
f = (36, 128, 200)  # Okeāna zils
g = (0, 204, 255)   # Debeszils

# Sajūtiet krāsu
rgb = sense.color # iegūt krāsu no sensora
c = (rgb.red, rgb.green, rgb.blue)

attelu = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(attelu)

--- /code ---

--- /collapse ---

--- collapse ---
---
nosaukums: Pabeigts vaļa koda piemērs (ar animāciju)
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importējiet bibliotēkas
from sense_hat import SenseHat
from time import sleep

# Iestatiet Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Krāsu sensora iestatīšana
sense.color.gain = 60 # Iestatiet sensitīvu jutību
sense.color.integration_cycles = 64 # Intervāls, kurā tiks veikts nolasījums

# Pievienojiet krāsu mainīgos un attēlu
a = (255, 255, 255) # Baltā
c = (0, 0, 0)       # Melns
f = (36, 128, 200)  # Okeāna zils
g = (0, 204, 255)   # Debeszils

# Sajūtiet krāsu
rgb = sense.color # iegūt krāsu no sensora
c = (rgb.red, rgb.green, rgb.blue)

attelu = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(attelu)

# PAMATA IESNIEGŠANA tagad ir pabeigta

# Papildu attēli/rāmji nonāk šeit:
attelu2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Cikls 14 reizes (14 * 2 sekundes = 28 sekundes kopā animācijas)
for i in range(14):
  # Parādiet otro attēlu
  sense.set_pixels(attelu2)
  sleep(1)

  # Parādiet pirmo attēlu
  sense.set_pixels(attelu)
  sleep(1)
  
--- /code ---

--- /collapse ---

--- /task ---
