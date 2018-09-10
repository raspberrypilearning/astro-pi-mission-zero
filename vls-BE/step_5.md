## Laat een beeld zien

Je kunt beelden tonen op de Astro Pi's LED matrix. Misschien kan je begroeting voor de astronauten een beeld of een patroon omvatten, evenals of in plaats van een geschreven boodschap?

![Astronaut](images/astronaut-pic.png)

\--- task \---

Onderaan je programma kun je wat variabele kleuren creëren om de kleuren te definiëren waarmee je je tekening wilt maken. Je kunt zoveel mogelijke kleuren naar wens gebruiken, maar in dit voorbeeld houden wij ons uitsluitend aan twee — wit (`w`) en zwart (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Aandacht:** Deze keer, is het een goed idee om de variabele kleuren een enkele letter naam te geven, omdat dit tijd zal besparen bij de volgende stap, waar je ze herhaaldelijk zult gaan typen. Daarenboven, zal het gebruiken van enkele letters het gemakkelijker maken om de tekening te zien die je zult maken.

\--- /task \---

\--- task \---

Onderaan je nieuwe variabelen, maak een lijst met 64 items. Ieder item vertegenwoordigt een pixel op de LED matrix, en komt overeen met een van de variabele kleuren die je hebt gedefinieerd. Maak je tekening door een variabele aan te brengen waar je de toegekende kleur wilt laten voorkomen. We hebben een een astronaut getekend door het gebruiken van zwarte (`b`) pixels als achtergrond en de witte (`w`) pixels om het ruimtepak van de astronaut te tekenen:

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

\--- /task \---

\--- task \---

Voeg een codelijn toe om je tekening te tonen op het led-kleurenbeeldscherm.

```python
sense.set_pixels(picture)
```

\--- /task \---

\--- task \---

Druk op **Run** om je vertoonde tekening te zien.

\--- /task \---

\--- task \---

Misschien wil je een soort code toevoegen om een korte wachttijd op te nemen (of `sleep` (slaap)) nadat de tekening is tentoongesteld. Dit zal de astronauten de tijd geven om uw tekening te zien voordat het volgende deel van je boodschap verschijnt. Voeg toe, bovenaan je programma:

```python
van tijd importatie slaap
```

Daarna, op de lijn na degene die jouw tekening toont, voeg je deze code toe om twee seconden te wachten:

```python
sleep(2)
```

\--- /task \---

\--- task \---

Definieer je eigen tekening of patroon om aan de astronauten te laten zine!

\--- /task \---