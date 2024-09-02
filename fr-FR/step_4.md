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
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9, 10
---

# Ajouter des variables de couleur et une image

a = (255, 255, 255) # White c = (0, 0, 0) # Black f = (25, 25, 112) # MidnightBlue m = (34, 139, 34) # ForestGreen

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ m, m, m, m, m, c, c, c, m, f, m, f, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, a, c, c, c, a, m, m, c, c, c ,c ,c ,c, m, m, c, c, c, a, c, c, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]


--- /code ---

--- /task ---

--- task ---

**Test :** déplace le curseur de couleur sur une couleur de ton choix, puis **exécute** ton code. Ta couleur d'arrière-plan va changer. Répète ce test avec une nouvelle couleur.

**Astuce :** tu devras cliquer sur « Run » chaque fois que tu changeras la couleur.

--- /task ---

## Fais tourner ton programme en boucle

Le programme Mission Zero de l'Astro Pi peut être exécuté pendant 30 secondes maximum. Tu utiliseras ce temps pour vérifier à plusieurs reprises le capteur de couleurs et actualiser l'image.

Ton code utilisera une boucle `for` pour s'exécuter 28 fois. À chaque **fois**, il va :
+ détecter la dernière couleur
+ mettre à jour la couleur d'arrière-plan de l'image
+ faire une pause d'une seconde

--- task ---

**Trouve** ta ligne de code `rgb = sense.color`.

**Ajoute** du code juste au-dessus pour configurer ta boucle `for` pour `28` répétitions.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ m, m, m, m, m, c, c, c, m, f, m, f, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, a, c, c, c, a, m, m, c, c, c ,c ,c ,c, m, m, c, c, c, a, c, c, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]


--- /code ---

--- /task ---

--- task ---

Tu dois maintenant indenter tout ton code sous la boucle `for` pour qu'il se trouve **à l'intérieur** de la boucle `for`.

**Astuce :** pour indenter plusieurs lignes, mets en surbrillance les lignes que tu souhaites indenter puis appuie sur la touche <kbd>Tab</kbd> de ton clavier (généralement au-dessus de la touche <kbd>Verr Maj</kbd> du clavier).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ m, m, m, m, m, c, c, c, m, f, m, f, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, a, c, c, c, a, m, m, c, c, c ,c ,c ,c, m, m, c, c, c, a, c, c, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]


  # Display the image

  sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Au bas de ton code, ajoute un `sleep` d'une seconde à l'intérieur de ta boucle :

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 5
---

  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Astuce :** assure-toi que cette ligne de code est indentée dans ta boucle `for`.

--- /task ---

--- task ---

**Test :** exécute ton code et modifie le sélecteur de couleur plusieurs fois lorsque ton projet est en cours d'exécution. Vérifie que ton image s'actualise pour utiliser la couleur détectée lors de sa prochaine exécution.

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
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7
---

  # Display the image

  sense.set_pixels(image) sleep(1)

sense.clear()

--- /code ---

--- /task ---

--- task ---

**Test :** exécute à nouveau ton code. Lorsque ton projet est terminé, la matrice LED est effacée, ce qui fait que toutes les lumières deviennent noires (éteintes).

--- /task ---

--- task ---

**Déboguer**

La matrice LED devient noire toutes les secondes :

- Vérifie que tu n'as pas indenté le code `sense.clear()` dans ta boucle `for`

--- /task ---

--- task ---

Ajoute du code pour effacer la matrice de LED par une couleur de ton choix. Crée une variable appelée `x` pour stocker ta nouvelle couleur.

Tu peux mélanger ta propre couleur ou utiliser les valeurs de la liste de couleurs pour créer ta nouvelle couleur `x`.

\[[[generic-theory-simple-colours]]\] \[[[ambient-colours\]]]

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7, 8
---

  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /task ---

--- task ---

**Test :** exécute à nouveau ton code. Lorsque ton projet est terminé, la matrice LED s'efface et utilise la couleur que tu as choisie. Tu peux changer puis tester la couleur autant de fois que tu le souhaites.

--- /task ---


--- task ---

**Enregistre ta progression**

Tu peux enregistrer ton programme sur le projet Mission Starter en entrant le nom de ton équipe, le nom des membres de ton équipe et le code de classe qui t'est donné. Tu peux recharger ton programme sur n'importe quel appareil avec une connexion Internet en entrant le nom de ton équipe et le code de classe.

![Capture d'écran du bouton Enregistrer Mission Zero](images/mz_savebutton_v2.png)

--- /task ---


--- task ---

--- collapse ---

---
title: Exemple de code terminé
---

![Une grille de 8 x 8 cases représentant un crocodile.](images/croc.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Import the libraries
from sense_hat import SenseHat from time import sleep

# Set up the Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image

a = (255, 255, 255) # White c = (0, 0, 0) # Black f = (25, 25, 112) # MidnightBlue m = (34, 139, 34) # ForestGreen

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ m, m, m, m, m, c, c, c, m, f, m, f, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, a, c, c, c, a, m, m, c, c, c ,c ,c ,c, m, m, c, c, c, a, c, c, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]


  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
