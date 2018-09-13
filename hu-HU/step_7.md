## Jelenítsd meg a hőmérsékletet!

A leolvasott hőmérsékletet egy képpel is összekapcsolhatod, hogy a hőmérsékletet grafikusan is szemléltesd. Például hideg idő esetén egy hóvihart is megjeleníthetsz, vagy egy napfényes képet meleg idő esetén:

![Hideg és meleg](images/hot-and-cold.png)

--- task ---

A programod végén hozz létre még több színváltozót azokra a színekre, amelyeket használni szeretnél a képeidben. Lehetséges, hogy van olyan, amit már egy előző lépésben meghatároztál. A mi példáinkban fehéret (`w`), sárgát (`y`), zöldet (`g`) és feketét/kitöltetlent (`b`) használunk.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

--- /task ---

--- task ---

Akárcsak korábban, a képeid megrajzolásához hozz létre egy listát mindegyiknek, majd állítsd be a listaelemeket azokra a színekre, amelyekre szeretnéd a pixeleidet beszínezni.

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

Add hozzá a kódot, hogy megkapd a hőmérsékletet:

```python
temp = sense.get_temperature()
```

--- /task ---

--- task ---

Most döntsd el, melyik képet szeretnéd megjeleníteni. Ebben a példában mi a `hot` („meleg”) képet jelenítjük majd meg, ha a mért hőmérséklet 20 fok vagy annál magasabb, és a `cold` („hideg”) képet, ha a hőmérséklet 20 foknál alacsonyabb.

```python
temp = sense.get_temperature()
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

--- /task ---

--- task ---

Használd a hőmérséklet-csúszkát az emulátoron a hőmérséklet beállításához. Futtasd a programod és ellenőrizd le, hogy a kép, amelyet az adott a hőmérséklethez kiválasztottál, helyesen jelenik-e meg.

--- /task ---

--- task ---

Változtasd meg a kódot, hogy a programod az általad választott módon jelenítse meg a hőmérsékletet az űrhajósok számára.

--- /task ---