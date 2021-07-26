## Mide la humedad

El sensor de humedad de Astro Pi puede medir la humedad del ambiente; una función útil para ayudarte a obtener datos sobre las condiciones en el espacio.

![Mensaje sobre la humedad](images/degrees-message.gif)

El Astro Pi mide la humedad en la ISS como un porcentaje de concentración de agua en el aire.

Parte de tu misión es contribuir a la vida diaria de la tripulación de la ISS, así que haciéndoles saber que la humedad a bordo de la estación espacial se encuentra dentro de la normalidad los tranquilizará.

[[[generic-theory-what-is-humidity]]]

--- task ---

Añade este código para tomar una lectura de la humedad:

```python
humedad = sense.temperature
```

Esta línea medirá la humedad actual y almacenará su valor en la variable `humedad`.

--- /task ---

--- task ---

La humedad se registra con gran precisión, es decir, el valor almacenado tendrá un gran número de decimales. Puedes redondear el valor a cualquier número de lugares decimales. En el ejemplo hemos redondeado a un decimal, sin embargo, para lograr otro nivel de precisión, cambia el número `1` al número de decimales que quieras ver.

```python
humedad = round( sense.humidity, 1 )
```

--- /task ---

--- task ---

Para ver la humedad actual a modo de mensaje desplazándose por la pantalla, añade esta línea de código:

```python
sense.show_message( str(humedad) )
```

La parte `str()` convierte la temperatura de número a texto, de modo que Astro Pi pueda mostrarla.

--- /task ---

--- task ---

También puedes mostrar la humedad como parte de otro mensaje uniendo las partes de tu mensaje con un `+`.

```python
sense.show_message( "Hay " + str(humedad) + " %" )
```

--- /task ---

El Astro Pi real medirá la humedad a su alrededor, sin embargo, tu podrás mover el control deslizante de la humedad en el emulador Sense HAT para simular cambios de humedad y probar tu código.

![Deslizador de humedad](images/humidity-slider.png)

**Nota:** Puede que te preguntes porqué el control deslizante de la humedad muestra la misma en números enteros a pesar de que la lectura que obtienes tiene decimales. El emulador simula una ligera inexactitud del sensor real, de modo que la medición de temperatura que ves podría ser ligeramente inferior o superior al valor establecido con el control deslizante.
