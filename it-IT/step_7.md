## Mostra l'umidità

Potreste anche combinare la lettura dell'umidità con un’immagine per indicare l'umidità graficamente. Ad esempio, potresti visualizzare un oceano per alta umidità e un deserto per bassa umidità:

![Caldo e freddo](images/wet-dry.png)

\--- task \---

Alla fine del programma create altre variabili di colore per gli altri colori che volete usare nelle vostre immagini. Potreste averne già definiti alcuni in un passo precedente.

```python
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)
```

\--- /task \---

\--- task \---

Proprio come prima, potete disegnare le immagini creando dapprima una lista per ciascuna immagine e quindi impostando le voci della lista sui colori che volete assumano i pixel corrispondenti.

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

\--- /task \---

\--- task \---

Aggiungete il codice necessario per ottenere l'umidità:

```python
umidita = sense.humidity
```

\--- /task \---

\--- task \---

Ora decidete quale immagine mostrare. In questo esempio, visualizzeremo l’immagine `wet` se la temperatura misurata è uguale o superiore a 40 gradi e l’immagine `dry` se la temperatura misurata è inferiore a 40 gradi.

```python
umidita = sense.humidity
if umidita >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

\--- /task \---

\--- task \---

Impostate un'umidità di prova sull’emulatore usando l’apposito cursore. Avviate il programma e controllate che l’immagine che avete selezionato per tale umidità sia visualizzata correttamente.

\--- /task \---

\--- task \---

Modificate il codice in modo che il vostro programma mostri l'umidità agli astronauti nel modo da voi scelto.

\--- /task \---