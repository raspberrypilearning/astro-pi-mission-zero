## Afficher l'humidité

Tu peux combiner ta mesure d'humidité avec une image pour aussi indiquer l'humidité d'une manière graphique. Par exemple, tu peux afficher un océan pour une humidité élevée, et un désert pour une faible humidité :

![Humide et sec](images/wet-dry.png)

\--- task \---

En bas de ton programme, crée d'autres variables pour les couleurs que tu veux utiliser pour dessiner tes images. Tu en as peut-être déjà défini certaines lors d'une étape précédente.

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

Comme précédemment, dessine tes images en créant d'abord une liste pour chacune d'entre elles, puis en indiquant la couleur que tu veux donner aux pixels de chaque élément de la liste.

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

Ajoute du code pour obtenir l'humidité :

```python
humid = sense.humidity
```

\--- /task \---

\--- task \---

Décide maintenant quelle image tu veux afficher. For this example, we will display the `wet` image if the humidity reading is 40% or above, and the `dry` image if the humidity is below 40%.

```python
humid = sense.humidity
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

\--- /task \---

\--- task \---

Utilise le curseur d'humidité pour définir une humidité sur l'émulateur. Exécute ton programme et vérifie que l'image que tu as choisie pour cette humidité est correctement affichée.

\--- /task \---

\--- task \---

Modifie ton code pour que ton programme affiche l'humidité pour les astronautes de la manière que tu as choisie.

\--- /task \---