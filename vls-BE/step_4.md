## Meet een kleur

In deze stap zal je de kleurintensiteitssensor installeren en hem gebruiken om de hoeveeldheid rood, groen en blauw te meten die de sensor bereikt. Deze kleur zal dan gebruikt worden om je gekozen afbeelding in te kleuren. Een astronaut die naar de sensor toeloopt met een blauw T-shirt zal een andere afbeelding zien dan een astronaut in een rood T-shirt.

![afbeelding getoond met een roze achtergrond op de LED-matrix](images/colour_background.png)

Welke afbeelding je ook kiest, de achtergrond gebruikt de `c` variabele die ingesteld is op zwart.

--- task ---

Gebruik de kleursensor om je achtergrond te kleuren.

Voeg code toe voor je afbeeldingslijst om de kleur van de sensor te ontvangen en verander je `c` achtergrondkleur om de kleur te gebruiken die gemeten wordt door de kleursensor van de Sense HAT in plaats van zwart.

**Tip:** je hoeft geen opmerkingen te typen die beginnen met '#' (die staan er om de code uit te leggen).


--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 9, 10
---

# Voeg kleurvariabelen en beeld toe

a = (255, 255, 255) # Wit
c = (0, 0, 0) # Zwart
f = (25, 25, 112) # Middernachtblauw
m = (34, 139, 34) # Bosgroen

rgb = sense.color # ontvang de kleur van de sensor
c = (rgb.red, rgb.green, rgb.blue) # gebruik de waargenomen kleur

afbeelding = [
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

**Test** Beweeg de kleurschuiver naar een kleur naar keuze en laat dan je code **run**. Je achtergrondkleur zal veranderen. Herhaal deze test nogmaals met een andere kleur.

**Tip:** Je zal elke keer je de kleur verandert op 'Run' moeten klikken.

--- /task ---

## Herhaal je programma

Het Astro Pi Mission Zero-programma mag tot 30 seconden werken. Je zal deze tijd gebruiken om verschillende keren de kleursensor te controleren en de afbeelding te actualiseren.

Je code zal een `for` lus gebruiken om 28 keer te werken. **Elke** keer zal het:
+ de laatste kleur meten
+ de achtergrondkleur van de afbeelding actualiseren
+ 1 seconde pauzeren

--- task ---

**Vind** je `rgb = sense.color` codelijn.

**Voeg** code hierboven toe om je `for` lus voor `28` herhalingen in te stellen.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 2
---

for i in range(28):
rgb = sense.color # ontvang de kleur van de sensor
c = (rgb.red, rgb.green, rgb.blue)

afbeelding = [
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

Je zal nu alle code onder de `for` lus moeten opslaan zodat die bewaard wordt **binnen** de `for` lus.

**Tip:** Om meerdere lijnen op te slaan, markeer de lijnen die je wil opslaan en druk dan de <kbd>Tab</kbd> toets op je klavier (meestal boven de <kbd>Caps Lock</kbd> toets op je klavier).

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
---

for i in range(28):
  rgb = sense.color # ontvang de kleur van de sensor
  c = (rgb.red, rgb.green, rgb.blue)

  afbeelding = [
    m, m, m, m, m, c, c, c,
    m, f, m, f, m, m, m, m,
    m, m, m, m, m, m, m, m,
    m, m, c, a, c, c, c, a,
    m, m, c, c, c ,c ,c ,c,
    m, m, c, c, c, a, c, c,
    m, m, m, m, m, m, m, m,
    m, m, m, m, m, m, m, m]

    
  # Toon de afbeelding

  sense.set_pixels(afbeelding)
 
--- /code ---

--- /task ---

--- task ---

Onderaan je code, voeg je een `sleep` van 1 seconde toe in je lus:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 5
---
  
  # Toon de afbeelding

  sense.set_pixels(afbeelding)
  sleep(1)  
  
--- /code ---

**Tip:** Zorg ervoor dat deze codelijn opgeslagen wordt in je `for` lus.

--- /task ---

--- task ---

**Test:** Start je code en verander de kleurkiezer verschillende keren terwijl je project werkt. Controleer dat je afbeelding geactualiseerd wordt met de gemeten kleur als het opnieuw start.

De afbeelding zal niet meer geactualiseerd worden als de lus eindigt zodat het programma niet langer dan 30 seconden werkt.

--- /task ---

--- task ---

**Problemen oplossen**

Mijn code geeft een foutmelding en werkt niet zoals verwacht:

- Controleer dat je code overeenkomt met de code in de voorbeelden hierboven
- Controleer dat je de code opgeslagen hebt in je `for` lus
- Controleer dat je lijst omgeven wordt door `[` en `]`
- Controleer dat elke kleurvariabele in de lijst gescheiden wordt door een komma

Mijn code werkt langer dan 30 seconden:

- Verlaag het aantal keren dat je lus werkt van 28 naar 25 of zelfs 20.
- Verminder de duur van de slaap, van 1 seconde naar 0,5 seconden.

--- /task ---

--- task ---

Voeg `sense.clear()` toe aan het einde van je code om de afbeelding te wissen aan het einde van je lus. Dit zal je helpen om te zien wanneer je animatie klaar is.

**Tip:** Zorg ervoor dat je **niet** de codelijn `sense.clear()` opslaat want je wil dit maar 1 keer laten gebeuren op het einde van je animatie.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 7
---
  
  # Toon de afbeelding

  sense.set_pixels(afbeelding)
  sleep(1) 
  
sense.clear()
  
--- /code ---

--- /task ---

--- task ---

**Test:** Start je code nog eens. Wanneer je project klaar is, zal de LED-matrix leeg worden door alle lichten op zwart (uit) te zetten.

--- /task ---

--- task ---

**Problemen oplossen**

De LED-matrix wordt elke seconde zwart:

- Controleer dat je de `sense.clear()` code niet in je `for` lus opgeslagen hebt

--- /task ---

--- task ---

Voeg code toe om de LED-matrix te wissen naar een kleur naar keuze. Creëer een variabele genaamd `x` om je nieuwe kleur op te slaan.

Je kan je eigen kleur mengen door de waarden van de kleurenlijst te gebruiken om je nieuwe `x` kleur te maken.

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
  
  # Toon de afbeelding

  sense.set_pixels(afbeelding)
  sleep(1) 

x = (178, 34, 34)  # kies je eigen rood-, groen-, blauw-waardes tussen 0 - 255
sense.clear(x)
  
--- /code ---


--- /task ---

--- task ---

**Test:** Start je code nogmaals. Als je project klaar is, zal de LED-matrix oplichten in de gekozen kleur. Je kan dan de kleur zo vaak aanpassen als je wil om te testen.

--- /task ---

--- task ---

**Sla je voortgang op**

Je kan je programma op het Mission Starter Project opslaan door je teamnaam, de namen van je teamleden en je klascode in te geven. Je kan je programma opnieuw laden op elk apparaat met een internetverbinding door je teamnaam en klascode in te geven.

![Mission Zero opslaan knop screenshot](images/savebutton_be.png)

--- /task ---

--- task ---

--- collapse ---

---
title: Afgewerkt codevoorbeeld
---

![Een krokodil wordt getoond in een raster van 8 x 8 vierkanten.](images/croc.png)

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

# SInstalleer de kleursensor
sense.color.gain = 60 # Stel de gevoeligheid van de sensor in
sense.color.integration_cycles = 64 # Het interval waarin het uitlezen gebeurt

# Voeg kleurvariabelen en beeld toe

a = (255, 255, 255) # Wit
c = (0, 0, 0) # Zwart
f = (25, 25, 112) # Middernachtblauw
m = (34, 139, 34) # Bosgroen

for i in range(28):
  rgb = sense.color # ontvang de kleur van de sensor
  c = (rgb.red, rgb.green, rgb.blue)

  afbeelding = [
    m, m, m, m, m, c, c, c,
    m, f, m, f, m, m, m, m,
    m, m, m, m, m, m, m, m,
    m, m, c, a, c, c, c, a,
    m, m, c, c, c ,c ,c ,c,
    m, m, c, c, c, a, c, c,
    m, m, m, m, m, m, m, m,
    m, m, m, m, m, m, m, m]


  # Toon de afbeelding

  sense.set_pixels(afbeelding)
  sleep(1)

x = (178, 34, 34)  # kies je eigen rood-, groen-, blauw-waardes tussen 0 - 255
sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
