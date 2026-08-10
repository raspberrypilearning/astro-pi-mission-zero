## Vis et billede

Det billede, du viser, består af 64 farvede felter, der kaldes **pixels**. Pixlerne er placeret i et 8 × 8-gitter. Hver pixel kan have en forskellig farve. Ved at vælge farverne med omhu kan du skabe et billede. Her er et eksempel på en hval lavet ved hjælp af forskellige nuancer af blå på en sort baggrund.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
En <span style="color: #0faeb0">**LED-matrix**</span> er et gitter af lysdioder, der kan styres individuelt eller som en gruppe til at skabe forskellige lyseffekter. LED-matrixen på Sense HAT har 64 lysdioder viset i et 8 x 8 gitter. Lysdioderne kan programmeres til at vise et stort udvalg af farver.
</p>

![et 8×8-billede af en hval med bogstaver, der angiver de forskellige farver](images/whale.png)

Bemærk, at hvert kvadrat er mærket med en kode til at repræsentere en bestemt farve. På dette billede er der brugt 3 farver:
+ c = sort
+ f = Havblå
+ g = Himmelblå


--- task ---

Åbn [Mission Zero startprojektet](https://missions.astro-pi.org/da/mz/code_submissions/){:target="_blank"}.

Her kan du se, at der automatisk er blevet tilføjet tre linjer kode for dig.

Denne kode opretter forbindelse til Astro Pi'en og sørger for, at LED-displayet vises korrekt og indstiller farvesensoren. Lad koden stå, for du får brug for den.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Importér bibliotekerne
from sense_hat import SenseHat from time import sleep

# Konfigurer Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Konfigurer farvesensoren
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Et skærmbillede af Sense Hat-emulatoren med tre linjer startkode vist i ruden til venstre.](images/sense-hat-emulator3.png)

--- /task ---

### RGB farver

Farver kan laves ved hjælp af forskellige blandinger af rød, grøn og blå. Du kan lære om RGB farver her:

![Tre skydere, der viser RGB-farveværdier](images/rgbsliders.gif)

LED-matricen er et 8 x 8 gitter. Hvert LED på gitteret kan indstilles til en anden farve. Vi kan bruge bogstaverne a til z som navnene på variabler til at repræsentere 24 forskellige farver. Hver farve har en værdi for rød, grøn og blå.

--- collapse ---

---
titel: Liste over farvevariabler
---

![Et gitter med 24 farvede felter, der hver er mærket med et forskelligt bogstav i alfabetet](images/palette.png)

```python
a = (255, 255, 255) # hvid
b = (171, 171, 171) # Grå
c = (0, 0, 0) # Sort
d = (25, 25, 113) # Navy Blue
e = (0, 0, 255) # Pure Blue
f = (36, 128, 200) # Ocean Blue
g = (0, 204, 255) # Sky Blue
h = (86, 255, 255) # Electric Cyan
j = (0, 255, 0) # Ren grøn
k = (46, 139, 33) # Leaf Green
l = (57, 97, 17) # Olivengrøn
m = (30, 65, 6) # Forest Green
n = (126, 88, 25) # Earth Brown
o = (179, 96, 65) # Terrakotta Brown
p = (180, 34, 34) # Mursten rød
q = (255, 0, 0) # Ren Rød
r = (232, 118, 5) # Orange
s = (241, 231, 100) # Bleggul
t = (255, 255, 0) # Pure Yellow
u = (255, 209, 209) # Pale Pink
v = (255, 177, 177) # Blush Pink
w = (249, 169, 255) # Lyserød
y = (248, 97, 255) # Magenta
z = (220, 53, 232) # Lilla

```

--- /collapse ---

### Vælg et billede

--- task ---

**Vælg:** Vælg et billede, der skal vises, blandt mulighederne nedenfor. Python gemmer informationen om et billede i en liste. Koden for hvert billede inkluderer de anvendte farvevariabler og listen.

Du skal **kopiere** hele koden for dit valgte billede og derefter **indsætte** den i dit projekt under den linje, der siger `# Tilføj farvevariabler og billede`.

--- collapse ---

---
titel: Hvale
---

![Et gitter med 8 x 8 felter, der viser en hval.](images/whale.png)

Lavet af Team Naicom, Italien

```python
c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue

image = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, a,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

```

--- /collapse ---


--- collapse ---

---
titel: Citron
---

![Et gitter med 8 × 8 felter, der viser en citron.](images/lemon.png)

Lavet af Team 4lemoni, Grækenland

```python
c = (0, 0, 0)       # Black
k = (46, 139, 33)   # Leaf Green
t = (255, 255, 0)   # Pure Yellow

image = [
c, c, c, k, k, c, c, c,
c, c, k, c, k, c, c, c,
c, k, c, t, t, c, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, c, t, t, c, c, c]

```

--- /collapse ---

--- collapse ---
---
titel: Gris
---

![Et gitter med 8 × 8 felter, der viser en gris.](images/pig.png)

Lavet af Gary, Storbritannien

```python
a = (255, 255, 255) # White
v = (255, 177, 177) # Blush Pink
y = (248, 97, 255)  # Magenta
o = (179, 96, 65)   # Terracotta Brown
c = (0, 0, 0)       # Black

image = [
a, a, y, a, a, y, a, a,
a, y, y, y, y, y, y, a,
a, y, c, y, c, y, y, y,
v, v, v, v, v, y, y, y,
v, o, v, o, v, y, y, y,
v, v, v, v, v, y, y, y,
a, y, y, y, y, y, y, y,
a, a, y, a, a, a, y, a]

```

--- /collapse ---


--- collapse ---
---
titel: Storm
---

![Et gitter med 8 × 8 felter, der viser en stormsky.](images/storm.png)

Lavet af Team hop2p023, Spanien

```python

c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue
t = (255, 255, 0)   # Pure Yellow

image = [
c, c, c, c, c, c, c, c,
c, c, f, f, f, f, c, c,
c, f, f, f, f, f, f, c,
c, g, c, g, t, g, c, c,
c, c, c, t, t, c, c, c,
c, c, t, t, c, c, c, c,
c, c, g, c, c, c, c, g,
c, g, c, c, c, c, c, c]


```

--- /collapse ---

--- collapse ---
---
titel: And
---

![Et gitter med 8 × 8 felter, der viser en and.](images/duck.png)

Lavet af Pater, Irland

```python

c = (0, 0, 0) # Black
l = (57, 97, 17)    # Olive Green
m = (30, 65, 6)     # Forest Green
r = (232, 118, 5)   # Orange
a = (255, 255, 255) # White
b = (171, 171, 171) # Grey

image = [
c, l, l, c, c, c, c, c,
r, r, m, c, c, c, c, c,
c, l, l, c, c, c, c, c,
c, a, a, l, a, a, c, c,
c, l, l, a, a, a, b, a,
c, a, a, b, b, b, a, a,
c, c, a, a, a, a, c, c,
c, c, c, r, c, r, c, c]

```

--- /collapse ---

--- collapse ---
---
titel: Frø
---

![Et gitter med 8 × 8 felter, der viser en frø.](images/frog.png)

Lavet af Team Jmeno, Tjekkiet

```python

a = (255, 255, 255) # White
b = (171, 171, 171) # Grey
c = (0, 0, 0)       # Black
q = (255, 0, 0)     # Pure Red
j = (0, 255, 0)     # Pure Green
k = (46, 139, 33)   # Leaf Green
n = (126, 88, 25)   # Earth Brown

image = [
a, a, a, a, a, a, a, a,
a, a, a, a, a, b, a, b,
a, a, a, a, a, a, c, a,
a, a, c, a, c, a, q, a,
a, a, j, j, j, q, a, a,
a, j, j, k, q, a, a, a,
j, k, j, k, k, a, a, a,
k, k, k, j, k, n, n, n]

```

--- /collapse ---

--- collapse ---
---
titel: Blossom Tree
---

![Et gitter med 8 × 8 felter, der viser et blomstrende træ.](images/blossom.png)

Lavet af Team Zssh14, Slovakiet

```python

t = (255, 255, 0)   # Pure Yellow
g = (0, 204, 255)   # Sky Blue
w = (249, 169, 255) # Light Pink
y = (248, 97, 255)  # Magenta
z = (220, 53, 232)  # Purple
n = (126, 88, 25)   # Earth Brown
o = (179, 96, 65)   # Terracotta Brown
k = (46, 139, 33)   # Leaf Green

image =  [
t, g, g, w, w, y, g, g,
g, g, w, w, y, y, z, g,
g, w, y, z, y, z, z, z,
w, y, z, z, g, n, w, g,
g, g, o, o, n, w, y, z,
g, g, g, g, n, g, g, g,
g, g, g, o, n, n, g, g,
k, k, o, n, n, n, k, k]

```

--- /collapse ---

--- /task ---

--- task ---

**Find:** linjen, der siger `# Vis billedet”`, og tilføj en linje kode for at vise dit billede på LED-matricen:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, a, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

# Vis billedet
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Tryk på **Kør** i bunden af editoren for at se dit billede vist på LED-matrixen.

--- /task ---

--- task ---

**Fejlsøgning**

Min kode har en syntaksfejl:

- Tjek at din kode matcher koden i eksemplerne ovenfor
- Tjek at du har indrykket koden i din liste
- Tjek at din liste er omgivet af `[` og `]`
- Tjek at hver farvevariabel i listen er adskilt af et komma

Mit billede vises ikke:

- Tjek at din `sense.set_pixels(billede)` ikke er indrykket

--- /task ---


--- task ---

**Gem dine fremskridt**

Nu hvor du har vist et billede, kan du gemme dit program på Mission Starter-projektet ved at indtaste dit holdnavn, holdmedlemmers navne og den klasseværelseskode, som du har fået. Du kan genindlæse dit program på enhver enhed med internetforbindelse ved at indtaste dit teamnavn og klasseværelseskode.

![Mission Zero-knappen ‘Gem’.](images/mz_savebutton_v2.png)

--- /task --- 
