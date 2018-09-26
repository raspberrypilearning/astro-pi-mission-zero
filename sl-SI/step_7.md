## Prikažite temperaturo

Odčitek temperature lahko združite s sliko in temperaturo tako prikažete tudi grafično. Tako lahko za nizke temperature prikažete snežno nevihto, za visoke pa sončen dan.

![Vroče in hladno](images/hot-and-cold.png)

--- task ---

Na dnu svojega programa določite več barvnih spremenljivk za barve, ki jih želite uporabiti v svojih slikah. Nekatere izmed njih ste morda določili že pri prejšnjem koraku. V naših primerih bomo uporabili belo (`w`), rumeno(`y`), zeleno(`g`), in črno/praznino (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

--- /task ---

--- task ---

Tako kot prej svoje slike ustvarite tako, da za vsako od njih ustvarite seznam in nato elementom seznama določite barve, ki jih želite uporabiti pri prikazu slikovnih pik.

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

--- /task ---

--- task ---

Za temperaturo dodajte kodo:

```python
temp = sense.get_temperature()
```

--- /task ---

--- task ---

Zdaj se odločite, katero sliko želite uporabiti. V tem primeru bomo uporabili sliko `hot`, če temperatura znaša 20 stopinj ali več, in sliko `cold`, če je temperatura nižja od 20 stopinj.

```python
temp = sense.get_temperature()
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

--- /task ---

--- task ---

Z drsnikom za temperaturo na emulatorju nastavite temperaturo. Zaženite svoj program in preverite, ali je slika, ki ste jo za to temperaturo izbrali, prikazana pravilno.

--- /task ---

--- task ---

Svojo kodo spremenite tako, da bo vaš program astronavtom temperaturo prikazal na želen način.

--- /task ---