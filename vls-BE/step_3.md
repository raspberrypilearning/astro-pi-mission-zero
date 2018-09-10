## Laat een boodschap zien

\--- task \---

Open de [Sense HAT emulator](https://trinket.io/mission-zero){:target="_blank"} voor het Mission Zero project.

Je zult zien dat drie lijnen van code automatisch voor je werden toegevoegd:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![sense Hat emulator](images/sense-hat-emulator2.png)

Deze code verbindt aan de Astro Pi en verzekert dat het Astro Pi's led-kleurenbeeldscherm op de juiste manier wordt weergegeven. Laat de code daar staan, omdat je hem later nodig hebt.

\--- /task \---

\--- task \---

Misschien kun je een leuke begroeting op de ISS achterlaten voor de astronauten die dichtbij de Astro Pi werken? Laten we een boodschap scrollen op het beeldscherm.

Voeg deze lijn toe onder de andere code:

```python
sense.show_message("Astro Pi")
```

\--- /task \---

\--- task \---

Druk op de **Run** knop en zie de boodschap `Astro Pi` scrollen op het led-kleurenbeeldscherm.

![laat de boodschap code zien klik op run](images/show-message-code-annotated.PNG)

\--- /task \---

![Boodschap scrollen](images/scroll-message.gif)

Om een andere boodschap te tonen, kun je wat je wil schrijven tussen de aanhalingstekens (`""`).

\--- collapse \---

* * *

## title: Welke tekens kunnen worden gebruikt?

De Sense HAT kan uitsluitend 1 Latijns tekenset tonen, wat betekent dat de volgende tekens uitsluitend verkrijgbaar zullen zijn. Andere tekens worden getoond als `?<0>.</p>

<pre><code>+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
`</pre> 

\--- /collapse \---

\--- taak \---

Je kunt ook de snelheid van het scrollen van de boodschap veranderen. Voeg een `scroll_speed` toe aan de lijn van de code die je reeds hebt, zoals dit:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

De versteksnelheid van de boodschap is `0.1`. Door het nummer kleiner te maken gaat het scrollen van de boodschap sneller en bij het groter maken van het nummer gaat de boodchap langzamer scrollen.

\--- /task \---