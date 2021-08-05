## Vise en melding og velge et navn for de nye Astro Pi datamaskinene

--- task ---

Åpne [Sense HAT-emulatoren](https://trinket.io/mission-zero){:target="_blank"} for Mission Zero-prosjektet.

Du vil se at tre kodelinjer er lagt til automatisk for deg:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![A screenshot of the Trinket Sense Hat emulator with three lines of starter code displayed in the left hand pane.](images/sense-hat-emulator2.png)

Denne koden kobler til Astro Pi og sørger for at Astro Pi's LED-skjerm vises den riktige veien. La koden være der, du vil trenge den senere.

--- /task ---

--- task ---

Kanskje du vil legge til en hyggelig hilsen til astronautene på ISS som jobber i nærheten av Astro Pi? La oss rulle en melding over skjermen.

Legg til denne linjen under den andre koden:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Trykk på **Run** (Kjør)-knappen og se meldingen `Astro Pi` rulle over LED-skjermen.

![vis meldingskoden klikk run](images/show-message-code-annotated.PNG)

--- /task ---

![Melding som ruller](images/scroll-message.gif)

For å vise en annen melding, kan du skrive hva som helst mellom anførselstegnene (`""`).

--- collapse ---

---
title: Hvilke tegn kan brukes?
---

Sense HAT kan bare vise tegnsettet Latin 1, noe som betyr at bare følgende tegn vil være tilgjengelig. Andre tegn vises som `?`.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

Du kan også endre hastigheten på meldingen som ruller over skjermen. Legg til en `scroll_speed` til kodelinjen du allerede har, slik:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Standardhastigheten til meldingen er `0.1`. Med lavere tall ruller meldingen raskere, og høyere tall gjør at meldingen går langsommere.

--- /task ---

### Velg et navn for de nye Astro Pi-datamaskinene

--- task --- We will name the Astro Pi computers after two inspirational European scientists. There are hundreds of men and women that have contributed to science and technology, and participants can suggest their own names, or pick from our list of suggestions:


[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"} \ [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing){:target="_blank"} \ [Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel){:target="_blank"} \ [Edsgar Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra){:target="_blank"} \ [Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr){:target="_blank"} \ [Hypatia](https://en.wikipedia.org/wiki/Hypatia){:target="_blank"} \ [John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone){:target="_blank"} \ [Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie){:target="_blank"} \ [Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla){:target="_blank"} \ [Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe){:target="_blank"} \

To vote, start your message with the words "My name should be". For example, you want to vote for Ada Lovelace, your code would look like this:

```python
sense.show_message("My name should be Ada Lovelace")
```
--- /task ---



