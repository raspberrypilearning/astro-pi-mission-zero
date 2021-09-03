## Mostre uma mensagem e escolha um nome para os novos computadores Astro Pi

--- task ---

Abra o [emulador Sense HAT](https://trinket.io/mission-zero){:target="_blank"} para o projeto Mission Zero.

Irá ver três linhas de código que foram adicionadas automaticamente para si:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![Uma captura de ecrã do emulador Trinket do Sense Hat com três linhas de código inicial exibido no painel esquerdo.](images/sense-hat-emulator2.png)

Este código liga-se ao Astro Pi e garante que o ecrã LED do Astro Pi seja visto da maneira correta. Deixe o código lá, porque você vai precisar.

--- /task ---

--- task ---

Quer deixar uma saudação agradável para os astronautas da EEI que estão a trabalhar perto do Astro Pi? Vamos passar uma mensagem no ecrã.

Adicione esta linha abaixo do outro código:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Para executar, pressiona o botão **Run** (Executar) e vê a mensagem `Astro Pi` passar no ecrã LED.

![O emulador Trinket do Sense HAT executando um programa de exemplo que desliza o texto "Astro PI" ao longo da matriz LED em letras brancas](images/M0_1.gif)

--- /task ---

Para exibir uma mensagem diferente, pode escrever o que quiser entre as aspas (`""`).

--- collapse ---
---
title: Que carateres podem ser usados?
---

O Sense HAT só pode exibir o conjunto de caracteres Latin 1, o que significa que apenas os seguintes caracteres estarão disponíveis. Outros caracteres serão exibidos como `?`.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

Também pode alterar a velocidade de deslize da mensagem que vê no ecrã. Adicione `scroll_speed` à linha de código que você já possui, assim:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

A velocidade padrão da mensagem é `0.1`. Tornar o número menor faz com que a mensagem deslize mais rapidamente e, ao torná-lo maior, faz com que a mensagem deslize mais lentamente.

--- /task ---

### Escolha um nome para os novos computadores Astro Pi

--- task --- Daremos aos computadores Astro Pi o nome de dois cientistas europeus inspiradores. Existem centenas de homens e mulheres que contribuíram para a ciência e a tecnologia, e os participantes podem sugerir os seus próprios nomes ou escolher da nossa lista de sugestões:

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

Para votar, comece a sua mensagem com as palavras "O meu nome deve ser". Por exemplo, se um participante ou equipa quisesse votar em Ada Lovelace, o seu código seria assim:

```python
sense.show_message("My name should be Ada Lovelace")
```

Se quiser votar, a sua mensagem tem que começar com estas palavras. De outra forma, a sua entrada não será contada.

--- /task ---



