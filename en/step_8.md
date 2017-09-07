## Display the temperature

You could combine your temperature reading with a picture to display the temperature in a graphical way. For example you might display a snowstorm for cold temperatures and a sunny day for hot temperatures.

![Hot and cold](images/hot-and-cold.png)

+ At the bottom of your program, create more colour variables for any colours you want to use in your pictures. You may already have defined some of the colours you want in a previous step. For these examples we will use white (`w`), yellow (`y`), green (`g`) and black/blank (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

+ Create your hot and cold pictures by first creating a list and then setting the pixels to the colours you want, just as you did before.

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

+ Add some code to take the temperature reading:

```python
temp = sense.get_temperature()
```

+ Now decide which picture to display. For this example, we will display the hot image if the temperature is 20 degrees or above, and the cold image if the temperature is below 20 degrees.

```python
temp = sense.get_temperature()
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

+ Use the temperature slider to set a temperature. Run your program and check that the correct image displays for the temperature you have selected.
