## Détecter une couleur

In this step, you will set up the colour and brightness sensor. Dans cette étape, tu vas configurer le capteur de luminosité des couleurs et l'utiliser pour détecter la quantité de rouge, de vert et de bleu qui atteint le capteur. Cette couleur sera ensuite utilisée pour coloriser ton image.

This means that the image can change depending on what the sensor sees. Un·e astronaute s'approchant du capteur en chemise bleue verrait une image différente de celle d'un·e astronaute en chemise rouge.

In the whale image we used in the previous step, the background colour was black. Crée une variable appelée `x` pour stocker ta nouvelle couleur.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 5
---
c = (0, 0, 0) --- /code ---


--- task ---

Utilise le capteur de couleurs pour coloriser ton arrière-plan.

Underneath the lines where you define the colours, add the following code:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---
# images/colour_background.png
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

This code replaces the RGB values stored in `c` with the values for the colour detected by the sensor.

Tip: If you didn't use the variable `c` in your own image, replace `c` with one of the colour variables that you did use. This will allow the sensor to change that colour instead.

--- task ---

**Test :** déplace le curseur de couleur sur une couleur de ton choix, puis **exécute** ton code. Ta couleur d'arrière-plan va changer. Répète ce test avec une nouvelle couleur.

**Astuce :** tu devras cliquer sur « Run » chaque fois que tu changeras la couleur.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Now you have displayed an image and sensed a colour and used it in your program, and your code is ready for submission! 

You can save and submit your program using the form at the bottom of the code editor.
  
However, you may wish to add more images to your project, or make it come to life with animation. The next steps show you how to do this.
</p>

## Animate your project (optional)

Le programme Mission Zero de l'Astro Pi peut être exécuté pendant 30 secondes maximum. Tu utiliseras ce temps pour vérifier à plusieurs reprises le capteur de couleurs et actualiser l'image.

--- task ---


**Astuce :** assure-toi que cette ligne de code est indentée dans ta boucle `for`. Give it the variable name `image2` and change a few pixels to make your animation frame look different. Then add a short pause after it.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
---
image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

sense.set_pixels(image)

# Extra images / frames go here:

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /code ---

--- /task ---

--- task ---

At the very bottom of your code file, set up your `for` loop to repeat `14` times and alternate between displaying `image` and `image2` pausing for 1 second on each frame.

**Astuce :** pour indenter plusieurs lignes, mets en surbrillance les lignes que tu souhaites indenter puis appuie sur la touche <kbd>Tab</kbd> de ton clavier (généralement au-dessus de la touche <kbd>Verr Maj</kbd> du clavier).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7, 8
---
images/fish.png

sense.set_pixels(image) sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  sense.set_pixels(image) sleep(1)

--- /task ---

--- task ---

**Test :** exécute à nouveau ton code. Lorsque ton projet est terminé, la matrice LED est effacée, ce qui fait que toutes les lumières deviennent noires (éteintes).

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
If you would like to have more than two frames in your animation, you must make sure that the program will run for no more than 30 seconds. For example, if you have 10 images that each display for 1 second, you must change your `for` loop to repeat 3 times (10 * 3 = 30 seconds)
</p>

**Test :** exécute à nouveau ton code.

Mon code a une erreur de syntaxe ou ne s'exécute pas comme prévu :
- Vérifie que tu as indenté le code dans ta boucle `for`
- Make sure you named your second image matrix `image2` and that it is placed outside and before the loop begins.
- Check that your `sleep` times are set to exactly `1` second to avoid running past the strict 30-second execution cutoff on the ISS.

--- /task ---

--- task ---

**Enregistrer ta progression**

Tu peux enregistrer ton programme sur le projet Mission Starter en entrant le nom de ton équipe, le nom des membres de ton équipe et le code de classe qui t'est donné. Tu peux recharger ton programme sur n'importe quel appareil avec une connexion Internet en entrant le nom de ton équipe et le code de classe.

--- /task ---

--- collapse ---
---
title: Completed Whale code example
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
z = (153, 50, 204) # Orchideefoncee q = (255, 255, 0) # Jaune d = (51, 153, 255) # bleu c = (0, 0, 0) # Noir

# sense.clear()
for i in range(28): rvb = sense.color # obtenir la couleur du capteur c = (rvb.red, rvb.green, rvb.blue)

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

sense.set_pixels(image) --- /code --- --- /collapse --- --- collapse ---
---
title: Exemple de code terminé
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
sense.color.gain = 60 # Régler la sensibilité du capteur sense.color.integration_cycles = 64 # L'intervalle auquel la lecture sera effectuée

# Add colour variables and image
z = (153, 50, 204) # Orchideefoncee q = (255, 255, 0) # Jaune d = (51, 153, 255) # bleu c = (0, 0, 0) # Noir

# détecter la dernière couleur
for i in range(28): rvb = sense.color # obtenir la couleur du capteur c = (rvb.red, rvb.green, rvb.blue)

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

sense.set_pixels(image)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
images/savebutton_fr.png

sense.set_pixels(image) sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  sense.set_pixels(image) sleep(1)
