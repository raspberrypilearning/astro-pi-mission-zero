## Détecter une couleur

Dans cette étape, tu configureras le capteur de couleur et de luminosité. Tu utiliseras ce capteur pour mesurer la quantité de lumière rouge, verte et bleue qui l'atteint. Ces valeurs seront ensuite utilisées pour modifier l'une des couleurs de l'image que tu as choisie.

Cela signifie que l'image peut changer en fonction de ce que voit le capteur. Par exemple, un astronaute portant un t-shirt bleu verrait une version différente de l'image d'un astronaute portant un t-shirt rouge.

Sur l'image de baleine utilisée à l'étape précédente, la couleur d'arrière-plan était noire. Nous avons utilisé la variable `c` pour stocker son code couleur RVB :

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Utilise le capteur de couleur pour changer l'une de tes couleurs.

Sous les lignes où tu définis les couleurs, ajoute le code suivant :

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

--- /code ---

--- /task ---

Ce code remplace les valeurs RVB stockées dans `c` par les valeurs de la couleur détectée par le capteur.

Astuce : si tu n'as pas utilisé la variable `c` dans ton image, remplace `c` par une des variables de couleurs que tu as utilisées. Cela permettra au capteur de changer cette couleur à la place.

--- task ---

**Test :** déplace le curseur de couleur sur une couleur de ton choix, puis **exécute** ton code. Ta couleur d'arrière-plan va changer. Répète ce test avec une nouvelle couleur.

**Astuce :** tu devras cliquer sur « Run » chaque fois que tu changeras la couleur.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Bravo ! Tu as affiché une image, détecté une couleur et utilisé cette couleur dans ton programme. Ton code est maintenant prêt à être envoyé ! 

Tu peux enregistrer et soumettre ton programme en utilisant le formulaire situé en bas du Code Editor.
  
Tu peux aussi ajouter d'autres images à ton projet ou lui donner vie grâce à des animations. Tu découvriras comment faire dans les étapes suivantes.
</p>

## Animer ton projet (facultatif)

Ton programme Mission Zero peut s'exécuter à bord de la Station spatiale internationale (ISS) pendant 30 secondes maximum. Tu peux profiter de ce temps d'exécution pour créer une animation sur la matrice LED en faisant défiler deux images différentes ou plus.

--- task ---


**Ajoute** une deuxième image juste en dessous de ta ligne de code `sense.set_pixels(image)`. Donne-lui le nom de variable `image2` et modifie quelques pixels pour que ton image d'animation soit différente. Ajoute ensuite une courte pause.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# Extra images / frames go here:

image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

Tout en bas de ton fichier de code, crée ta boucle `for` pour qu'elle se répète `14` fois et alterne l'affichage de `image` et `image2`, en faisant une pause d'une seconde entre chaque image.

**Astuce :** vérifie que les lignes de code sous `for i in range(14):` sont indentées avec un espace afin qu'elles se trouvent **à l'intérieur** du bloc de la boucle.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1)

--- /code ---

--- /task ---

--- task ---

**Test :** exécute à nouveau ton code. Ton programme affichera instantanément la couleur détectée, puis alternera entre les deux images pour créer une animation.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Si tu veux ajouter plus de deux images à ton animation, vérifie que la durée d'exécution de ton programme ne dépasse pas 30 secondes. Par exemple, si tu as 10 images qui s'affichent chacune pendant 1 seconde, tu dois modifier ta boucle for pour qu'elle se répète 3 fois (10 × 3 = 30 secondes)
</p>

--- task ---

**Vérifier les erreurs**

Mon code contient une erreur de syntaxe ou ne change pas d'image :
- Vérifie que ton code de boucle `for` correspond à l'indentation de l'exemple.
- Vérifie que tu as bien nommé ta deuxième matrice d'image `image2` et qu'elle est placée en dehors de la boucle, avant le début de celle-ci.
- Vérifie que tes temps d'attente `sleep` sont réglés exactement sur `1` seconde afin d'éviter de dépasser la limite stricte d'exécution de 30 secondes à bord de l'ISS.

--- /task ---

--- task ---

**Enregistrer ta progression**

Tu peux enregistrer ton programme sur le projet Mission Starter en entrant le nom de ton équipe, le nom des membres de ton équipe et le code de classe qui t'est donné. Tu peux recharger ton programme sur n'importe quel appareil avec une connexion Internet en entrant le nom de ton équipe et le code de classe.

--- /task ---

--- task ---

--- collapse ---
---
title: Exemple de code complet pour une baleine
---

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
a = (255, 255, 255) # White c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Exemple de code complet pour une baleine (avec animation)
---

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
a = (255, 255, 255) # White c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1)

--- /code ---

--- /collapse ---

--- /task ---
