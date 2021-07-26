## Mérd meg a páratartalmat!

The humidity sensor in the Astro Pi can measure the humidity in the air around it, a useful feature to help you gather data about the conditions in space.

![Üzenet a páratartalomról](images/degrees-message.gif)

Az Astro Pi az ISS-en a páratartalmat a levegőben levő víz százalékos arányaként méri meg.

A küldetésedhez tartozik a Nemzetközi Űrállomás legénységének napi életéhez való hozzájárulás, úgyhogy, ha tudatod velük, hogy az űrállomáson a páratartalom a normális tartományon belül van, azzal megnyugtatod őket.

[[[generic-theory-what-is-humidity]]]

--- task ---

Add hozzá ezt a kódot a páratartalom leolvasásához:

```python
humid = sense.humidity
```

Ez a sor az aktuális páratartalmat méri majd meg, és a `humid` változóban tárolja a mért értéket.

--- /task ---

--- task ---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. You can round the value to any number of decimal places. In the example we have rounded to one decimal place, but for a different level of precision, change the number `1` to the number of decimal places you would like to see.

```python
humid = round( sense.humidity, 1 )
```

--- /task ---

--- task ---

Az aktuális páratartalom futó üzenetként való megjelenítéséhez add hozzá ezt a kódsort:

```python
sense.show_message( str(humid) )
```

A `str()` rész a páratartalmat számból szöveggé alakítja, hogy az Astro Pi meg tudja jeleníteni.

--- /task ---

--- task ---

Egy másik üzenet részeként is megjelenítheted a páratartalmat az üzeneted különböző részeit egy `+` jellel összekötve.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

--- /task ---

A valódi Astro Pi a körülötte levő páratartalmat méri majd, de a Sense HAT emulátor páratartalom-csúszkájával szimulálhatod a páratartalom-változásokat és tesztelheted a kódod.

![Páratartalom csúszka](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.
