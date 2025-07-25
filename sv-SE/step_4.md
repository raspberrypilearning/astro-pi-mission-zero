## Känn en färg

I det här steget kommer du att ställa in färgljussensorn och använda den för att känna av mängden rött, grönt och blått som når sensorn. Denna färg kommer sedan att användas för att färglägga din valda bild. En astronaut som går upp till sensorn i en blå skjorta skulle se en annan bild än en astronaut i en röd skjorta.

![bild visas med en rosa bakgrund på LED-matrisen](images/colour_background.png)

Vilken bild du än väljer använder bakgrunden variabeln `c` som är inställd på svart.

--- task ---

Använd färgsensorn för att färga din bakgrund.

Lägg till kod före din bildlista för att få färgen från sensorn och ändra din `c` bakgrundsfärgvariabel för att använda färgen som avkänns av Sense HAT-färgsensorn istället för svart.

**Tips:** Du behöver inte skriva kommentarerna som börjar med '#' (de är till för att förklara koden).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9, 10
---

# Lägg till färgvariabler och bild

a = (255, 255, 255) # Vit c = (0, 0, 0) # Svart f = (25, 25, 112) # Midnattsblå m = (34, 139, 34) # Skogsgrön

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


--- /code ---

--- /task ---

--- task ---

**Test:** Flytta färgreglaget till en färg som du väljer och sedan **kör** din kod. Din bakgrundsfärg kommer att ändras. Upprepa detta test igen med en ny färg.

**Tips:** Du måste klicka på "Kör" varje gång du ändrar färg.

--- /task ---

## Loopa ditt program

Astro Pi Mission Zero-programmet får köras i upp till 30 sekunder. Du kommer att använda denna tid för att upprepade gånger kontrollera färgsensorn och uppdatera bilden.

Din kod kommer att använda en `for` loop för att köra 28 gånger. **Varje** gång kommer den att:
+ känna den senaste färgen
+ uppdatera bildens bakgrundsfärg
+ pausa i en sekund

--- task ---

**Hitta** din `rgb = sense.color` kodrad.

**Lägg till** kod ovanför den för att ställa in din `for` -loop för `28` repetitioner.

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

Du måste nu indentera all din kod under `for` loopen så att den är **inuti** `for` loopen.

**Tips:** För att indentera flera rader, markera de rader som du vill indentera och tryck sedan på <kbd>Tab</kbd> -tangenten på ditt tangentbord (vanligtvis ovanför <kbd>Caps Lock</kbd> -tangenten på tangentbordet).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


  # Display the image

  sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Längst ned i koden lägger du till en `-sleep` på en sekund i din loop:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 5
---

  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Tips:** Se till att denna kodrad är indenterad i din `for` -loop.

--- /task ---

--- task ---

**Testa:** Kör din kod och ändra färgväljaren flera gånger medan ditt projekt körs. Kontrollera att din bild uppdateras för att använda den avkända färgen vid nästa körning.

Bilden kommer att sluta uppdateras när loopen är klar så att programmet inte körs i mer än 30 sekunder.

--- /task ---

--- task ---

**Felsökning**

Min kod har ett syntaxfel eller fungerar inte som förväntat:

- Kontrollera att din kod matchar koden i exemplen ovan
- Kontrollera att du har indenterat koden i din `for` -loop
- Kontrollera att din lista är omgiven av `[` och `]`
- Kontrollera att varje färgvariabel i listan är avgränsad med ett kommatecken

Min kod körs i längre än 30 sekunder:

- Minska antalet gånger din for loop kör, från 28 till 25 eller till och med 20.
- Minska längden på sleep, från 1 sekund till 0,5 sekunder.

--- /task ---

--- task ---

Lägg till `sense.clear()` i slutet av din kod för att rensa bilden i slutet av din loop. Detta hjälper dig att se när din animation har körts färdigt.

**Tips:** Se till att du **inte** indenterar raden `sense.clear()` eftersom du vill att den bara ska köras en gång i slutet av din animering.

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

**Testa:** Kör din kod igen. När ditt projekt har körts klart försvinner LED-matrisen, vilket gör att alla lampor blir svarta (släckta).

--- /task ---

--- task ---

**Felsökning**

LED-matrisen blir svart varje sekund:

- Kontrollera att du inte har indenterat koden `sense.clear()` i din `for` -loop

--- /task ---

--- task ---

Lägg till kod för att rensa LED-matrisen till en färg som du väljer. Skapa en variabel som heter `x` för att lagra din nya färg.

Du kan blanda din egen färg eller använda värdena från listan över färger för att skapa din nya `x`-färg.

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

**Test:** Kör din kod igen. När ditt projekt är klart kommer LED-matrisen att rensas till din valda färg. Du kan ändra och sedan testa färgen så många gånger du vill.

--- /task ---


--- task ---

**Spara dina framsteg**

Du kan spara ditt program i Mission Starter-projektet genom att ange ditt teamnamn, teammedlemmarnas namn och klassrumskoden du fått. Du kan ladda om ditt program på vilken enhet som helst med en internetanslutning genom att ange ditt teamnamn och klassrumskod.

![Mission Zero Spara skärmgrepp](images/mz_savebutton_v2.png)

--- /task ---


--- task ---

--- collapse ---

---
title: Färdigt kodexempel
---

![Ett rutnät med 8 x 8 rutor som visar en krokodill.](images/fish.png)

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

a = (255, 255, 255) # Vit c = (0, 0, 0) # Svart f = (25, 25, 112) # Midnattsblå m = (34, 139, 34) # Skogsgrön

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # välj dina egna röda, gröna, blå värden mellan 0 - 255 sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
