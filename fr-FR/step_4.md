## Ajouter de la couleur

Les LED de l'Astro Pi peuvent également afficher des couleurs. Tu peux spécifier une couleur en créant une variable et en lui attribuant une valeur de couleur RGB.

Tu peux apprendre ici comment créer toutes les couleurs en utilisant différentes proportions de rouge, de vert et de bleu :

[[[generic-theory-colours]]]

\--- task \---

Choisis une couleur et découvre la valeur RGB de cette couleur. Tu peux utiliser un [sélecteur de couleur](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} pour t'aider.

\--- /task \---

\--- task \---

Crée une variable qui servira à stocker la couleur que tu as choisi. Par exemple, si tu as choisi la couleur rouge, tu vas écrire cette ligne de code :

```python
red = (255,0,0)
```

\--- /task \---

\--- task \---

Tu peux maintenant afficher ton texte dans la couleur de ton choix ! Pour indiquer au programme d'utiliser la couleur que tu as créée, ajoute le paramètre `text_colour` (couleur du texte) à la ligne de code qui affiche ton texte :

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

\--- /task \---

![afficher le message en couleur](images/show-message-color.gif)

\--- task \---

Tu peux également modifier la couleur de fond de l'écran. Choisis une autre couleur et crée une autre variable pour cette couleur. Pour indiquer au programme d'utiliser la couleur de fond que tu as choisie, ajoute le paramètre `back_colour` (couleur de fond) à ton code :

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

\--- /task \---

\--- task \---

Modifie le texte et la couleur du message de salutation - quel message veux-tu envoyer aux astronautes à bord de l'ISS ?

\--- /task \---