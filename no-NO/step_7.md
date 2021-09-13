## Vise luftfuktigheten

Du kan kombinere luftfuktighetsavlesningen med et bilde for å angi luftfuktigheten på en grafisk måte i tillegg. For eksempel kan du vise et hav for høy luftfuktighet, og en ørken for lav luftfuktighet:

![Fuktig og tørt](images/wet-dry.png)

--- task ---

På slutten av programmet kan dere opprette flere fargevariabler for fargene dere vil bruke i bildene. Dere har kanskje allerede definert noen av dem i et tidligere trinn.

```python
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)
```

--- /task ---

--- task ---

Som tidligere begynner dere med å opprette en liste for hver av dem, og deretter angir dere farger for punktene på listen slik dere vil at bildene skal være.

```python
wet = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


dry = [
  c, c, g, g, c, c, c, c,
  c, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, g, g, g, g, g, c, c,
  c, c, g, g, c, c, c, c,
  y, y, y, y, y, y, y, y,
  y, y, y, y, y, y, y, y
]
```

--- /task ---

--- task ---

Legg til kode for å få luftfuktigheten:

```python
humid = sense.get_humidity()
```

--- /task ---

--- task ---

Nå bestemmer dere hvilket bilde som skal vises. I dette eksemplet vil vi vise et `wet` (fuktig) bilde hvis luftfuktigheten er 40% eller høyere, og et `dry` (tørt) bilde hvis luftfuktigheten er under 40%.

```python
humid = sense.get_humidity()
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

Bruk skyveknappen for luftfuktighet til å angi en luftfuktighet på emulatoren. Kjør programmet og kontroller at bildet dere har valgt for den luftfuktigheten vises riktig.

--- /task ---

--- task ---

Endre koden slik at programmet viser luftfuktigheten til astronautene slik dere har valgt.

--- /task ---

--- task --- Test koden din med forskjellige fuktighetsinnstillinger (ved hjelp av glidebryteren) for å sikre at den alltid kjører riktig. Hvis dere har fulgt eksemplet ovenfor, vises et bilde både når fuktigheten er satt til en verdi mindre enn 40% og når den er satt til mer enn 40%?

--- /task ---
