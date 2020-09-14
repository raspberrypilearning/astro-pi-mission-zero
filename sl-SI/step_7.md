## Prikažite vlažnost

Odčitek vlage lahko združite s sliko in vlago tako prikažete tudi grafično. Na primer, lahko prikažete ocean za visoko vlažnost in puščavo za nizko vlažnost:

![Mokro in suho](images/wet-dry.png)

--- task ---

Na dnu svojega programa določite več barvnih spremenljivk za barve, ki jih želite uporabiti v svojih slikah. Nekatere izmed njih ste morda določili že pri prejšnjem koraku.

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

Tako kot prej svoje slike ustvarite tako, da za vsako od njih ustvarite seznam in nato elementom seznama določite barve, ki jih želite uporabiti pri prikazu slikovnih pik.

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

Za informacije o vlažnosti dodajte kodo:

```python
humid = sense.humidity
```

--- /task ---

--- task ---

Zdaj se odločite, katero sliko želite uporabiti. V tem primeru bomo uporabili sliko `wet`, če vlaga znaša 40% ali več, in sliko `dry`, če je vlaga nižja od 40%.

```python
humid = sense.humidity
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

Z drsnikom za vlago na emulatorju nastavite vlago. Zaženite svoj program in preverite, ali je slika, ki ste jo za to vlago izbrali, prikazana pravilno.

--- /task ---

--- task ---

Svojo kodo spremenite tako, da bo vaš program astronavtom vlažnost prikazal na želen način.

--- /task ---