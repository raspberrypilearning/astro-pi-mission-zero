## Identifica un color

In this step, you will set up the colour and brightness sensor. En este paso, configurarás el sensor de luminosidad de color y lo utilizarás para detectar la cantidad de rojo, verde y azul que llega al sensor. Este color se usará para colorear la imagen que has elegido.

This means that the image can change depending on what the sensor sees. Un astronauta caminando hacia el sensor con una camisa azul vería una imagen diferente a la de un astronauta con una camisa roja.

In the whale image we used in the previous step, the background colour was black. Crea una variable `x` para guardar el color que has seleccionado.

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0) --- /code ---


--- task ---

Usa el sensor de color para colorear tu fondo.

Underneath the lines where you define the colours, add the following code:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---
# **Encuentra** tu línea de código `rgb = sense.color`.
rgb = sense.color # obtener el color del sensor c = (rgb.red, rgb.green, rgb.blue) # usar el color detectado

This code replaces the RGB values stored in `c` with the values for the colour detected by the sensor.

Tip: If you didn't use the variable `c` in your own image, replace `c` with one of the colour variables that you did use. This will allow the sensor to change that colour instead.

--- task ---

**Prueba:** Mueve el control deslizante de color a un color de tu elección y luego **ejecuta** tu código. Tu color de fondo cambiará. Repite esta prueba con un nuevo color.

**Consejo:** Tendrás que hacer clic en 'Ejecutar' cada vez que cambies el color.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Now you have displayed an image and sensed a colour and used it in your program, and your code is ready for submission! 

You can save and submit your program using the form at the bottom of the code editor.
  
However, you may wish to add more images to your project, or make it come to life with animation. The next steps show you how to do this.
</p>

## Animate your project (optional)

El programa Astro Pi Mission Zero puede ejecutarse hasta 30 segundos. Utilizarás este tiempo para comprobar repetidamente el sensor de color y actualizar la imagen.

--- task ---


**Consejo:** Asegúrate de que esta línea de código está indentada dentro de tu bucle `for`. Give it the variable name `image2` and change a few pixels to make your animation frame look different. Then add a short pause after it.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
---
imagen = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

sense.set_pixels(image)

# Extra images / frames go here:

imagen = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /code ---

--- /task ---

--- task ---

At the very bottom of your code file, set up your `for` loop to repeat `14` times and alternate between displaying `image` and `image2` pausing for 1 second on each frame.

**Consejo:** Para indentar varias líneas al mismo tiempo, resalta las líneas que deses indentar y luego presiona la tecla <kbd>Tab</kbd> del teclado (normalmente sobre la tecla <kbd>Bloqueo de mayúsculas</kbd> del teclado).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7, 8
---
images/fish.png

sense.set_pixels(imagen) sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  sense.set_pixels(imagen) sleep(1)

--- /task ---

--- task ---

**Prueba:** Ejecuta su código nuevamente. Cuando su proyecto haya terminado de ejecutarse, la matriz de LED se borrará y todas las luces se apagarán (lo cual hará que se vea negro).

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
If you would like to have more than two frames in your animation, you must make sure that the program will run for no more than 30 seconds. For example, if you have 10 images that each display for 1 second, you must change your `for` loop to repeat 3 times (10 * 3 = 30 seconds)
</p>

**Cada** vez:

My code has a syntax error or doesn't change frames:
- Comprueba que tu código coincide con el código en los ejemplos anteriores
- Make sure you named your second image matrix `image2` and that it is placed outside and before the loop begins.
- Check that your `sleep` times are set to exactly `1` second to avoid running past the strict 30-second execution cutoff on the ISS.

--- /task ---

--- task ---

**Guarda tu progreso**

Puedes guardar tu programa en el proyecto de inicio de la misión introduciendo el nombre de tu equipo, los nombres de los miembros del equipo y el código que recibiste. Puedes recargar tu programa en cualquier dispositivo con conexión a Internet ingresando el nombre de tu equipo y el código de aula.

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
z = (153, 50, 204) # Orquídea Oscuro q = (255, 255, 0) # Amarillo d = (51, 153, 255) # Azul c = (0, 0, 0) # Negro

# sense.clear()
for i in range(28): rgb = sense.color # obtener el color del sensor c = (rgb.red, rgb.green, rgb.blue)

imagen = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /collapse ---
---
title: Ejemplo de código terminado
---

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Repite tu programa
from sense_hat import SenseHat from time import sleep

# Añade código antes de tu lista de imágenes para obtener el color del sensor y cambia tu variable de color de fondo `c` para usar el color detectado por el sensor de color HAT Sense en lugar de negro.
sense = SenseHat() sense.set_rotation(270)

# actualizará el color de fondo de la imagen
for i in range(28): rgb = sense.color # obtener el color del sensor c = (rgb.red, rgb.green, rgb.blue)

# Add colour variables and image
z = (153, 50, 204) # Orquídea Oscuro q = (255, 255, 0) # Amarillo d = (51, 153, 255) # Azul c = (0, 0, 0) # Negro

# detectará el último color
for i in range(28): rgb = sense.color # obtener el color del sensor c = (rgb.red, rgb.green, rgb.blue)

imagen = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

images/colour_background.png

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
images/savebutton_es.png

sense.set_pixels(imagen) sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  sense.set_pixels(imagen) sleep(1)
