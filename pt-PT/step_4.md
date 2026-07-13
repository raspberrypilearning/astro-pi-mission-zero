## Identificar uma cor

In this step, you will set up the colour and brightness sensor. Neste passo, irás configurar o sensor de luminosidade de cor e usá-lo para detetar a quantidade de vermelho, verde e azul que chegam ao sensor. Esta cor será então usada para colorir a imagem escolhida.

This means that the image can change depending on what the sensor sees. Um astronauta a caminhar até o sensor com uma camisa azul verá uma imagem diferente de um astronauta com uma camisa vermelha.

In the whale image we used in the previous step, the background colour was black. Cria uma variável chamada `x` para armazenar a tua nova cor.

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0) --- /code ---


--- task ---

Usa o sensor de cor para colorir o teu plano de fundo.

Underneath the lines where you define the colours, add the following code:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---
# Sense a colour
rgb = sense.color # obter a cor do sensor c = (rgb.red, rgb.green, rgb.blue) # usa a cor detetada

This code replaces the RGB values stored in `c` with the values for the colour detected by the sensor.

Independentemente da imagem que escolheres, o plano fundo usa a variável `c` definida para preto. This will allow the sensor to change that colour instead.

--- task ---

**Teste:** Move o controle deslizante de cores para uma cor da tua escolha e **executa** o teu código. A tua cor de fundo será alterada. Repete este teste novamente com uma nova cor.

**Dica:** Tu precisas de clicar em 'Run (Executar)' todas as vezes que alterares a cor.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Now you have displayed an image and sensed a colour and used it in your program, and your code is ready for submission! 

You can save and submit your program using the form at the bottom of the code editor.
  
However, you may wish to add more images to your project, or make it come to life with animation. The next steps show you how to do this.
</p>

## Animate your project (optional)

O programa Astro Pi Missão Zero é permitido executar até ao máximo de 30 segundos. Tu usarás este tempo para verificar repetidamente o sensor de cores e atualizar a imagem.

--- task ---


**Encontra** a tua `rgb = sense.color` linha de código. Give it the variable name `image2` and change a few pixels to make your animation frame look different. Then add a short pause after it.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
---
imagem = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

sense.set_pixels(image)

# Extra images / frames go here:

imagem = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /code ---

--- /task ---

--- task ---

At the very bottom of your code file, set up your `for` loop to repeat `14` times and alternate between displaying `image` and `image2` pausing for 1 second on each frame.

**Dica:** Para indentar várias linhas, realça as linhas que desejas indentar e pressiona a tecla <kbd>Tab</kbd> no teclado (geralmente acima da tecla <kbd>Caps Lock</kbd> no teclado).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7, 8
---
images/fish.png

sense.set_pixels(imagem) sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  sense.set_pixels(imagem) sleep(1)

--- /task ---

--- task ---

**Teste:** Executa o teu código novamente. Quando o teu projeto terminar de executar a matriz LED irá desligar, tornando todas as luzes pretas (apagadas).

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
If you would like to have more than two frames in your animation, you must make sure that the program will run for no more than 30 seconds. For example, if you have 10 images that each display for 1 second, you must change your `for` loop to repeat 3 times (10 * 3 = 30 seconds)
</p>

**Teste:** Executa o teu código novamente.

O meu código tem um erro de sintaxe ou não é executado como esperado:
- Verifica que indentaste o código no teu ciclo `for`
- Make sure you named your second image matrix `image2` and that it is placed outside and before the loop begins.
- Check that your `sleep` times are set to exactly `1` second to avoid running past the strict 30-second execution cutoff on the ISS.

--- /task ---

--- task ---

**Guarda o teu progresso**

Podes guardar o teu programa no projeto Inicio de Missão ao entrar com o nome de equipa, os nomes dos elementos e o código de sala de aula que te foi dado. Podes abrir o teu programa em qualquer dispositivo com conexão à Internet ao entrar com o nome da tua equipa e o código de sala de aula.

--- /task ---

--- collapse ---
---
title: Completed Whale code example
---

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
z = (153, 50, 204) # Orquídea escura q = (255, 255, 0) # Amarelo d = (51, 153, 255) # Azul c = (0, 0, 0) # Preto

# Sense a colour
for i in range(28): rgb = sense.color # obter a cor do sensor c = (rgb.red, rgb.green, rgb.blue)

imagem = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /collapse ---
---
title: Exemplo de código completo
---

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Repete o teu programa
from sense_hat import SenseHat from time import sleep

# Configurar o Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Adiciona código antes da tua lista de imagens para obter a cor do sensor e alterar a tua variável de cor de fundo `c` para usar a cor detectada pelo sensor de cores Sense HAT em vez de preto.
for i in range(28): rgb = sense.color # obter a cor do sensor c = (rgb.red, rgb.green, rgb.blue)

# Add colour variables and image
z = (153, 50, 204) # Orquídea escura q = (255, 255, 0) # Amarelo d = (51, 153, 255) # Azul c = (0, 0, 0) # Preto

# Sense a colour
for i in range(28): rgb = sense.color # obter a cor do sensor c = (rgb.red, rgb.green, rgb.blue)

imagem = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

images/colour_background.png

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
images/savebutton_pt.png

sense.set_pixels(imagem) sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  sense.set_pixels(imagem) sleep(1)
