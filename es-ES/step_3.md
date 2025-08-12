## Muestra una imagen

La matriz LED del Astro Pi puede mostrar colores. En este paso, mostrarás imágenes de la naturaleza en la matriz LED de Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Una <span style="color: #0faeb0">**matriz de LEDs**</span> es una cuadrícula de LEDs que se puede controlar individualmente o en grupo para crear diferentes efectos de iluminación. La matriz de LEDs del Sense HAT tiene 64 LEDs que se muestran en una cuadrícula de 8 x 8. Los LED se pueden programar para producir una amplia gama de colores.
</p>

![Una captura de pantalla de la ventana del emulador que muestra la Unidad de vuelo con la matriz de LEDs mostrando una foto de una flor.](images/fu-pic.png)

--- task ---

Abre el [proyecto inicial de Mission Zero](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"} para el proyecto Mission Zero.

Comprobarás que se han añadido automáticamente unas líneas de código.

Este código se conecta al Astro Pi, se asegura de que la pantalla LED de Astro Pi se muestre en la orientación correcta e inicializa el sensor de color. Deja estas líneas de código, ya que las necesitarás más adelante.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Importar las bibliotecas
from sense_hat import SenseHat from time import sleep

# Configurar el Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Configurar el sensor de color
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Una captura de pantalla del emulador Sense Hat con las líneas de código de inicio que se muestran en el panel de la izquierda.](images/sense-hat-emulator3.png)

--- /task ---

### Colores RGB

Los colores se pueden crear usando diferentes proporciones de rojo, verde y azul. Aquí puedes encotrar información sobre los colores RGB:

[[[generic-theory-simple-colours]]]

La matriz de LEDs es una cuadrícula de 8 x 8. Cada LED de la cuadrícula se puede configurar en un color diferente. Aquí hay una lista de variables para 24 colores diferentes. Cada color tiene un valor para rojo, verde y azul:

[[[ambient-colours]]]

### Elige una imagen

--- task ---

**Seleccionar:** Elije una imagen para mostrar entre las opciones a continuación. Python almacena la información de una imagen en una lista. El código para cada imagen incluye las variables de color utilizadas y la lista.

Deberás **copiar** todo el código para la imagen elegida y luego **pegarlo** en ru proyecto debajo de la línea que dice `# Agregar variables de color e imagen`.

--- collapse ---

---
title: Zorro
---

![Una cuadrícula con cuadrados de 8 x 8 que muestra la cara de un zorro.](images/fish.png)

Creado por el equipo Chalka, Polonia

```python
c = (0, 0, 0) # Negro
a = (255, 255, 255) # Blanco
t = (255, 140, 0) # Naranja oscuro

imagen = [
t, a, t, c, c, t, a, t,
t, a, t, c, c, t, a, t,
t, t, t, t, t, t, t, t,
t, a, c, t, t, c, a, t,
t, t, t, t, t, t, t, t,
a, a, a, c, c, a, a, a,
c, a, a, a, a, a, a, c,
c, c, a, a, a, a, c, c]

```

--- /collapse ---


--- collapse ---

---
title: Elefante
---

![Una cuadrícula con cuadrados de 8 x 8 que muestra un elefante.](images/walrus.png)

Creado por el equipo ILiFanT, Finlandia

```python
c = (0, 0, 0) # Negro
b = (105, 105, 105) # Gris oscuro
a = (255, 255, 255) # Blanco

imagen = [
    c, c, c, c, c, c, c, c,
    c, b, b, b, c, c, c, c,
    c, b, c, b, c, c, b, b,
    c, b, c, c, c, b, b, b,
    c, b, b, c, c, b, c, b,
    c, b, b, b, b, b, b, b,
    c, c, b, b, a, b, b, b,
    c, c, c, c, a, b, b, b]

```

--- /collapse ---

--- collapse ---
---
Creado por el equipo 6TETHASI, Países Bajos
---

![Una cuadrícula con cuadrados de 8 x 8 que muestra un cactus.](images/paxi.png)

Creado por el equipo i_pupi, Italia

```python
a = (255, 255, 255) # Blanco
c = (0, 0, 0) # Negro
n = (154, 205, 50) # Verde amarillo
q = (255, 255, 0) # Amarillo
t = (255, 140, 0) # Naranja oscuro

imagen = [   
  q, q, c, n, c, c, a, c,
  q, c, c, n, c, a, a, a,
  c, n, c, n, c, c, c, c,
  c, n, n, n, c, n, c, c,
  c, a, n, n, n, n, c, c,
  a, a, a, n, c, a, a, a,
  c, c, c, n, a, a, a, c,
  t, t, t, t, t, t, t, t]

```

--- /collapse ---


--- collapse ---
---
title: Cocodrilo
---

![Una cuadrícula con cuadrados de 8 x 8 que muestra la cabeza de un cocodrilo.](images/dog.png)

Creado por el equipo camrus_6, Reino Unido

```python

c = (0, 0, 0) # Negro
r = (184, 134, 11) # VerdeOscuro
s = (139, 69, 19) # MarrónCuero
y = (255, 20, 147) # RosaProfundo

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
title: Arco iris
---

![Una cuadrícula con cuadrados de 8 x 8 que muestra un arco iris.](images/chameleon.png)

Creado por el equipo hwplucyr, Reino Unido

```python

c = (100, 149, 237) # Azul Aciano
a = (255, 255, 255) # Blanco
v = (255, 0, 0) # Rojo
t = (255, 140, 0) # Naranja oscuro
q = (255, 255, 0) # Amarillo
l = (0, 255, 127) # Verde Primavera
e = (0, 0, 205) # Azul medio

arco_iris = [
  c, c, c, c, c, c, c, c, 
  v, v, v, v, c, c, c, c,
  t, t, t, t, v, v, c, c,
  q, q, q, q, t, v, c, c,
  l, l, l, l, q, t, v, c,
  e, e, e, l, q, t, v, c,
  c, c, e, a, a, a, a, c,
  c, a, a, a, a, a, a, a
]

```

--- /collapse ---

--- collapse ---
---
title: Dragón
---

![Una cuadrícula con cuadrados de 8 x 8 que muestra un dragón.](images/kite.png)

Creado por el equipo Val, Grecia

```python

a = (255, 255, 255) # Blanco
c = (0, 0, 0) # Negro
f = (25, 25, 112) # Azul medianoche
m = (34, 139, 34) # Verde bosque

imagen = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

```

--- /collapse ---

--- collapse ---
---
title: Cactus
---

![Una cuadrícula con cuadrados de 8 x 8 que muestra un pollo.](images/chicken.png)

Creado por el equipo de Slepicky, República Checa

```python

a = (255, 255, 255) # Blanco
c = (0, 0, 0) # Negro
f = (25, 25, 112) # Azul medianoche
m = (34, 139, 34) # Verde bosque

imagen = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

# Mostrar la imagen
sense.set_pixels(imagen)

```

--- /collapse ---

--- /task ---

--- task ---

**Busca:** la línea que dice `# Mostrar la imagen` y añade una línea de código para mostrar la imagen en la matriz LED:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 18, 19
---
b = (105, 105, 105) # Gris apagado c = (0, 0, 0) # Negro d = (100, 149, 237) # Azul Aciano v = (255, 0, 0) # Rojo z = (153, 50, 204) # Orquídea Oscuro imagen = [ c, c, v, c, v, c, c, c, c, z, z, z, z, v, c, c, z, b, z, b, z, c, c, c, z, z, z, z, z, v, c, c, c, c, d, d, d, c, c, z, c, z, d, z, z, z, z, c, c, c, d, d, z, c, c, c, c, c, z, c, z, c, c, c]

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

# Muestra la imagen
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Pulsa **Ejecutar** en la parte inferior del editor, para ver tu imagen en la matriz de LEDs.

--- /task ---

--- task ---

**Depurar**

Mi código tiene un error de sintaxis:

- Comprueba que tu código coincide con el código en los ejemplos anteriores
- Comprueba que has indentado el código en tu lista
- Compruebe que su lista está rodeada por `[` y `]`
- Verifica que cada variable de color de la lista esté separada por una coma

Mi imagen no aparece:

- Comprueba que tu `sense.set_pixels(imagen)` no esté indentado

--- /task ---


--- task ---

**Guarda tu progreso**

Ahora que has mostrado una imagen, puedes guardar tu programa en el Proyecto Inicial de la Misión ingresando el nombre de tu equipo, los nombres de los miembros del equipo y el código de aula que te dieron. Puedes recargar tu programa en cualquier dispositivo con conexión a Internet ingresando el nombre de tu equipo y el código de aula.

![Botón Guardar de Mission Zero](images/mz_savebutton_v2.png)

--- /task --- 
