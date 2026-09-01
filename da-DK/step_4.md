## Registrer en farve

I dette trin skal du konfigurere farve- og lysstyrkesensoren. Du skal bruge denne sensor til at måle mængden af rødt, grønt og blåt lys, der rammer sensoren. Disse værdier bruges derefter til at ændre en af farverne i det billede, du har valgt.

Det betyder, at billedet kan ændre sig afhængigt af, hvad sensoren ser. For eksempel ville en astronaut iført en blå skjorte se en anden version af billedet end en astronaut iført en rød skjorte.

På hvalbilledet, som vi brugte i det forrige trin, var baggrundsfarven sort. Vi brugte variablen `c` til at gemme dens RGB farvekode:

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

Brug farvesensoren til at ændre en af dine farver.

Under linjerne, hvor du definerer farverne, skal du tilføje følgende kode:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4
---
# Registrer en farve
rgb = sense.color # få farven fra sensoren
c = (rgb.red, rgb.green, rgb.blue) # brug den opfangede farve

--- /code ---

--- /task ---

Denne kode erstatter RGB-værdierne gemt i `c` med værdierne for den farve, der registreres af sensoren.

Tip: Hvis du ikke brugte variablen `c` i dit eget billede, erstatte `c` med en af de farver, du har brugt. Dette vil gøre det muligt for sensoren at ændre denne farve i stedet.

--- task ---

**Test:** Flyt farvevælgeren til en farve efter eget valg og **kør** derefter din kode. Din baggrundsfarve vil ændre sig. Gentag denne test med en ny farve.

**Tip:** Du skal klikke på 'Kør' hver gang, du ændrer farven.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Nu har du vist et billede og registreret en farve og brugt den i dit program og din kode er klar til indsendelse! 

Du kan gemme og indsende dit program ved hjælp af formularen i bunden af kodeeditoren.
  
Du kan dog vælge at tilføje flere billeder til dit projekt eller gøre det mere levende med animation. De næste trin viser dig, hvordan du gør dette.
</p>

## Animér dit projekt (valgfrit)

Dit Mission Zero-program kan køre på den internationale rumstation (ISS) i op til 30 sekunder. Du kan bruge denne køretid til at vise en animation på LED-matrixen ved at skifte mellem to eller flere forskellige billeder.

--- task ---


**Tilføj** et andet billede lige under kodelinjen `sense.set_pixels(billede)`. Giv det variabelnavnet `billede2` og ændr nogle få pixels, så dette billede i animationen ser anderledes ud. Tilføj derefter en kort pause efter det.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
billede = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(billede)

# Ekstra billeder/billedrammer indsættes her:

billede2 = [
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

Nederst i din kodefil skal du oprette din `for`-løkke, så den gentages `14` gange og skiftevis viser `billede` og `billede2` med en pause på 1 sekund for hvert billede.

**Tip:** Sørg for, at kodelinjerne under `for i in range(14):` er rykket ind med et mellemrum, så de ligger **inde i** løkken.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
billede2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Gentag 14 gange (14 * 2 sekunder = 28 sekunders animation i alt)
for i in range(14):
  # Vis det andet billede
  sense.set_pixels(billede2)
  sleep(1)

  # Vis det første billede
  sense.set_pixels(billede)
  sleep(1)
  
--- /code ---

--- /task ---

--- task ---

**Test:** Kør din kode igen. Dit program viser den registrerede farve med det samme og skifter derefter frem og tilbage mellem billederne i en animation.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Hvis du gerne vil have mere end to billeder i din animation, skal du sørge for, at programmet ikke kører i mere end 30 sekunder. Hvis du f. eks. har 10 billeder, der hver vises i 1 sekund, skal du ændre din for-løkke, så den gentages 3 gange (10 × 3 = 30 sekunder)
</p>

--- task ---

**Tjek for fejl**

Min kode har en syntaksfejl eller skifter ikke mellem billederne:
- Kontrollér, at indrykningen i koden i din `for`-løkke svarer til indrykningen i eksemplet.
- Sørg for, at du har kaldt din anden billedmatrix `billede2` og at den er placeret uden for løkken og før løkken begynder.
- Kontrollér, at dine `sleep`-tider er sat til præcis `1` sekund, så programmet ikke overskrider ISS' strenge grænse på 30 sekunders køretid.

--- /task ---

--- task ---

**Gem dine fremskridt**

Du kan gemme dit program på Mission Starter-projektet ved at indtaste dit teamnavn, teammedlemmers navne og klasseværelseskoden, som du har fået. Du kan genindlæse dit program på enhver enhed med internetforbindelse ved at indtaste dit teamnavn og klasseværelseskode.

--- /task ---

--- task ---

--- collapse ---
---
title: Eksempel på færdig hvalkode
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importér bibliotekerne
from sense_hat import SenseHat
from time import sleep

# Konfigurer Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Konfigurer farvesensoren
sense.color.gain = 60 # Indstil sensorens følsomhed
sense.color.integration_cycles = 64 # Intervallet som aflæsningen vil blive taget med

# Tilføj farvevariabler og billede
a = (255, 255, 255) # Hvid
c = (0, 0, 0)       # Sort
f = (36, 128, 200)  # Havblå
g = (0, 204, 255)   # Himmelblå

# Registrer en farve
rgb = sense.color # få farven fra sensoren
c = (rgb.red, rgb.green, rgb.blue)

billede = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(billede)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Eksempel på færdig hvalkode (med animation)
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importér bibliotekerne
from sense_hat import SenseHat
from time import sleep

# Konfigurer Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Konfigurer farvesensoren
sense.color.gain = 60 # Indstil sensorens følsomhed
sense.color.integration_cycles = 64 # Intervallet som aflæsningen vil blive taget med

# Tilføj farvevariabler og billede
a = (255, 255, 255) # Hvid
c = (0, 0, 0)       # Sort
f = (36, 128, 200)  # Havblå
g = (0, 204, 255)   # Himmelblå

# Registrer en farve
rgb = sense.color # få farven fra sensoren
c = (rgb.red, rgb.green, rgb.blue)

billede = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(billede)

# DEN GRUNDLÆGGENDE INDSENDELSE er nu færdig

# Ekstra billeder/billedrammer indsættes her:
billede2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Gentag 14 gange (14 * 2 sekunder = 28 sekunders animation i alt)
for i in range(14):
  # Vis det andet billede
  sense.set_pixels(billede2)
  sleep(1)

  # Vis det første billede
  sense.set_pixels(billede)
  sleep(1)
  
--- /code ---

--- /collapse ---

--- /task ---

