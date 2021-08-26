## Reageeri õhuniiskusele

Võid oma õhuniiskuse mõõtmise tulemust kombineerida pildiga, et näidata niiskust ka graafiliselt. Näiteks võid kuvada kõrge õhuniiskuse korral ookeani ja madala õhuniiskuse korral kõrbe:

![Märg ja kuiv](images/wet-dry.png)

--- task ---

Oma programmi alaosas saad luua rohkem värvimuutujaid määramaks piltide joonistamisel kasutatavaid värve. Võimalik, et oled mõned juba eelmises etapis määranud.

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

Täpselt samamoodi nagu varem, tee oma piltide joonistamiseks kõigepealt iga pildi jaoks loend ja seejärel määra vastavalt soovitud pikslite värvidele loendi elementidele värvid.

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

Õhuniiskuse saamiseks lisa kood:

```python
humid = sense.get_humidity()
```

--- /task ---

--- task ---

Nüüd otsusta, millist pilti kuvada. Selle näite puhul kuvatakse `wet` pilt, kui mõõdetud õhuniiskus on 40% või rohkem ja `dry` pilt, kui õhuniiskus on alla 40%.

```python
humid = sense.get_humidity()
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

Õhuniiskuse määramiseks emulaatoril kasuta niiskuse liugurit. Käivita oma programm ja kontrolli, et sinu poolt selle õhuniiskuse jaoks valitud pilt kuvatakse korrektselt.

--- /task ---

--- task ---

Muuda oma koodi, et sinu programm kuvaks õhuniiskuse astronautidele sinu poolt valitud viisil.

--- /task ---

--- task --- Testi oma koodi erinevate niiskuseseadetega (kasutades liugurit), et veenduda, et see töötab alati õigesti. Kui oled järginud ülaltoodud näidet, kas pilti kuvatakse nii siis, kui õhuniiskus on seatud väärtusele alla 40%, kui ka siis, kui see on seatud üle 40%?

--- /task ---
