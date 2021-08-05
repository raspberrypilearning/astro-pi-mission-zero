## Adiciona um pouco de cor

Os ecrãs LED do Astro Pi também podem exibir cores. Podes especificar uma cor ao criar uma variável e atribui-lhe um valor de cor RGB.

Podes aprender como todas as cores podem ser criadas usando diferentes proporções de vermelho, verde e azul, vê aqui:

[[[generic-theory-colours]]]

--- task ---

Escolhe uma cor e descobre o valor RGB dessa cor. Para te ajudar, podes usar um [seletor de cores](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"}.

--- /task ---

--- task ---

Cria uma variável para armazenar a cor que escolheste. Por exemplo, se escolhes-te o vermelho, deves escrever este código:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

Agora podes exibir o teu texto na cor que escolheste! Para que o programa use a cor que criaste, adiciona um parâmetro `text_colour` ao código que exibe o teu texto:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /task ---

![The Trinket Sense HAT emulator running a sample program which scrolls the text "Astro Pi" across the LED matrix using red letters](images/M0_4.gif)

--- task ---

Também podes alterar a cor de fundo do ecrã. Escolhe outra cor e cria outra variável para armazenar essa cor. Para dizer ao programa que use a cor de fundo escolhida, adiciona o parâmetro `back_colour` ao teu código:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Altera o texto e a cor da saudação - que mensagem queres enviar aos astronautas a bordo da Estação Espacial?

--- /task ---
