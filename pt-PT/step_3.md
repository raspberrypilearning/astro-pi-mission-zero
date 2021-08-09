## Mostre uma mensagem e escolha um nome para os novos computadores Astro Pi

--- task ---

Abra o [emulador Sense HAT](https://trinket.io/mission-zero){:target="_blank"} para o projeto Missão Zero.

Irá ver três linhas de código que foram adicionadas automaticamente para si:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![A screenshot of the Trinket Sense Hat emulator with three lines of starter code displayed in the left hand pane.](images/sense-hat-emulator2.png)

Este código conecta-se ao Astro Pi e garante que o ecrã LED do Astro Pi seja visto da maneira correta. Deixe o código lá, porque você vai precisar.

--- /task ---

--- task ---

Quer deixar uma saudação agradável para os astronautas da EEI que estão a trabalhar perto do Astro Pi? Vamos passar uma mensagem no ecrã.

Adicione esta linha abaixo do outro código:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Para executar, pressiona o botão **Run** e vê a mensagem `Astro Pi` passar no ecrã LED.

![The Trinket Sense HAT emulator running a sample program which scrolls the text "Astro PI" across the LED matrix in white letters](images/M0_1.gif)

--- /task ---



Para exibir uma mensagem diferente, pode escrever o que quiser entre as aspas (`""`).

--- collapse ---

---
title: Que carateres podem ser usados?
---

O Sense HAT só pode exibir o conjunto de caracteres Latin 1, o que significa que apenas os seguintes caracteres estarão disponíveis. Outros caracteres serão exibidos como `?`.

```
+-*/!"#$><0123456789.=)( ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

You can also change the speed of the message scrolling across the screen. Add a `scroll_speed` to the line of code you already have, like this:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

The default speed of the message is `0.1`. Making the number smaller makes the message scroll more quickly, and making it larger makes the message scroll more slowly.

--- /task ---

### Choose a name for the new Astro Pi computers

--- task --- We will name the Astro Pi computers after two inspirational European scientists. There are hundreds of men and women that have contributed to science and technology, and participants can suggest their own names, or pick from our list of suggestions:


[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"} 
[Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing){:target="_blank"} 
[Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel){:target="_blank"} 
[Edsgar Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra){:target="_blank"} 
[Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr){:target="_blank"} 
[Hypatia](https://en.wikipedia.org/wiki/Hypatia){:target="_blank"} 
[John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone){:target="_blank"} 
[Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie){:target="_blank"} 
[Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla){:target="_blank"} 
[Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe){:target="_blank"}

To vote, start your message with the words "My name should be". For example, you want to vote for Ada Lovelace, your code would look like this:

```python
sense.show_message("My name should be Ada Lovelace")
```
--- /task ---



