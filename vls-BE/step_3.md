## Laat een boodschap zien en kies een naam voor de nieuwe Astro Pi-computers

--- task ---

Open de [Sense HAT emulator](https://trinket.io/mission-zero){:target="_blank"} voor het Mission Zero project.

Je zult zien dat drie lijnen code automatisch voor je werden toegevoegd:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![A screenshot of the Trinket Sense Hat emulator with three lines of starter code displayed in the left hand pane.](images/sense-hat-emulator2.png)

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

![laat de boodschapcode zien klik op run](images/show-message-code-annotated.PNG)

--- /task ---

![Boodschap scrollen](images/scroll-message.gif)

Om een andere boodschap te tonen, kun je wat je maar wil tussen de aanhalingstekens schrijven (`""`).

--- collapse ---

---
titel: Welke tekens kunnen worden gebruikt?
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

--- task --- We will name the Astro Pi computers after two inspirational European scientists. There are hundreds of men and women that have contributed to science and technology, and participants can suggest their own names, or pick from our list of suggestions:


[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"} \ [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing){:target="_blank"} \ [Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel){:target="_blank"} \ [Edsgar Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra){:target="_blank"} \ [Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr){:target="_blank"} \ [Hypatia](https://en.wikipedia.org/wiki/Hypatia){:target="_blank"} \ [John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone){:target="_blank"} \ [Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie){:target="_blank"} \ [Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla){:target="_blank"} \ [Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe){:target="_blank"} \

To vote, start your message with the words "My name should be". For example, you want to vote for Ada Lovelace, your code would look like this:

```python
sense.show_message("My name should be Ada Lovelace")
```
--- /task ---



