## Toon een afbeelding

De afbeelding die je weergeeft, is opgebouwd uit 64 gekleurde vierkantjes, genaamd **pixels**. De pixels zijn gerangschikt in een raster van 8 x 8. Elke pixel kan een andere kleur hebben. Door de kleuren zorgvuldig te kiezen, kun je een afbeelding creëren. Hier is een voorbeeld van een walvis gemaakt met verschillende tinten blauw op een zwarte achtergrond.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Een <span style="color: #0faeb0">**LED-matrix**</span> is een raster van LED's die afzonderlijk of als groep kunnen worden aangestuurd om verschillende lichteffecten te creëren. De LED-matrix op de Sense HAT heeft 64 LED's die worden weergegeven in een 8 x 8 raster. De LED's kunnen worden geprogrammeerd om een breed scala aan kleuren te produceren.
</p>

![een afbeelding van 8x8 cm van een walvis met letters die verschillende kleuren aanduiden](images/whale.png)

Merk op dat elk vierkantje is voorzien van een code die een bepaalde kleur vertegenwoordigt. In deze afbeelding worden 3 kleuren gebruikt:
+ c = zwart
+ f = Oceaanblauw
+ g = Hemelsblauw


--- task ---

Open het [Mission Zero-startproject](https://missions.astro-pi.org/nl/mz/code_submissions/){:target="_blank"}.

Je zult zien dat er automatisch enkele regels met code voor je zijn toegevoegd.

Deze code maakt verbinding met de Astro Pi en zorgt ervoor dat het LED-display van de Astro Pi op de juiste manier wordt weergegeven en doet de set up van de kleurensensor. Laat de code staan, want je hebt hem nodig.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Importeer de bibliotheken
from sense_hat import SenseHat from time import sleep

# Stel de Sense HAT in
sense = SenseHat() sense.set_rotation(270, False)

# Stel de kleurensensor in
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Een schermafbeelding van de Sense HAT emulator met enkele regels startcode weergegeven in het linkervenster.](images/sense-hat-emulator3.png)

--- /task ---

### RGB-kleuren

Kleuren kunnen worden gemaakt met verschillende verhoudingen van rood, groen en blauw. Meer informatie over de RGB kleuren vind je hier:

![Drie schuifregelaars die RGB kleurwaarden laten zien](images/rgbsliders.gif)

De LED-matrix is een 8 x 8 raster. Elke LED op het raster kan op een andere kleur worden ingesteld. We kunnen de letters a tot en met z gebruiken als namen voor variabelen om 24 verschillende kleuren weer te geven. Elke kleur heeft een waarde voor rood, groen en blauw.

--- collapse ---

---
title: Lijst met kleurvariabelen
---

![Een raster van 24 gekleurde vierkantjes, elk voorzien van een label met een andere letter van het alfabet](images/palette.png)

```python
a = (255, 255, 255) # Wit
b = (171, 171, 171) # Grijs
c = (0, 0, 0) # Zwart
d = (25, 25, 113) # Marineblauw
e = (0, 0, 255) # Puur blauw
f = (36, 128, 200) # Oceaanblauw
g = (0, 204, 255) # Hemelsblauw
h = (86, 255, 255) # Elektrisch cyaan
j = (0, 255, 0) # Puur groen
k = (46, 139, 33) # Bladgroen
l = (57, 97, 17) # Olijfgroen
m = (30, 65, 6) # Bosgroen
n = (126, 88, 25) # Aardbruin
o = (179, 96, 65) # Terracotta bruin
p = (180, 34, 34) # Baksteenrood
q = (255, 0, 0) # Puur rood
r = (232, 118, 5) # Oranje
s = (241, 231, 100) # Bleekgeel
t = (255, 255, 0) # Puur geel
u = (255, 209, 209) # Bleekroze
v = (255, 177, 177) # Blush roze
w = (249, 169, 255) # Lichtroze
y = (248, 97, 255) # Magenta
z = (220, 53, 232) # Paars

```

--- /collapse ---

### Kies een afbeelding

--- task ---

You can either choose one of the example images below or create your own original design. Feel free to draw anything you like - such as an animal, plant, or imaginary creature - as long as it follows the Mission Zero guidelines.

**Kies:** Kies een afbeelding om weer te geven uit de onderstaande opties. Python slaat de informatie voor een afbeelding op in een lijst. De code voor elke afbeelding bevat de gebruikte kleurvariabelen en de lijst.

Je moet alle code **kopiëren** voor je gekozen afbeelding en **plak** het in je project onder de regel `# Voeg kleurvariablen en afbeelding toe`.

--- collapse ---

---
title: Walvis
---

![Een raster met 8 x 8 vierkantjes die een walvis tonen.](images/whale.png)

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
title: Citroen
---

![Een raster met 8 x 8 vierkantjes die een citroen tonen.](images/lemon.png)

Gemaakt door team g4lemoni, Griekenland

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
title: Varken
---

![Een raster met 8 x 8 vierkantjes die een varken tonen.](images/pig.png)

Gemaakt door Gary, Verenigd Koninkrijk

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
title: Storm
---

![Een raster met 8 x 8 vierkantjes die een stormwolk tonen.](images/storm.png)

Gemaakt door team hop2p023, Spanje

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
title: Eend
---

![Een raster met 8 x 8 vierkantjes die een eend tonen.](images/duck.png)

Gemaakt door Peter, Ierland

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
title: Kikker
---

![Een raster met 8 x 8 vierkantjes die een kikker tonen.](images/frog.png)

Gemaakt door team Jmeno, Tsjechische Republiek

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
title: Bloesemboom
---

![Een raster met 8 x 8 vierkantjes die een boom in bloesem tonen.](images/blossom.png)

Gemaakt door team Zssh14, Slowakije

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

**Zoek:** de regel `# Toon de afbeelding` en voeg een regel code toe om je afbeelding op de LED-matrix weer te geven:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, a, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

# Geef de afbeelding weer
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Druk op de **Run** knop onderaan de editor, en zie je bericht weergegeven op de LED matrix.

--- /task ---

--- task ---

**Fouten oplossen (Debuggen)**

Mijn code heeft een syntax fout:

- Controleer of je code overeenkomt met de code in de bovenstaande voorbeelden
- Controleer of je de code in je lijst hebt ingesprongen
- Controleer of je lijst is omgeven door `[` en `]`
- Controleer of elke kleurvariabele in de lijst is gescheiden door een komma

Mijn afbeelding verschijnt niet:

- Controleer of je `sense.set_pixels(afbeelding)` niet ingesprongen is

--- /task ---


--- task ---

**Sla je voortgang op**

Nu je een afbeelding hebt weergegeven, kun je je programma opslaan in het Mission Start-project door je teamnaam, de namen van de teamleden en de klascode die je hebt gekregen in te voeren. Je kunt je programma herladen op elk apparaat met een internetverbinding door je teamnaam en klascode in te voeren.

![Mission Zero Save-knop](images/mz_savebutton_v2.png)

--- /task --- 
