## Détecter une couleur

Dans cette étape, tu vas configurer le capteur de luminosité des couleurs et l'utiliser pour détecter la quantité de rouge, de vert et de bleu qui atteint le capteur. Cette couleur sera ensuite utilisée pour coloriser ton image. Un astronaute s'approchant du capteur en chemise bleue verrait une image différente de celle d'un astronaute en chemise rouge.

![image affichée avec un arrière-plan rose sur la matrice LED](images/colour_background.png)

Quelle que soit l'image choisie, l'arrière-plan utilise la variable `c` qui est définie sur le noir.

--- task ---

Utilise le capteur de couleurs pour coloriser ton arrière-plan.

Ajoute du code avant ta liste d'images pour obtenir la couleur du capteur et modifie ta variable de couleur d'arrière-plan `c` pour utiliser la couleur détectée par le capteur de couleur Sense HAT au lieu du noir.

**Astuce :** tu n'as pas besoin de taper les commentaires qui commencent par « # » (ils sont là pour expliquer le code).

--- code ---
---
language: python 
filename: main.py 
line_numbers: false 
line_number_start: 1
line_highlights: 9-10
---
# Ajouter des variables de couleur et une image

c = (0, 0, 0) # Noir
m = (34, 139, 34) # Vert forêt
q = (255, 255, 0) # Jaune
t = (255, 140, 0) # Orange foncé
y = (255, 20, 147) # Rose foncé

rvb = sense.color # obtenir la couleur du capteur
c = (rvb.red, rvb.green, rvb.blue) # utiliser la couleur détectée

image = [
  c, c, y, y, y, y, c, c,
  c, y, y, t, t, y, y, c,
  y, y, t, q, q, t, y, y,
  c, y, y, t, t, y, y, c,
  c, c, y, y, y, y, c, c,
  m, c, c, m, m, c, c, m,
  c, m, m, m, m, m, m, c,
  c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

**Test :** déplace le curseur de couleur sur une couleur de ton choix, puis **exécute** ton code. Ta couleur de fond va changer. Répète ce test avec une nouvelle couleur.

**Astuce :** tu devras cliquer sur « Exécuter » chaque fois que tu changeras la couleur.

--- /task ---

## Fais tourner ton programme en boucle

Le programme Mission Zero de l'Astro Pi peut être exécuté pendant 30 secondes maximum. Tu utiliseras ce temps pour vérifier à plusieurs reprises le capteur de couleurs et actualiser l'image.

Ton code utilisera une boucle `for` pour s'exécuter 28 fois. À chaque **fois**, il va :
+ détecter la dernière couleur
+ mettre à jour la couleur d'arrière-plan de l'image
+ faire une pause d'une seconde

--- task ---

**Trouve** ta ligne de code `rvb = sense.color`.

**Ajoute** du code juste au-dessus pour configurer ta boucle `for` pour `28` répétitions.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---
for i in range(28):
rvb = sense.color # obtenir la couleur du capteur
c = (rvb.red, rvb.green, rvb.blue)

image = [
  c, c, y, y, y, y, c, c,
  c, y, y, t, t, y, y, c,
  y, y, t, q, q, t, y, y,
  c, y, y, t, t, y, y, c,
  c, c, y, y, y, y, c, c,
  m, c, c, m, m, c, c, m,
  c, m, m, m, m, m, m, c,
  c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

Tu dois maintenant indenter tout ton code sous la boucle `for` pour qu'il se trouve **à l'intérieur** de la boucle `for`.

**Astuce :** pour indenter plusieurs lignes, mets en surbrillance les lignes que tu souhaites indenter puis appuie sur la touche <kbd>Tab</kbd> de ton clavier (généralement au-dessus de la touche <kbd>Verr Maj</kbd> du clavier).

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 2 - 17
---
for i in range(28):
  rvb = sense.color # obtenir la couleur du capteur
  c = (rvb.red, rvb.green, rvb.blue)

  image = [
    c, c, y, y, y, y, c, c,
    c, y, y, t, t, y, y, c,
    y, y, t, q, q, t, y, y,
    c, y, y, t, t, y, y, c,
    c, c, y, y, y, y, c, c,
    m, c, c, m, m, c, c, m,
    c, m, m, m, m, m, m, c,
    c, c, c, m, m, c, c, c]
    
  # Afficher l'image

  sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Au bas de ton code, ajoute un `sleep` d'une seconde à l'intérieur de ta boucle :

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 4
---
  # Afficher l'image

  sense.set_pixels(image)
  sleep(1)  
  
--- /code ---

**Astuce :** assure-toi que cette ligne de code est indentée dans ta boucle `for`.

--- /task ---

--- task ---

**Test :** Exécute ton code et modifie le sélecteur de couleur plusieurs fois lorsque ton projet est en cours d'exécution. Vérifie que ton image s'actualise pour utiliser la couleur détectée lors de sa prochaine exécution.

L'image cessera de s'actualiser lorsque la boucle se terminera afin que le programme ne dure pas plus de 30 secondes.

--- /task ---

--- task ---

**Déboguer**

Mon code a une erreur de syntaxe ou ne s'exécute pas comme prévu :

- Vérifie que ton code correspond au code des exemples ci-dessus
- Vérifie que tu as indenté le code dans ta boucle `for`
- Vérifie que ta liste est entourée de `[` et `]`
- Vérifie que chaque variable de couleur de la liste est séparée par une virgule

Mon code s'exécute pendant plus de 30 secondes :

- Diminue le nombre de fois où ta boucle « for » s'exécute, de 28 à 25 ou même 20.
- Diminue la durée du « sleep », de 1 seconde à 0,5 seconde.

--- /task ---

--- task ---

Ajoute `sense.clear()` à la fin de ton code pour effacer l'image à la fin de ta boucle. Cela t'aidera à voir quand ton animation a fini de fonctionner.

**Astuce :** assure-toi de **ne pas** indenter la ligne de code `sense.clear()` car tu veux que cela ne s'exécute qu'une fois à la fin de ton animation.

--- code ---
---
language: python 
filename: main.py 
line_numbers: false 
line_number_start: 1
line_highlights: 6
---
  # Afficher l'image

  sense.set_pixels(image) 
  sleep(1)

sense.clear()

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute à nouveau ton code. Lorsque ton projet est terminé, la matrice LED est effacée, ce qui fait que toutes les lumières deviennent noires (éteintes).

--- /task ---

--- task ---

**Déboguer**

La matrice LED devient noire toutes les secondes :

- Vérifie que tu n'as pas indenté le code `sense.clear()` dans ta boucle `for`

--- /task ---

--- task ---

Ajoute du code pour effacer la matrice de LED par une couleur de ton choix. Crée une variable appelée `x` pour stocker ta nouvelle couleur.

Tu peux mélanger ta propre couleur ou utiliser les valeurs de la liste de couleurs pour créer ta nouvelle couleur `x`.

[[[generic-theory-colours]]]

--- code ---
---
language: python 
filename: main.py 
line_numbers: false 
line_number_start: 1
line_highlights: 6-7
---
  # Afficher l'image

  sense.set_pixels(image) 
  sleep(1)

x = (178, 34, 34)  # choisis tes propres valeurs de rouge, vert et bleu entre 0 et 255 sense.clear(x)

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute à nouveau ton code. Lorsque ton projet est terminé, la matrice LED s'efface et utilise la couleur que tu as choisie. Tu peux changer puis tester la couleur autant de fois que tu le souhaites.

--- /task ---

--- task ---

--- collapse ---

---
title: Exemple de code terminé
---

![Une grille avec des carrés de 8 x 8 montrant une fleur rose sur une tige verte.](images/flower.png)

--- code ---
---
language: python 
filename: main.py
line_numbers: false
---
# Importer les bibliothèques
from sense_hat import SenseHat 
from time import sleep

# Configuer le Sense HAT
sense = SenseHat() 
sense.set_rotation(270)

# Configurer le capteur de couleurs
sense.color.gain = 60 # Régler la sensibilité du capteur 
sense.color.integration_cycles = 64 # L'intervalle auquel la mesure est effectuée

# Ajouter des variables de couleur et une image

c = (0, 0, 0) # Noir
m = (34, 139, 34) # Vert forêt
q = (255, 255, 0) # Jaune
t = (255, 140, 0) # Orange foncé
y = (255, 20, 147) # Rose foncé

for i in range(28):
  rvb = sense.color # obtenir la couleur du capteur
  c = (rvb.red, rvb.green, rvb.blue)

  image = [
    c, c, y, y, y, y, c, c,
    c, y, y, t, t, y, y, c,
    y, y, t, q, q, t, y, y,
    c, y, y, t, t, y, y, c,
    c, c, y, y, y, y, c, c,
    m, c, c, m, m, c, c, m,
    c, m, m, m, m, m, m, c,
    c, c, c, m, m, c, c, c]

  # Afficher l'image

  sense.set_pixels(image)
  sleep(1)

x = (178, 34, 34)  # choisis tes propres valeurs de rouge, vert et bleu entre 0 et 255
sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
