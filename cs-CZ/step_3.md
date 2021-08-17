## Zobraz zprávu a vyber název nových počítačů Astro Pi

--- task ---

Otevři [emulátor Sense HAT](https://trinket.io/mission-zero){:target="_blank"} pro založení projektu Mission Zero.

Uvidíš tři řádky kódu, které tam už budou automaticky přichystané:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![Snímek obrazovky emulátoru Trinket Sense Hat se třemi řádky startovacího kódu zobrazeným v levém panelu.](images/sense-hat-emulator2.png)

Tenhle kód slouží k připojení k Astro Pi a zajistí, že se jeho LED displej bude zobrazovat správně. Ten kód tam nech, protože ho budeš potřebovat.

--- /task ---

--- task ---

Nechceš třeba astronauty na ISS, kteří pracují poblíž Astro Pi, nějak hezky pozdravit? Pojďme na displeji zobrazit běžící vzkaz.

Pod kód, který už tam je, přidej tenhle řádek:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Stiskni tlačítko **Run** (spustit) a dívej se, jak zpráva `Astro Pi` běží přes LED displej.

![Emulátor Trinket Sense HAT, na kterém je spuštěn ukázkový program, který posouvá bílý text „Astro Pi“ po LED matici](images/M0_1.gif)

--- /task ---



Pokud chceš zobrazit nějakou jinou zprávu, napiš ji mezi uvozovky (`""`).

--- collapse ---

---
title: Jaké znaky můžeš použít?
---

Sense HAT dokáže zobrazit pouze znakovou sadu Latin 1, což znamená, že dostupné budou pouze následující znaky. Ostatní znaky se zobrazí jako `?`.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

Můžeš také změnit rychlost, jakou zpráva poběží přes displej. Ke kódu, který už máš, přidej `scroll_speed`, například takhle:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Výchozí rychlost zprávy je `0,1`. (Pozor, v Pythonu se nepíše desetinná čárka, ale desetinná tečka!) Když číslo zmenšíš, zpráva poběží rychleji, a když ho zvětšíš, poběží pomaleji.

--- /task ---

### Vyber název nových počítačů Astro Pi

--- task --- Počítače Astro Pi pojmenujeme po dvou inspirujících evropských vědcích. K vědě a technologii přispěly stovky mužů a žen a účastníci mohou navrhnout své vlastní názvy nebo si vybrat z našeho seznamu návrhů:


[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"} 
[Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing){:target="_blank"} 
[Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel){:target="_blank"} 
[Edsger Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra){:target="_blank"} 
[Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr){:target="_blank"} 
[Hypatia](https://en.wikipedia.org/wiki/Hypatia){:target="_blank"} 
[John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone){:target="_blank"} 
[Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie){:target="_blank"} 
[Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla){:target="_blank"} 
[Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe){:target="_blank"}

Pokud chceš hlasovat, začni svoji zprávu slovy „My name should be“. Chceš-li například hlasovat pro Adu Lovelaceovou, tvůj kód by vypadal takhle:

```python
sense.show_message("My name should be Ada Lovelace")
```

Pokud chceš hlasovat, *musí* tvoje zpráva začínat těmito slovy, jinak nebudeme moci tvůj příspěvek započítat.

--- /task ---



