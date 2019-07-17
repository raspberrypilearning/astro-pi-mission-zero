## Meet de temperatuur

De temperatuur sensor op de Astro Pi kan de temperatuur meten van de lucht eromheen, een nuttige eigenschap om je te helpen met het verzamelen van gegevens over de condities in Space.

![Boodschap over de temperatuur](images/degrees-message.gif)

De Astro Pi meet de temperatuur op de ISS in graden Celsius (&deg;C). Omdat de temperaturen in Space veel meer verschillen dan op Aarde, kan de Astro Pi de temperaturen meten van slechts -40 graden Celsius tot wel +120 graden Celsius.

Een deel van je missie is het bijdragen tot het dagelijkse leven van de bemanning aan boord de ISS, dus hun laten weten dat de temperatuur aan boord het ruimtestation binnen de normale parameters ligt zal hun geruststellen.

## \--- collapse \---

## title: Wat is de temperatuur?

Temperatuur is de maat van hoe heet iets is. Misschien heb je wel eens je temperatuur laten opnemen met een thermometer gedurende een bezoek aan de dokter.

![Thermometer](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} via Wikimedia Commons*

Om precies te zijn, de temperatuur is een maat van de hoeveelheid warmte-energie van een bepaalde substantie. Je weet dat een ijsklontje massief is, maar als het opwarmt, d.w.z. als het warmte-energie absorbeert van zijn omgeving, smelt het en wordt het vloeibaar. Dit is omdat, wanneer een stof warmte-energie absorbeert of voldoende verliest, dan verandert de substantie van staat, namelijk verandert van het massief zijn naar een vloeistof.

\--- /collapse \---

\--- task \---

Voeg deze code toe bij het meten van een temperatuur:

```python
temp = sense.get_temperature()
```

Deze lijn meet de huidige temperatuur en slaat de meetwaarde op in de variabele `temp`.

\--- /task \---

\--- task \---

De temperatuur wordt heel precies opgenomen, d.w.z. de opgeslagen waarde heeft een groot aantal decimale cijfers. Je kunt de waarde afronden tot een aantal decimale cijfers. In het voorbeeld hebben wij het cijfer afgerond tot een decimaal, maar voor een ander niveau van nauwkeurigheid, verander het nummer `1` tot het nummer van decimale cijfers die je wenst te zien.

```python
temp = rond( sense.neem_temperatuur(), 1 )
```

\--- /task \---

\--- task \---

Om de huidige temperatuur tentoon te stellen als een scrollende boodschap op het schermbeeld, voeg je deze codelijn toe:

```python
sense.show_message( str(temp) )
```

Het `str()` deel zet de temperatuur om van een nummer naar tekst zodat de Astro Pi het tentoon kan stellen.

\--- /task \---

\--- task \---

Je kunt ook de temperatuur tentoonstellen als deel van een andere boodschap door delen van je boodschap samen te voegen met een `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

De werkelijke Astro Pi zal de temperatuur eromheen meten, maar je kunt de temperatuur schuifknop op de Sense HAT emulator verschuiven om de temperatuur veranderingen te simuleren en je code te testen.

![Temperatuur schuifknop](images/temperature-slider.png)

**Aandacht:** Je vraagt je misschien af waarom de temperatuur schuifknop de temperatuur laat zien als een geheel getal, maar de lezing die je ziet is een decimaal. De emulator simuleert de onnauwkeurigheid van de werkelijke sensor, zodat de temperatuurmeting die je ziet misschient iets groter of kleiner is dan de waarde die je hebt gezet met de schuifknop.