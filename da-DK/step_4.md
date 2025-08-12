## Registrer en farve

I dette trin vil du lære at indstille farvelysstyrkesensoren og bruge den til at 'fornemme' mængden af rød, grøn og blå, der rammer sensoren. Denne farve vil derefter blive brugt til at farve med i dit valgte billede. En astronaut, der går op til sensoren i en blå skjorte, vil se et andet billede end en astronaut i en rød skjorte.

![billede vist med en lyserød baggrund på LED-matrixen](images/colour_background.png)

Uanset hvilket billede du vælger, bruger baggrunden `c` -variablen, som er sat til sort.

--- task ---

Brug farvesensoren til at farve din baggrund.

Tilføj kode før din liste med billeder for at få farven fra sensoren og ændre din `c` baggrundsfarvevariabel for at bruge den farve, som Sense HAT farvesensoren 'fornemmer', i stedet for sort.

**Tip:** Du behøver ikke at skrive kommentarerne, der starter med '#' (de er der for at forklare koden).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9, 10
---

# Add colour variables and image

z = (153, 50, 204) # DarkOrchid q = (255, 255, 0) # Yellow d = (51, 153, 255) # blue c = (0, 0, 0) # Black

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


--- /code ---

--- /task ---

--- task ---

**Test:** Flyt farvevælgeren til en farve efter eget valg og **kør** derefter din kode. Din baggrundsfarve vil ændre sig. Gentag denne test med en ny farve.

**Tip:** Du skal klikke på 'Kør' hver gang, du ændrer farven.

--- /task ---

## Få dit program kørt i en løkke

Astro Pi Mission Zero-programmet får lov til at køre i op til 30 sekunder. Du skal bruge denne tid til løbende at kontrollere farvesensoren og opdatere billedet.

Din kode bruger en `for`-løkke til at køre 28 gange. **Hver** gang vil den:
+ registrere den seneste farve
+ opdatere billedets baggrundsfarve
+ pause i et sekund

--- task ---

**Find** din `rgb = sense.color` kodelinje.

**Tilføj** kode over det for at konfigurere din `for`-løkke til `28` gentagelser.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


--- /code ---

--- /task ---

--- task ---

Du skal nu indrykke al din kode under `for`-løkken, så den er **inde under** `for` løkken.

**Tip:** For at indrykke flere linjer skal du fremhæve de linjer, du vil indrykke og derefter trykke på <kbd>Tab</kbd>-tasten på dit tastatur (normalt over <kbd>Caps Lock</kbd> -tasten på tastaturet).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


  # Display the image

  sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

I bunden af din kode skal du tilføje en `-sleep` på et sekund inde i din løkke:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 5
---

  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Tip:** Sørg for, at denne kodelinje er indrykket i din `for`-løkke.

--- /task ---

--- task ---

**Test:** Kør din kode og ændre farvevælgeren flere gange, mens dit projekt kører. Tjek, at dit billede opdateres til at bruge den registrerede farve ved næste kørsel.

Billedet stopper med at blive opdateret, når løkken er færdig, så programmet ikke kører i mere end 30 sekunder.

--- /task ---

--- task ---

**Fejlsøgning**

Min kode har en syntaksfejl eller kører ikke som forventet:

- Tjek, at din kode matcher koden i eksemplerne ovenfor
- Tjek, at du har indrykket koden i din `for` løkke
- Tjek, at din liste er omgivet af `[` og `]`
- Tjek, at hver farvevariabel i listen er adskilt af et komma

Min kode kører i mere end 30 sekunder:

- Reducer antallet af gange din for-løkke kører, fra 28 til 25 eller endda 20.
- Reducer længden på din "sleep", fra 1 sekund til 0,5 sekunder.

--- /task ---

--- task ---

Tilføj `sense.clear()` i slutningen af din kode for at resette billedet i slutningen af din løkke. Dette vil hjælpe dig med at se, når din animation er færdig med at køre.

**Tip:** Sørg for, at du **ikke** indrykker `sense.clear()` kodelinjen, da du gerne vil have, at den kun skal køre én gang i slutningen af din animation.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7
---

  # Display the image

  sense.set_pixels(image) sleep(1)

sense.clear()

--- /code ---

--- /task ---

--- task ---

**Test:** Kør din kode igen. Når dit projekt er færdig med at køre, vil LED-matrixen resette og sætte alle lysene til sort (slukket).

--- /task ---

--- task ---

**Fejlsøgning**

LED-matrixen bliver sort hvert sekund:

- Tjek, at du ikke har indrykket `sense.clear()`-koden i din `for`-løkke

--- /task ---

--- task ---

Tilføj kode for at resette LED-matrixen til en farve efter eget valg. Opret en variabel kaldet `x` til at gemme din nye farve.

Du kan blande din egen farve eller bruge værdierne fra farvelisten til at oprette din nye `x`farve.

\[[[generic-theory-simple-colours]]\] \[[[ambient-colours\]]]

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7, 8
---

  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /task ---

--- task ---

**Test:** Kør din kode igen. Når dit projekt er færdig med at køre, vil LED-matrixen resettes til din valgte farve. Du kan ændre og derefter teste farven så mange gange, du vil.

--- /task ---


--- task ---

**Gem dine fremskridt**

Du kan gemme dit program på Mission Starter-projektet ved at indtaste dit teamnavn, teammedlemmers navne og klasseværelseskoden, som du har fået. Du kan genindlæse dit program på enhver enhed med internetforbindelse ved at indtaste dit teamnavn og klasseværelseskode.

![Mission Zero Gem-knap skærmbillede](images/mz_savebutton_v2.png)

--- /task ---


--- task ---

--- collapse ---

---
title: Fuldført kodeeksempel
---

![Et gitter med 8 x 8 kvadrater, der viser en krokodille.](images/fish.png)

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

z = (153, 50, 204) # DarkOrchid q = (255, 255, 0) # Yellow d = (51, 153, 255) # blue c = (0, 0, 0) # Black

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 and 255 sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
