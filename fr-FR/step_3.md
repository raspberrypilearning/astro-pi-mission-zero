## Afficher une image

L'image que tu afficheras sera composée de 64 carrés colorés appelés **pixels**. Les pixels sont disposés selon une grille de 8 x 8. Chaque pixel peut être d'une couleur différente. En choisissant soigneusement les couleurs, tu peux créer une image. Voici un exemple de baleine réalisée avec différentes nuances de bleu sur arrière-plan noir.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Une <span style="color: #0faeb0">**matrice LED**</span> est une grille de LED qui peuvent être contrôlées individuellement ou en groupe pour créer différents effets de lumière. La matrice LED du Sense HAT comporte 64 LED affichées dans une grille de 8 x 8. Les LED peuvent être programmées pour produire une large gamme de couleurs.
</p>

![une image 8x8 d'une baleine avec des lettres indiquant différentes couleurs](images/whale.png)

Tu remarqueras que chaque case est identifiée par un code correspondant à une couleur précise. Cette image utilise 3 couleurs :
+ c = Noir
+ f = Bleu océan
+ g = Bleu ciel


--- task ---

Ouvre le [projet de démarrage de Mission Zero](https://missions.astro-pi.org/fr/mz/code_submissions/){:target="_blank"}.

Tu verras que quelques lignes de code ont été ajoutées pour toi automatiquement.

Ce code se connecte à l'Astro Pi et fait en sorte que l'écran LED de l'Astro Pi s'affiche correctement et effectue la configuration du capteur de couleurs. Laisse ce code ici car tu en auras besoin.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
---
# Importer les bibliothèques
from sense_hat import SenseHat
from time import sleep

# Configuer le Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Configurer le capteur de couleurs
sense.color.gain = 60 # Régler la sensibilité du capteur
sense.color.integration_cycles = 64 # L'intervalle auquel la lecture sera effectuée

--- /code ---

![Une capture d'écran de l'émulateur Sense HAT avec des lignes de code de démarrage affichées dans le panneau de gauche.](images/sense-hat-emulator3.png)

--- /task ---

### Couleurs RVB

Tu peux créer des couleurs en utilisant différentes valeurs de rouge, vert et bleu. Tu peux découvrir les couleurs RVB ici :

![Trois curseurs illustrant les valeurs de couleur RVB](images/rgbsliders.gif)

La matrice LED est une grille 8 x 8. Chaque LED de la grille peut être réglée sur une couleur différente. Nous pouvons utiliser les lettres de a à z comme noms de variables pour représenter 24 couleurs différentes. Chaque couleur comporte une valeur de rouge, vert et bleu.

--- collapse ---

---
title: Liste des variables de couleur
---

![Une grille de 24 carrés colorés, chacun portant une lettre différente de l'alphabet](images/palette.png)

```python
a = (255, 255, 255) # Blanc
b = (171, 171, 171) # Gris
c = (0, 0, 0) # Noir
d = (25, 25, 113) # Bleu marine
e = (0, 0, 255) # Bleu pur
f = (36, 128, 200) # Bleu océan
g = (0, 204, 255) # Bleu ciel
h = (86, 255, 255) # Cyan électrique
j = (0, 255, 0) # Vert pur
k = (46, 139, 33) # Vert feuille
l = (57, 97, 17) # Vert olive
m = (30, 65, 6) # Vert forêt
n = (126, 88, 25) # Brun terre
o = (179, 96, 65) # Brun terracotta
p = (180, 34, 34) # Rouge brique
q = (255, 0, 0) # Rouge pur
r = (232, 118, 5) # Orange
s = (241, 231, 100) # Jaune pâle
t = (255, 255, 0) # Jaune pur
u = (255, 209, 209) # Rose pâle
v = (255, 177, 177) # Rose poudré
w = (249, 169, 255) # Rose clair
y = (248, 97, 255) # Magenta
z = (220, 53, 232) # Violet

```

--- /collapse ---

### Choisir une image

--- task ---

**Choisir :** choisis une image à afficher parmi les options ci-dessous. Python stocke les informations d'une image dans une liste. Le code de chaque image comprend les variables de couleur utilisées et la liste.

Tu devras **copier** tout le code de l'image que tu as choisie puis le **coller** dans ton projet sous la ligne indiquant `# Ajouter des variables de couleur et une image`.

--- collapse ---

---
title: Baleine
---

![Une grille de 8 x 8 cases représentant une baleine.](images/whale.png)

Créé par la Team Naicom, Italie

```python
c = (0, 0, 0)       # Noir
f = (36, 128, 200)  # Bleu océan
g = (0, 204, 255)   # Bleu ciel

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
title: Citron
---

![Une grille de 8 x 8 cases représentant un citron.](images/lemon.png)

Créé par la Team g4lemoni, Grèce

```python
c = (0, 0, 0)       # Noir
k = (46, 139, 33)   # Vert feuille
t = (255, 255, 0)   # Jaune pur

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
title: Cochon
---

![Une grille de 8 x 8 cases représentant un cochon.](images/pig.png)

Créé par Gary, Royaume-Uni

```python
a = (255, 255, 255) # Blanc
v = (255, 177, 177) # Rose poudré
y = (248, 97, 255)  # Magenta
o = (179, 96, 65)   # Brun terracotta
c = (0, 0, 0)       # Noir

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
title: Orage
---

![Une grille de 8 × 8 cases représentant un nuage d'orage.](images/storm.png)

Créé par la Team hop2p023, Espagne

```python

c = (0, 0, 0)       # Noir
f = (36, 128, 200)  # Bleu océan
g = (0, 204, 255)   # Bleu ciel
t = (255, 255, 0)   # Jaune pur

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
title: Canard
---

![Une grille de 8 x 8 cases représentant un canard.](images/duck.png)

Créé par Peter, Irlande

```python

c = (0, 0, 0) # Noir
l = (57, 97, 17)    # Vert olive
m = (30, 65, 6)     # Vert forêt
r = (232, 118, 5)   # Orange
a = (255, 255, 255) # Blanc
b = (171, 171, 171) # Gris

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
title: Grenouille
---

![Une grille de 8 x 8 cases représentant une grenouille.](images/frog.png)

Créé par la Team Jmeno, République tchèque

```python

a = (255, 255, 255) # Blanc
b = (171, 171, 171) # Gris
c = (0, 0, 0)       # Noir
q = (255, 0, 0)     # Rouge pur
j = (0, 255, 0)     # Vert pur
k = (46, 139, 33)   # Vert feuille
n = (126, 88, 25)   # Brun terre

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
title: Arbre en fleurs
---

![Une grille de 8 x 8 cases représentant un arbre en fleurs.](images/blossom.png)

Créé par la Team Zssh14, Slovaquie

```python

t = (255, 255, 0)   # Jaune pur
g = (0, 204, 255)   # Bleu ciel
w = (249, 169, 255) # Rose clair
y = (248, 97, 255)  # Magenta
z = (220, 53, 232)  # Violet
n = (126, 88, 25)   # Brun terre
o = (179, 96, 65)   # Brun terracotta
k = (46, 139, 33)   # Vert feuille

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
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Noir
f = (36, 128, 200)  # Bleu océan
g = (0, 204, 255)   # Bleu ciel

image = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, a,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

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

