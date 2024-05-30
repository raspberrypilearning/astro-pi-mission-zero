## Afficher une image

La matrice LED de l'Astro Pi peut afficher des couleurs. Dans cette étape, tu vas afficher des images de la nature sur la matrice LED de l'Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Une <span style="color: #0faeb0">**matrice LED**</span> est une grille de LED qui peuvent être contrôlées individuellement ou en groupe pour créer différents effets de lumière. La matrice LED du Sense HAT comporte 64 LED affichées dans une grille de 8 x 8. Les LED peuvent être programmées pour produire une large gamme de couleurs.
</p>

![Une capture d'écran de la fenêtre de l'émulateur montrant l'unité de vol avec la matrice LED qui affiche l'image d'une fleur.](images/fu-pic.png)

--- task ---

Ouvre le [projet de démarrage de Mission Zero](http://rpf.io/mzcode){:target="_blank"}.

Tu verras que quelques lignes de code ont été ajoutées pour toi automatiquement.

Ce code se connecte à l'Astro Pi et fait en sorte que l'écran LED de l'Astro Pi s'affiche correctement et effectue la configuration du capteur de couleurs. Laisse ce code ici car tu en auras besoin.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Importer les bibliothèques
from sense_hat import SenseHat from time import sleep

# Configuer le Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Configurer le capteur de couleurs
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Une capture d'écran de l'émulateur Sense HAT avec des lignes de code de démarrage affichées dans le panneau de gauche.](images/sense-hat-emulator2.png)

--- /task ---

### Les couleurs RVB

Tu peux créer des couleurs en utilisant différentes valeurs de rouge, vert et bleu. Tu peux découvrir les couleurs RVB ici :

[[[generic-theory-simple-colours]]]

La matrice LED est une grille 8 x 8. Chaque LED de la grille peut être réglée sur une couleur différente. Voici une liste de variables pour 24 couleurs différentes. Chaque couleur comporte une valeur de rouge, vert et bleu :

[[[ambient-colours]]]

### Choisis une image

--- task ---

**Choisir :** Choisis une image à afficher parmi les options ci-dessous. Python stocke les informations d'une image dans une liste. Le code de chaque image comprend les variables de couleur utilisées et la liste.

Tu devras **copier** tout le code de l'image que tu as choisie puis le **coller** dans ton projet sous la ligne indiquant `# Ajouter des variables de couleur et une image`.

--- collapse ---

---
title: Poulet
---

![Une grille avec des carrés de 8 x 8 montrant un poussin dans un œuf.](images/fox_mz3.png)

Created by team i_pupi, Italy

```python
a = (255, 255, 255) # Blanc
c = (0, 0, 0) # Noir
v = (255, 0, 0) # Rouge
```

--- /collapse ---


--- collapse ---

---
title: Grenouille
---

![Une grille avec des carrés de 8 x 8 montrant un serpent.](images/elephant.png)

Created by team ILiFanT, Finland

```python
image = [
  c, c, c, q, q, q, c, c,
  c, c, t, q, e, q, c, c,
  c, c, c, q, q, q, c, c,
  c, w, w, w, w, w, w, c,
  c, w, a, a, a, a, w, c,
  c, w, a, a, a, a, w, c,
  c, c, w, a, a, w, c, c,
  c, c, c, w, w, c, c, c]
```

--- /collapse ---

--- collapse ---
---
title: Fleur
---

![Une grille avec des carrés de 8 x 8 montrant une fleur rose sur une tige verte.](images/cactus.png)

Created by team 6TETHASI, The Netherlands

```python
a = (255, 255, 255) # Blanc
c = (0, 0, 0) # Noir
e = (0, 0, 205) # Bleu moyen
q = (255, 255, 0) # Jaune
t = (255, 140, 0) # Orange foncé
w = (255, 192, 203) # Rose

```

--- /collapse ---


--- collapse ---
---
title: Crocodile
---

![Une grille avec des carrés de 8 x 8 montrant une tête de crocodile.](images/croc.png)

```python

a = (255, 255, 255) # Blanc
c = (0, 0, 0) # Noir
f = (25, 25, 112) # MidnightBlue
m = (34, 139, 34) # Vert forêt

```

--- /collapse ---

--- collapse ---
---
title: Crabe
---

![Une grille avec des carrés de 8 x 8 montrant une grenouille.](images/rainbow.png)

Created by team camrus_6, United Kingdom

```python

c = (0, 0, 0) # Noir
m = (34, 139, 34) # Vert forêt
q = (255, 255, 0) # Jaune
t = (255, 140, 0) # Orange foncé
y = (255, 20, 147) # Rose foncé

```

--- /collapse ---

--- collapse ---
---
title: Serpent
---

![Une grille avec des carrés de 8 x 8 montrant un crabe.](images/dragon.png)

Created by team hwplucyr, United Kingdom

```python

b = (105, 105, 105) # DimGray
c = (0, 0, 0) # Black
d = (100, 149, 237) # CornflowerBlue
v = (255, 0, 0) # Red
z = (153, 50, 204) # DarkOrchid

image = [
    c, c, v, c, v, c, c, c,
    c, z, z, z, z, v, c, c,
    z, b, z, b, z, c, c, c,
    z, z, z, z, z, v, c, c,
    c, c, d, d, d, c, c, z,
    c, z, d, z, z, z, z, c,
    c, c, d, d, z, c, c, c,
    c, c, z, c, z, c, c, c]

```

--- /collapse ---

--- /task ---

--- task ---

**Recherche :** la ligne indiquant `# Afficher l'image` et ajoute une ligne de code pour afficher ton image sur la matrice LED :

```python
c = (0, 0, 0) # Noir
m = (34, 139, 34) # Vert forêt
q = (255, 255, 0) # Jaune
v = (255, 0, 0) # Rouge

```

--- /task ---

--- task ---

Appuie sur **Run** en bas de l'éditeur, pour voir ton image s'afficher sur la matrice LED.

--- /task ---

--- task ---

**Déboguer**

Mon code a une erreur de syntaxe :

- Vérifie que ton code correspond au code des exemples ci-dessus
- Vérifie que tu as bien indenté le code dans ta liste
- Vérifie que ta liste est entourée de `[` et `]`
- Vérifie que chaque variable de couleur de la liste est séparée par une virgule

Mon image n'apparaît pas :

- Vérifie que ton `sense.set_pixels(image)` n'est pas indenté

--- /task ---


--- task ---

**Save your progress**

Now that you have displayed an image, you can save your program on the Mission Starter project by entering your team name, team members' names, and the classroom code given to you. You can reload your program on any device with an internet connection by entering your team name and classroom code.

![Mission Zero Save button](images/savebutton.png)

--- /task --- 
