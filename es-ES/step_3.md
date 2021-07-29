## Muestra un mensaje y elige un nombre para los nuevos ordenadores Astro Pi

--- task ---

Abre el [emulador Sense HAT](https://trinket.io/mission-zero){:target="_blank"} para el proyecto Mission Zero.

Comprobarás que se han añadido automáticamente tres líneas de código.

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![emulador sense hat](images/sense-hat-emulator2.png)

Este código se conecta al Astro Pi y se asegura de que la pantalla LED de Astro Pi se muestre en la orientación correcta. Deja estas líneas de código, ya que las necesitarás más adelante.

--- /task ---

--- task ---

¿Quizás podrías dejar un bonito saludo para los astronautas de la ISS que están trabajando cerca del Astro Pi? Vamos a mostrar un mensaje que se desplace por la pantalla.

Añade esta línea debajo del otro código:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Pulsa el botón **Run** (Ejecutar) y observa cómo el mensaje `Astro Pi` se desplaza por la pantalla LED.

![show message code click run](images/show-message-code-annotated.PNG)

--- /task ---

![Scrolling message](images/scroll-message.gif)

Para mostrar otro mensaje, escribe lo que quieras entre las comillas (`""`).

--- collapse ---

---
title: ¿Qué caracteres puedo utilizar?
---

Sense HAT solamente muestra el set de caracteres Latin 1, es decir, solamente están disponibles los siguientes caracteres. El resto de caracteres se mostrarán como `?`.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

También puedes cambiar la velocidad de desplazamiento del mensaje por la pantalla. Añade `scroll_speed` a la línea del código que ya tienes, así:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

La velocidad predeterminada del mensaje es `0.1`. Disminuir el número hará que el mensaje se desplace más rápidamente; y aumentarlo, que se desplace más lentamente.

--- /task ---

### Elige un nombre para los nuevos ordenadores Astro Pi

--- task --- Si quieres entrar en la competición para elegir los nombres de los nuevos ordenadores Mark II Astro Pi, comienza tu mensaje con las palabras "Mi nombre debería ser" y luego añade tu selección de esta lista.

Por ejemplo, si quieres votar por Ada Lovelace, tu código se vería así:

```python
sense.show_message ("Mi nombre debería ser Ada Lovelace")
```
--- /task ---



