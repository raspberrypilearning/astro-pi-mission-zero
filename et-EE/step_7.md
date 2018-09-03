## Õhutemperatuuri kuvamine

Võid õhutemperatuuri mõõtmise tulemust kombineerida pildiga, et näidata õhutemperatuuri ka graafiliselt. Näiteks võid külma õhutemperatuuri korral näidata lumetormi ja kuuma õhutemperatuuri korral päikesepaistelist päeva:

![Kuum ja külm](images/hot-and-cold.png)

\--- task \---

Oma programmi lõpus lisa rohkem värvimuutujaid värvide jaoks, mida tahad oma piltidel kasutada. Võimalik, et oled mõned juba eelmises etapis määranud. Meie näites kasutatakse valget (`w`), kollast (`y`), rohelist (`g`) ja musta/tühja (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Täpselt samamoodi kui varem, oma piltide joonistamiseks tee kõigepealt iga pildi jaoks loetelu ja seejärel vastavalt soovitud pikslite värvidele määra loetelu ühikutele värvid.

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

Õhutemperatuuri saamiseks lisa kood:

```python
temp = sense.get_temperature()
```

\--- /task \---

\--- task \---

Nüüd otsusta, millist pilti kuvada. Selle näite jaoks kuvatakse `hot` pilti, kui mõõdetav õhutemperatuur on 20 kraadi või rohkem ja `cold` pilti, kui õhutemperatuur on alla 20 kraadi.

```python
temp = sense.get_temperature()
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /task \---

\--- task \---

Õhutemperatuuri määramiseks emulaatoril kasuta temperatuuri liugurit. Käivita oma programm ja kontrolli, et sinu poolt selle õhutemperatuuri jaoks valitud pilti kuvatakse korrektselt.

\--- /task \---

\--- task \---

Muuda oma koodi, et sinu programm kuvaks õhutemperatuuri astronautidele sinu poolt valitud viisil.

\--- /task \---