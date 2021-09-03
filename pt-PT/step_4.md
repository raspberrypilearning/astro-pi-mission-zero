## Adiciona um pouco de cor

Os LEDs do Astro Pi também podem exibir cores. Pode especificar uma cor, criando uma variável e atribuir-lhe um valor de cor RGB (Red, Green, Blue - Vermelho, Verde, Azul).

Pode aprender como todas as cores podem ser criadas usando diferentes proporções de vermelho, verde e azul aqui:

[[[generic-theory-colours]]]

--- task ---

Escolha uma cor e descubra o valor RGB dessa cor. Para ajudar, pode usar um [selector de cores](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"}.

--- /task ---

--- task ---

Crie uma variável para armazenar a sua cor escolhida. Por exemplo, se escolheu o vermelho, deve escrever este código:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

Agora pode exibir o seu texto na cor que escolheu! Para que o programa use a cor que criou, adicione um parâmetro `text_colour` ao código que exibe o seu texto:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /task ---

![O emulador Trinket do Sense HAT executando um programa de exemplo que desliza o texto \"Astro Pi\" ao longo da matriz de LED usando letras vermelhas](images/M0_2.gif)

--- task ---

Também pode alterar a cor de fundo do ecrã. Escolha outra cor e crie outra variável para armazenar essa cor. Para dizer ao programa que use a cor de fundo escolhida, adicione o parâmetro `back_colour` ao seu código:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Altere o texto e a cor da saudação - que mensagem enviará aos astronautas a bordo da EEI?

--- /task ---
