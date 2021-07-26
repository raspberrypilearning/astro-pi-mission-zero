## Zobrazte zprávu

--- task ---

Otevřete [emulátor desky Sense HAT](https://trinket.io/mission-zero){:target="_blank"} pro založení projektu Mission Zero.

Tři řádky kódu, přidané automaticky, už tam budou:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![emulátor desky sense hat](images/sense-hat-emulator2.png)

This code connects to the Astro Pi and makes sure the Astro Pi's LED display is shown the correct way around. Leave the code there, because you'll need it.

--- /task ---

--- task ---

Perhaps you could leave a nice greeting for the astronauts on the ISS who are working near the Astro Pi? Let's scroll a message across the display.

Přidejte pod kód, který už tam je, tuhle řádku:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Stiskněte tlačítko **Run** (Spustit) a sledujte, jak zpráva `Astro Pi` běží přes LED displej.

![kód pro zobrazení zprávy stisknout run (spustit)](images/show-message-code-annotated.PNG)

--- /task ---

![Běžící text](images/scroll-message.gif)

Jestli chcete zobrazit nějakou jinou zprávu, napište ji mezi uvozovky (`""`).

--- collapse ---

---
title: Jaké znaky je možné použít?
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



