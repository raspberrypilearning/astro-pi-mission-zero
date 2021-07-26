## Afișează un mesaj

--- task ---

Deschide [emulatorul Sense HAT](https://trinket.io/mission-zero){:target="_blank"} pentru proiectul Mission Zero.

Vei vedea că au fost adăugate automat pentru tine trei linii de cod:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![emulator Sense Hat](images/sense-hat-emulator2.png)

This code connects to the Astro Pi and makes sure the Astro Pi's LED display is shown the correct way around. Leave the code there, because you'll need it.

--- /task ---

--- task ---

Perhaps you could leave a nice greeting for the astronauts on the ISS who are working near the Astro Pi? Let's scroll a message across the display.

Adaugă acest rând sub celelalte linii de cod:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Apasă pe butonul **Run** și urmărește cum mesajul `Astro Pi` se derulează pe ecranul LED.

![afișează codul de mesaj dă click pe run](images/show-message-code-annotated.PNG)

--- /task ---

![Derularea mesajului](images/scroll-message.gif)

Pentru a afișa un alt mesaj, poți scrie orice dorești între ghilimele (`""`).

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

### Choose a name for the new Astro Pi computers

--- task --- If you'd like to enter the competition to choose the names of the new Mark II Astro Pi computers, start your message with the words "My name should be" and then add in your selection from this list.

For example, if you'd like to vote for Ada Lovelace, your code would look like this:

```python
sense.show_message("My name should be Ada Lovelace")
```
--- /task ---



