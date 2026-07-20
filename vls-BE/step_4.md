## Meet een kleur

In deze stap zal je de kleur en helderheidssensor instellen. Je zal deze sensor gebruiken om te meten hoeveel rood, groen en blauw licht de sensor bereikt. Deze waarden zullen dan gebruikt worden om één van de kleuren in je gekozen afbeelding te veranderen.

Dit betekent dat de afbeelding kan veranderen afhankelijk van wat de sensor ziet. Bijvoorbeeld, een astronaut die een blauw shirt draagt zal een andere versie van de afbeelding zien dan een astronaut die een rood shirt draagt.

In de afbeelding van de walvis die we in de vorige stap gebruikten, was de achtergrond zwart. We gebruikten de variabele `c`om de RGB-kleur code op te slaan:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Gebruik de kleursensor om één van je kleuren te veranderen.

Onder de lijnen waar je de kleuren bepaalt, voeg je deze code toe:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

--- /code ---

--- /task ---

Deze code vervangt de RGB-waarden die opgeslagen zijn in `c`</0> door de waarden van de kleur die de sensor waarneemt.

Tip: als je variabele `c` niet gebruikte in je eigen afbeelding, vervang dan `c` door één van de kleurvariabelen die je wel gebruikte. Dit zorgt ervoor dat de sensor naar die kleur zal veranderen.

--- task ---

**Test** Beweeg de kleurschuiver naar een kleur naar keuze en laat dan je code **run**. Je achtergrondkleur zal veranderen. Herhaal deze test nogmaals met een andere kleur.

**Tip:** Je zal elke keer je de kleur verandert op 'Run' moeten klikken.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Je hebt nu een afbeelding getoond, een kleur gemeten en een dit in je programma gebruikt. Je code is klaar om in te dienen!  

Je kan je programma opslaan en indienen door het formulier te gebruiken dat onderaan de code-aanpasser staat.
  
Je kan ook als je dat wil nog meer afbeeldingen aan je project wil toevoegen of het tot leven laten komen door animatie. De volgende stappen laten je zien hoe je dat moet doen.
</p>

## Maak een animatie van je project (optioneel)

Je Mission Zero programma kan werken in het internationaal ruimtestation (ISS) gedurende maximum 30 seconden. Je kan deze tijd gebruiken om een animatie te tonen op de LED-matrix door af te wisselen tussen twee of meer verschillende afbeeldingen.

--- task ---


**Toevoegen** van een tweede afbeelding net onder je `sense.set_pixels(afbeelding)` codeerlijn. Geef het de variabelennaam `afbeelding2` en verander een aantal pixels om ervoor te zorgen dat je animatiekader er anders uitziet. Voeg daarna een korte pauz toe.

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

Helemaal onderaan je codeerfile, stel je je `for`lus in op herhaal `14` keer en wissel af tussen het tonen van `image` en `image2` terwijl je 1 seconde pauzeert bij elk kader.

**Tip:** Zorg ervoor dat de codeerlijnen onder `for i in range(14):` aangeduid worden met een spatie zodat ze **inside** het lusblok zitten.

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

**Test:** Start je code nog eens. Je programma zal je gemeten code onmiddellijk tonen en daarna start de lus heen en weer om een geanimeerd beeld te tonen.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Als je graag meer dan twee kaders in je animatie hebt, moet je ervoor zorgen dat het programma langer dan 30 seconden duurt. Bijvoorbeeld, als je 10 afbeeldingen hebt die elk gedurende 1 seconde getoond worden, moet je je 'for'-lus aanpassen om 3 keer te herhalen (10 * 3 =30 seconden)
</p>

--- task ---

**Controleer op fouten**

Mijn code heeft een syntax error of verandert de kaders niet:
- Controleer dat je `for` luscode overeenkomt met de onderbreking in het voorbeeld.
- Zorg ervoor dat je je tweede afbeeldingsmatrix `image2` genoemd hebt en dat deze buiten staat en voor de lus begint.
- Controleer dat je `sleep` tijden ingesteld staan op exact `1` seconde om te vermijden dat je buiten de strikte 30 seconden uitvoerstop op het ISS valt.

--- /task ---

--- task ---

**Sla je voortgang op**

Je kan je programma op het Mission Starter Project opslaan door je teamnaam, de namen van je teamleden en je klascode in te geven. Je kan je programma opnieuw laden op elk apparaat met een internetverbinding door je teamnaam en klascode in te geven.

--- /task ---

--- task ---

--- collapse ---
---
titel: Afgewerkt codeervoorbeeld Walvis
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
titel: Afgewerkt codeervoorbeeld Walvis (met animatie)
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
