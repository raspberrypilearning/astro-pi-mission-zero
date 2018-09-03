## Vis temperaturen

Du kan kombinere din temperaturaflæsning med et billede for også at angive temperaturen på grafisk vis. Du kunne for eksempel vise en snestorm ved kolde temperaturer og en solskinsdag ved varme temperaturer:

![Varmt og koldt](images/hot-and-cold.png)

\--- task \---

I bunden af dit program skal du oprette flere farvevariabler for vilkårlige farver, du ønsker at anvende på dine billeder. Du har måske allerede defineret nogle af dem i et tidligere trin. I vores eksempler anvender vi hvid (`w`), gul (`y`), grøn (`g`) og sort/blank (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Ligesom tidligere skal du tegne dine billeder ved først at oprette en liste for hvert af dem og derefter indstille elementerne på listen til de farver, du ønsker, dine pixels skal være.

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

Tilføj en kode for at få temperaturen:

```python
temp = sense.get_temperature()
```

\--- /task \---

\--- task \---

Beslut dig derefter for, hvilket billede du vil vise. I dette eksempel viser vi billedet `hot` (varmt), hvis temperaturaflæsningen er på 20 grader eller derover, og billedet `cold` (koldt), hvis temperaturen er på under 20 grader.

```python
temp = sense.get_temperature()
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /task \---

\--- task \---

Anvend temperaturskyderen til at indstille en temperatur på efterligneren. Kør dit program, og kontrollér, at det billede, du har valgt for pågældende temperatur, vises korrekt.

\--- /task \---

\--- task \---

Skift din kode, så dit program viser astronauterne temperaturen på den måde, du selv har valgt.

\--- /task \---