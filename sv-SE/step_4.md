## Känn en färg

I det här steget konfigurerar du färg- och ljusstyrkesensorn. Du kommer att använda den här sensorn för att mäta mängden rött, grönt och blått ljus som når sensorn. Dessa värden kommer sedan att användas för att ändra en av färgerna i din valda bild.

Det betyder att bilden kan ändras beroende på vad sensorn ser. Till exempel skulle en astronaut som bär en blå tröja se en annan version av bilden än en astronaut som bär en röd tröja.

I valbilden som vi använde i föregående steg var bakgrundsfärgen svart. Vi använde variabeln `c` för att lagra dess RGB-färgkod:

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

Använd färgsensorn för att ändra en av dina färger.

Under raderna där du definierar färgerna, lägg till följande kod:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4
---
# Känn av en färg
rgb = sense.color # hämta färgen från sensorn
c = (rgb.red, rgb.green, rgb.blue) # använd den avkända färgen

--- /code ---

--- /task ---

Denna kod ersätter RGB-värdena som lagras i `c` med värdena för den färg som sensorn detekterar.

Tips: Om du inte använde variabeln `c` i din egen bild, ersätt `c` med en av de färgvariabler som du använde. Detta gör att sensorn kan ändra färgen istället.

--- task ---

**Test:** Flytta färgreglaget till en färg som du väljer och sedan **kör** din kod. Din bakgrundsfärg kommer att ändras. Upprepa detta test igen med en ny färg.

**Tips:** Du måste klicka på "Kör" varje gång du ändrar färg.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Nu har du visat en bild och avkänt en färg och använt den i ditt program, och din kod är redo att skickas in! 

Du kan spara och skicka in ditt program med hjälp av formuläret längst ner i kodredigeraren.
  
Du kanske dock vill lägga till fler bilder i ditt projekt, eller ge det liv med animering. Nästa steg visar hur du gör detta.
</p>

## Animera ditt projekt (valfritt)

Ert Mission Zero-program kan köras på den internationella rymdstationen (ISS) i upp till 30 sekunder. Du kan använda denna körtid för att visa en animation på LED-matrisen genom att växla mellan två eller flera olika bilder.

--- task ---


**Lägg till** en andra bild precis under din `sense.set_pixels(bild)` kodrad. Ge den variabelnamnet `bild2` och ändra några pixlar för att få din animationsbildruta att se annorlunda ut. Lägg sedan till en kort paus efteråt.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
bild = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(bild)

# Extra bilder/ramar finns här:

bild2 = [
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

Längst ner i din kodfil, ställ in din `for` loop för att upprepa `14` gånger och växla mellan att visa `bild` och `bild2` med en paus i 1 sekund för varje bildruta.

**Tips:** Se till att kodraderna under `for i in range(14):` är indragna med ett mellanslag så att de sitter **innanför** loopblocket.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
bild2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Loopa 14 gånger (14 * 2 sekunder = 28 sekunder total animation)
for i in range(14):
  # Visa den andra bilden
  sense.set_pixels(bild2)
  sleep(1)

  # Visa den första bilden
  sense.set_pixels(bild)
  sleep(1)
  
--- /code ---

--- /task ---

--- task ---

**Testa:** Kör din kod igen. Ditt program visar din avkända färg direkt och loopar sedan fram och tillbaka för en animerad visning.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Om du vill ha fler än två bildrutor i din animation måste du se till att programmet körs i högst 30 sekunder. Om du till exempel har 10 bilder som var och en visas i 1 sekund, måste du ändra din `for`-loop så att den upprepas 3 gånger (10 * 3 = 30 sekunder)
</p>

--- task ---

**Kontrollera om det finns fel**

Min kod har ett syntaxfel eller ändrar inte bildrutor:
- Kontrollera att din `for` loopkod matchar indenteringen i exemplet.
- Se till att du har döpt din andra bildmatris till `bild2` och att den är placerad utanför och före loopen börjar.
- Kontrollera att dina `sleep-` timers är inställda på exakt `1` sekund för att undvika att överskrida den strikta gränsen på 30 sekunder på ISS.

--- /task ---

--- task ---

**Spara dina framsteg**

Du kan spara ditt program i Mission Starter-projektet genom att ange ditt teamnamn, teammedlemmarnas namn och klassrumskoden du fått. Du kan ladda om ditt program på vilken enhet som helst med en internetanslutning genom att ange ditt teamnamn och klassrumskod.

--- /task ---

--- task ---

--- collapse ---
---
title: Slutförd valkod exempel
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importera biblioteken
from sense_hat import SenseHat
from time import sleep

# Ställ in Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Ställ in färgsensorn
sense.color.gain = 60 # Ställ in sensorns känslighet
sense.color.integration_cycles = 64 # Intervallet med vilket avläsningen kommer att ske

# Lägg till färgvariabler och bild
a = (255, 255, 255) # Vit
c = (0, 0, 0)       # Svart
f = (36, 128, 200)  # Havsblå
g = (0, 204, 255)   # Himmelsblå

# Känn av en färg
rgb = sense.color # hämta färgen från sensorn
c = (rgb.red, rgb.green, rgb.blue)

bild = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(bild)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Slutförd valkod (med Animation)
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importera biblioteken
from sense_hat import SenseHat
from time import sleep

# Ställ in Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Ställ in färgsensorn
sense.color.gain = 60 # Ställ in sensorns känslighet
sense.color.integration_cycles = 64 # Intervallet med vilket avläsningen kommer att ske

# Lägg till färgvariabler och bild
a = (255, 255, 255) # Vit
c = (0, 0, 0)       # Svart
f = (36, 128, 200)  # Havsblå
g = (0, 204, 255)   # Himmelsblå

# Känn av en färg
rgb = sense.color # hämta färgen från sensorn
c = (rgb.red, rgb.green, rgb.blue)

bild = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(bild)

# GRUNDINLÄMNINGEN är nu klar

# Extra bilder/ramar finns här:
bild2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Loopa 14 gånger (14 * 2 sekunder = 28 sekunder total animation)
for i in range(14):
  # Visa den andra bilden
  sense.set_pixels(bild2)
  sleep(1)

  # Visa den första bilden
  sense.set_pixels(bild)
  sleep(1)
  
--- /code ---

--- /collapse ---

--- /task ---

