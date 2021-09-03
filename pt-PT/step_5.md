## Mostrar uma imagem

Podes visualizar imagens na matriz de LED do Astro Pi. Talvez a sua saudação para os astronautas possa incluir uma imagem ou um desenho, junto com, ou em vez de uma mensagem escrita?

![Uma captura de ecrã da janela do emulador mostrando a unidade de voo com a matriz de LED exibindo uma imagem da própria unidade de voo](images/fu-pic.png)

--- task ---

Na parte inferior do programa, crie algumas variáveis ​​para definir as cores que quer usar no seu desenho. Pode usar quantas cores quiser, mas neste exemplo usaremos apenas algumas cores - vermelho (`v`), branco (`b`), preto (`p`) e dois tons de cinza (`g` e `s`). Observe que as sombras são alcançadas reduzindo a quantidade de luz em todos os três canais mantendo as proporções iguais.

```python
w = (255, 255, 255)
b = (0, 0, 0)
g = (50,50,50)
s = (200,255,200)
r = (255,0,0)
```

**Nota:** Desta vez, é uma boa ideia dar um nome às variáveis ​​de cor utilizando uma letra só, porque isso economizará tempo na próxima etapa, onde terá que digitá-las várias vezes. Além disso, usar uma única letra facilitará a visualização da imagem que vai desenhar.

--- /task ---

--- task ---



Em baixo das suas novas variáveis, crie uma lista de 64 itens. Cada item representa um pixel na matriz de LED e corresponde a uma das variáveis ​​de cor que definiu. Desenhe a sua imagem colocando uma variável onde deseja que a cor atribuída apareça. Nós desenhámos um astronauta utilizando pixeis pretos (`p`) como fundo e pixeis brancos (`b`) para desenhar a roupa do astronauta:

```python
 picture = [
    g, b, b, b, b, b, b, g,
    b, g, g, g, g, g, g, b,
    b, g, b, b, g, w, g, g,
    b, g, b, b, g, g, g, g,
    b, g, g, g, s, s, g, g,
    b, g, r, g, g, g, g, g,
    b, g, g, g, g, g, g, b,
    g, b, b, b, b, b, b, g
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

Para visualizar a tua imagem basta clicar em **Run** (Executar).

--- /task ---

--- task ---

Se quiser pode adicionar código para incluir uma pequena pausa (ou `sleep`) depois de exibir a imagem. Isso dará tempo aos astronautas para ver a sua imagem antes que a próxima parte da sua mensagem apareça. No topo do programa, adicione:

```python
from time import sleep
```

Em seguida, por baixo do código de visualizar a imagem, adicione este código para aguardar dois segundos:

```python
sleep(2)
```

--- /task ---

--- task ---

Crie a sua própria imagem ou desenho para mostrar aos astronautas!

--- /task ---
