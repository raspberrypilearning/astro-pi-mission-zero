## Mostre uma mensagem e escolha um nome para os novos computadores Astro Pi

--- task ---

Abra o [emulador Sense HAT](https://trinket.io/mission-zero){:target="_blank"} para o projeto Missão Zero.

Irá ver três linhas de código que foram adicionadas automaticamente para si:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![Uma captura de ecrã do emulador Trinket do Sense Hat com três linhas de código inicial exibido no painel esquerdo.](images/sense-hat-emulator2.png)

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

![O emulador Trinket do Sense HAT executando um programa de exemplo que desliza o texto "Astro PI" ao longo da matriz LED em letras brancas](images/M0_1.gif)

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

Também pode alterar a velocidade de deslize da mensagem que vê no ecrã. Adicione `scroll_speed` à linha de código que você já possui, assim:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

A velocidade padrão da mensagem é `0.1`. Tornar o número menor faz com que a mensagem deslize mais rapidamente e, ao torná-lo maior, faz com que a mensagem deslize mais lentamente.

--- /task ---

### Escolha um nome para os novos computadores Astro Pi

--- task --- Daremos aos computadores Astro Pi o nome de dois cientistas europeus inspiradores. Existem centenas de homens e mulheres que contribuíram para a ciência e a tecnologia, e os participantes podem sugerir os seus próprios nomes ou escolher da nossa lista de sugestões:


[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){: target = "_ blank"} 
[Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing){: target = "_ blank"} 
[Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel){: target = "_ blank"} 
[Edsger Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra){: target = "_ blank"} 
[Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr){: target = "_ blank"} 
[Hypatia](https://en.wikipedia.org/wiki/Hypatia){: target = "_ blank"} 
[John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone){: target = "_ blank"} 
[Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie){: target = "_ blank "} 
[Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla){: target =" _ blank "} 
[Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe){: target =" _ blank "}

Para votar, comece a sua mensagem com as palavras "O meu nome deve ser". Por exemplo, se um participante ou equipa quisesse votar em Ada Lovelace, o seu código seria assim:

```python
sense.show_message("O meu nome deve ser Ada Lovelace")
```

If you would like to vote, your message *must* start with these words, otherwise we won't be able to automatically count your entry.

--- /task ---



