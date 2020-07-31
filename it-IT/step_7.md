## Mostrate la temperatura

Potete anche combinare la lettura della temperatura con un’immagine per indicare la temperatura graficamente. For example, you might display an ocean for high humidity, and a desert for low humidity:

![Caldo e freddo](images/wet-dry.png)

\--- task \---

Alla fine del programma create altre variabili di colore per gli altri colori che volete usare nelle vostre immagini. Potreste averne già definiti alcuni in un passo precedente.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Proprio come prima, potete disegnare le immagini creando dapprima una lista per ciascuna immagine e quindi impostando le voci della lista sui colori che volete assumano i pixel corrispondenti.

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

Aggiungete il codice necessario per ottenere la temperatura:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Ora decidete quale immagine mostrare. In questo esempio, visualizzeremo l’immagine `hot` se la temperatura misurata è uguale o superiore a 20 gradi e l’immagine `cold` se la temperatura misurata è inferiore a 20 gradi.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /task \---

\--- task \---

Impostate una temperatura di prova sull’emulatore usando l’apposito cursore. Avviate il programma e controllate che l’immagine che avete selezionato per tale temperatura sia visualizzata correttamente.

\--- /task \---

\--- task \---

Modificate il codice in modo che il vostro programma mostri la temperatura agli astronauti nel modo scelto da voi.

\--- /task \---