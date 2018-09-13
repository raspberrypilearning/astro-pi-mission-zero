## Jeleníts meg egy üzenetet!

--- task ---

Nyisd meg a MIssion Zero projekthez tartozó [Sense HAT emulátort](https://trinket.io/mission-zero){:target="_blank"}.

Látni fogod, hogy három kódsort már automatikusan hozzáadtunk neked:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![sense hat emulátor](images/sense-hat-emulator2.png)

Ez a kód az Astro Pi-hoz kapcsolódik, és biztosítja, hogy az Astro Pi LED kijelzője a helyes irányba mutat. Hagyd meg a kódot, mert szükséged lesz rá!

--- /task ---

--- task ---

Akár egy kedves üzenetet is hagyhatsz a Nemzetközi Űrállomás űrhajósainak, akik az Astro Pi közelében dolgoznak! Futtassunk egy üzenetet keresztül a kijelzőn!

Írd be ezt a sort a többi kód alá:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Kattints a **Run** (Futtatás) gombra, és figyeld, hogy fut az `Astro Pi` üzenet keresztül a LED kijelzőn!

![üzenet kód megmutatása kattints futtatás](images/show-message-code-annotated.PNG)

--- /task ---

![Képernyőn átfutó üzenet](images/scroll-message.gif)

Egy másik üzenet megjelenítéséhez írj be az idézőjelek (`""`) közé bármit, amit szeretnél .

--- collapse ---
---
title: Milyen karaktereket lehet használni?
---
A Sense HAT csak a Latin 1-es karakterkészletet tudja megjeleníteni, ami azt jelenti, hogy csak a lentebb látható karakterek lesznek elérhetők. Minden más karakter `?`-ként jelenik majd meg.

    +-*/!"#$><0123456789.=)(
    
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    abcdefghijklmnopqrstuvwxyz
    
    ?,;:|@%[&_']~
    

--- /collapse ---

--- task ---

Az üzenet képernyőn való végigfutásának sebességét is megváltoztathatod. Add a `scroll_speed` sort a kódsorodhoz, valahogy így:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Az üzenet alapértelmezett sebessége `0.1`. Ha kisebb számot írsz be, az üzenet gyorsabban fut majd, a nagyobb számok pedig lelassítják az üzenetet.

--- /task ---