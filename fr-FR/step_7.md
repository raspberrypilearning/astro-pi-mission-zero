## Affiche la température

Tu peux combiner ta mesure de la température avec une image pour indiquer également la température de manière graphique. Par exemple, tu peux afficher une tempête de neige pour les températures froides et une journée ensoleillée pour les températures chaudes :

![Chaud et froid](images/hot-and-cold.png)

\--- task \---

En bas de ton programme, crée d'autres variables pour les couleurs que tu veux utiliser pour dessiner tes images. Tu en as peut-être déjà défini certaines lors d'une étape précédente. Dans nos exemples, nous utiliserons du blanc (`w`), jaune (`y`), vert (`g`), et noir / blanc (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Comme précédemment, dessine tes images en créant d'abord une liste pour chacune d'entre elles, puis en indiquant la couleur que tu veux donner aux pixels de chaque élément de la liste.

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

Ajoute du code pour obtenir la température :

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Décide maintenant quelle image tu veux afficher. Pour cet exemple, nous afficherons l'image correspondant à la chaleur `hot` (chaud) si la mesure de la température est de 20 degrés ou plus, et l'image correspondant au froid `cold` (froid) si la température est inférieure à 20 degrés.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /task \---

\--- task \---

Utilise le curseur de température pour définir une température sur l'émulateur. Exécute ton programme et vérifie que l'image que tu as chosie pour cette température est correctement affichée.

\--- /task \---

\--- task \---

Modifie ton code pour que ton programme affiche la température pour les astronautes de la manière que tu as choisie.

\--- /task \---