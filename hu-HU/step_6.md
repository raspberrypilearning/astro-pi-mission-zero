## Mérd meg a hőmérsékletet!

Az Astro Pi hőmérsékletérzékelője képes a körülötte levő levegő hőmérsékletének mérésére. Ez egy hasznos funkció, amely segít az űrbeli viszonyokról szóló adatgyűjtésben.

![Üzenet a hőmérsékletről](images/degrees-message.gif)

Az Astro Pi a Nemzetközi Űrállomáson Celsius-fokban méri a hőmérsékletet (&deg;C). Mivel az űrben sokkal nagyobb a hőmérsékletingadozás, mint a Földön, az Astro Pi akár -40 Celsius-foktól egészen +120 Celsius-fokig képes a hőmérsékletet mérni.

A küldetésedhez tartozik a Nemzetközi Űrállomás legénységének napi életéhez való hozzájárulás, úgyhogy, ha tudatod velük, hogy az űrállomáson a hőmérséklet a normális tartományon belül van, azzal megnyugtatod őket.

--- collapse ---
---
title: Mi a hőmérséklet?
---

A hőmérséklet azt méri, milyen forró valami. Lehet, hogy egy orvosi vizit során már mérték a te hőmérsékletedet is egy hőmérővel.

![Hőmérő](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} via Wikimedia Commons*

Pontosabban, a hőmérséklet egy anyag hőenergia-mennyiségének mértéke. Ahogy azt te is tudod, a jégkocka szilárd, de ahogy felmelegszik, azaz elnyeli a környezet hőenergiáját, elolvad és folyékonnyá válik. Ez azért van, mert amikor egy anyag elég hőenergiát nyel el vagy veszít el, az anyag halmazállapota megváltozik, pl. egy szilárd halmazállapotú anyag folyékonnyá válik.

--- /collapse ---

--- task ---

Add hozzá ezt a kódot a hőmérséklet leolvasásához:

```python
temp = sense.temperature
```

Ez a sor az aktuális hőmérsékletet méri majd meg, és a `temp` változóban tárolja a mért értéket.

--- /task ---

--- task ---

A hőmérséklet nagyon pontosan kerül rögzítésre, azaz a tárolt érték sok tizedesjegyet fog tartalmazni. Az értéket akárhány tizedesjegyre lekerekítheted. A példában egy tizedesjegyre kerekítettük le, de ha más szintű pontosságot szeretnél, változtasd meg az `1`-es számot arra számra, ahány tizedesjegyet szeretnél látni.

```python
temp = round( sense.temperature, 1 )
```

--- /task ---

--- task ---

Az aktuális hőmérsékletet futó üzenetként való megjelenítéséhez add hozzá ezt a kódsort:

```python
sense.show_message( str(temp) )
```

A `str()` rész a hőmérsékletet számból szöveggé alakítja, hogy az Astro Pi meg tudja jeleníteni.

--- /task ---

--- task ---

Egy másik üzenet részeként is megjelenítheted a hőmérsékletet az üzeneted különböző részeit egy `+` jellel összekötve.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

--- /task ---

A valódi Astro Pi a körülötte levő hőmérsékletet méri majd, de a Sense HAT emulátor hőmérséklet-csúszkájával szimulálhatod a hőmérsékletváltozásokat és tesztelheted a kódod.

![Hőmérsélet-csúszka](images/temperature-slider.png)

**Megjegyzés:** Furcsa lehet, hogy a hőmérséklet-csúszka egy egész számként mutatja a hőmérsékletet, de a leolvasott érték egy tizedes tört lesz. Az emulátor a valódi érzékelő enyhe pontatlanságát szimulálja, úgyhogy a mért hőmérséklet, amit látsz, kicsit nagyobb vagy kisebb lehet annál az értéknél, amit a csúszkával állítottál be.