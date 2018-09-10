## Afficher une image

Tu peux afficher des images sur la matrice LED de l'Astro Pi. Ton message de salutation pour les astronautes pourrait peut-être inclure une image ou un motif avec le texte, ou à la place du texte ?

![Astronaute](images/astronaut-pic.png)

\--- task \---

En bas de ton programme, crée des variables pour les couleurs que tu veux définir et utiliser pour dessiner une image. Tu peux utiliser autant de couleurs que tu veux mais dans cet exemple, nous nous limiterons à deux couleurs - blanc (`w` ) et noir (`b` ).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Remarque :** Cette fois-ci, il est conseillé de donner aux variables définies pour les couleurs des noms se limitant à une lettre, car cela permettra de gagner du temps à l'étape suivante, quand tu les saisiras de nombreuses fois. De plus, en utilisant des noms à une seule lettre tu pourras voir plus facilement l'image que tu vas dessiner.

\--- /task \---

\--- task \---

Sous tes nouvelles variables, crée une liste de 64 éléments. Chaque élément représente un pixel de la matrice du LED et correspond à l'une des variables de couleur que tu as définies. Dessine ton image en mettant une variable à l'endroit où tu veux que la couleur de cette variable apparaisse. Nous avons dessiné un astronaute en utilisant les pixels noirs (`b` ) pour l'arrière-plan et les pixels blancs (`w` ) pour dessiner la combinaison spatiale de l'astronaute :

```python
picture = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
```

\--- /task \---

\--- task \---

Ajoute une ligne de code pour afficher ton image sur l'écran LED.

```python
sense.set_pixels(picture)
```

\--- /task \---

\--- task \---

Appuie sur **Run** (Exécuter) pour afficher ton image.

\--- /task \---

\--- task \---

Si tu veux tu peux ajouter du code pour inclure un court moment d'attente (ou `sleep` (pause)) après l’affichage de l'image. Cela donnera aux astronautes le temps de voir ton image avant l'affichage de la partie suivante de ton message. En haut de ton programme, rajoute :

```python
from time import sleep
```

Ensuite, sur la ligne qui suit celle qui affiche ton image, ajoute ce code pour créer un moment d'attente de deux secondes :

```python
sleep(2)
```

\--- /task \---

\--- task \---

Crée ta propre image ou ton propre motif que tu veux afficher pour les astronautes !

\--- /task \---