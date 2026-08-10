## Afficher une image

La matrice LED de l'Astro Pi peut afficher des couleurs. Dans cette étape, tu vas afficher des images de la nature sur la matrice LED de l'Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Une <span style="color: #0faeb0">**matrice LED**</span> est une grille de LED qui peuvent être contrôlées individuellement ou en groupe pour créer différents effets de lumière. La matrice LED du Sense HAT comporte 64 LED affichées dans une grille de 8 x 8. Les LED peuvent être programmées pour produire une large gamme de couleurs.
</p>

![Une capture d'écran de la fenêtre de l'émulateur montrant l'unité de vol avec la matrice LED qui affiche l'image d'une fleur.](images/fu-pic.png)

--- task ---

Ouvre le [projet de démarrage de Mission Zero](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"}.

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
sense = SenseHat() s
ense.set_rotation(270)

# Configurer le capteur de couleurs
sense.color.gain = 60 # Régler la sensibilité du capteur 
sense.color.integration_cycles = 64 # L'intervalle auquel la lecture sera effectuée

--- /code ---

![Une capture d'écran de l'émulateur Sense HAT avec des lignes de code de démarrage affichées dans le panneau de gauche.](images/sense-hat-emulator3.png)

--- /task ---

### Couleurs RVB

Tu peux créer des couleurs en utilisant différentes valeurs de rouge, vert et bleu. Tu peux découvrir les couleurs RVB ici :

[[[generic-theory-simple-colours]]]

La matrice LED est une grille 8 x 8. Chaque LED de la grille peut être réglée sur une couleur différente. Voici une liste de variables pour 24 couleurs différentes. Chaque couleur comporte une valeur de rouge, vert et bleu :

[[[ambient-colours]]]

### Choisir une image

--- task ---

**Choisir :** choisis une image à afficher parmi les options ci-dessous. Python stocke les informations d'une image dans une liste. Le code de chaque image comprend les variables de couleur utilisées et la liste.

Tu devras **copier** tout le code de l'image que tu as choisie puis le **coller** dans ton projet sous la ligne indiquant `# Ajouter des variables de couleur et une image`.

--- collapse ---

---
title: Poisson
---

![Une grille de 8 x 8 cases représentant un poisson.](images/fish.png)

Créé par l'équipe chalka, Pologne

```python
z = (153, 50, 204) # Orchideefoncee
q = (255, 255, 0) # Jaune
d = (51, 153, 255) # bleu
c = (0, 0, 0) # Noir

image = [
d, d, z, d, d, d, d, d,
d, d, d, z, z, d, d, d,
z, d, q, q, q, q, d, d,
z, z, q, q, q, c, q, d,
z, z, z, q, q, q, q, d,
z, z, q, q, q, q, q, d,
z, d, q, z, z, q, d, d,
d, d, d, z, d, d, d, d]

```

--- /collapse ---


--- collapse ---

---
title: Morse
---

![Une grille de 8 x 8 cases représentant un morse.](images/walrus.png)

Créé par l'équipe Walrus, Finlande

```python
h = (0, 255, 255) # Cyan
c = (0, 0, 0) # Noir
s = (139, 69, 19) # Brunfonce
a = (255, 255, 255) # Blanc
r = (184, 134, 11) # Jaunedorefonce

image = [
h, h, h, h, h, h, h, h,
h, h, s, s, s, h, h, h,
h, s, s, s, s, s, h, h,
h, s, c, s, c, s, s, s,
h, r, r, r, r, r, s, s,
h, h, a, s, a, s, s, s,
h, h, a, s, a, s, s, s,
r, r, s, s, s, s, s, s]

```

--- /collapse ---

--- collapse ---
---
title: Paxi
---

![Une grille de 8 x 8 cases représentant un Paxi.](images/paxi.png)

Créé par l'équipe tony_pi, Italie

```python
v = (255, 0, 0) # Rouge
m = (34, 139, 34) # Vertforet
c = (0, 0, 0) # Noir 
e = (100, 149, 237) # Bleubleuet
l = (0, 255, 0) # Vert

image = [
    c, v, m, c, c, m, v, c,
    c, c, v, v, v, v, c, c,
    c, v, c, e, l, e, v, c,
    c, v, c, l, l, l, v, c,
    c, v, c, l, c, l, v, c,
    c, c, v, v, v, v, c, c,
    c, c, l, c, c, l, c, c,
    c, m, m, c, c, m, m, c]

```

--- /collapse ---


--- collapse ---
---
title: Chien
---

![Une grille de 8 x 8 cases représentant une tête de chien.](images/dog.png)

Créé par l'équipe ptpr_07, Espagne

```python

c = (0, 0, 0) # Noir
r = (184, 134, 11) # Jaunedorefonce
s = (139, 69, 19) # Brunfonce
y = (255, 20, 147) # Fuchsiavif

image = [
    c, r, r, c, c, r, r, c,
    c, r, s, s, s, s, r, c,
    c, r, c, s, s, c, r, c,
    c, s, s, s, s, s, s, c,
    c, s, s, s, s, s, s, c,
    c, s, s, c, c, s, s, c,
    c, c, s, y, y, s, c, c,
    c, c, c, y, y, c, c, c]


```

--- /collapse ---

--- collapse ---
---
title: Caméléon
---

![Une grille de 8 x 8 carrés représentant un caméléon aux couleurs de l'arc-en-ciel.](images/chameleon.png)

Créé par l'équipe The_ETs, Royaume-Uni

```python

c = (0, 0, 0) # Noir
s = (139, 69, 19) # Brunfonce
a = (255, 255, 255) # Blanc
v = (255, 0, 0) # Rouge
t = (255, 140, 0) # Orangefonce
q = (255, 255, 0) # Jaune
m = (34, 139, 34) # Vertfonce
h = (0, 255, 255) # Cyan
z = (153, 50, 204) # Orchideefoncee
y = (255, 20, 147) # Fuchsiavif

image = [
    a, a, v, v, t, a, a, a,
    a, v, v, t, t, q, a, a,
    v, c, t, t, q, q, m, a,
    v, t, t, q, q, m, m, h,
    s, s, q, s, s, m, s, h,
    a, a, a, a, a, a, a, z,
    a, a, a, a, y, a, a, z,
    a, a, a, a, a, y, z, a]

```

--- /collapse ---

--- collapse ---
---
title: Cerf-volant
---

![Une grille de 8 x 8 cases représentant un cerf-volant.](images/kite.png)

Créé par l'équipe Val, Grèce

```python

c = (0, 0, 0) # Noir
m = (34, 139, 34) # Vertforet
v = (255, 0, 0) # Rouge
q = (255, 255, 0) # Jaune
e = (0, 0, 205) # Bleumoyen
h = (0, 255, 255) # Cyan

image = [
    h, h, h, h, h, h, h, h, 
    h, h, h, e, e, v, v, h, 
    h, h, h, e, e, v, v, h, 
    h, h, h, q, q, m, m, h, 
    h, h, h, q, q, m, m, h,
    h, h, c, h, h, h, h, h, 
    h, c, h, h, h, h, h, h, 
    c, h, h, h, h, h, h, h]

```

--- /collapse ---

--- collapse ---
---
title: Poulet
---

![Une grille de 8 x 8 cases représentant un poulet.](images/chicken.png)

Créé par l'équipe Slepicky, Tchéquie

```python

v = (255, 0, 0) # Rouge
c = (0, 0, 0) # Noir
b = (105, 105, 105) # Grismat
q = (255, 255, 0) # Jaune
r = (184, 134, 11) # Jaunedorefonce

image =  [
    c, c, v, v, v, c, c, c,
    c, v, b, b, r, c, c, r,
    c, b, c, b, b, c, r, b,
    q, r, b, b, b, b, b, r,
    c, v, b, b, b, b, r, b,
    c, v, b, r, r, r, b, r,
    c, c, c, r, b, q, r, c,
    c, c, c, c, q, q, c, c]

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
line_highlights: 18, 19
---
z = (153, 50, 204) # Orchideefoncee
q = (255, 255, 0) # Jaune
d = (51, 153, 255) # bleu
c = (0, 0, 0) # Noir

image = [
d, d, z, d, d, d, d, d,
d, d, d, z, z, d, d, d,
z, d, q, q, q, q, d, d,
z, z, q, q, q, c, q, d,
z, z, z, q, q, q, q, d,
z, z, q, q, q, q, q, d,
z, d, q, z, z, q, d, d,
d, d, d, z, d, d, d, d]

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

![Bouton Enregistrer Mission Zero](images/savebutton_fr.png)

--- /task --- 
