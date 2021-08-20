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



Pentru a afișa un alt mesaj, poți scrie orice dorești între ghilimele (`""`).

--- collapse ---

---
title: Ce caractere pot fi folosite?
---

Sense HAT poate afișa numai setul de caractere Latin 1, adică numai următoarele caractere vor fi disponibile. Alte caractere se vor afișa ca și `?`.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

De asemenea, poți schimba viteza derulării mesajului pe ecran. Adaugă un `scroll_speed` la linia de cod pe care o ai deja, după cum urmează:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Viteza implicită a mesajului este `0.1`. Introducerea unui număr mai mic face ca mesajul să se deruleze mai repede, iar unul mai mare face ca mesajul să se deruleze mai lent.

--- /task ---

### Alege un nume pentru noile calculatoare Astro Pi

--- task --- Vom numi computerele Astro Pi după doi oameni de știință europeni care ne inspiră. Există sute de bărbați și femei care au contribuit la știință și tehnologie; participanții pot sugera propriile lor nume sau pot alege din lista noastră de sugestii:


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

Trebuie să îți începi mesajul cu cuvintele "My name should be", în engleză. De exemplu, dacă ai vrea să votezi pentru Ada Lovelace, codul tău ar arăta astfel:

```python
sense.show_message("My name should be Ada Lovelace")
```

Dacă ai vrea să votezi, mesajul tău trebuie să înceapă cu aceste cuvinte, în caz contrar nu vom putea să îți luăm în calcul răspunsul.

--- /task ---



