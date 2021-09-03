## Laat een boodschap zien en kies een naam voor de nieuwe Astro Pi-computers

--- task ---

Open de [Sense HAT emulator](https://trinket.io/mission-zero){:target="_blank"} voor het Mission Zero project.

Je zult zien dat drie lijnen code automatisch voor je werden toegevoegd:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![Een screenshot van de Trinket Sense Hat-emulator met drie regels startcode wordt getoond op de linkerhelft van het scherm.](images/sense-hat-emulator2.png)

Deze code maakt verbinding met de Astro Pi en zorgt ervoor de het LED-scherm van de Astro Pi op de juiste manier weergegeven wordt. Laat de code staan, want je zal ze nodig hebben.

--- /task ---

--- task ---

Misschien kan je een leuke begroeting achterlaten voor de astronauten die in de buurt van de Astro Pi op het ISS werken? Laten we een boodschap over het scherm laten rollen.

Voeg deze lijn toe onder de andere code:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Druk op de **Run** knop en zie de boodschap `Astro Pi` over het LED-scherm rollen.

![De Trinket Sense HAT-emulator waarop een voorbeeldprogramma draait die de tekst "Astro PI" over de LED-matrix laat scrollen in witte letters](images/M0_1.gif)

--- /task ---

Om een andere boodschap te tonen, kan je wat je maar wil schrijven tussen de aanhalingstekens (`""`).

--- collapse ---
---
title: Welke tekens kunnen worden gebruikt?
---

De Sense HAT kan alleen de Latijnse tekenset met 1 karakter tonen, wat betekent dat alleen de volgende karakters beschikbaar zijn. Andere karakters zullen weergegeven worden als een `?`.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

Je kan de weergavesnelheid van de boodschap die over het scherm rolt ook aanpassen. Voeg een `scroll_speed` toe aan de codelijn die je al hebt, op deze manier:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

De startsnelheid van de boodschap is `0.1`. Als je het getal kleiner maakt, zal de boodschap sneller bewegen en het getal vergroten zal de boodschap trager doen bewegen.

--- /task ---

### Kies een naam voor de nieuwe Astro Pi-computers

--- task -- We zullen de Astro Pi-computers noemen naar twee inspirerende Europese wetenschappers. Er zijn honderden mannen en vrouwen die bijgedragen hebben tot wetenschap en technologie, deelnemers kunnen hun eigen naam voorstellen of kiezen uit onze lijst met suggesties:

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

Om te stemmen, begin je je boodschap met de woorden "My name should be". Bijvoorbeeld, als je wil stemmen van Ada Lovelace, zal je code er als volgt uitzien:

```python
sense.show_message("My name should be Ada Lovelace")
```

Als je wil stemmen, moet je boodschpa beginnen met deze woorden, anders kunnen we je deelname niet registreren.

--- /task ---



