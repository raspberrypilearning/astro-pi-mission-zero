## Vise et bilde

Bildet du viser, vil bestå av 64 fargede firkanter kalt **piksler**. Pikslene er ordnet i et rutenett på 8x8 ruter. Hver piksel kan ha en egen farge. Ved å velge fargene nøye kan du skape et bilde. Her er et eksempel på en hval laget med forskjellige nyanser av blått på svart bakgrunn.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
En <span style="color: #0faeb0">**LED-matrise**</span> er et rutenett av LED-pærer som kan styres individuelt eller som en gruppe for å skape forskjellige lyseffekter. LED-matrisen på Sense HAT har 64 LED'er som vises i 8 x 8 rutenett. LED-pærene kan programmeres til å produsere en lang rekke farger.
</p>

![et 8x8 felt stort bilde av en hval med bokstaver som markerer forskjellige farger](images/whale.png)

Legg merke til at hver rute er merket med en kode som representerer en bestemt farge. I dette bildet er det brukt 3 farger:
+ c = svart
+ f = havblå
+ g = himmelblå


--- task ---

Åpne [Mission Zero startprosjektet](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"}.

Du vil se at et par kodelinjer er lagt til automatisk for deg.

Denne koden kobles til Astro Pi, sørge for at Astro Pi's LED-skjerm vises på riktig måte rundt og setter opp fargesensoren. La koden være, du vil trenge den senere.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Importer bibliotekene
from sense_hat import SenseHat from time import sleep

# Sett opp Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Sett opp fargesensoren
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Et skjermbilde av Sense HAT-emulatoren med linjer med startkode vist i venstre panel.](images/sense-hat-emulator3.png)

--- /task ---

### RGB farger

Farger kan lages ved hjelp av ulike deler av rød, grønn og blå. Du kan finne ut om RGB farger her:

![Tre glidebrytere som viser RGB-fargeverdier](images/rgbsliders.gif)

LED-matrisen er et 8 x 8-rutenett. Hver LED på rutenettet kan settes til en annen farge. Vi kan bruke bokstavene a til å som navn på variabler for å representere 24 forskjellige farger. Hver farge har en verdi for rød, grønn og blå.

--- collapse ---

---
tittel: Liste over fargevariabler
---

![Et rutenett med 24 fargede firkanter, hver merket med en egen bokstav](images/palette.png)

```python
a = (255, 255, 255) # Hvit
b = (171, 171, 171) # Grå
c = (0, 0, 0) # Svart
d = (25, 25, 113) # Marineblå
e = (0, 0, 255) # Ren blå
f = (36, 128, 200) # Havblå
g = (0, 204, 255) # Himmelblå
h = (86, 255, 255) # Elektrisk cyan
j = (0, 255, 0) # Ren grønn
k = (46, 139, 33) # Bladgrønn
l = (57, 97, 17) # Olivengrønn
m = (30, 65, 6) # Skoggrønn
n = (126, 88, 25) # Jordbrun
o = (179, 96, 65) # Terrakottabrun
p = (180, 34, 34) # Mursteinsrød
q = (255, 0, 0) # Ren rød
r = (232, 118, 5) # Oransje
s = (241, 231, 100) # Blekgul
t = (255, 255, 0) # Ren gul
u = (255, 209, 209) # Blekrosa
v = (255, 177, 177) # Blush-rosa
w = (249, 169, 255) # Lys rosa
y = (248, 97, 255) # Magenta
z = (220, 53, 232) # Lilla

```

--- /collapse ---

### Velg et bilde

--- task ---

**Velg:** Velg et bilde for visning blant valgene nedenfor. Python lagrer informasjonen for et bilde i en liste. Koden for hvert bilde inneholder fargevariablene som er brukt, og listen.

Du må **kopiere** all koden for det valgte bildet og **lime inn** den inn i prosjektet under linjen som sier `# Legg til fargevariabler og bilde`.

--- collapse ---

---
tittel: Hval
---

![Et rutenett med 8 x 8 ruter som viser en hval.](images/whale.png)

Laget av team Naicom fra Italia

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
tittel: Sitron
---

![Et rutenett med 8 x 8 ruter som viser en sitron.](images/lemon.png)

Laget av team g4lemoni fra Hellas

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
tittel: Gris
---

![Et rutenett med 8 x 8 ruter som viser en gris.](images/pig.png)

Laget av Gary fra Storbritannia

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
tittel: Storm
---

![Et rutenett med 8 x 8 ruter som viser en stormsky.](images/storm.png)

Laget av team hop2p023 fra Spania

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
tittel: And
---

![Et rutenett med 8 x 8 ruter som viser en and.](images/duck.png)

Laget av Peter fra Irland

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
tittel: Frosk
---

![Et rutenett med 8 x 8 ruter som viser en frosk.](images/frog.png)

Laget av team Jmeno fra Tsjekkia

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
tittel: Blomstrende tre
---

![Et rutenett med 8 x 8 ruter som viser et blomstrende tre.](images/blossom.png)

Laget av team Zssh14 fra Slovakia

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

**Finn:** linjen med teksten `# Vis bildet`, og legg til en kodelinje for å vise bildet på LED-matrisen:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, a, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

# Vis bildet
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Trykk **Kjør** nederst i editoren for å se bildet vist på LED-matrisen.

--- /task ---

--- task ---

**Debug**

Min kode har en syntaksfeil:

- Kontroller at koden samsvarer med koden i eksemplene ovenfor
- Sjekk at du har skrevet inn koden i listen din
- Sjekk at listen din er omgitt av `[` and `]`
- Kontroller at hver fargevariabel i listen er adskilt med et komma

Bildet mitt vises ikke:

- Sjekk at din `sense.set_pixels(bilde)` ikke er innrykket

--- /task ---


--- task ---

**Lagre fremgangen din**

Nå som du har vist et bilde, kan du lagre programmet ditt på Mission Starter-prosjektet ved å skrive inn lagnavnet ditt, lagmedlemmenes navn og klasseromskoden du har fått. Du kan laste inn programmet på nytt på en hvilken som helst enhet med internettforbindelse ved å skrive inn lagnavnet og klasseromskoden.

![Lagreknappen for Mission Zero.](images/mz_savebutton_v2.png)

--- /task --- 
