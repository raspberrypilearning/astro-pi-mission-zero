## Añadir algo de color

Las pantallas LED de Astro Pi también pueden mostrar colores. Puedes especificar un color creando una variable y asignándola a un valor de color RGB.

Puedes aprender a crear colores aquí usando distintas proporciones de rojo, verde y azul:

[[[generic-theory-colours]]]

\--- task \---

Selecciona un color y averigua el valor RGB de dicho color. Puedes usar un [selector de colores](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} para que te ayude.

\--- /task \---

\--- task \---

Crea una variable para guardar el color que has seleccionado. Por ejemplo, si has seleccionado el rojo, puedes escribir esta línea de código:

```python
red = (255,0,0)
```

\--- /task \---

\--- task \---

¡Ahora podrás ver tu texto en el color seleccionado! Para decirle al programa que use el color que has creado, añade un parámetro `text_colour` al código que muestra tu texto:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

\--- /task \---

![mostrar el mensaje en color](images/show-message-color.gif)

\--- task \---

También puedes cambiar el color de fondo de la pantalla. Selecciona otro color y crea otra variable para guardar dicho color. Para decirle al programa que use el color de fondo que has seleccionado, añade el parámetro `back_colour` a tu código:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

\--- /task \---

\--- task \---

Cambia el texto y el color del saludo. ¿Qué mensaje enviarás a los astronautas de la ISS?

\--- /task \---