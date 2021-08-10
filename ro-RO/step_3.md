## Afișează un mesaj

--- task ---

Deschide [emulatorul Sense HAT](https://trinket.io/mission-zero){:target="_blank"} pentru proiectul Mission Zero.

Vei vedea că au fost adăugate automat pentru tine trei linii de cod:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![A screenshot of the Trinket Sense Hat emulator with three lines of starter code displayed in the left hand pane.](images/sense-hat-emulator2.png)

Acest cod se conectează la Astro Pi și se asigură că afișajul LED al lui Astro Pi este afișat corect. Lasă codul acolo, pentru că vei avea nevoie de el.

--- /task ---

--- task ---

Poate ai putea lăsa un salut prietenos pentru astronauții de la ISS care lucrează lângă Astro Pi? Să derulam un mesaj pe ecran.

Adaugă acest rând sub celelalte linii de cod:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Apasă pe butonul **Run** și urmărește cum mesajul `Astro Pi` se derulează pe ecranul LED.

![The Trinket Sense HAT emulator running a sample program which scrolls the text "Astro PI" across the LED matrix in white letters](images/M0_1.gif)

--- /task ---



To display a different message, you can write anything you like between the quotation marks (`""`).

--- collapse ---

---
title: Ce caractere pot fi folosite?
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

### Alege un nume pentru noile calculatoare Astro Pi

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
sense.show_message("Numele meu ar trebui sa fie Ada Lovelace")
```

If you would like to vote, your message *must* start with these words, otherwise we won't be able to automatically count your entry.

--- /task ---



