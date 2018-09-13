## Vise et bilde

Dere kan vise bilder på Astro Pi's LED-matrise. Kanskje hilsenen til astronautene kan inkludere et bilde eller et mønster, i tillegg til eller i stedet for en skriftlig melding?

![Astronaut](images/astronaut-pic.png)

--- task ---

På slutten av programmet oppretter dere noen fargevariabler for å definere fargene dere vil tegne bildet med. Dere kan bruke så mange farger dere vil, men i dette eksemplet bruker vi bare to — hvit (`w`) og svart (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Merk:** Denne gangen er det en god ide å gi fargevariablene enkeltbokstavsnavn, for det vil spare tid i neste trinn, der de skal skrives inn mange ganger. Dessuten vil bruk av enkeltbokstaver gjøre det enklere å se bildet dere vil tegne.

--- /task ---

--- task ---

Under de nye variablene lager dere en liste med 64 punkter. Hvert punkt representerer en piksel på LED-matrisen, og tilsvarer en av fargevariablene dere definerte. Tegn bildet ved å sette en variabel der dere vil at den angitte fargen skal vises. Vi har tegnet en astronaut ved å bruke de svarte (`b`)-pikslene som bakgrunn og de hvite (`w`)-pikslene for å tegne astronautens romdrakt:

```python
picture = [
b, b, w, w, w, w, b, b,
b, w, b, b, b, b, w, b,
b, w, b, w, w, b, w, b,
b, w, b, b, b, b, w, b,
b, b, w, w, w, w, b, b,
b, b, w, w, w, w, b, b,
b, w, w, w, w, w, w, b,
b, w, w, w, w, w, w, b
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
fra tid importer søvn
```

På linjen etter den som viser bildet, legger dere til denne koden for å et opphold på to sekunder:

```python
sleep(2)
```

--- /task ---

--- task ---

Lag et eget bilde eller mønster for å vise til astronautene!

--- /task ---