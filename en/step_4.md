## Display a message

+ Open the [Sense HAT emulator](https://trinket.io/mission-zero){:target="_blank"} for the Mission Zero project.

You will see that three lines of code have been added automatically for you:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```
This code connects to the Sense HAT and makes sure the LED display is shown the correct way around in the Astro Pi display on the right. Leave it there because you'll need it.

+ Let's scroll a message across the screen. Add this code underneath the other code:

```python
sense.show_message("Astro Pi")
```

+ Press the **Run** button and watch as the message "Astro Pi" scrolls across the LED matrix on the Sense HAT.

![Scrolling message](images/scroll-message.gif)

To display a different message, you can write anything you like between the quotation marks (`""`).

+ You can also change the speed of the message scrolling across the screen. Add a `scroll_speed` to the line of code you already have, like this:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

The original speed of the message is `0.1`. Making the number smaller will make the message scroll more quickly, and making the number larger makes the message scroll more slowly.

+ Perhaps you could leave a nice greeting for the Astronauts who will be working near where the Sense HAT is installed on the ISS?
