## Visualizar a temperatura

Podes combinar a leitura de temperatura com uma imagem para também indicar a temperatura de maneira gráfica. Por exemplo, podes escolher a imagem de uma tempestade de neve para mostrar temperaturas frias e um dia ensolarado para temperaturas altas:

![Quente e frio](images/hot-and-cold.png)

--- task ---

Na parte inferior do programa, cria mais variáveis ​​de cor para definir as cores que queres usar nos teus desenhos. Talvez já tenhas definido algumas variáveis num passo anterior. Nos nossos exemplos, vamos usar branco (`w`), amarelo (`y`), verde (`g`) e preto / em branco (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

--- /task ---

--- task ---

Como fizeste antes, desenha a tua imagem primeiro por criar uma lista para cada desenho, e em seguida combina os itens da lista com as cores que queres que os pixels tenham.

```python
hot = [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g
]


cold = [
  b, b, w, b, b, b, w, b,
  b, b, b, b, b, w, b, b,
  b, w, b, b, b, b, b, w,
  b, b, b, b, w, b, b, b,
  w, b, b, w, b, b, w, b,
  b, b, b, b, b, b, b, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w
]
```

--- /task ---

--- task ---

Adiciona um código para obter a temperatura:

```python
temp = sense.temperature
```

--- /task ---

--- task ---

Agora decide que imagem queres mostrar. Para este exemplo, vamos mostrar a imagem `hot` se a leitura da temperatura for igual ou superior a 20 graus, e a imagem `cold` se a temperatura estiver abaixo dos 20 graus.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

--- /task ---

--- task ---

Usa o controlo de deslize de temperatura para definir uma temperatura no emulador. Executa o teu programa e verifica se a imagem que selecionaste para essa temperatura foi exibida corretamente.

--- /task ---

--- task ---

Altera o teu código para que o teu programa mostre a temperatura aos astronautas da maneira que escolheste.

--- /task ---