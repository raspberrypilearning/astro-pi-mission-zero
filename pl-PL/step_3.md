## Wyświetlanie wiadomości

--- task ---

Otwórz [emulator Sense HAT](https://trinket.io/mission-zero){:target="_blank"} dla projektu Misja Zero.

Zobaczysz, że trzy wiersze kodu zostały dodane automatycznie:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![A screenshot of the Trinket Sense Hat emulator with three lines of starter code displayed in the left hand pane.](images/sense-hat-emulator2.png)

Kod ten łączy się z Astro Pi i zapewnia, że wyświetlacz LED Astro Pi jest pokazany we właściwy sposób. Kod należy zostawić, gdyż będzie on potrzebny.

--- /task ---

--- task ---

Może zamieścisz miłe pozdrowienia dla astronautów z ISS, którzy pracują w pobliżu Astro Pi? Dodajmy przewijaną wiadomość na wyświetlaczu.

Dodaj ten wiersz poniżej drugiego kodu:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Po naciśnięciu przycisku **Run** (Uruchom) zobaczysz, jak wiadomość `Astro Pi` przewija się na wyświetlaczu LED.

![pokaż kod wiadomości kliknij uruchom](images/show-message-code-annotated.PNG)

--- /task ---

![Przewijanie wiadomości](images/scroll-message.gif)

Aby wyświetlić inną wiadomość, można napisać dowolną treść między znakami cudzysłowu (`""`).

--- collapse ---

---
title: Jakich znaków można użyć?
---

Sense HAT może wyświetlać tylko zestaw znaków Latin 1, co oznacza, że ​​dostępne będą tylko następujące znaki. Inne znaki będą wyświetlane jako `?`.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

Można również zmienić tempo przewijania wiadomości na ekranie. Dodaj `scroll_speed` (tempo_przewijania) do istniejącego wiersza kodu, na przykład:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Domyślne tempo przewijania wiadomości to `0.1`. Zmniejszenie liczby spowoduje, że wiadomość będzie przewijać się szybciej, a jej zwiększenie spowoduje, że wiadomość będzie przewijać się wolniej.

--- /task ---

### Choose a name for the new Astro Pi computers

--- task --- We will name the Astro Pi computers after two inspirational European scientists. There are hundreds of men and women that have contributed to science and technology, and participants can suggest their own names, or pick from our list of suggestions:


[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"} \ [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing){:target="_blank"} \ [Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel){:target="_blank"} \ [Edsgar Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra){:target="_blank"} \ [Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr){:target="_blank"} \ [Hypatia](https://en.wikipedia.org/wiki/Hypatia){:target="_blank"} \ [John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone){:target="_blank"} \ [Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie){:target="_blank"} \ [Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla){:target="_blank"} \ [Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe){:target="_blank"} \

To vote, start your message with the words "My name should be". For example, you want to vote for Ada Lovelace, your code would look like this:

```python
sense.show_message("My name should be Ada Lovelace")
```
--- /task ---



