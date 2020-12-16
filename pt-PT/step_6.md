## Medir a humidade

O sensor de humidade no Astro Pi pode medir a humidade do ar ao seu redor, uma funcionalidade útil para ajudar-te a recolher dados sobre as condições no espaço.

![Mensagem sobre a humidade](images/degrees-message.gif)

O Astro Pi mede a humidade na ISS em percentagem da concentração de água no ar.

Parte da tua missão é contribuir para o dia-a-dia da tripulação a bordo da Estação Espacial, por isso informa-os que a temperatura a bordo da estação espacial está dentro da escala normal, isso irá tranquilizá-los.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Adiciona este código para obter uma leitura da temperatura:

```python
humidade= sense.humidity()
```

Este código vai medir a humidade atual e armazenar o valor medido na variável `humid`.

\--- /task \---

\--- task \---

A temperatura é registada com bastante precisão, ou seja, o valor armazenado terá um grande número de casas decimais. Se quiseres podes arredondar o valor para qualquer número de casas decimais. No exemplo, arredondámos para uma casa decimal, mas para um nível diferente de precisão, altera o número `1` para o número de casas decimais que gostarias de ver.

```python
humidade = round( sense.humidity(), 1)
```

\--- /task \---

\--- task \---

Para visualizar a temperatura atual como uma mensagem no ecrã, adiciona este código:

```python
sense.show_message( str(humidade))
```

A parte `str()` converte a humidade de um número para texto para que o Astro Pi possa exibi-lo.

\--- /task \---

\--- task \---

A parte `str()` converte a temperatura de um número para texto para que o Astro Pi possa exibi-lo.

```python
sense.show_message ("É" + str (humido) + "%")
```

\--- /task \---

O verdadeiro Astro Pi irá medir a temperatura ao seu redor, mas podes mover o controlo de deslize de temperatura no emulador Sense HAT para simular mudanças de temperatura e testar o teu código.

![Controle deslizante de humidade](images/humidity-slider.png)

**Nota:** Deves estar curioso para saber por que é que o controlo de deslize de temperatura exibe a temperatura como um número inteiro, mas a leitura obtida é um decimal. O emulador simula a pequena imprecisão do sensor real, por isso, a medição da temperatura que vês pode ser muito maior ou menor do que o valor que definiste com o controle de deslize.