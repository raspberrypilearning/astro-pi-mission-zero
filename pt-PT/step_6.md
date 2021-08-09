## Medir a humidade

O sensor de humidade no Astro Pi pode medir a humidade do ar ao seu redor, uma funcionalidade útil para ajudar a recolher dados sobre as condições no espaço.

![O emulador Trinket do Sense HAT executando um programa de exemplo que desliza o valor da humidade ao longo da matriz LED em letras brancas](images/M0_3.gif)

O Astro Pi mede a humidade na EEI em percentagem da concentração de água no ar.

Parte da sua missão é contribuir para o dia-a-dia da tripulação a bordo da EEI, por isso informá-los que a humidade a bordo da estação espacial está dentro da escala normal irá tranquilizá-los.

[[[generic-theory-what-is-humidity]]]

--- task ---

Adicione este código para fazer uma leitura da humidade:

```python
humid= sense.get_humidity()
```

Este código vai medir a humidade atual e armazenar o valor medido na variável `humid`.

--- /task ---

--- task ---

A temperatura é registada com bastante precisão, ou seja, o valor armazenado terá um grande número de casas decimais. Pode arredondar o valor para qualquer número de casas decimais. No exemplo, arredondámos para uma casa decimal, mas para um nível diferente de precisão, alter o número `1` para o número de casas decimais que gostaria de ver.

```python
humid = round(sense.get_humidity(), 1)
```

--- /task ---

--- task ---

Para visualizar a humidade atual como uma mensagem no ecrã, adicione este código:

```python
sense.show_message(str(humid))
```

A parte `str()` converte a humidade de um número para texto para que o Astro Pi possa exibi-lo.

--- /task ---

--- task ---

Também pode visualizar a humidade como parte de outra mensagem, unindo as partes da mensagem com o sinal `+`.

```python
sense.show_message ("É" + str(humid) + " %")
```

--- /task ---

O verdadeiro Astro Pi irá medir a humidade ao seu redor, mas pode mover o controlo de deslize de humidade no emulador Sense HAT para simular mudanças de humidade e testar o seu código.

![Uma captura de ecrã rotulada do emulador Sense HAT com a janela de código à esquerda e o emulador à direita. O controle de deslize usado para ajustar a humidade está assinalado no canto superior direito](images/humidity-slider.png)

**Nota:** Deve estar curioso para saber por que é que o controlo de deslize de temperatura exibe a temperatura como um número inteiro, mas a leitura obtida é um decimal. O emulador simula a pequena imprecisão do sensor real, por isso, a medição da temperatura que vê pode ser muito maior ou menor do que o valor que definiu com o controle de deslize.
