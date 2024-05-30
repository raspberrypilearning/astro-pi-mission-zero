## Muestra una imagen

La matriz LED del Astro Pi puede mostrar colores. En este paso, mostrarás imágenes de la naturaleza en la matriz LED de Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Una <span style="color: #0faeb0">**matriz de LEDs**</span> es una cuadrícula de LEDs que se puede controlar individualmente o en grupo para crear diferentes efectos de iluminación. La matriz de LEDs del Sense HAT tiene 64 LEDs que se muestran en una cuadrícula de 8 x 8. Los LED se pueden programar para producir una amplia gama de colores.
</p>

![Una captura de pantalla de la ventana del emulador que muestra la Unidad de vuelo con la matriz de LEDs mostrando una foto de una flor.](images/fu-pic.png)

--- task ---

Abre el [proyecto inicial de Mission Zero](http://rpf.io/mzcode){:target="_blank"}.

Comprobarás que se han añadido automáticamente tres líneas de código.

Este código se conecta al Astro Pi y se asegura de que la pantalla LED de Astro Pi se muestre en la orientación correcta. Deja estas líneas de código, ya que las necesitarás más adelante.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
title: ¿Qué caracteres puedo utilizar?
---
# Importar las bibliotecas
Muestra un mensaje y elige un nombre para los nuevos ordenadores Astro Pi

# Configurar el Sense HAT
from sense_hat import SenseHat sense = SenseHat() sense.set_rotation(270)

# Configurar el sensor de color
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Una captura de pantalla del emulador Trinket Sense Hat con tres líneas de código de inicio que se muestran en el panel de la izquierda.](images/sense-hat-emulator2.png)

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
title: Pollo
---

![Una cuadrícula con cuadrados de 8 x 8 que muestra un pollito en un huevo.](images/fox_mz3.png)

Created by team i_pupi, Italy

```python
c = (0, 0, 0) # Negro
m = (34, 139, 34) # Verde bosque
q = (255, 255, 0) # Amarillo
t = (255, 140, 0) # Naranja oscuro
y = (255, 20, 147) # Rosa profundo
```

--- /collapse ---


--- collapse ---

---
title: Rana
---

![Una cuadrícula con cuadrados de 8 x 8 que muestra una serpiente.](images/elephant.png)

Created by team ILiFanT, Finland

```python
a = (255, 255, 255) # Blanco
c = (0, 0, 0) # Negro
v = (255, 0, 0) # Rojo
```

--- /collapse ---

--- collapse ---
---
title: Flor
---

![Una cuadrícula con cuadrados de 8 x 8 que muestra una flor rosada con un tallo verde.](images/cactus.png)

Created by team 6TETHASI, The Netherlands

```python
a = (255, 255, 255) # Blanco
c = (0, 0, 0) # Negro
e = (0, 0, 205) # Azul medio
q = (255, 255, 0) # Amarillo
t = (255, 140, 0) # Naranja oscuro
w = (255, 192, 203) # Rosado

```

--- /collapse ---


--- collapse ---
---
title: Cocodrilo
---

![Una cuadrícula con cuadrados de 8 x 8 que muestra la cabeza de un cocodrilo.](images/croc.png)

```python

a = (255, 255, 255) # Blanco
c = (0, 0, 0) # Negro
f = (25, 25, 112) # Azul medianoche
m = (34, 139, 34) # Verde bosque

```

--- /collapse ---

--- collapse ---
---
title: Cangrejo
---

![Una cuadrícula con cuadrados de 8 x 8 que muestra una rana.](images/rainbow.png)

Created by team camrus_6, United Kingdom

```python

c = (0, 0, 0) # Negro
m = (34, 139, 34) # Verde bosque
q = (255, 255, 0) # Amarillo
v = (255, 0, 0) # Rojo

```

--- /collapse ---

--- collapse ---
---
title: Serpiente
---

![Una cuadrícula con cuadrados de 8 x 8 que muestra un cangrejo.](images/dragon.png)

Created by team hwplucyr, United Kingdom

```python

b = (105, 105, 105) # DimGray
c = (0, 0, 0) # Black
d = (100, 149, 237) # CornflowerBlue
v = (255, 0, 0) # Red
z = (153, 50, 204) # DarkOrchid

image = [
    c, c, v, c, v, c, c, c,
    c, z, z, z, z, v, c, c,
    z, b, z, b, z, c, c, c,
    z, z, z, z, z, v, c, c,
    c, c, d, d, d, c, c, z,
    c, z, d, z, z, z, z, c,
    c, c, d, d, z, c, c, c,
    c, c, z, c, z, c, c, c]

```

--- /collapse ---

--- /task ---

--- task ---

**Buscar:** la línea que dice `# Mostrar la imagen` y añade una línea de código para mostrar la imagen en la matriz LED:

```python
c = (0, 0, 0) # Negro
 m = (34, 139, 34) # Verde bosque
 q = (255, 255, 0) # Amarillo
 v = (255, 0, 0) # Rojo

```

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

- Comprueba que tu `sense.set_pixels(image)` no esté indentado

--- /task ---


--- task ---

**Save your progress**

Now that you have displayed an image, you can save your program on the Mission Starter project by entering your team name, team members' names, and the classroom code given to you. You can reload your program on any device with an internet connection by entering your team name and classroom code.

![Mission Zero Save button](images/savebutton.png)

--- /task --- 
