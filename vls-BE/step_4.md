## Meet een kleur

In deze stap zal je de kleur en helderheidssensor instellen. Je zal deze sensor gebruiken om te meten hoeveel rood, groen en blauw licht de sensor bereikt. Deze waarden zullen dan gebruikt worden om één van de kleuren in je gekozen afbeelding te veranderen.

Dit betekent dat de afbeelding kan veranderen afhankelijk van wat de sensor ziet. Bijvoorbeeld, een astronaut die een blauw shirt draagt zal een andere versie van de afbeelding zien dan een astronaut die een rood shirt draagt.

In de afbeelding van de walvis die we in de vorige stap gebruikten, was de achtergrond zwart. We gebruikten de variabele `c`om de RGB-kleur code op te slaan:

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

Gebruik de kleursensor om één van je kleuren te veranderen.

Onder de lijnen waar je de kleuren bepaalt, voeg je deze code toe:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4
---
# Meet een kleur
rgb = sense.color # ontvang de kleur van de sensor
c = (rgb.red, rgb.green, rgb.blue) # gebruik de waargenomen kleur

--- /code ---

--- /task ---

Deze code vervangt de RGB-waarden die opgeslagen zijn in `c`</0> door de waarden van de kleur die de sensor waarneemt.

Tip: als je variabele `c` niet gebruikte in je eigen afbeelding, vervang dan `c` door één van de kleurvariabelen die je wel gebruikte. Dit zorgt ervoor dat de sensor naar die kleur zal veranderen.

--- task ---

**Test** Beweeg de kleurschuiver naar een kleur naar keuze en laat dan je code **run**. Je achtergrondkleur zal veranderen. Herhaal deze test nogmaals met een andere kleur.

**Tip:** Je zal elke keer je de kleur verandert op 'Run' moeten klikken.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Je hebt nu een afbeelding getoond, een kleur gemeten en dit in je programma gebruikt. Je code is klaar om in te dienen! 

Je kan je programma opslaan en indienen door het formulier te gebruiken dat onderaan de code-editor staat.
  
Je kan ook als je dat wil nog meer afbeeldingen aan je project wil toevoegen of het tot leven laten komen door animatie. De volgende stappen laten je zien hoe je dat moet doen.
</p>

## Maak een animatie van je project (optioneel)

Je Mission Zero programma kan werken in het internationaal ruimtestation (ISS) gedurende maximum 30 seconden. Je kan deze tijd gebruiken om een animatie te tonen op de LED-matrix door af te wisselen tussen twee of meer verschillende afbeeldingen.

--- task ---


**Toevoegen** van een tweede afbeelding net onder je `sense.set_pixels(afbeelding)` codeerlijn. Geef het de variabelennaam `afbeelding2` en verander een aantal pixels om ervoor te zorgen dat je animatiekader er anders uitziet. Voeg daarna een korte pauze toe.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
afbeelding = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(afbeelding)

# Extra afbeeldingen/frames kunnen hier worden geplaatst:

afbeelding2 = [
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

Helemaal onderaan je codebestand moet je je `for` lus zo instellen dat deze `14` keer herhaalt en afwisselend `afbeelding` en `afbeelding2` weergeeft, met een pauze van 1 seconde tussen elk frame.

**Tip:** Zorg ervoor dat de regels code onder `for i in range(14):` ingesprongen zijn met een spatie, zodat ze **binnen** het lusblok vallen.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
afbeelding2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Herhaal 14 keer (14 * 2 seconden = 28 seconden totale animatie)
for i in range(14):
  # Toon de tweede afbeelding
  sense.set_pixels(afbeelding2)
  sleep(1)

  # Toon de eerste afbeelding
  sense.set_pixels(afbeelding)
  sleep(1)
  
--- /code ---

--- /task ---

--- task ---

**Test:** Start je code nog eens. Je programma laat meteen de kleur zien die de sensor meet, daarna beweegt de kleur heen en weer als een animatie.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Als je graag meer dan twee kaders in je animatie hebt, moet je ervoor zorgen dat het programma niet langer dan 30 seconden duurt. Bijvoorbeeld, als je 10 afbeeldingen hebt die elk gedurende 1 seconde getoond worden, moet je je 'for'-lus aanpassen om 3 keer te herhalen (10 * 3 =30 seconden)
</p>

--- task ---

**Controleer op fouten**

Mijn code heeft een syntax error of verandert de kaders niet:
- Controleer of de inspringing van je `for` luscode overeenkomt met de inspringing in het voorbeeld.
- Zorg ervoor dat je je tweede afbeeldingsmatrix de naam `afbeelding2` hebt gegeven en dat deze buiten en vóór het begin van de lus is geplaatst.
- Controleer of je `sleep` tijden precies zijn ingesteld op `1` seconde om te voorkomen dat de strikte uitvoeringslimiet van 30 seconden op het ISS wordt overschreden.

--- /task ---

--- task ---

**Sla je voortgang op**

Je kan je programma op het Mission Starter Project opslaan door je teamnaam, de namen van je teamleden en je klascode in te geven. Je kan je programma opnieuw laden op elk apparaat met een internetverbinding door je teamnaam en klascode in te geven.

--- /task ---

--- task ---

--- collapse ---
---
title: Voltooide walvis-codevoorbeeld
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importeer de bibliotheken
from sense_hat import SenseHat
from time import sleep

# Installeer de Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Installeer de kleursensor
sense.color.gain = 60 # Stel de gevoeligheid van de sensor in
sense.color.integration_cycles = 64 # Het interval waarin het uitlezen zal gebeuren

# Voeg kleurvariabelen en beeld toe
a = (255, 255, 255) # Wit
c = (0, 0, 0)       # Zwart
f = (36, 128, 200)  # Oceaanblauw
g = (0, 204, 255)   # Hemelsblauw

# Meet een kleur
rgb = sense.color # ontvang de kleur van de sensor
c = (rgb.red, rgb.green, rgb.blue)

afbeelding = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(afbeelding)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Voltooide walvis-codevoorbeeld (met animatie)
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importeer de bibliotheken
from sense_hat import SenseHat
from time import sleep

# Installeer de Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Installeer de kleursensor
sense.color.gain = 60 # Stel de gevoeligheid van de sensor in
sense.color.integration_cycles = 64 # Het interval waarin het uitlezen zal gebeuren

# Voeg kleurvariabelen en beeld toe
a = (255, 255, 255) # Wit
c = (0, 0, 0)       # Zwart
f = (36, 128, 200)  # Oceaanblauw
g = (0, 204, 255)   # Hemelsblauw

# Meet een kleur
rgb = sense.color # ontvang de kleur van de sensor
c = (rgb.red, rgb.green, rgb.blue)

afbeelding = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(afbeelding)

# BASIS INDIENEN is nu klaar

# Extra afbeeldingen/frames kunnen hier worden geplaatst:
afbeelding2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Herhaal 14 keer (14 * 2 seconden = 28 seconden totale animatie)
for i in range(14):
  # Toon de tweede afbeelding
  sense.set_pixels(afbeelding2)
  sleep(1)

  # Toon de eerste afbeelding
  sense.set_pixels(afbeelding)
  sleep(1)
  
--- /code ---

--- /collapse ---

--- /task ---
