## Reagálj a páratartalomra!

A leolvasott páratartalmat egy képpel is összekapcsolhatod, hogy a páratartalmat grafikusan is szemléltesd. Például megjeleníthetsz egy óceánt magas páratartalomnál, és egy sivatagot alacsony páratartalomnál:

![Nedves és száraz](images/wet-dry.png)

--- task ---

A programod végén hozz létre még több színváltozót azokra a színekre, amelyeket használni szeretnél a képeidben. Lehetséges, hogy van olyan, amit már egy előző lépésben meghatároztál.

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

Akárcsak korábban, a képeid megrajzolásához hozz létre egy listát mindegyiknek, majd állítsd be a listaelemeket azokra a színekre, amelyekre szeretnéd a pixeleidet beszínezni.

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

Add hozzá a kódot, hogy megkapd a páratartalmat:

```python
humid = sense.get_humidity()
```

--- /task ---

--- task ---

Most döntsd el, melyik képet szeretnéd megjeleníteni. Ebben a példában mi a `wet` („nedves”) képet jelenítjük majd meg, ha a mért páratartalom 40% vagy annál magasabb, és a `dry` („száraz”) képet, ha a páratartalom 40%-nál alacsonyabb.

```python
humid = sense.get_humidity()
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

Használd a páratartalom-csúszkát az emulátoron a páratartalom beállításához. Futtasd a programod és ellenőrizd le, hogy a kép, amelyet az adott a páratartalomhoz kiválasztottál, helyesen jelenik-e meg.

--- /task ---

--- task ---

Változtasd meg a kódot, hogy a programod az általad választott módon jelenítse meg a páratartalmat az űrhajósok számára.

--- /task ---

--- task --- Teszteld a kódodat több különböző páratartalom-beállítással (ehhez mozgasd a csúszkát), hogy megbizonyosodj róla, mindig helyesen fut-e. Ha követted a fenti példát, megjelenik-e valamelyik kép akkor is, ha 40% alatt van a páratartalom, és akkor is, ha 40% felett van?

--- /task ---
