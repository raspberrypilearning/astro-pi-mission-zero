## Toon een bericht en kies een naam voor de nieuwe Astro Pi computers

--- task ---

Open de [Sense HAT-emulator](https://trinket.io/mission-zero){:target="_blank"} voor het Mission Zero-project.

Je zult zien dat er automatisch drie regels met code voor je zijn toegevoegd:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![A screenshot of the Trinket Sense Hat emulator with three lines of starter code displayed in the left hand pane.](images/sense-hat-emulator2.png)

Deze code maakt verbinding met de Astro Pi en zorgt ervoor dat het LED-display van de Astro Pi op de juiste manier wordt weergegeven. Laat de code daar staan, want je hebt hem nodig.

--- /task ---

--- task ---

Misschien kun je een leuke groet achterlaten voor de astronauten in het ISS die in de buurt van de Astro Pi werken? Laten we een bericht over het scherm scrollen.

Voeg deze regel toe onder de andere code:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Druk op de **Run** knop en kijk terwijl het bericht `Astro Pi` over het LED-display scrolt.

![toon berichtcode klik op uitvoeren](images/show-message-code-annotated.PNG)

--- /task ---

![Scrollend bericht](images/scroll-message.gif)

Om een ​​ander bericht weer te geven, kun je alles wat je maar wilt tussen de aanhalingstekens (`""`) schrijven.

--- collapse ---

---
title: Welke tekens kunnen worden gebruikt?
---

De Sense HAT kan alleen de tekenset Latin 1 weergeven, wat betekent dat alleen de volgende tekens beschikbaar zullen zijn. Andere tekens worden weergegeven als een `?`.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

Je kunt ook de snelheid veranderen van het bericht dat over het scherm scrolt. Voeg een `scroll_speed` (scroll_snelheid) toe aan de regel met code die je al hebt, zoals deze:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

De standaardsnelheid van het bericht is `0.1`. Door het getal kleiner te maken, scrolt het bericht sneller en door het groter te maken, scrolt het bericht langzamer.

--- /task ---

### Kies een naam voor de nieuwe Astro Pi computers

--- task --- We will name the Astro Pi computers after two inspirational European scientists. There are hundreds of men and women that have contributed to science and technology, and participants can suggest their own names, or pick from our list of suggestions:


[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"} \ [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing){:target="_blank"} \ [Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel){:target="_blank"} \ [Edsgar Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra){:target="_blank"} \ [Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr){:target="_blank"} \ [Hypatia](https://en.wikipedia.org/wiki/Hypatia){:target="_blank"} \ [John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone){:target="_blank"} \ [Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie){:target="_blank"} \ [Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla){:target="_blank"} \ [Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe){:target="_blank"} \

To vote, start your message with the words "My name should be". For example, you want to vote for Ada Lovelace, your code would look like this:

```python
sense.show_message("Mijn naam zou Ada Lovelace moeten zijn")
```
--- /task ---



