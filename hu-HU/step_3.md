## Jeleníts meg egy üzenetet és válassz nevet az új Astro Pi számítógépeknek!

--- task ---

Nyisd meg a Mission Zero projekthez tartozó [Sense HAT emulátort](https://trinket.io/mission-zero){:target="_blank"}.

Látni fogod, hogy három kódsort már automatikusan hozzáadtunk neked:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![Képernyőkép a Sense Hat emulátorról a három sornyi kezdőkóddal a bal oldali panelen.](images/sense-hat-emulator2.png)

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

![A Trinket Sense HAT emulátor egy példakódot futtat, amely az "Astro PI" szöveget futtatja végig a LED-mátrixon fehér betűkkel](images/M0_1.gif)

--- /task ---

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

--- task --- Az Astro Pi számítógépeket két inspiráló európai tudósról fogjuk elnevezni. Több száz férfi és nő járult hozzá a tudományhoz és technológiához, és a résztvevők javasolhatják a saját neveiket, vagy választhatnak a javasolt nevek listájáról:


[Ada Lovelace](https://hu.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"} 
[Alan Turing](https://hu.wikipedia.org/wiki/Alan_Turing){:target="_blank"} 
[Caroline Herschel](https://sciencemeetup.444.hu/2016/03/08/a-tudomany-volt-a-principiuma-caroline-herschel){:target="_blank"} 
[Edsger Dijkstra](https://hu.wikipedia.org/wiki/Edsger_Wybe_Dijkstra){:target="_blank"} 
[Hedy Lamarr](https://hu.wikipedia.org/wiki/Hedy_Lamarr){:target="_blank"} 
[Hypatia](https://hu.wikipedia.org/wiki/Alexandriai_H%C3%BCpatia){:target="_blank"} 
[John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone){:target="_blank"} 
[Marie Curie](https://hu.wikipedia.org/wiki/Marie_Curie){:target="_blank"} 
[Nikola Tesla](https://hu.wikipedia.org/wiki/Nikola_Tesla_(feltal%C3%A1l%C3%B3)){:target="_blank"} 
[Tycho Brahe](https://hu.wikipedia.org/wiki/Tycho_Brahe){:target="_blank"}

A szavazáshoz kezdd az üzenetedet így: "My name should be" ("A nevem legyen ..."). Például ha Ada Lovelace-ra szeretnél szavazni, akkor így nézzen ki a kódod:

```python
sense.show_message("My name should be Ada Lovelace")
```

Ha szeretnél szavazni, az üzenetednek *kötelezően* ezekkel a szavakkal kell kezdődnie, különben nem fogjuk tudni automatikusan beszámítani a szavazatodat. 

--- /task ---



