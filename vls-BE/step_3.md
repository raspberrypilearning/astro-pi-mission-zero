## Laat een afbeelding zien

De afbeelding die je laat zien zal gemaakt worden door 64 gekleurde vierkanten die **pixels** genoemd worden. De pixels staan gesorteerd in een raster van 8 x 8. Elke pixel kan een andere kleur hebben. Door de kleuren zorgvuldig te kiezen, kan je een afbeelding maken. Dit is een voorbeeld van een walvis gemaakt door verschillende tinten blauw te gebruiken op een zwarte achtergrond.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Een <span style="color: #0faeb0">**LED-matrix**</span> is een raster met LEDs die individueel of in groep bestuurd kunnen worden om verschillende lichteffecten te creëeren. De LED matrix op de Sense HAT heeft 64 LEDs die in een raster van 8 x 8 getoond worden. De LEDs kunnen geprogrammeerd worden om een breeder gamma van kleuren te maken.
</p>

![een 8x8 afbeelding van een walvis met letters die verschillende kleuren bepalen](images/whale.png)

Merk op dat elk vierkant gelabeld is met een code om een specifieke kleur voor te stellen. In deze afbeelding worden er 3 kleuren gebruikt:
+ c = zwart
+ f = oceaanblauw
+ g = hemelsblauw


--- task ---

Open het [Mission ZeroMission Zero start project](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"}.

Je zal zien dat er enkele coderegels automatisch toegevoegd werden.

Deze code maakt verbinding met de Astro Pi, zorgt ervoor dat de LED-display van de Astro Pi op de juiste manier getoond wordt en installeert de kleursensor. Laat de code staan, want je zal ze nodig hebben.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Importeer de bibliotheken
from sense_hat import SenseHat from time import sleep

# Installeer de Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Installeer de kleursensor
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Een screenshot van de Sense HAT-emulator met de lijnen van de begincode die getoond wordt aan de linkerkant.](images/sense-hat-emulator3.png)

--- /task ---

### RGB-kleuren

Kleuren kunnen gemaakt worden door het gebruik van rood, groen en blauw in verschillende verhoudingen. Je kan hier meer info over RGB-kleuren vinden:

![Drie schuifknoppen tonen de RGB-kleurwaardes](images/rgbsliders.gif)

De LED-matrix is een raster van 8 x 8. Elke LED op het raster kan in een andere kleur ingesteld worden. We kunnen de letters van a tot z gebruiken zodat de namen van de variabelen 24 verschillende kleuren voorstellen. Elke kleur heeft een waarde voor rood, groen en blauw.

--- collapse ---

---
titel: Lijst van kleurvariabelen
---

![Een raster van 24 gekleurde vierkanten, elke gelabeld met een andere letter van het alfabet](images/palette.png)

```python
a = (255, 255, 255) # Wit
b = (171, 171, 171) # Grijs
c = (0, 0, 0)       # Zwart
d = (25, 25, 113)   # Marineblauw 
e = (0, 0, 255)     # Puur blauw
f = (36, 128, 200)  # Oceaanblauw
g = (0, 204, 255)   # Hemelsblauw
h = (86, 255, 255)  # Electricsch Cyaan
j = (0, 255, 0)     # Puur Groen
k = (46, 139, 33)   # Bladgroen
l = (57, 97, 17)    # Olijfgroen
m = (30, 65, 6)     # Bosgroen
n = (126, 88, 25)   # Aardebruin
o = (179, 96, 65)   # Terracottabruin
p = (180, 34, 34)   # Baksteenrood
q = (255, 0, 0)     # Puur rood
r = (232, 118, 5)   # Oranje
s = (241, 231, 100) # Lichtgeel
t = (255, 255, 0)   # Puur geel
u = (255, 209, 209) # Bleek roze
v = (255, 177, 177) # Blush roze
w = (249, 169, 255) # Licht roze
y = (248, 97, 255)  # Magenta
z = (220, 53, 232)  # Paars

```

--- /collapse ---

### Kies een afbeelding

--- task ---

**Kies** Kies een afbeelding om te tonen uit de opties hieronder. Python slaat de informatie voor een afbeelding op in een lijst. De code voor elke afbeelding bevat de kleurvariabelen die gebruikt worden en de lijst.

Je zal alle code moeten **kopieren** voor je gekozen afbeelding en dan **plakken** in je project onder de lijn waar staat `# Voeg kleurvariabelen en afbeelding toe`.

--- collapse ---

---
titel: Walvis
---

![Een raster met 8 x 8 vierkanten die een walvis tonen.](images/whale.png)

Gemaakt door Team Naicom, Italië

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
titel: Citroen
---

![Een raster met 8 x 8 vierkanten die een citroen tonen.](images/lemon.png)

Gemaakt door team g4lemoni, Griekenland

```python
a = (255, 255, 255) # White
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
titel: Varken
---

![Een raster met 8 x 8 vierkanten die een varken tonen.](images/pig.png)

Gemaakt door Gary, Verenigd Koninkrijk

```python
a = (255, 255, 255) # White
u = (255, 209, 209) # Pale Pink
v = (255, 177, 177) # Blush Pink
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

![Een raster met 8 x 8 vierkanten dat een stormwolk toont.](images/storm.png)

Created by team hop2p023, Spain

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
title: Duck
---

![Een raster met 8 x 8 veirkanten dat een eend toont.](images/duck.png)

Created by Peter, Ireland

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
title: Frog
---

![Een raster met 8 x 8 vierkanten dat een kikker toont.](images/frog.png)

Created by team Jmeno, Czech Republic

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
title: Blossom Tree
---

![Een raster met 8 x 8 vierkanten dat een boom met bloesems toont.](images/blossom.png)

Created by team Zssh14, Slovakia

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

**Vind:** de regel die zegt `# Toon de afbeelding` en voeg een codelijn toe om je afbeelding op de LED-matrix weer te geven:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, a, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

# Toon de afbeelding
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Druk **Run** onderaan de editor om je afbeelding te zien op de LED-matrix.

--- /task ---

--- task ---

**Fouten oplossen**

Mijn code geeft een foutmelding:

- Controleer dat je code overeenkomt met de code in de voorbeelden hierboven
- Controleer dat je de code gecopieerd hebt in je lijst
- Controleer dat je lijst omgeven wordt door `[` en `]`
- Controleer dat elke kleurvariabele in de lijst gescheiden wordt door een komma

Mijn afbeelding wordt niet getoond:

- Controleer dat je `sense.set_pixels(afbeelding)` niet opgeslagen werd

--- /task ---


--- task ---

**Sla je voortgang op**

Nu dat je een beeld getoond hebt, kan je je programma opslaan op het Mission Starter project door de naam van je team, de namen van de teamleden en de klascode die je ontving in te geven. Je kan je programma nu opnieuw laden op eender welk apparaat met een internetverbinding door je teamnaam en klascode in te geven.

![Knop om Mission Zero op te slaan.](images/mz_savebutton_v2.png)

--- /task --- 
