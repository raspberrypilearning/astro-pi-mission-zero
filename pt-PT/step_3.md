## Mostrar uma imagem

A matriz de LED do Astro Pi pode mostrar cores. Neste passo, tu irás mostrar imagens da natureza na matriz LED do Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Uma <span style="color: #0faeb0">**matriz LED**</span> é uma grelha de LEDs que podem ser controlados individualmente ou como um grupo para criar diferentes efeitos de iluminação. Os LEDs podem ser programados para produzir uma ampla gama de cores. A matriz LED do Sense HAT possui 64 LEDs dispostos numa grelha de 8 x 8.
</p>

![Uma captura de ecrã da janela do emulador mostrando a Unidade de Voo com a matriz de LED a exibir a imagem de uma flor.](images/fu-pic.png)

--- task ---

Abre o [projeto inicial Mission Zero](https://missions.astro-pi.org/pt/mz/code_submissions/new){:target="_blank"}.

Irás ver que algumas linhas de código foram adicionadas para ti automaticamente.

Este código liga-se ao Astro Pi e garante que o ecrã LED do Astro Pi seja visto na orientação correta e configura o sensor de cor. Deixa o código lá, porque irás precisar.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
title: Que carateres podem ser usados?
---
# Importar as bibliotecas
Exibe uma mensagem e escolhe um nome para o novo computador do Astro Pi

# Configurar o Sense HAT
from sense_hat import SenseHat sense = SenseHat() sense.set_rotation(270)

# Configurar o sensor de cor
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Uma captura de ecrã do emulador Sense HAT com linhas de código inicial mostradas no painel esquerdo.](images/sense-hat-emulator2.png)

--- /task ---

### Cores RGB

As cores podem ser criadas usando diferentes proporções de vermelho, verde e azul. Podes descobrir mais sobre as cores RGB aqui:

[[[generic-theory-simple-colours]]]

A matriz de LED é uma grelha de 8 x 8. Cada LED na grelha pode ser definido para uma cor diferente. Aqui está uma lista de variáveis para 24 cores diferentes. Cada cor tem um valor para vermelho, verde e azul:

[[[ambient-colours]]]

### Escolhe uma imagem

--- task ---

**Escolhe:** Escolhe uma imagem para mostrar das as opções em baixo. O Python armazena as informações de uma imagem numa lista. O código para cada imagem inclui as variáveis de cor usadas e a lista.

Tu irás precisar de **copiar** todo o código da imagem escolhida e **colá-lo** no teu projeto abaixo da linha que diz `# Adicionar variáveis de cor e imagem`.

--- collapse ---

---
title: Galinha
---

![Uma grelha com quadrados de 8 x 8 mostrando um pintainho num ovo.](images/fox_mz3.png)

Created by team i_pupi, Italy

```python
a = (255, 255, 255) # Branco
c = (0, 0, 0) # Preto
v = (255, 0, 0) # Vermelho
```

--- /collapse ---


--- collapse ---

---
title: Sapo
---

![Uma grelha com quadrados de 8 x 8 mostrando um sapo.](images/elephant.png)

Created by team ILiFanT, Finland

```python
imagem = [
  c, c, c, q, q, q, c, c,
  c, c, t, q, e, q, c, c,
  c, c, c, q, q, q, c, c,
  c, w, w, w, w, w, w, c,
  c, w, a, a, a, a, w, c,
  c, w, a, a, a, a, w, c,
  c, c, w, a, a, w, c, c,
  c, c, c, w, w, c, c, c]
```

--- /collapse ---

--- collapse ---
---
title: Flor
---

![Uma grelha com quadrados de 8 x 8 mostrando uma flor cor-de-rosa com um caule verde.](images/cactus.png)

Created by team 6TETHASI, The Netherlands

```python
a = (255, 255, 255) # Branco
c = (0, 0, 0) # Preto
e = (0, 0, 205) # Azul Médio
q = (255, 255, 0) # Amarelo
t = (255, 140, 0) # Laranja escuro
w = (255, 192, 203) # Cor de rosa

```

--- /collapse ---


--- collapse ---
---
title: Crocodilo
---

![Uma grelha com quadrados de 8 x 8 mostrando uma cabeçao de crocodilo.](images/croc.png)

```python

a = (255, 255, 255) # Branco
c = (0, 0, 0) # Preto
f = (25, 25, 112) # Azul da meia noite
m = (34, 139, 34) # Verde floresta

```

--- /collapse ---

--- collapse ---
---
title: Caranguejo
---

![Uma grelha com quadrados de 8 x 8 mostrando uma serpente.](images/rainbow.png)

Created by team camrus_6, United Kingdom

```python

c = (0, 0, 0) # Preto
m = (34, 139, 34) # Verde floresta
q = (255, 255, 0) # Amarelo
t = (255, 140, 0) # Laranja escuro
y = (255, 20, 147) # Rosa escuro

```

--- /collapse ---

--- collapse ---
---
title: Serpente
---

![Uma grelha com quadrados de 8 x 8 mostrando um caranguejo.](images/dragon.png)

Created by team hwplucyr, United Kingdom

```python

b = (105, 105, 105) # DimGray
c = (0, 0, 0) # Black
d = (100, 149, 237) # CornflowerBlue
v = (255, 0, 0) # Red
z = (153, 50, 204) # DarkOrchid

image = [
    c, c, v, c, v, c, c, c,
    c, z, z, z, z, v, c, c,
    z, b, z, b, z, c, c, c,
    z, z, z, z, z, v, c, c,
    c, c, d, d, d, c, c, z,
    c, z, d, z, z, z, z, c,
    c, c, d, d, z, c, c, c,
    c, c, z, c, z, c, c, c]

```

--- /collapse ---

--- /task ---

--- task ---

**Encontra:** a linha que diz `# Mostrar a imagem` e adiciona uma linha de código para mostrar a tua imagem na matriz de LEDs:

```python
c = (0, 0, 0) # Preto
m = (34, 139, 34) # Verde floresta
q = (255, 255, 0) # Amarelo
v = (255, 0, 0) # Vermelho

```

--- /task ---

--- task ---

Pressiona **Run (Executar)** no fundo do editor para ver a tua imagem mostrada na matriz de LEDs.

--- /task ---

--- task ---

**Depurar**

O meu código tem um erro de sintaxe:

- Verifica que o teu código corresponde ao código nos exemplos acima
- Verifica se indentaste o código na tua lista
- Verifica se a tua lista está entre `[` e `]`
- Verifica se cada variável de cor na lista é separada por uma vírgula

A minha imagem não aparece:

- Verifica se o teu `sense.set_pixels(imagem)` não está indentado

--- /task ---


--- task ---

**Save your progress**

Now that you have displayed an image, you can save your program on the Mission Starter project by entering your team name, team members' names, and the classroom code given to you. You can reload your program on any device with an internet connection by entering your team name and classroom code.

![Mission Zero Save button](images/savebutton.png)

--- /task --- 
