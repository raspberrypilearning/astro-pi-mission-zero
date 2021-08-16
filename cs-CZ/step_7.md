## Zobrazit vlhkost

You could combine your humidity reading with a picture to also indicate the humidity in a graphical way. For example, you might display an ocean for high humidity, and a desert for low humidity:

![Vlhko a sucho](images/wet-dry.png)

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

Stejně jako předtím nakreslete obrázky tak, že pro každý z nich vytvoříte seznam a potom položky tohoto seznamu nastavíte na barvy, které mají mít jednotlivé pixely.

```python
vlhko = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


sucho = [
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

Přidejte kód pro získání vlhkosti:

```python
temp = sense.temperature
```

--- /task ---

--- task ---

Now decide which picture to display. For this example, we will display the `wet` image if the humidity reading is 40% or above, and the `dry` image if the humidity is below 40%.

```python
vlhkost = sense.get_humidity()
if vlhkost >= 40:
    sense.set_pixels(vlhko)
else:
    sense.set_pixels(sucho)
```

--- /task ---

--- task ---

Use the humidity slider to set a humidity on the emulator. Run your program and check that the image you've selected for that humidity is correctly displayed.

--- /task ---

--- task ---

Změňte kód tak, aby váš program ukazoval astronautům vlhkost tak, jak chcete vy.

--- /task ---

--- task --- Test your code with a few different humidity settings (using the slider) to make sure it always runs correctly. If you've followed the example above, is an image displayed both when the humidity is set to a value less than 40% and also when it is set to more than 40%?

--- /task ---
