## Vise et bilde

Dere kan vise bilder på Astro Pi's LED-matrise. Kanskje hilsenen til astronautene kan inkludere et bilde eller et mønster, i tillegg til eller i stedet for en skriftlig melding?

![Et skjermbilde av emulatorvinduet som viser flyenheten med LED -matrisen som viser et bilde av selve flyenhenten](images/fu-pic.png)

--- task ---

På slutten av programmet oppretter dere noen fargevariabler for å definere fargene dere vil tegne bildet med. Du kan bruke så mange farger du vil, men i dette eksemplet bruker vi bare noen få farger - rød (`r`), hvit (`w`), svart (`b`) og to gråtoner (`g` og `s`). Legg merke til at nyansene oppnås ved å redusere mengden lys i alle tre kanalene, samtidig som forholdene er de samme.

```python
w = (255, 255, 255)
b = (0, 0, 0)
g = (50,50,50)
s = (200,255,200)
r = (255,0,0)
```

**Merk:** Denne gangen er det en god ide å gi fargevariablene enkeltbokstavsnavn, for det vil spare tid i neste trinn, der de skal skrives inn mange ganger. Dessuten vil bruk av enkeltbokstaver gjøre det enklere å se bildet dere vil tegne.

--- /task ---

--- task ---



Under de nye variablene lager dere en liste med 64 punkter. Hvert punkt representerer en piksel på LED-matrisen, og tilsvarer en av fargevariablene dere definerte. Tegn bildet ved å sette en variabel der dere vil at den angitte fargen skal vises. Vi har tegnet en Astro Pi ved å bruke de svarte (`b`)-pikslene som bakgrunn og de grå (`g`)-pikslene for å tegne metalldelene til Astro Pi kabinettet:

```python
 picture = [
    g, b, b, b, b, b, b, g,
    b, g, g, g, g, g, g, b,
    b, g, b, b, g, w, g, g,
    b, g, b, b, g, g, g, g,
    b, g, g, g, s, s, g, g,
    b, g, r, g, g, g, g, g,
    b, g, g, g, g, g, g, b,
    g, b, b, b, b, b, b, g
    ]
```
--- /task ---

--- task ---

Legg til en kodelinje for å vise bildet på LED-skjermen.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Trykk **Run** (Kjør) for å se bildet på skjermen.

--- /task ---

--- task ---

Dere vil kanskje legge til koder for å få et kort tidsrom (eller `sleep` (søvn)) etter at bildet er vist. Dette gir astronautene tid til å se bildet før neste del av meldingen vises. På toppen av programmet legger dere til:

```python
from time import sleep
```

På linjen etter den som viser bildet, legger dere til denne koden for å få et opphold på to sekunder:

```python
sleep(2)
```

--- /task ---

--- task ---

Lag ditt eget bilde eller mønster for å vise til astronautene!

--- /task ---
