## Mostrar una imagen

Puedes mostrar imágenes en la matriz LED de Astro Pi. ¿Por qué no incluir en tu saludo a los astronautas una imagen o patrón además, o en lugar de, un mensaje escrito?

![Astronauta](images/astronaut-pic.png)

--- task ---

En la parte inferior de tu programa, crea algunas variables de color que definan los colores que deseas usar en la imagen. Puedes usar tantos colores como quieras. En este ejemplo solamente hemos usado dos: blanco (`w`) y negro (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Nota:** Es una buena idea dar a las variables de color nombres de una sola letra, puesto que te ahorrará tiempo en el siguiente paso, en donde vas a escribirlas muchas veces. Es más, usar una sola letra facilitará ver la imagen que vas a dibujar.

--- /task ---

--- task ---

Debajo de tus nuevas variables, crea una lista de 64 elementos. Cada elemento representa un píxel en la matriz LED, y se corresponde con una de las variables de color definidas. Dibuja tu imagen colocando una variable donde quieras que aparezca su color asignado. Hemos dibujado un astronauta usando píxeles negros (`b`) para el fondo y píxeles blancos (`w`) para dibujar el traje espacial del astronauta:

```python
picture = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
```

--- /task ---

--- task ---

Añade una línea de código para ver tu imagen en la pantalla LED.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Pulsa **Run** (Ejecutar) para ver tu imagen en pantalla.

--- /task ---

--- task ---

Puede que quieras añadir más código para incluir una breve espera (o `sleep`) después de mostrar la imagen. Esto permitirá que los astronautas puedan ver tu imagen antes de que aparezca la siguiente parte de tu mensaje. En la parte de arriba de tu programa, añade:

```python
from time import sleep
```

A continuación, en la línea siguiente a la que muestra tu imagen, añade este código para realizar una pausa de dos segundos:

```python
sleep(2)
```

--- /task ---

--- task ---

Crea tu propia imagen o patrón, ¡y enséñasela a los astronautas!

--- /task ---