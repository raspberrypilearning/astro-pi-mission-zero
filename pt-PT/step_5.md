## Visualizar uma imagem

Podes visualizar imagens na matriz de LED do Astro Pi. Talvez a tua saudação para os astronautas possa incluir uma imagem ou um desenho, junto com ou em vez de uma mensagem escrita?

![A screenshot of the emulator window showing the Flight Unit with the LED matrix displaying a picture of the Flight Unit itself](images/fu-pic.png)

--- task ---

Na parte inferior do programa, cria algumas variáveis ​​para definir as cores que queres usar no teu desenho. Podes usar quantas cores quiseres, mas neste exemplo vamos usar apenas duas - branco (`w`) e preto (`b`). Notice that the shades are achieved by reducing the amount of light in all three channels while keeping the proportions the same.

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Nota:** Desta vez, é uma boa ideia dar um nome às variáveis ​​de cor utilizando uma letra só, porque isso economizará tempo na próxima etapa, onde terás que digitá-las várias vezes. Além disso, usar uma única letra facilitará a visualização da imagem que vais desenhar.

--- /task ---

--- task ---



Abaixo tens as tuas novas variáveis, cria uma lista de 64 itens. Cada item representa um pixel na matriz de LED e corresponde a uma das variáveis ​​de cor que definiste. Desenha a tua imagem colocando uma variável onde queres que a tua cor apareça. Nós desenhámos um astronauta utilizando pixels pretos (`b`) como fundo e pixels brancos (`w`) para desenhar a roupa do astronauta:

```python
 picture = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
```
--- /task ---

--- task ---

Adiciona o seguinte código para visualizar a tua imagem no ecrã LED.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Para visualizar a tua imagem basta clicar em **Run**.

--- /task ---

--- task ---

Se quiseres podes adicionar um código para incluir uma pequena pausa (ou `sleep` para suspender) depois de exibires a imagem. Isso dará tempo aos astronautas para ver a tua foto antes que o resto da tua mensagem apareça. No topo do programa, adiciona:

```python
from time import sleep
```

Em seguida, por baixo do código de visualizar a imagem, adiciona este código para aguardar dois segundos:

```python
sleep(2)
```

--- /task ---

--- task ---

Cria a tua própria imagem ou desenho para mostrar aos astronautas!

--- /task ---
