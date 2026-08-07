## Rodyti vaizdą

Jūsų rodomas vaizdas bus sudarytas iš 64 spalvotų kvadratų, vadinamų **pikseliais**. Pikseliai yra išdėstyti 8 x 8 tinklelyje. Kiekvienas pikselis gali būti skirtingos spalvos. Atidžiai pasirinkdami spalvas, galite sukurti norimą vaizdą. Štai banginio, sukurto naudojant skirtingus mėlynos spalvos atspalvius juodame fone, pavyzdys.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**LED matrica**</span> – tai LED tinklelis, kurį galima valdyti atskirai arba kaip grupę, siekiant sukurti skirtingus apšvietimo efektus. „Sense HAT“ LED matricą sudaro 64 LED diodai, rodomi 8 x 8 tinklelyje. Šviesos diodus galima užprogramuoti taip, kad jie skleistų platų spalvų spektrą.
</p>

![8x8 banginio atvaizdas su raidėmis, žyminčiomis skirtingas spalvas](images/whale.png)

Atkreipkite dėmesį, kad kiekvienas kvadratas yra pažymėtas kodu, kuris žymi tam tikrą spalvą. Šiame paveikslėlyje panaudotos 3 spalvos:
+ c = juoda
+ f = šviesiai mėlyna
+ g = dangaus mėlyna


--- task ---

Atidarykite [„Mission Zero“ pradinį projektą](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"}.

Pamatysite, kad kelios kodo eilutės buvo pridėtos automatiškai.

Šis kodas prisijungia prie „Astro Pi“, užtikrina, kad „Astro Pi“ LED ekranas būtų rodomas teisingai, ir nustato spalvų jutiklį. Palikite kodą, nes jo prireiks.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
---
# Importuoti bibliotekas
from sense_hat import SenseHat
from time import sleep

# Nustatyti Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Nustatyti spalvų jutiklį
sense.color.gain = 60 # Nustatyti jutiklio jautrumą
sense.color.integration_cycles = 64 # Intervalas, kuriuo bus imamas rodmuo

--- /code ---

![„Sense HAT“ emuliatoriaus ekrano kopija su pradinio kodo eilutėmis, rodomomis kairiajame lange.](images/sense-hat-emulator3.png)

--- /task ---

### RGB spalvos

Spalvos gali būti kuriamos naudojant skirtingas raudonos, žalios ir mėlynos spalvų proporcijas. Apie RGB spalvas galite sužinoti čia:

![Trys slankikliai, rodantys RGB spalvų vertes](images/rgbsliders.gif)

LED matrica yra 8 x 8 tinklelis. Kiekvieną tinklelio šviesos diodą galima nustatyti šviesi skirtinga spalva. Raides nuo a iki z galime naudoti kaip kintamųjų pavadinimus, reiškiančius 24 skirtingas spalvas. Kiekviena spalva turi savo raudonos, žalios ir mėlynos spalvos reikšmę.

--- collapse ---

---
pavadinimas: Spalvų kintamųjų sąrašas
---

![24 spalvotų kvadratėlių tinklelis, kuriame kiekvienas kvadratėlis pažymėtas skirtinga abėcėlės raide](images/palette.png)

```python
a = (255, 255, 255) # Balta
b = (171, 171, 171) # Pilka
c = (0, 0, 0) # Juoda
d = (25, 25, 113) # Tamsiai mėlyna
e = (0, 0, 255) # Tikra mėlyna
f = (36, 128, 200) # Šviesiai mėlyna
g = (0, 204, 255) # Dangaus mėlyna
h = (86, 255, 255) # Elektrinė žydra
j = (0, 255, 0) # Tikra žalia
k = (46, 139, 33) # Lapų žalia
l = (57, 97, 17) # Alyvuogių žalia
m = (30, 65, 6) # Miško žalia
n = (126, 88, 25) # Žemės ruda
o = (179, 96, 65) # Terakotos ruda
p = (180, 34, 34) # Plytų raudona
q = (255, 0, 0) # Tikra raudona
r = (232, 118, 5) # Oranžinė
s = (241, 231, 100) # Šviesiai geltona
t = (255, 255, 0) # Tikra geltona
u = (255, 209, 209) # Blyškiai rožinė
v = (255, 177, 177) # Švelniai rožinė
w = (249, 169, 255) # Šviesiai rožinė
y = (248, 97, 255) # Purpurinė
z = (220, 53, 232) # Violetinė

```

--- /collapse ---

### Pasirinkite vaizdą

--- task ---

**Pasirinkite:** iš toliau pateiktų parinkčių pasirinkite paveikslėlį, kurį norite rodyti. „Python“ saugo paveikslėlio informaciją sąraše. Kiekvieno paveikslėlio kode yra naudojami spalvų kintamieji ir jų sąrašas.

Reikės **nukopijuoti** visą pasirinkto paveikslėlio kodą, tada **įklijuoti** jį į savo projektą po eilute `# Pridėti spalvų kintamuosius ir vaizdą`.

--- collapse ---

---
pavadinimas: Banginis
---

![8 x 8 kvadratų tinklelis, kuriame pavaizduotas banginis.](images/whale.png)

Sukūrė „Naicom“ komanda, Italija

```python
c = (0, 0, 0)       # Juoda
f = (36, 128, 200)  # Vandenyno mėlyna
g = (0, 204, 255)   # Dangaus mėlyna

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
pavadinimas: Citrina
---

![8 x 8 kvadratų tinklelis, kuriame pavaizduota citrina.](images/lemon.png)

Sukūrė „g4lemoni“ komanda, Graikija

```python
c = (0, 0, 0)       # Juoda
k = (46, 139, 33)   # Lapų žalia
t = (255, 255, 0)   # Tikra geltona

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
pavadinimas: Kiaulė
---

![8 x 8 kvadratų tinklelis, kuriame pavaizduota kiaulė.](images/pig.png)

Sukūrė Gary, Jungtinė Karalystė

```python
a = (255, 255, 255) # Balta
v = (255, 177, 177) # Švelniai rožinė
y = (248, 97, 255)  # Purpurinė
o = (179, 96, 65)   # Terakotos ruda
c = (0, 0, 0)       # Juoda

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
pavadinimas: Audra
---

![8 x 8 kvadratų tinklelis, kuriame pavaizduotas audros debesis.](images/storm.png)

Sukūrė „hop2p023“ komanda, Ispanija

```python

c = (0, 0, 0)       # Juoda
f = (36, 128, 200)  # Vandenyno mėlyna
g = (0, 204, 255)   # Dangaus mėlyna
t = (255, 255, 0)   # Tikra geltona

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
pavadinimas: Antis
---

![8 x 8 kvadratų tinklelis, kuriame pavaizduota antis.](images/duck.png)

Sukūrė Peter, Airija

```python

c = (0, 0, 0) # Juoda
l = (57, 97, 17)    # Alyvuogių žalia
m = (30, 65, 6)     # Miško žalia
r = (232, 118, 5)   # Oranžinė
a = (255, 255, 255) # Balta
b = (171, 171, 171) # Pilka

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
pavadinimas: Varlė
---

![8 x 8 kvadratų tinklelis, kuriame pavaizduota varlė.](images/frog.png)

Sukūrė „Jmeno“ komanda, Čekija

```python

a = (255, 255, 255) # Balta
b = (171, 171, 171) # Pilka
c = (0, 0, 0)       # Juoda
q = (255, 0, 0)     # Tikra raudona
j = (0, 255, 0)     # Tikra žalia
k = (46, 139, 33)   # Lapų žalia
n = (126, 88, 25)   # Žemės ruda

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
pavadinimas: Žydintis medis
---

![8 x 8 kvadratų tinklelis, kuriame pavaizduotas žydintis medis.](images/blossom.png)

Sukūrė „Zssh14“ komanda, Slovakija

```python

t = (255, 255, 0)   # Tikra geltona
g = (0, 204, 255)   # Dangaus mėlyna
w = (249, 169, 255) # Šviesiai rožinė
y = (248, 97, 255)  # Purpurinė
z = (220, 53, 232)  # Violetinė
n = (126, 88, 25)   # Žemės ruda
o = (179, 96, 65)   # Terakotos ruda
k = (46, 139, 33)   # Lapų žalia

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

**Raskite:** eilutę, kurioje parašyta `# Rodyti vaizdą` ir pridėkite kodo eilutę, kad jūsų vaizdas būtų rodomas LED matricoje:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Juoda
f = (36, 128, 200)  # Vandenyno mėlyna
g = (0, 204, 255)   # Dangaus mėlyna

image = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, a,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

# Rodyti vaizdą
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Paspauskite **Paleisti** redagavimo įrankio apačioje, kad pamatytumėte, kaip jūsų paveikslėlis atrodys LED matricoje.

--- /task ---

--- task ---

**Derinti**

Mano kode yra sintaksės klaida:

- Patikrinkite, ar jūsų kodas atitinka pirmiau pateiktuose pavyzdžiuose pateiktą kodą
- Patikrinkite, ar į sąraše pateikėte kodą su įtrauka
- Patikrinkite, ar jūsų sąrašas pradeda ir baigiasi `[` ir `]`
- Patikrinkite, ar kiekvienas sąraše esantis spalvos kintamasis yra atskirtas kableliu

Mano paveikslėlis nerodomas:

- Patikrinkite, ar jūsų `sense.set_pixels(image)` pateiktas be įtraukos

--- /task ---


--- task ---

**Išsaugokite savo progresą**

Peržiūrėję paveikslėlį galite išsaugoti savo programą misijos pradiniame projekte, įvesdami savo komandos pavadinimą, komandos narių vardus ir jums suteiktą klasės kodą. Programą galite įkelti iš naujo bet kuriame įrenginyje, turinčiame interneto ryšį, įvesdami savo komandos pavadinimą ir klasės kodą.

![„Mission Zero“ išsaugojimo mygtukas.](images/mz_savebutton_v2.png)

--- /task --- 
