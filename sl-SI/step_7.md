## Prikažite temperaturo

Odčitek vlage lahko združite s sliko in vlago tako prikažete tudi grafično. Na primer, lahko prikažete ocean za visoko vlažnost in puščavo za nizko vlažnost:

![Vroče in hladno](images/wet-dry.png)

\--- task \---

Na dnu svojega programa določite več barvnih spremenljivk za barve, ki jih želite uporabiti v svojih slikah. Nekatere izmed njih ste morda določili že pri prejšnjem koraku.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

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

\--- /task \---

\--- task \---

Za temperaturo dodajte kodo:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Zdaj se odločite, katero sliko želite uporabiti. V tem primeru bomo uporabili sliko `wet`, če vlaga znaša 40% ali več, in sliko `dry`, če je vlaga nižja od 40%.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /task \---

\--- task \---

Z drsnikom za vlago na emulatorju nastavite vlago. Zaženite svoj program in preverite, ali je slika, ki ste jo za to vlago izbrali, prikazana pravilno.

\--- /task \---

\--- task \---

Svojo kodo spremenite tako, da bo vaš program astronavtom temperaturo prikazal na želen način.

\--- /task \---