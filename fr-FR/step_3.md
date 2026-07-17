## Afficher une image

The image you display will be made from 64 coloured squares called **pixels**. The pixels are arranged in an 8 x 8 grid. Each pixel can be a different colour. By choosing the colours carefully, you can create a picture. Here is an example of a whale made using different shades of blue on a black background.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Une <span style="color: #0faeb0">**matrice LED**</span> est une grille de LED qui peuvent être contrôlées individuellement ou en groupe pour créer différents effets de lumière. La matrice LED du Sense HAT comporte 64 LED affichées dans une grille de 8 x 8. Les LED peuvent être programmées pour produire une large gamme de couleurs.
</p>

![an 8x8 image of a whale with letters labelling different colours](images/whale.png)

Notice that each square is labelled with a code to represent a particular colour. In this image 3 colours are used:
+ c = black
+ f = Ocean blue
+ g = Sky blue


--- task ---

Ouvre le [projet de démarrage de Mission Zero](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"}.

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

![Une capture d'écran de l'émulateur Sense HAT avec des lignes de code de démarrage affichées dans le panneau de gauche.](images/sense-hat-emulator3.png)

--- /task ---

### Couleurs RVB

Tu peux créer des couleurs en utilisant différentes valeurs de rouge, vert et bleu. Tu peux découvrir les couleurs RVB ici :

![Three sliders demonstrating RGB colour values](images/rgbsliders.gif)

La matrice LED est une grille 8 x 8. Chaque LED de la grille peut être réglée sur une couleur différente. We can use the letters a to z as the names of variables to represent 24 different colours. Each colour has a value for red, green, and blue.

--- collapse ---

---
title: List of Colour Variables
---

![A grid of 24 coloured squared each labelled with a different letter of the alphabet](images/palette.png)

```python
a = (255, 255, 255) # White
b = (171, 171, 171) # Grey
c = (0, 0, 0)       # Black
d = (25, 25, 113)   # Navy Blue
e = (0, 0, 255)     # Pure Blue
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue
h = (86, 255, 255)  # Electric Cyan
j = (0, 255, 0)     # Pure Green
k = (46, 139, 33)   # Leaf Green
l = (57, 97, 17)    # Olive Green
m = (30, 65, 6)     # Forest Green
n = (126, 88, 25)   # Earth Brown
o = (179, 96, 65)   # Terracotta Brown
p = (180, 34, 34)   # Brick Red
q = (255, 0, 0)     # Pure Red
r = (232, 118, 5)   # Orange
s = (241, 231, 100) # Pale Yellow
t = (255, 255, 0)   # Pure Yellow
u = (255, 209, 209) # Pale Pink
v = (255, 177, 177) # Blush Pink
w = (249, 169, 255) # Light Pink
y = (248, 97, 255)  # Magenta
z = (220, 53, 232)  # Purple

```

--- /collapse ---

### Choisir une image

--- task ---

**Choisir :** choisis une image à afficher parmi les options ci-dessous. Python stocke les informations d'une image dans une liste. Le code de chaque image comprend les variables de couleur utilisées et la liste.

Tu devras **copier** tout le code de l'image que tu as choisie puis le **coller** dans ton projet sous la ligne indiquant `# Ajouter des variables de couleur et une image`.

--- collapse ---

---
title: Whale
---

![A grid with 8 x 8 squares showing a whale.](images/whale.png)

Created by Team Naicom, Italy

```python
c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue

image = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, a,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

```

--- /collapse ---


--- collapse ---

---
title: Lemon
---

![A grid with 8 x 8 squares showing a lemon.](images/lemon.png)

Created by team g4lemoni, Greece

```python
a = (255, 255, 255) # White
k = (46, 139, 33)   # Leaf Green
t = (255, 255, 0)   # Pure Yellow

image = [
c, c, c, k, k, c, c, c,
c, c, k, c, k, c, c, c,
c, k, c, t, t, c, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, c, t, t, c, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Pig
---

![A grid with 8 x 8 squares showing a pig.](images/pig.png)

Created by Gary, United Kingdom

```python
a = (255, 255, 255) # White
u = (255, 209, 209) # Pale Pink
v = (255, 177, 177) # Blush Pink
o = (179, 96, 65)   # Terracotta Brown
c = (0, 0, 0)       # Black

image = [
a, a, y, a, a, y, a, a,
a, y, y, y, y, y, y, a,
a, y, c, y, c, y, y, y,
v, v, v, v, v, y, y, y,
v, o, v, o, v, y, y, y,
v, v, v, v, v, y, y, y,
a, y, y, y, y, y, y, y,
a, a, y, a, a, a, y, a]

```

--- /collapse ---


--- collapse ---
---
title: Storm
---

![A grid with 8 x 8 squares showing a storm cloud.](images/storm.png)

Created by team hop2p023, Spain

```python

c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue
t = (255, 255, 0)   # Pure Yellow

image = [
c, c, c, c, c, c, c, c,
c, c, f, f, f, f, c, c,
c, f, f, f, f, f, f, c,
c, g, c, g, t, g, c, c,
c, c, c, t, t, c, c, c,
c, c, t, t, c, c, c, c,
c, c, g, c, c, c, c, g,
c, g, c, c, c, c, c, c]


```

--- /collapse ---

--- collapse ---
---
title: Duck
---

![A grid with 8 x 8 squares showing a duck.](images/duck.png)

Created by Peter, Ireland

```python

c = (0, 0, 0) # Black
l = (57, 97, 17)    # Olive Green
m = (30, 65, 6)     # Forest Green
r = (232, 118, 5)   # Orange
a = (255, 255, 255) # White
b = (171, 171, 171) # Grey

image = [
c, l, l, c, c, c, c, c,
r, r, m, c, c, c, c, c,
c, l, l, c, c, c, c, c,
c, a, a, l, a, a, c, c,
c, l, l, a, a, a, b, a,
c, a, a, b, b, b, a, a,
c, c, a, a, a, a, c, c,
c, c, c, r, c, r, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Frog
---

![A grid with 8 x 8 squares showing a Frog.](images/frog.png)

Created by team Jmeno, Czech Republic

```python

a = (255, 255, 255) # White
b = (171, 171, 171) # Grey
c = (0, 0, 0)       # Black
q = (255, 0, 0)     # Pure Red
j = (0, 255, 0)     # Pure Green
k = (46, 139, 33)   # Leaf Green
n = (126, 88, 25)   # Earth Brown

image = [
a, a, a, a, a, a, a, a,
a, a, a, a, a, b, a, b,
a, a, a, a, a, a, c, a,
a, a, c, a, c, a, q, a,
a, a, j, j, j, q, a, a,
a, j, j, k, q, a, a, a,
j, k, j, k, k, a, a, a,
k, k, k, j, k, n, n, n]

```

--- /collapse ---

--- collapse ---
---
title: Blossom Tree
---

![A grid with 8 x 8 squares showing a tree in blossom.](images/blossom.png)

Created by team Zssh14, Slovakia

```python

t = (255, 255, 0)   # Pure Yellow
g = (0, 204, 255)   # Sky Blue
w = (249, 169, 255) # Light Pink
y = (248, 97, 255)  # Magenta
z = (220, 53, 232)  # Purple
n = (126, 88, 25)   # Earth Brown
o = (179, 96, 65)   # Terracotta Brown
k = (46, 139, 33)   # Leaf Green

image =  [
t, g, g, w, w, y, g, g,
g, g, w, w, y, y, z, g,
g, w, y, z, y, z, z, z,
w, y, z, z, g, n, w, g,
g, g, o, o, n, w, y, z,
g, g, g, g, n, g, g, g,
g, g, g, o, n, n, g, g,
k, k, o, n, n, n, k, k]

```

--- /collapse ---

--- /task ---

--- task ---

**Trouver :** la ligne qui indique`# Afficher l'image` et ajoute une ligne de code pour afficher ton image sur la matrice LED :

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, a, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

# Afficher l'image
sense.set_pixels(image)

--- /code ---

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

**Enregistre ta progression**

Maintenant que tu as affiché une image, tu peux enregistrer ton programme sur le projet Mission Starter en entrant le nom de ton équipe, les noms des membres de l'équipe et le code de classe qui t'a été donné. Tu peux recharger ton programme sur n'importe quel appareil avec une connexion Internet en entrant le nom de ton équipe et le code de classe.

![Bouton Enregistrer Mission Zero](images/mz_savebutton_v2.png)

--- /task --- 
