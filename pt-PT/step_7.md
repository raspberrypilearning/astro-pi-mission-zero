## Exibir a humidade

Podes combinar a leitura da humidade com uma imagem para também indicar a humidade de maneira gráfica. Por exemplo, pode-se mostrar um oceano para alta humidade e um deserto para baixa humidade:

![Quente e frio](images/wet-dry.png)

--- task ---

Na parte inferior do programa, cria mais variáveis ​​de cor para definir as cores que queres usar nos teus desenhos. Talvez já tenhas definido algumas variáveis num passo anterior.

```python
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)
```

--- /task ---

--- task ---

Como fizeste antes, desenha a tua imagem primeiro por criar uma lista para cada desenho, e em seguida combina os itens da lista com as cores que queres que os pixels tenham.

```python
wet = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


dry = [
  c, c, g, g, c, c, c, c,
  c, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, g, g, g, g, g, c, c,
  c, c, g, g, c, c, c, c,
  y, y, y, y, y, y, y, y,
  y, y, y, y, y, y, y, y
]
```

--- /task ---

--- task ---

Adiciona um código para obter a temperatura:

```python
humid = sense.humidity
```

--- /task ---

--- task ---

Agora decide que imagem queres mostrar. Para este exemplo, mostraremos a imagem `wet (molhada)` se a leitura da humidade estiver 40% ou acima, e a imagem `dry (seca)` se a um humidade estiver abaixo de 40%.

```python
humid = sense.humidity
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

Use o controle deslizante de humidade para definir uma humidade no emulador. Executa o teu programa e verifica se a imagem que seleccionaste para essa humidade foi exibida correctamente.

--- /task ---

--- task ---

Altera o teu código para que o teu programa mostre a temperatura aos astronautas da maneira que escolheste.

--- /task ---

--- task --- Test your code with a few different humidity settings (using the slider) to make sure it always runs correctly. If you've followed the example above, is an image displayed both when the humidity is set to a value less than 40% and also when it is set to more than 40%?

--- /task ---
