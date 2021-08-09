## Reage à humidade

Pode combinar a leitura da humidade com uma imagem para também indicar a humidade de maneira gráfica. Por exemplo, pode-se mostrar um oceano para humidade alta e um deserto para humidade baixa:

![Molhado e seco](images/wet-dry.png)

--- task ---

Na parte inferior do programa, crie mais variáveis ​​de cor para definir as cores que quer usar nos seus desenhos. Talvez já tenha definido algumas delas num passo anterior.

```python
l = (255,130,0)
a = (0,0,255)
c = (0,150,255)
e = (80,80,80)
v = (0,255,0)
y = (255,255,0)
```

--- /task ---

--- task ---

Assim como antes, desenhe as suas imagens criando primeiro uma lista para cada uma delas e, em seguida, definindo os itens da lista com as cores que deseja que seus pixeis tenham.

```python
molhado = [
  a, a, a, a, a, a, a, a,
  a, a, a, a, a, a, a, a,
  a, l, a, l, l, l, a, a,
  a, l, l, l, l, e, l, a,
  a, l, l, l, l, l, l, l, a,
  a, l, a, l, l, l , a, a,
  a, a, a, a, a, a, a, a,
  a, a, a, a, a, a, a, a
]


seco = [
  c, c, v , v, c, c, c, c,
  c, c, v, v, c, v, c, c,
  v, c, v, v, c, v, c, c,
  v, c, v, v, c, v, c, c,
  v, v, v, v, v, v, c, c,
  c, c, v, v, c, c, c, c,
  y, y , y, y, y, y, y, y,
  y, y, y, y, y, y, y, y
]
```

--- /task ---

--- task ---

Adicione algum código para obter a humidade:

```python
humid = sense.get_humidity()
```

--- /task ---

--- task ---

Agora decida que imagem quer mostrar. Para este exemplo, mostraremos a imagem `molhado` se a leitura da humidade estiver 40% ou acima, e a imagem `seco` se a um humidade estiver abaixo de 40%.

```python
humid = sense.get_humidity()
if humid >= 40:
    sense.set_pixels(molhado)
else:
    sense.set_pixels(seco)
```

--- /task ---

--- task ---

Use o controlo de deslize da humidade para definir uma humidade no emulador. Execute o seu programa e verifique se a imagem que selecionou para essa humidade foi exibida corretamente.

--- /task ---

--- task ---

Altere o seu código para que o seu programa mostre a humidade aos astronautas da maneira que escolheu.

--- /task ---

--- tarefa --- Teste o seu código com algumas configurações de humidade diferentes (usando o controle de deslize) para ter a certeza de que ele funciona sempre corretamente. Se seguiu o exemplo acima, uma imagem é exibida quando a humidade está definida para um valor inferior a 40% e também quando está definida para mais de 40%?

--- /task ---
