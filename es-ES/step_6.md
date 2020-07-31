## Medir la temperatura

El sensor de temperatura de Astro Pi puede medir la temperatura del ambiente; una función útil para ayudarte a obtener datos sobre las condiciones del espacio.

![Mensaje sobre la temperatura](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

Parte de tu misión es contribuir a la vida diaria de la tripulación de la ISS. Informarles de que la temperatura a bordo de la estación espacial se encuentra dentro de la normalidad los tranquilizará.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Añade este código para tomar una lectura de temperatura:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- /task \---

\--- task \---

La temperatura se registra con gran precisión, es decir, el valor almacenado tendrá un gran número de decimales. Puedes redondear el valor a cualquier número de decimales. En el ejemplo hemos redondeado a un decimal, sin embargo, para lograr otro nivel de precisión, cambia el número `1` al número de decimales que quieras ver.

```python
temp = round( sense.temperature, 1 )
```

\--- /task \---

\--- task \---

Para ver la temperatura actual a modo de mensaje desplazándose por la pantalla, añade esta línea de código:

```python
sense.show_message( str(temp) )
```

The `str()` part converts the humidity from a number into text so that the Astro Pi can display it.

\--- /task \---

\--- task \---

La parte `str()` convierte la temperatura de número a texto, de modo que Astro Pi pueda mostrarla.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

El Astro Pi real medirá la temperatura a su alrededor, sin embargo, tu podrás mover el control deslizante de la temperatura en el emulador Sense HAT para simular cambios de temperatura y probar tu código.

![Humidity slider](images/humidity-slider.png)

**Nota:** Puede que te preguntes porqué el control deslizante de la temperatura muestra la temperatura en números enteros a pesar de que la lectura que obtienes tiene decimales. El emulador simula la ligera inexactitud del sensor real, de modo que la medición de temperatura que ves podría ser ligeramente inferior o superior al valor establecido con el control deslizante.