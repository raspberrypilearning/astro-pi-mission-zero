## Identificar uma cor

Nesta etapa, vais configurar o sensor de cor e brilho. Vais utilizar este sensor para medir a quantidade de luz vermelha, verde e azul que chega ao sensor. Estes valores serão então utilizados para alterar uma das cores da imagem que escolheste.

Isto significa que a imagem pode variar consoante o que o sensor capta. Por exemplo, um astronauta que use uma camisa azul veria uma versão diferente da imagem do que um astronauta que use uma camisa vermelha.

Na imagem da baleia que utilizámos no passo anterior, a cor de fundo era preta. Utilizámos a variável `c` para armazenar o código de cor RGB:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Utiliza o sensor de cor para alterar uma das tuas cores.

Por baixo das linhas onde defines as cores, adiciona o seguinte código:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4
---
# Identificar uma cor
rgb = sense.color # obter a cor do sensor
c = (rgb.red, rgb.green, rgb.blue) # usa a cor detetada

--- /code ---

--- /task ---

Este código substitui os valores RGB armazenados em `c` pelos valores da cor detetada pelo sensor.

Tip: Se não utilizaste a variável `c` na tua própria imagem, substitui `c` por uma das variáveis de cor que utilizaste. Isto permite que o sensor mude para essa cor.

--- task ---

**Teste:** Move o controle deslizante de cores para uma cor da tua escolha e **executa** o teu código. A tua cor de fundo será alterada. Repete este teste novamente com uma nova cor.

**Dica:** Tu precisas de clicar em 'Run (Executar)' todas as vezes que alterares a cor.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Agora que já visualizaste a imagem, detetaste uma cor e utilizaste-a no teu programa, o teu código está pronto para ser enviado! 

Podes guardar e enviar o teu programa com o formulário que se encontra na parte inferior do editor de código.
  
No entanto, talvez queiras adicionar mais imagens ao teu projeto ou dar-lhe vida com animações. Os próximos passos mostram como o fazer.
</p>

## Anima o teu projeto (opcional)

O teu programa Mission Zero pode decorrer na Estação Espacial Internacional (EEI) durante um máximo de 30 segundos. Podes aproveitar este tempo de execução para exibir uma animação na matriz de LED, alternando entre duas ou mais imagens diferentes.

--- task ---


**Adiciona** uma segunda imagem logo abaixo da linha de código `sense.set_pixels(imagem)`. Atribui-lhe o nome de variável `imagem2` e altera alguns píxeis para que o quadro da tua animação tenha um aspeto diferente. Adiciona uma pequena pausa depois disso.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
imagem = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(imagem)

# As imagens / frames extras vão para aqui:

imagem2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

No final do teu ficheiro de código, configura o ciclo `for` para se repetir `14` vezes e alterna entre a exibição da `imagem` e `imagem2`, com uma pausa de 1 segundo em cada frame.

**Tip:** Certifica-te de que as linhas de código abaixo de `for i in range(14):` estão recuadas com um espaço, para que fiquem **dentro** do bloco de ciclo.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
imagem2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Ciclo de repetição de 14 vezes (14 * 2 segundos = 28 segundos de animação total)
for i in range(14):
  # Mostrar a segunda imagem
  sense.set_pixels(imagem2)
  sleep(1)

  # Mostrar a primeira imagem
  sense.set_pixels(imagem)
  sleep(1)
  
--- /code ---

--- /task ---

--- task ---

**Teste:** Executa o teu código novamente. O teu programa vai apresentar a cor detetada instantaneamente e, em seguida, alternar entre as duas cores para criar um efeito animado.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Se pretendes incluir mais de dois frames na tua animação, deves certificar-te de que o programa não demora mais de 30 segundos a ser executado. Por exemplo, se tiveres 10 imagens que ficam visíveis durante 1 segundo cada, tens de alterar o teu ciclo «for» para que se repita 3 vezes (10 * 3 = 30 segundos)
</p>

--- task ---

**Verifica se existem erros**

O meu código tem um erro de sintaxe ou não altera as frames:
- Verifica se o código do teu ciclo `for` corresponde à indentação do exemplo.
- Certifica-te que nomeaste a tua segunda matriz de imagens `imagem2` e de que esta se encontra fora do ciclo e antes do início do mesmo.
- Verifica se os teus tempos de `sleep` estão definidos exatamente para `1` segundo, para evitar ultrapassar o limite estrito de 30 segundos de execução na EEI.

--- /task ---

--- task ---

**Guarda o teu progresso**

Podes guardar o teu programa no projeto Inicio de Missão ao entrar com o nome de equipa, os nomes dos elementos e o código de sala de aula que te foi dado. Podes abrir o teu programa em qualquer dispositivo com conexão à Internet ao entrar com o nome da tua equipa e o código de sala de aula.

--- /task ---

--- task ---

--- collapse ---
---
title: Exemplo do código da Baleia concluído
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importar as bibliotecas
from sense_hat import SenseHat
from time import sleep

# Configurar o Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Configurar o sensor de cor
sense.color.gain = 60 # Definir a sensibilidade do sensor
sense.color.integration_cycles = 64 # O intervalo em que a leitura será feita

# Adicionar variáveis de cor e imagem
a = (255, 255, 255) # Branco
c = (0, 0, 0)       # Preto
f = (36, 128, 200)  # Azul Oceano
g = (0, 204, 255)   # Azul Céu

# Identificar uma cor
rgb = sense.color # obter a cor do sensor
c = (rgb.red, rgb.green, rgb.blue)

imagem = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(imagem)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Exemplo do código Baleia concluído (com Animação)
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importar as bibliotecas
from sense_hat import SenseHat
from time import sleep

# Configurar o Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Configurar o sensor de cor
sense.color.gain = 60 # Definir a sensibilidade do sensor
sense.color.integration_cycles = 64 # O intervalo em que a leitura será feita

# Adicionar variáveis de cor e imagem
a = (255, 255, 255) # Branco
c = (0, 0, 0)       # Preto
f = (36, 128, 200)  # Azul Oceano
g = (0, 204, 255)   # Azul Céu

# Identificar uma cor
rgb = sense.color # obter a cor do sensor
c = (rgb.red, rgb.green, rgb.blue)

imagem = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(imagem)

# O ENVIO BÁSICO está por esta altura, concluído

# As imagens / frames extras vão para aqui:
imagem2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Ciclo de repetição de 14 vezes (14 * 2 segundos = 28 segundos de animação total)
for i in range(14):
  # Mostrar a segunda imagem
  sense.set_pixels(imagem2)
  sleep(1)

  # Mostrar a primeira imagem
  sense.set_pixels(imagem)
  sleep(1)
  
--- /code ---

--- /collapse ---

--- /task ---

