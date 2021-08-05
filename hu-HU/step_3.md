## Jeleníts meg egy üzenetet és válassz nevet az új Astro Pi számítógépeknek!

--- task ---

Nyisd meg a Mission Zero projekthez tartozó [Sense HAT emulátort](https://trinket.io/mission-zero){:target="_blank"}.

Látni fogod, hogy három kódsort már automatikusan hozzáadtunk neked:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![A screenshot of the Trinket Sense Hat emulator with three lines of starter code displayed in the left hand pane.](images/sense-hat-emulator2.png)

Ez a kód az Astro Pi-hoz kapcsolódik, és biztosítja, hogy az Astro Pi LED kijelzője a helyes irányba mutat. Hagyd meg a kódot, mert szükséged lesz rá!

--- /task ---

--- task ---

Akár egy kedves üzenetet is hagyhatsz a Nemzetközi Űrállomás űrhajósainak, akik az Astro Pi közelében dolgoznak! Futtassunk egy üzenetet a kijelzőn keresztül.

Írd be ezt a sort a többi kód alá:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Kattints a **Run** (Futtatás) gombra, és figyeld, hogy fut az `Astro Pi` üzenet keresztül a LED kijelzőn!

![üzenet megjelenítéséhez kattints a futtatásra](images/show-message-code-annotated.PNG)

--- /task ---

![Képernyőn átfutó üzenet](images/scroll-message.gif)

Egy másik üzenet megjelenítéséhez írj be az idézőjelek (`""`) közé bármit, amit szeretnél.

--- collapse ---

---
title: Milyen karaktereket lehet használni?
---

A Sense HAT csak a Latin 1-es karakterkészletet tudja megjeleníteni, ami azt jelenti, hogy csak a lentebb látható karakterek lesznek elérhetők. Minden más karakter `?`-ként jelenik majd meg.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

Az üzenet képernyőn való végigfutásának sebességét is megváltoztathatod. Add a `scroll_speed` paramétert a kódsorodhoz, valahogy így:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Az üzenet alapértelmezett sebessége `0.1`. Ha kisebb számot írsz be, az üzenet gyorsabban fut majd, a nagyobb számok pedig lelassítják az üzenetet.

--- /task ---

### Válassz nevet az új Astro Pi számítógépeknek

--- task --- We will name the Astro Pi computers after two inspirational European scientists. There are hundreds of men and women that have contributed to science and technology, and participants can suggest their own names, or pick from our list of suggestions:


[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"} \ [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing){:target="_blank"} \ [Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel){:target="_blank"} \ [Edsgar Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra){:target="_blank"} \ [Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr){:target="_blank"} \ [Hypatia](https://en.wikipedia.org/wiki/Hypatia){:target="_blank"} \ [John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone){:target="_blank"} \ [Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie){:target="_blank"} \ [Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla){:target="_blank"} \ [Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe){:target="_blank"} \

To vote, start your message with the words "My name should be". For example, you want to vote for Ada Lovelace, your code would look like this:

```python
sense.show_message("My name should be Ada Lovelace")
```
--- /task ---



