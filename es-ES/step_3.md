## Muestra un mensaje y elige un nombre para los nuevos ordenadores Astro Pi

--- task ---

Abre el [emulador Sense HAT](https://trinket.io/mission-zero){:target="_blank"} para el proyecto Mission Zero.

Comprobarás que se han añadido automáticamente tres líneas de código.

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![Una captura de pantalla del emulador Trinket Sense Hat con tres líneas de código de inicio que se muestran en el panel de la izquierda.](images/sense-hat-emulator2.png)

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

![El emulador HAT Trinket Sense ejecutando un programa de ejemplo que desplaza el texto &quot;Astro PI&quot; a través de la matriz LED en letras blancas](images/M0_1.gif)

--- /task ---

Para mostrar un mensaje diferente, puedes escribir cualquier cosa que quieras entre las comillas (`""`).

--- collapse ---
---
title: ¿Qué caracteres puedo utilizar?
---

El Sense HAT sólo puede mostrar el conjunto de caracteres Latín 1, lo que significa que sólo los siguientes caracteres estarán disponibles. Otros caracteres se mostrarán como un `?`.

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

--- task --- Vamos a nombrar losordenadores Astro Pi en honor a dos científicos europeos inspiradores. Hay cientos de hombres y mujeres que han contribuido a la ciencia y la tecnología; los participantes pueden sugerir sus propios nombres o elegir de nuestra lista de sugerencias (asegúrate de usar la versión inglesa del nombre):


[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"} 
[Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing){:target="_blank"} 
[Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel){:target="_blank"} 
[Edsger Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra){:target="_blank"} 
[Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr){:target="_blank"} 
[Hypatia](https://en.wikipedia.org/wiki/Hypatia){:target="_blank"} 
[John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone){:target="_blank"} 
[Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie){:target="_blank"} 
[Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla){:target="_blank"} 
[Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe){:target="_blank"}

Para votar, comienza tu mensaje con las palabras "My name should be" (en Inglés). Por ejemplo, si quieres votar por Ada Lovelace, tu código se vería así:

```python
sense.show_message("My name should be Ada Lovelace")
```

Si quieres votar, tu mensaje debe comenzar con estas palabras, de no ser así tu voto no contará.

--- /task ---



