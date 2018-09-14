## Vise temperaturen

Du kan kombinere temperaturavlesningen med et bilde for å angi temperaturen på en grafisk måte i tillegg. Dere kan for eksempel vise en snøstorm for minustemperaturer og en solskinnsdag for plusstemperaturer:

![Varmt og kaldt](images/hot-and-cold.png)

--- task ---

På slutten av programmet kan dere opprette flere fargevariabler for fargene dere vil bruke i bildene. Dere har kanskje allerede definert noen av dem i et tidligere trinn. I våre eksempler vil vi bruke hvit (`w`), gul (`y`), grønn (`g`) og svart/tomt (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

--- /task ---

--- task ---

Som tidligere begynner dere med å opprette en liste for hver av dem, og deretter angir dere farger for punktene på listen slik dere vil at bildene skal være.

```python
hot = [
b, b, b, b, b, y, y, b,
b, b, b, b, y, y, y, y,
b, b, b, b, b, y, y, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
g, g, g, g, g, g, g, g,
g, g, g, g, g, g, g, g
]


cold = [
b, b, w, b, b, b, w, b,
b, b, b, b, b, w, b, b,
b, w, b, b, b, b, b, w,
b, b, b, b, w, b, b, b,
w, b, b, w, b, b, w, b,
b, b, b, b, b, b, b, b,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w
]
```

--- /task ---

--- task ---

Legg til koder for å få temperaturen:

```python
temp = sense.get_temperature()
```

--- /task ---

--- task ---

Nå bestemmer dere hvilket bilde som skal vises. I dette eksemplet vil vi vise et `hot` (varmt) bilde hvis temperaturavlesningen er 20 grader eller høyere, og et `cold` (kaldt) bilde hvis temperaturen er under 20 grader.

```python
temp = sense.get_temperature()
if temp >= 20:
    sense.set_pixels(varm)
else:
    sense.set_pixels(kald)
```

--- /task ---

--- task ---

Bruk temperaturregulatoren til å angi en temperatur på emulatoren. Kjør programmet og kontroller at bildet dere har valgt for den temperaturen, vises riktig.

--- /task ---

--- task ---

Endre koden slik at programmet viser temperaturen til astronautene slik dere har valgt.

--- /task ---