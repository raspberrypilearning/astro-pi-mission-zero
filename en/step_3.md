## Display a message and choose a name for the new Astro Pi computers

--- task ---

Open the [Sense HAT emulator](https://trinket.io/mission-zero){:target="_blank"} for the Mission Zero project.

You will see that three lines of code have been added for you automatically:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![A screenshot of the Trinket Sense Hat emulator with three lines of starter code displayed in the left hand pane.](images/sense-hat-emulator2.png)

This code connects to the Astro Pi and makes sure the Astro Pi's LED display is shown the correct way around. Leave the code there, because you'll need it.

--- /task ---

--- task ---

Perhaps you could leave a nice greeting for the astronauts on the ISS who are working near the Astro Pi? Let's scroll a message across the display. 

Add this line below the other code:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Press the **Run** button and watch as the message `Astro Pi` scrolls across the LED display.

![show message code click run](images/show-message-code-annotated.PNG)

--- /task ---

![Scrolling message](images/scroll-message.gif)

To display a different message, you can write anything you like between the quotation marks (`""`).

--- collapse ---

---
title: What characters can be used?
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

--- task ---
We will name the Astro Pi computers after two inspirational European scientists. There are hundreds of men and women that have contributed to science and technology, and participants can suggest their own names, or pick from our list of suggestions:


[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"} \
[Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing){:target="_blank"} \
[Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel){:target="_blank"} \
[Edsgar Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra){:target="_blank"} \
[Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr){:target="_blank"} \
[Hypatia](https://en.wikipedia.org/wiki/Hypatia){:target="_blank"} \
[John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone){:target="_blank"} \
[Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie){:target="_blank"} \
[Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla){:target="_blank"} \
[Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe){:target="_blank"} \

To vote, start your message with the words "My name should be". For example, you want to vote for Ada Lovelace, your code would look like this:

```python
sense.show_message("My name should be Ada Lovelace")
```
--- /task ---



