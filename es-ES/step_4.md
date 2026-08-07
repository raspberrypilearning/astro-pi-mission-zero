## Identifica un color

En este paso, configurarás el sensor de color y brillo. Utilizarás este sensor para medir la cantidad de luz roja, verde y azul que llega al sensor. Estos valores se utilizarán posteriormente para cambiar uno de los colores de la imagen que hayas elegido.

Esto significa que la imagen puede cambiar dependiendo de lo que vea el sensor. Por ejemplo, un astronauta que llevaba una camisa azul vería una versión diferente de la imagen de un astronauta que llevaba una camisa roja.

En la imagen de ballena que usamos en el paso anterior, el color de fondo era negro. Utilizamos la variable `c` para almacenar su código de colores RGB:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Utiliza el sensor de color para cambiar uno de tus colores.

Debajo de las líneas donde se definen los colores, añade el siguiente código:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4
---
# Percibir un color
rgb = sense.color # obtener el color del sensor
c = (rgb.red, rgb.green, rgb.blue) # usar el color detectado

--- /code ---

--- /task ---

Este código reemplaza los valores RGB almacenados en `c` por el color detectado por el sensor.

Consejo: Si no usaste la variable `c` en tu propia imagen, sustituye `c` por una de las variables de color que usaste. Esto permitirá que el sensor cambie a ese color.

--- task ---

**Prueba:** Mueve el control deslizante de color a un color de tu elección y luego **ejecuta** tu código. Tu color de fondo cambiará. Repite esta prueba con un nuevo color.

**Consejo:** Tendrás que hacer clic en 'Ejecutar' cada vez que cambies el color.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Ahora has mostrado una imagen, detectado un color y lo has usado en tu programa, ¡y tu código está listo para la sumisión! 

Puedes guardar y enviar tu programa usando el formulario en la parte inferior del editor de código.
  
Sin embargo, es posible que desees agregar más imágenes a tu proyecto o darle vida usando una animación. Los siguientes pasos le muestran cómo hacerlo.
</p>

## Anima tu proyecto (opcional)

Tu programa Mission Zero puede ejecutarse en la Estación Espacial Internacional (ISS) durante 30 segundos. Puedes usar este tiempo de ejecución para mostrar una animación en la matriz de LED alternando entre dos o más imágenes diferentes.

--- task ---


**Añade** una segunda imagen justo debajo de la línea de código `sense.set_pixels(imagen)`. Asígnale el nombre de variable `imagen2` y cambia algunos píxeles para que el fotograma de tu animación se vea diferente. Luego, añade una breve pausa.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
imagen = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(imagen)

# Aquí se incluyen imágenes/marcos adicionales:

imagen2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

En la parte inferior de tu fichero de programa, configura tu bucle `for` para que se repita `14` veces y alterne entre mostrar `imagen` e `imagen2` haciendo una pausa de 1 segundo en cada fotograma.

**Consejo:** Asegúrate de que las líneas de código debajo de `for i in range(14):` estén indentadas con un espacio para que se encuentren **dentro** del bloque del bucle.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
imagen2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Bucle 14 veces (14 * 2 segundos = 28 segundos total de animación)
for i in range(14):
  # Mostrar la segunda imagen
  sense.set_pixels(imagen2)
  sleep(1)

  # Mostrar la primera imagen
  sense.set_pixels(imagen)
  sleep(1)
  
--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta su código nuevamente. Tu programa mostrará el color detectado al instante y, a continuación, mostrará el bucle de imágenes para crear una animación.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Si quieres tener más de dos fotogramas en tu animación, debes asegurarte de que el programa se ejecutará por no más de 30 segundos. Por ejemplo, si tienes 10 imágenes que se muestran por 1 segundo, debes cambiar tu ciclo `for` a repetir 3 veces (10 * 3 = 30 segundos)
</p>

--- task ---

**Comprueba si hay errores**

Mi código tiene un error de sintaxis o no cambia fotogramas:
- Comprueba que tu bucle `for` coincide con la sangría en el ejemplo.
- Asegúrate que nombraste tu segunda imagen `imagen2` y de que está colocada fuera y antes de que el bucle comience.
- Comprueba que el tiempo del comando `sleep` esté configurado exactamente como `1` segundo para evitarpasarte de una ejecución de 30 segundos en el ISS.

--- /task ---

--- task ---

**Guarda tu progreso**

Puedes guardar tu programa en el proyecto de inicio de la misión introduciendo el nombre de tu equipo, los nombres de los miembros del equipo y el código que recibiste. Puedes recargar tu programa en cualquier dispositivo con conexión a Internet ingresando el nombre de tu equipo y el código de aula.

--- /task ---

--- task ---

--- collapse ---
---
title: Ejemplo del código de ballena terminado
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importar las bibliotecas
from sense_hat import SenseHat
from time import sleep

# Configurar el Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Configurar el sensor de color
sense.color.gain = 60 # Establecer la sensibilidad del sensor
sense.color.integration_cycles = 64 # El intervalo en el que se tomará la lectura

# Agregar variables de color e imagen
a = (255, 255, 255) # Blanco
c = (0, 0, 0)       # Negro
f = (36, 128, 200)  # Azul océano
g = (0, 204, 255)   # Azul cielo

# Percibir un color
rgb = sense.color # obtener el color del sensor
c = (rgb.red, rgb.green, rgb.blue)

imagen = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(imagen)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Ejemplo del código ballena completado (con animación)
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importar las bibliotecas
from sense_hat import SenseHat
from time import sleep

# Configurar el Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Configurar el sensor de color
sense.color.gain = 60 # Establecer la sensibilidad del sensor
sense.color.integration_cycles = 64 # El intervalo en el que se tomará la lectura

# Agregar variables de color e imagen
a = (255, 255, 255) # Blanco
c = (0, 0, 0)       # Negro
f = (36, 128, 200)  # Azul océano
g = (0, 204, 255)   # Azul cielo

# Percibir un color
rgb = sense.color # obtener el color del sensor
c = (rgb.red, rgb.green, rgb.blue)

imagen = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(imagen)

# La SUBMISIÓN BÁSICA ya está hecha

# Aquí se incluyen imágenes/marcos adicionales:
imagen2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Bucle 14 veces (14 * 2 segundos = 28 segundos total de animación)
for i in range(14):
  # Mostrar la segunda imagen
  sense.set_pixels(imagen2)
  sleep(1)

  # Mostrar la primera imagen
  sense.set_pixels(imagen)
  sleep(1)
  
--- /code ---

--- /collapse ---

--- /task ---
