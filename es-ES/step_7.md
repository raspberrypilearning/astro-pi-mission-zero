## Mostrar la temperatura

Podrás combinar tu lectura de temperatura con una imagen para indicar la temperatura a modo de gráfico. Por ejemplo, puedes hacer que aparezca una tormenta de nieve para bajas temperaturas y un día soleado para altas temperaturas:

![Caliente y frío](images/hot-and-cold.png)

\--- task \---

En la parte inferior de tu programa, crea más variables de color para cualquiera de los colores que deseas usar en tus imágenes. Es posible que ya hayas definido algunas en el paso anterior. En nuestros ejemplos usaremos blanco (`w`), amarillo (`y`), verde (`g`) y negro/vacío (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Al igual que antes, dibuja tus imágenes creando primero una lista para cada uno y, a continuación, ajustando los elementos de la lista a los colores que quieres que sean tus píxeles.

```python
hot = [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g
]


cold = [
  b, b, w, b, b, b, w, b,
  b, b, b, b, b, w, b, b,
  b, w, b, b, b, b, b, w,
  b, b, b, b, w, b, b, b,
  w, b, b, w, b, b, w, b,
  b, b, b, b, b, b, b, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w
]
```

\--- /task \---

\--- task \---

Añade un código para obtener la temperatura:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Ahora decide la imagen que quieres mostrar. Para este ejemplo, mostraremos la imagen `hot` si la lectura de la temperatura es de 20 grados o superior, y la imagen `cold` si la temperatura es inferior a 20 grados.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /task \---

\--- task \---

Usa el control deslizante de la temperatura para establecer una temperatura en el emulador. Ejecuta tu programa y comprueba que la imagen que has seleccionado para dicha temperatura sea correctamente visualizada.

\--- /task \---

\--- task \---

Cambia tu código de forma que tu programa muestre la temperatura a los astronautas del modo que hayas seleccionado.

\--- /task \---