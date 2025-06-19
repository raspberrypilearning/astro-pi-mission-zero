## Identificar uma cor

Neste passo, irás configurar o sensor de luminosidade de cor e usá-lo para detetar a quantidade de vermelho, verde e azul que chegam ao sensor. Esta cor será então usada para colorir a imagem escolhida. Um astronauta a caminhar até o sensor com uma camisa azul verá uma imagem diferente de um astronauta com uma camisa vermelha.

![imagem mostrada com fundo cor-de-rosa na matriz de LED](images/colour_background.png)

Qualquer que seja a imagem que escolheres, o plano fundo usa a variável `c` que é definida para preta.

--- task ---

Usa o sensor de cor para colorir o teu plano de fundo.

Adiciona código antes da tua lista de imagens para obter a cor do sensor e alterar a tua variável de cor de fundo `c` para usar a cor detectada pelo sensor de cores Sense HAT em vez de preto.

**Dica:** tu não precisas de escrever os comentários que começam com '#' (eles estão lá para explicar o código).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9, 10
---

# Adicionar variáveis de cor e imagem

z = (204, 0, 204) # magenta q = (255, 255, 0) # yellow d = (51, 153, 255) # blue c = (0, 0, 0) # black

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


--- /code ---

--- /task ---

--- task ---

**Teste:** Move o controle deslizante de cores para uma cor da tua escolha e **executa** o teu código. A tua cor de fundo será alterada. Repete este teste novamente com uma nova cor.

**Dica:** Tu precisas de clicar em 'Run (Executar)' todas as vezes que alterares a cor.

--- /task ---

## Repete o teu programa

O programa Astro Pi Missão Zero é permitido executar até ao máximo de 30 segundos. Tu usarás este tempo para verificar repetidamente o sensor de cores e atualizar a imagem.

O teu código usará um ciclo `for` para executar 28 vezes. **A cada** vez ele irá:
+ identificar a cor mais recente
+ atualizar a cor de fundo da imagem
+ pausar por um segundo

--- task ---

**Encontra** a tua `rgb = sense.color` linha de código.

**Adiciona** código acima dela para configurar o teu ciclo `for` para `28` repetições.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


--- /code ---

--- /task ---

--- task ---

Agora precisas de indentar todo o teu código abaixo do ciclo `for` para que fique **dentro** do ciclo `for`.

**Dica:** Para indentar várias linhas, realça as linhas que desejas indentar e pressiona a tecla <kbd>Tab</kbd> no teclado (geralmente acima da tecla <kbd>Caps Lock</kbd> no teclado).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


  # Display the image

  sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

No final do teu código, adiciona um `sleep` de um segundo dentro do teu ciclo:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 5
---

  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Dica:** Certifica-te de que esta linha de código é indentada dentro do teu ciclo `for`.

--- /task ---

--- task ---

**Teste:** Executa o teu código e altera o seletor de cores várias vezes enquanto o teu projeto está em execução. Verifica que a tua imagem é atualizada para usar a cor detectada na próxima execução.

A imagem parará de atualizar quando o ciclo terminar para que o programa não seja executado por mais de 30 segundos.

--- /task ---

--- task ---

**Depurar**

O meu código tem um erro de sintaxe ou não é executado como esperado:

- Verifica que o teu código corresponde ao código nos exemplos acima
- Verifica que indentaste o código no teu ciclo `for`
- Verifica se a tua lista está entre `[` e `]`
- Verifica se cada variável de cor na lista é separada por uma vírgula

O meu código é executado por mais de 30 segundos:

- Diminui o número de vezes que o teu ciclo for é executado, de 28 para 25 ou até 20.
- Diminui a duração do sleep, de 1 segundo para 0.5 segundos.

--- /task ---

--- task ---

Adiciona `sense.clear()` no final do teu código para limpar a imagem no final do teu ciclo. Isto irá ajudar-te a ver quando a tua animação terminar a execução.

**Dica:** Certifica-te de **não** indentar a linha de código `sense.clear()`, pois tu desejas que seja executada apenas uma vez no final da tua animação.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7
---

  # Display the image

  sense.set_pixels(image) sleep(1)

sense.clear()

--- /code ---

--- /task ---

--- task ---

**Teste:** Executa o teu código novamente. Quando o teu projeto terminar de executar a matriz LED irá desligar, tornando todas as luzes pretas (apagadas).

--- /task ---

--- task ---

**Depurar**

A matriz LED fica preta a cada segundo:

- Verifica que não indentaste o código `sense.clear()` dentro do teu ciclo `for`

--- /task ---

--- task ---

Adiciona código para limpar a matriz LED para uma cor da tua escolha. Cria uma variável chamada `x` para armazenar a tua nova cor.

Podes misturar a tua própria cor ou usar os valores da lista de cores para criar a tua nova cor `x`.

\[[[generic-theory-simple-colours]]\] \[[[ambient-colours\]]]

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7, 8
---

  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /task ---

--- task ---

**Teste:** Executa o teu código novamente. Quando o teu projeto terminar de executar a matriz LED irá acender com a tua cor escolhida. Tu podes mudar e testar a cor quantas vezes quiseres.

--- /task ---


--- task ---

**Guarda o teu progresso**

Podes guardar o teu programa no projeto Inicio de Missão ao entrar com o nome de equipa, os nomes dos elementos e o código de sala de aula que te foi dado. Podes abrir o teu programa em qualquer dispositivo com conexão à Internet ao entrar com o nome da tua equipa e o código de sala de aula.

![Captura de ecrã do botão Guardar Missão Zero](images/mz_savebutton_v2.png)

--- /task ---


--- task ---

--- collapse ---

---
title: Exemplo de código completo
---

![Uma grelha com 8 x 8 quadrados a exibir um crocodilo.](images/fish.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Import the libraries
from sense_hat import SenseHat from time import sleep

# Set up the Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image

z = (204, 0, 204) # magenta q = (255, 255, 0) # yellow d = (51, 153, 255) # blue c = (0, 0, 0) # black

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
