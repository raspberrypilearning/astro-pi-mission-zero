## Vis en besked

Astro Pi'ens LED-matrix kan vise farver. I dette trin skal du vise billeder fra naturen på Astro Pi'ens LED-matrix.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
En <span style="color: #0faeb0">**LED-matrix**</span> er et gitter af lysdioder, der kan styres individuelt eller som en gruppe til at skabe forskellige lyseffekter. LED-matrixen på Sense HAT har 64 lysdioder viset i et 8 x 8 gitter. Lysdioderne kan programmeres til at vise et stort udvalg af farver.
</p>

![Et skærmbillede af emulatorvinduet, der viser flyenheden med LED-matrixen, der viser et billede af en blomst.](images/fu-pic.png)

--- task ---

Åbn [Mission Zero startprojektet](http://rpf.io/mzcode){:target="_blank"}.

Her kan du se, at der automatisk er blevet tilføjet tre linjer kode for dig.

Denne kode opretter forbindelse til Astro Pi'en og sørger for, at LED-displayet vises korrekt og indstiller farvesensoren. Lad koden stå, for du får brug for den.

--- code ---
---
Tilføj denne linje under den anden kode:
title: Hvilke tegn kan bruges?
---
# Importér bibliotekerne
from sense_hat import SenseHat from time import sleep

# Konfigurer Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Konfigurer farvesensoren
Tryk på knappen **Run** (Kør) og kig på, mens beskeden `Astro Pi` ruller hen over LED-displayet.

--- /code ---

![Et skærmbillede af Sense Hat-emulatoren med tre linjer startkode vist i ruden til venstre.](images/sense-hat-emulator2.png)

--- /task ---

### Vælg et navn til de nye Astro Pi -computere

Farver kan laves ved hjælp af forskellige blandinger af rød, grøn og blå. Du kan lære om RGB farver her:

[[[generic-theory-simple-colours]]]

LED-matrixen er et 8 x 8 gitter. Hvert LED på gitteret kan indstilles til en anden farve. Her er en liste over variabler for 24 forskellige farver. Hver farve har en værdi for rød, grøn og blå:

[[[ambient-colours]]]

### Vælg et billede

--- task ---

**Vælg:** Vælg et billede, der skal vises, blandt mulighederne nedenfor. Python gemmer informationen om et billede i en liste. Koden for hvert billede inkluderer de anvendte farvevariabler og listen.

Du skal **kopiere**hele koden for dit valgte billede og derefter **indsætte** den i dit projekt under den linje, der siger `# Tilføj farvevariabler og billede`.

--- collapse ---

---
titel: Kylling
---

![Et gitter med 8 x 8 firkanter, der viser en kylling i et æg.](images/chick.png)

--- code ---
---
Hvis du ønsker at stemme, *skal* din besked starte med disse ord, ellers vil vi ikke automatisk kunne tælle den med.
line_numbers: false
---
a = (255, 255, 255) # White c = (0, 0, 0) # Black e = (0, 0, 205) # MediumBlue q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange w = (255, 192, 203) # Pink

image = [ c, c, c, q, q, q, c, c, c, c, t, q, e, q, c, c, c, c, c, q, q, q, c, c, c, w, w, w, w, w, w, c, c, w, a, a, a, a, w, c, c, w, a, a, a, a, w, c, c, c, w, a, a, w, c, c, c, c, c, w, w, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---

---
titel: Blomst
---

![Et gitter med 8 x 8 firkanter, viser en lyserød blomst på en grøn stilk.](images/flower.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange y = (255, 20, 147) # DeepPink

image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---
---
titel: Krabbe
---

![A grid with 8 x 8 squares showing a crab.](images/crab.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
a = (255, 255, 255) # White c = (0, 0, 0) # Black v = (255, 0, 0) # Red

image = [ c, a, a, c, a, a, c, c, c, a, c, c, a, c, c, c, c, v, c, c, v, c, c, c, c, v, c, c, v, c, c, c, v, v, v, v, v, c, v, v, v, v, c, c, v, v, v, c, v, v, v, v, v, c, v, v, v, c, v, c, v, c, c, c]

--- /code ---

--- /collapse ---


--- collapse ---
---
title: Crocodile
---

![A grid with 8 x 8 squares showing a crocodile head.](images/croc.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
a = (255, 255, 255) # White c = (0, 0, 0) # Black f = (25, 25, 112) # MidnightBlue m = (34, 139, 34) # ForestGreen

image = [ m, m, m, m, m, c, c, c, m, f, m, f, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, a, c, c, c, a, m, m, c, c, c ,c ,c ,c, m, m, c, c, c, a, c, c, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]

--- /code ---


--- /collapse ---

--- collapse ---
---
title: Snake
---

![A grid with 8 x 8 squares showing a snake.](images/snake.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
 c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow v = (255, 0, 0) # Red

image = [ c, c, c, c, c, c, c, m, c, m, m, m, m, m, m, m, c, m, c, c, c, c, c, c, c, m, m, m, m, m, c, c, c, c, c, c, c, m, c, c, q, m, q, m, m, m, c, c, m, m, m, c, c, c, c, c, v, c, c, c, c, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Frog
---

![A grid with 8 x 8 squares showing a frog.](images/frog.png)

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start:
line_highlights:
---
c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow v = (255, 0, 0) # Red

image = [ c, m, m, m, c, m, m, m, c, m, q, m, c, m, q, m, m, m, m, m, m, m, m, m, m, v, v, v, v, v, v, v, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, m, m, m, c, m]

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Find:** the line which says `# Display the image` and add a line of code to display your image on the LED matrix:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 12
---
image = [ c, c, c, q, q, q, c, c, c, c, t, q, e, q, c, c, c, c, c, q, q, q, c, c, c, w, w, w, w, w, w, c, c, w, a, a, a, a, w, c, c, w, a, a, a, a, w, c, c, c, w, a, a, w, c, c, c, c, c, w, w, c, c, c]

# Display the image
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Press **Run** at the bottom of the editor, to see your image displayed on the LED matrix.

--- /task ---

--- task ---

**Debug**

My code has a syntax error:

- Check that your code matches the code in the examples above
- Check that you have indented the code in your list
- Check that your list is surrounded by `[` and `]`
- Check that each colour variable in the list is separated by a comma

My image does not appear:

- Check that your `sense.set_pixels(image)` is not indented

--- /task ---



