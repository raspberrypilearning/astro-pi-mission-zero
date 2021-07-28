## Muestra la humedad

Podrías combinar tu lectura de humedad con una imagen para indicar la temperatura a modo de gráfico. Por ejemplo, puedes hacer que aparezca una tormenta de nieve para bajas temperaturas y un día soleado para altas temperaturas:

![Húmedo y seco](images/wet-dry.png)

--- task ---

En la parte inferior de tu programa, crea más variables de color para cualquiera de los colores que deseas usar en tus imágenes. Es posible que ya hayas definido algunas en el paso anterior.

```python
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)
```

--- /task ---

--- task ---

Al igual que antes, dibuja tus imágenes creando primero una lista para cada uno y, a continuación, ajustando los elementos de la lista a los colores que quieres que sean tus píxeles.

```python
humedo = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


seco = [
  c, c, g, g, c, c, c, c,
  c, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, g, g, g, g, g, c, c,
  c, c, g, g, c, c, c, c,
  y, y, y, y, y, y, y, y,
  y, y, y, y, y, y, y, y
]
```

--- /task ---

--- task ---

Añade algo de código para obtener la humedad:

```python
humedad = sense.get_humidity()
```

--- /task ---

--- task ---

Ahora decide la imagen que quieres mostrar. Para este ejemplo, mostraremos la imagen `humedo` si la lectura de la humedad es del 40% o superior, y la imagen `seco` si la temperatura es inferior al 40%.

```python
humedad = sense.humidity
if humedad >= 40:
    sense.set_pixels(humedo)
else:
    sense.set_pixels(seco)
```

--- /task ---

--- task ---

Usa el control deslizante de la humedad para establecer una determinada humedad en el emulador. Ejecuta tu programa y comprueba que la imagen que has seleccionado para dicha humedad se visualice correctamente.

--- /task ---

--- task ---

Cambia tu código de forma que tu programa muestre la humedad a los astronautas del modo que hayas seleccionado.

--- /task ---

--- task --- Prueba tu código con algunas opciones diferentes de humedad (usando el deslizador) para asegurarte de que siempre funciona correctamente. Si ha seguido el ejemplo anterior, ¿se muestra una imagen cuando la humedad se ajusta a un valor inferior al 40% y también cuando se fija a más del 40%?

--- /task ---
