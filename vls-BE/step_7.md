## Laat de vochtigheid zien

You could combine your humidity reading with a picture to also indicate the humidity in a graphical way. For example, you might display an ocean for high humidity, and a desert for low humidity:

![Nat en droog](images/wet-dry.png)

--- task ---

At the bottom of your program, create more colour variables for any colours you want to use in your pictures. You may already have defined some of them in a previous step.

```python
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)
```

--- /task ---

--- task ---

Net zoals eerder, teken je tekeningen door eerst een lijst aan te maken voor elk van hen, en zet dan de items met de kleuren op de lijst die je voor je pixels wilt gebruiken.

```python
wet = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


dry = [
  c, c, g, g, c, c, c, c,
  c, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, g, g, g, g, g, c, c,
  c, c, g, g, c, c, c, c,
  y, y, y, y, y, y, y, y,
  y, y, y, y, y, y, y, y
]
```

--- /task ---

--- task ---

Voeg code toe om de vochtigheid te verkrijgen:

```python
humid = sense.humidity
```

--- /task ---

--- task ---

Now decide which picture to display. For this example, we will display the `wet` image if the humidity reading is 40% or above, and the `dry` image if the humidity is below 40%.

```python
humid = sense.humidity
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

Use the humidity slider to set a humidity on the emulator. Run your program and check that the image you've selected for that humidity is correctly displayed.

--- /task ---

--- task ---

Verander je code zodat je programma de vochtigheid weergeeft aan de astronauten op de door jou gekozen manier.

--- /task ---

--- task --- Test your code with a few different humidity settings (using the slider) to make sure it always runs correctly. If you've followed the example above, is an image displayed both when the humidity is set to a value less than 40% and also when it is set to more than 40%?

--- /task ---
