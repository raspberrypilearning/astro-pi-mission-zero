## Laat een boodschap zien en kies een naam voor de nieuwe Astro Pi-computers

--- task ---

Open de [Sense HAT emulator](https://trinket.io/mission-zero){:target="_blank"} voor het Mission Zero project.

Je zult zien dat drie lijnen code automatisch voor je werden toegevoegd:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![sense hat emulator](images/sense-hat-emulator2.png)

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

--- task --- Als je wil meedoen aan de wedstrijd om de namen voor de nieuwe Mark II Astro Pi-computers te kiezen, begin je je boodschap met de woorden "My name should be" en voeg jouw keuze uit deze lijst toe.

Bijvoorbeeld, als je wil stemmen voor Ada Lovelace, zal je code er als volgt uitzien:

```python
sense.show_message("My name should be Ada Lovelace")
```
--- /task ---



