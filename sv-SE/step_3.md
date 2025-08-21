## Visa en bild

Astro Pis LED-matris kan visa färger. I det här steget kommer du att visa bilder från naturen på Astro Pis LED-matris.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
En <span style="color: #0faeb0">**LED-matris**</span> är ett rutnät av lysdioder som kan styras individuellt eller som en grupp för att skapa olika ljuseffekter. LED-matrisen på Sense HAT har 64 lysdioder som visas i ett 8 x 8 rutnät. Lysdioderna kan programmeras för att producera ett brett spektrum av färger.
</p>

![En skärmdump av emulatorfönstret som visar flygenheten med LED-matrisen som visar en bild av en blomma.](images/fu-pic.png)

--- task ---

Öppna [startprojektet Mission Zero](https://missions.astro-pi.org/sv/mz/code_submissions/){:target="_blank"}.

Du kommer att se att några rader kod har lagts till för dig automatiskt.

Den här koden ansluter till Astro Pi, ser till att Astro Pis LED-display visas på rätt sätt och ställer in färgsensorn. Lämna kvar koden där, för du kommer att behöva den.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Importera biblioteken
from sense_hat import SenseHat from time import sleep

# Ställ in Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Ställ in färgsensorn
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![En skärmdump av Sense HAT-emulatorn med rader med startkod som visas i den vänstra rutan.](images/sense-hat-emulator3.png)

--- /task ---

### RGB-färger

Färger kan skapas med olika proportioner av rött, grönt och blått. Du kan läsa mer om RGB färger här:

[[[generic-theory-simple-colours]]]

LED-matrisen är ett 8 x 8 rutnät. Varje lysdiod på nätet kan ställas in på olika färger. Här är en lista med variabler för 24 olika färger. Varje färg har ett värde för rött, grönt och blått:

[[[ambient-colours]]]

### Välj en bild

--- task ---

**Välj:** Välj en bild att visa från alternativen nedan. Python lagrar informationen för en bild i en lista. Koden för varje bild inkluderar de färgvariabler som används och listan.

Du måste **kopiera** hela koden för din valda bild och sedan **klistra in** den i ditt projekt under raden som säger `# Lägg till färgvariabler och bild`.

--- collapse ---

---
titel: Räv
---

![Ett rutnät med 8 x 8 rutor som visar ett rävansikte.](images/fish.png)

Skapad av team i_pupi, Italien

```python
z = (153, 50, 204) # MörkOrkidé
q = (255, 255, 0) # Gul
d = (51, 153, 255) # blå
c = (0, 0, 0) # Svart

bild = [
d, d, z, d, d, d, d,
d, d, d, z, z, d, d,
z, d, q, q, q, q, d, d,
z, z, q, q, q, c, q, d,
z, z, z, q, q, q, q, d,
z, z, q, q, q, q, q, d,
z, d, q, z, z, q, d, d,
d, d, d, z, d, d, d]

```

--- /collapse ---


--- collapse ---

---
titel: Valross
---

![Ett rutnät med 8 x 8 rutor som visar en valross.](images/walrus.png)

Skapad av team Walrus, Finland

```python
h = (0, 255, 255) # Cyan
c = (0, 0, 0) # Svart
s = (139, 69, 19) # Sadelbrun
a = (255, 255, 255) # Vit
r = (184, 134, 11) # MörkGuldris

bild = [
h, h, h, h, h, h, h, h,
h, h, s, s, s, h, h, h,
h, s, s, s, s, s, h, h,
h, s, c, s, c, s, s, s,
h, r, r, r, r, r, s, s,
h, h, a, s, a, s, s, s,
h, h, a, s, a, s, s, s,
r, r, s, s, s, s, s, s, s]

```

--- /collapse ---

--- collapse ---
---
titel: Paxi
---

![Ett rutnät med 8 x 8 rutor som visar Paxi.](images/paxi.png)

Skapad av teamet tony_pi, Italien

```python
v = (255, 0, 0) # Röd
m = (34, 139, 34) # Skogsgrön
c = (0, 0, 0) # Svart 
e = (100, 149, 237) # Blåklintblå
l = (0, 255, 0) # Grön

bild = [
    c, v, m, c, c, m, v, c,
    c, c, v, v, v, v, c, c,
    c, v, c, e, l, e, v, c,
    c, v, c, l, l, l, v, c,
    c, v, c, l, c, l, v, c,
    c, c, v, v, v, v, c, c,
    c, c, l, c, c, l, c, c,
    c, m, m, c, c, m, m, c]

```

--- /collapse ---


--- collapse ---
---
titel: Hund
---

![Ett rutnät med 8 x 8 rutor som visar ett hundhuvud.](images/dog.png)

Skapad av team ptpr_07, Spanien

```python

c = (0, 0, 0) # Svart
r = (184, 134, 11) # MörkGuldris
s = (139, 69, 19) # Sadelbrun
y = (255, 20, 147) # Mörkrosa

bild = [
    c, r, r, c, c, r, r, c,
    c, r, s, s, s, s, r, c,
    c, r, c, s, s, c, r, c,
    c, s, s, s, s, s, s, c,
    c, s, s, s, s, s, s, c,
    c, s, s, c, c, s, s, c,
    c, c, s, y, y, s, c, c,
    c, c, c, y, y, c, c, c]


```

--- /collapse ---

--- collapse ---
---
titel: Kameleont
---

![Ett rutnät med 8 x 8 rutor som visar en regnbågsfärgad kameleont.](images/chameleon.png)

Skapad av teamet The_ETs, Storbritannien

```python

c = (0, 0, 0) # Svart
s = (139, 69, 19) # Sadelbrun
a = (255, 255, 255) # Vit
v = (255, 0, 0) # Röd
t = (255, 140, 0) # Mörkorange
q = (255, 255, 0) # Gul
m = (34, 139, 34) # Skogsgrön
h = (0, 255, 255) # Cyan
z = (153, 50, 204) # Mörkorkidé
y = (255, 20, 147) # Mörkrosa

bild = [
    a, a, v, v, t, a, a,
    a, v, v, t, t, q, a, a,
    v, c, t, t, q, q, m, a,
    v, t, t, q, q, m, m, h,
    s, s, q, s, s, m, s, h,
    a, a, a, a, a, a, a, z,
    a, a, a, a, y, a, a, z,
    a, a, a, a, a, a, y, z, a]

```

--- /collapse ---

--- collapse ---
---
titel: Drake
---

![Ett rutnät med 8 x 8 rutor som visar en drake.](images/kite.png)

Skapad av team Val, Grekland

```python

c = (0, 0, 0) # Svart
m = (34, 139, 34) # Skogsgrön
v = (255, 0, 0) # Röd
q = (255, 255, 0) # Gul
e = (0, 0, 205) # Mellanblå
h = (0, 255, 255) # Cyan

bild = [
    h, h, h, h, h, h, h, h, 
    h, h, h, e, e, v, v, h, 
    h, h, h, e, e, v, v, h, 
    h, h, h, q, q, m, m, h, 
    h, h, h, q, q, m, m, h,
    h, h, c, h, h, h, h, h, 
    h, c, h, h, h, h, h, h, 
    c, h, h, h, h, h, h, h, h]

```

--- /collapse ---

--- collapse ---
---
titel: Kyckling
---

![Ett rutnät med 8 x 8 rutor som visar en kyckling.](images/chicken.png)

Skapad av teamet Slepicky, Tjeckien

```python

v = (255, 0, 0) # Röd
c = (0, 0, 0) # Svart
b = (105, 105, 105) # Dimgrå
q = (255, 255, 0) # Gul
r = (184, 134, 11) # MörkGuldris

bild = [
    c, c, v, v, v, c, c, c,
    c, v, b, b, r, c, c, r,
    c, b, c, b, c, b, c, r, b,
    q, r, b, b, b, b, b, b, r,
    c, v, b, b, b, b, r, b,
    c, v, b, r, r, r, b, r,
    c, c, c, r, b, q, r, c,
    c, c, c, c, q, q, c, c]

```

--- /collapse ---

--- /task ---

--- task ---

**Hitta:** den linje som säger `# Visa bilden` och lägg till en rad kod för att visa din bild på LED-matrisen:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 18, 19
---
z = (153, 50, 204) # MörkOrkidé q = (255, 255, 0) # Gul d = (51, 153, 255) # blå c = (0, 0, 0) # Svart

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

# Visa bilden
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Tryck på **Kör** längst ner i editorn för att se din bild visas på LED-matrisen.

--- /task ---

--- task ---

**Felsökning**

Min kod har ett syntaxfel:

- Kontrollera att din kod matchar koden i exemplen ovan
- Kontrollera att du har dragit in koden i din lista
- Kontrollera att din lista är omgiven av `[` och `]`
- Kontrollera att varje färgvariabel i listan är avgränsad med ett kommatecken

Min bild visas inte:

- Kontrollera att din `sense.set_pixels(image)` inte är indragen

--- /task ---


--- task ---

**Spara dina framsteg**

Nu när du har visat en bild kan du spara ditt program i Mission Starter-projektet genom att ange ditt teamnamn, teammedlemmarnas namn och klassrumskoden som du fått. Du kan ladda om programmet på vilken enhet som helst med en internetanslutning genom att ange teamets namn och klassrumskod.

![Mission Zero Spara-knapp.](images/mz_savebutton_v2.png)

--- /task --- 
