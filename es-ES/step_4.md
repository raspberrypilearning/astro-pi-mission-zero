## Identifica un color

En este paso, configurarás el sensor de luminosidad de color y lo utilizarás para detectar la cantidad de rojo, verde y azul que llega al sensor. Este color se usará para colorear la imagen que has elegido. Un astronauta caminando hacia el sensor con una camisa azul vería una imagen diferente a la de un astronauta con una camisa roja.

![imagen con un fondo rosado en la matriz LED](images/colour_background.png)

Cualquiera que sea la imagen que elijas, el fondo usa la variable `c` que se establece en negro.

--- task ---

Usa el sensor de color para colorear tu fondo.

Añade código antes de tu lista de imágenes para obtener el color del sensor y cambia tu variable de color de fondo `c` para usar el color detectado por el sensor de color HAT Sense en lugar de negro.

**Sugerencia:** No necesitas escribir los comentarios que comienzan con '#' (están ahí para explicar el código).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9, 10
---

# Agregar variables de color e imagen

a = (255, 255, 255) # Blanco c = (0, 0, 0) # Negro f = (25, 25, 112) # Azul medianoche m = (34, 139, 34) # Verde bosque

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


--- /code ---

--- /task ---

--- task ---

**Prueba:** Mueve el control deslizante de color a un color de tu elección y luego **ejecuta** tu código. Tu color de fondo cambiará. Repite esta prueba con un nuevo color.

**Consejo:** Tendrás que hacer clic en 'Ejecutar' cada vez que cambies el color.

--- /task ---

## Repite tu programa

El programa Astro Pi Mission Zero puede ejecutarse hasta 30 segundos. Utilizarás este tiempo para comprobar repetidamente el sensor de color y actualizar la imagen.

Tu código usará un bucle `for` para que se ejecute 28 veces. **Cada** vez:
+ detectará el último color
+ actualizará el color de fondo de la imagen
+ se detendrá por un segundo

--- task ---

**Encuentra** tu línea de código `rgb = sense.color`.

**Agrega** código por encima para configurar tu bucle `for` para `28` repeticiones.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


--- /code ---

--- /task ---

--- task ---

Ahora necesitas indentar todo tu código debajo del bucle `for` para que quede **dentro** del bucle `for`.

**Consejo:** Para indentar varias líneas al mismo tiempo, resalta las líneas que deses indentar y luego presiona la tecla <kbd>Tab</kbd> del teclado (normalmente sobre la tecla <kbd>Bloqueo de mayúsculas</kbd> del teclado).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


  # Display the image

  sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

En la parte inferior de tu código, añade un `sleep` de un segundo dentro de tu bucle:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 5
---

  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Consejo:** Asegúrate de que esta línea de código está indentada dentro de tu bucle `for`.

--- /task ---

--- task ---

**Prueba:** Ejecuta su código y cambia el selector de color varias veces mientras se ejecuta tu proyecto. Comprueba que tu imagen se actualiza para usar el color detectado en la próxima ejecución.

La imagen dejará de actualizarse cuando termine el bucle para que el programa no se ejecute durante más de 30 segundos.

--- /task ---

--- task ---

**Depurar**

Mi código tiene un error de sintaxis o no se ejecuta como se esperaba:

- Comprueba que tu código coincide con el código en los ejemplos anteriores
- Verifica que has indentado el código en su bucle `for`
- Comprueba que tu lista está rodeada por `[` y `]`
- Verifica que cada variable de color de la lista esté separada por una coma

Mi código se ejecuta por más de 30 segundos:

- Reduce el número de veces que se ejecuta tu bucle for de 28 a 25 o incluso a 20.
- Disminuye la longitud de sleep, de 1 segundo a 0.5 segundos.

--- /task ---

--- task ---

Añade `sense.clear()` al final de tu código para borrar la imagen al final de tu bucle. Esto te ayudará a ver cuándo tu animación ha terminado de ejecutarse.

**Consejo:** Asegúrate de **no** indentar la línea de código `sense.clear()` ya que quieres que esto solo se ejecute una vez al final de tu animación.

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

**Prueba:** Ejecuta su código nuevamente. Cuando su proyecto haya terminado de ejecutarse, la matriz de LED se borrará y todas las luces se apagarán (lo cual hará que se vea negro).

--- /task ---

--- task ---

**Depurar**

La matriz de LEDs se vuelve negra cada segundo:

- Comprueba que no hayas indentado el código `sense.clear()` dentro de tu bucle `for`

--- /task ---

--- task ---

Agrega código para borrar la matriz de LEDs a un color de su elección. Crea una variable `x` para guardar el color que has seleccionado.

Puedes mezclar tu propio color o usar los valores de la lista de colores para crear tu nuevo color `x`.

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

**Prueba:** Ejecuta su código de nuevo. Cuando su proyecto haya terminado de ejecutarse, la matriz de LEDs cambiará al color elegido. Puedes cambiar y luego probar el color tantas veces como quieras.

--- /task ---


--- task ---

**Guarda tu progreso**

Puedes guardar tu programa en el proyecto de inicio de la misión introduciendo el nombre de tu equipo, los nombres de los miembros del equipo y el código que recibiste. Puedes recargar tu programa en cualquier dispositivo con conexión a Internet ingresando el nombre de tu equipo y el código de aula.

![Captura de pantalla del botón Guardar de Mission Zero](images/mz_savebutton_v2.png)

--- /task ---


--- task ---

--- collapse ---

---
title: Ejemplo de código terminado
---

![Una cuadrícula con cuadrados de 8 x 8 que muestra un pez.](images/fish.png)

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

a = (255, 255, 255) # Blanco c = (0, 0, 0) # Negro f = (25, 25, 112) # Azul medianoche m = (34, 139, 34) # Verde bosque

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # elige tus propios valores de rojo, verde y azul entre 0 y 255 sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
