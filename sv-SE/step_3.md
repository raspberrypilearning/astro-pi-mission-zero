## Visa ett meddelande

--- uppgift ---

Öppna [Sense HAT-emulatorn](https://trinket.io/mission-zero){:target="_blank"} för projektet Mission Zero.

Du kommer att se tre rader kod som har lagts till åt dig automatiskt:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![sense hat-emulator](images/sense-hat-emulator2.png)

This code connects to the Astro Pi and makes sure the Astro Pi's LED display is shown the correct way around. Leave the code there, because you'll need it.

--- / uppgift ---

--- uppgift ---

Perhaps you could leave a nice greeting for the astronauts on the ISS who are working near the Astro Pi? Let's scroll a message across the display.

Lägg till den här raden under de andra kodraderna:

```python
sense.show_message("Astro Pi")
```

--- / uppgift ---

--- uppgift ---

Tryck på knappen **Run** (Kör) och se meddelandet `Astro Pi` rullar över LED-displayen.

![visa meddelandekod klicka på kör](images/show-message-code-annotated.PNG)

--- /uppgift ---

![Rullande meddelande](images/scroll-message.gif)

För att visa ett annat meddelande, kan du skriva vad du vill mellan citationstecknen (`""`).

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

### Choose a name for the new Astro Pi computers

--- task --- If you'd like to enter the competition to choose the names of the new Mark II Astro Pi computers, start your message with the words "My name should be" and then add in your selection from this list.

For example, if you'd like to vote for Ada Lovelace, your code would look like this:

```python
sense.show_message("My name should be Ada Lovelace")
```
--- /uppgift ---



