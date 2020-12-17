## Mérd meg a páratartalmat!

Az Astro Pi páratartalom-érzékelője képes a körülötte levő levegő páratartalmának mérésére. Ez egy hasznos funkció, amely segít az űrbeli viszonyokról szóló adatgyűjtésben.

![Üzenet a páratartalomról](images/degrees-message.gif)

Az Astro Pi az ISS-en a páratartalmat a levegőben levő víz százalékos arányaként méri meg.

A küldetésedhez tartozik a Nemzetközi Űrállomás legénységének napi életéhez való hozzájárulás, úgyhogy, ha tudatod velük, hogy az űrállomáson a páratartalom a normális tartományon belül van, azzal megnyugtatod őket.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Add hozzá ezt a kódot a páratartalom leolvasásához:

```python
humid = sense.get_humidity()
```

Ez a sor az aktuális páratartalmat méri majd meg, és a `humid` változóban tárolja a mért értéket.

\--- /task \---

\--- task \---

A páratartalom nagyon pontosan kerül rögzítésre, azaz a tárolt érték sok tizedesjegyet fog tartalmazni. Az értéket akárhány tizedesjegyre lekerekítheted. A példában egy tizedesjegyre kerekítettük le, de ha más szintű pontosságot szeretnél, változtasd meg az `1`-es számot arra számra, ahány tizedesjegyet szeretnél látni.

```python
humid = round(sense.get_humidity(), 1)
```

\--- /task \---

\--- task \---

Az aktuális páratartalom futó üzenetként való megjelenítéséhez add hozzá ezt a kódsort:

```python
sense.show_message(str(humid))
```

A `str()` rész a páratartalmat számból szöveggé alakítja, hogy az Astro Pi meg tudja jeleníteni.

\--- /task \---

\--- task \---

Egy másik üzenet részeként is megjelenítheted a páratartalmat az üzeneted különböző részeit egy `+` jellel összekötve.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

\--- /task \---

A valódi Astro Pi a körülötte levő páratartalmat méri majd, de a Sense HAT emulátor páratartalom-csúszkájával szimulálhatod a páratartalom-változásokat és tesztelheted a kódod.

![Páratartalom csúszka](images/humidity-slider.png)

**Megjegyzés:** Furcsa lehet, hogy a páratartalom-csúszka egy egész számként mutatja a páratartalmat, de a leolvasott érték egy tizedes tört lesz. Az emulátor a valódi érzékelő enyhe pontatlanságát szimulálja, úgyhogy a mért páratartalom, amit látsz, kicsit nagyobb vagy kisebb lehet annál az értéknél, amit a csúszkával állítottál be.