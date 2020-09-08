## Visualizar a humidade

Podes combinar a leitura da humidade com uma imagem para também indicar a humidade de maneira gráfica. Por exemplo, pode-se mostrar um oceano para alta humidade e um deserto para baixa humidade:

![Quente e frio](images/wet-dry.png)

\--- task \---

Na parte inferior do programa, cria mais variáveis ​​de cor para definir as cores que queres usar nos teus desenhos. Talvez já tenhas definido algumas variáveis num passo anterior.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

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

\--- /task \---

\--- task \---

Adiciona um código para obter a temperatura:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Agora decide que imagem queres mostrar. Para este exemplo, vamos mostrar a imagem `hot` se a leitura da temperatura for igual ou superior a 20 graus, e a imagem `cold` se a temperatura estiver abaixo dos 20 graus.

```python
humid = sense.humidity
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

\--- /task \---

\--- task \---

Use o controle deslizante de humidade para definir uma humidade no emulador. Executa o teu programa e verifica se a imagem que seleccionaste para essa humidade foi exibida correctamente.

\--- /task \---

\--- task \---

Altera o teu código para que o teu programa mostre a temperatura aos astronautas da maneira que escolheste.

\--- /task \---