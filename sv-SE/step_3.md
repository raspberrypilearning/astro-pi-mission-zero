## Visa ett meddelande

--- uppgift ---

Öppna [Sense HAT-emulatorn](https://trinket.io/mission-zero){:target="_blank"} för projektet Mission Zero.

Du kommer att se tre rader kod som har lagts till åt dig automatiskt:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![A screenshot of the Trinket Sense Hat emulator with three lines of starter code displayed in the left hand pane.](images/sense-hat-emulator2.png)

Den här koden ansluter till Astro Pi och ser till att LED-displayen i Astro PI visas åt rätt håll. Lämna kvar koden där, för du kommer att behöva den.

--- / uppgift ---

--- uppgift ---

Du kanske kan skicka en trevlig hälsning till astronauterna på ISS som arbetar i närheten av Astro Pi? Låt oss rulla meddelandet över displayen.

Lägg till den här raden under de andra kodraderna:

```python
sense.show_message("Astro Pi")
```

--- / uppgift ---

--- uppgift ---

Tryck på knappen **Run** (Kör) och se meddelandet `Astro Pi` rullar över LED-displayen.

![The Trinket Sense HAT emulator running a sample program which scrolls the text "Astro PI" across the LED matrix in white letters](images/M0_1.gif)

--- /uppgift ---



To display a different message, you can write anything you like between the quotation marks (`""`).

--- collapse ---

---
title: Vilka tecken går att använda?
---

The Sense HAT can only display the Latin 1 character set, meaning only the following characters will be available. Other characters will display as a `?`.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

You can also change the speed of the message scrolling across the screen. Add a `scroll_speed` to the line of code you already have, like this:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

The default speed of the message is `0.1`. Making the number smaller makes the message scroll more quickly, and making it larger makes the message scroll more slowly.

--- /task ---

### Välj ett namn för de nya Astro Pi-datorerna

--- task --- We will name the Astro Pi computers after two inspirational European scientists. There are hundreds of men and women that have contributed to science and technology, and participants can suggest their own names, or pick from our list of suggestions:


[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"} 
[Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing){:target="_blank"} 
[Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel){:target="_blank"} 
[Edsgar Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra){:target="_blank"} 
[Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr){:target="_blank"} 
[Hypatia](https://en.wikipedia.org/wiki/Hypatia){:target="_blank"} 
[John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone){:target="_blank"} 
[Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie){:target="_blank"} 
[Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla){:target="_blank"} 
[Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe){:target="_blank"}

To vote, start your message with the words "My name should be". For example, you want to vote for Ada Lovelace, your code would look like this:

```python
sense.show_message("Mitt namn ska vara Ada Lovelace")
```
--- /task ---



