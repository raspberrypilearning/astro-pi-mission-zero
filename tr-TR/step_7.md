## Display the temperature

You could combine your temperature reading with a picture to also indicate the temperature in a graphical way. For example, you might display a snowstorm for cold temperatures, and a sunny day for hot temperatures:

![Hot and cold](images/hot-and-cold.png)

\--- task \---

At the bottom of your program, create more colour variables for any colours you want to use in your pictures. You may already have defined some of them in a previous step. In our examples we will use white (`w`), yellow (`y`), green (`g`), and black/blank (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /görev \---

\--- task \---

Just like earlier, draw your pictures by first creating a list for each of them, and then setting the list items to the colours you want your pixels to be.

```python
hot = [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g
]


cold = [
  b, b, w, b, b, b, w, b,
  b, b, b, b, b, w, b, b,
  b, w, b, b, b, b, b, w,
  b, b, b, b, w, b, b, b,
  w, b, b, w, b, b, w, b,
  b, b, b, b, b, b, b, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w
]
```

\--- /görev \---

\--- task \---

Add some code to get the temperature:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Now decide which picture to display. For this example, we will display the `hot` image if the temperature reading is 20 degrees or above, and the `cold` image if the temperature is below 20 degrees.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /görev \---

\--- task \---

Use the temperature slider to set a temperature on the emulator. Run your program and check that the image you've selected for that temperature is correctly displayed.

\--- /görev \---

\--- task \---

Change your code so that your program displays the temperature to the astronauts in your own chosen way.

\--- /görev \---