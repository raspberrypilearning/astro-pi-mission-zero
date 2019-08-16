## Meet de temperatuur

De temperatuursensor op de Astro Pi kan de temperatuur meten van de lucht eromheen, een nuttige eigenschap om je te helpen met het verzamelen van gegevens over de condities in de ruimte.

![Boodschap over de temperatuur](images/degrees-message.gif)

De Astro Pi meet de temperatuur op het ISS in graden Celsius (&deg;C). Omdat de temperaturen in de ruimte veel meer verschillen dan op aarde, kan de Astro Pi de temperaturen meten van slechts -40 graden Celsius tot wel +120 graden Celsius.

Een deel van je missie is het bijdragen tot het dagelijkse leven van de bemanning aan boord het ISS, dus hun laten weten dat de temperatuur aan boord het ruimtestation binnen de normale parameters ligt zal hun geruststellen.

## \--- collapse \---

## title: Wat is de temperatuur?

Temperatuur is de maat van hoe heet iets is. Misschien heb je wel eens je temperatuur laten opnemen met een thermometer gedurende een bezoek aan de dokter.

![Thermometer](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} via Wikimedia Commons*

Om precies te zijn, de temperatuur is een maat van de hoeveelheid warmte-energie van een bepaalde substantie. Je weet dat een ijsklontje massief is, maar als het opwarmt, d.w.z. als het warmte-energie absorbeert van zijn omgeving, smelt het en wordt het vloeibaar. Dit is omdat, wanneer een stof warmte-energie absorbeert of voldoende verliest, dan verandert de substantie van staat, namelijk verandert van het massief zijn naar een vloeistof.

\--- /collapse \---

\--- task \---

Voeg deze code toe bij het meten van een temperatuur:

```python
temp = sense.temperature
```

Deze lijn meet de huidige temperatuur en slaat de meetwaarde op in de variabele `temp`.

\--- /task \---

\--- task \---

De temperatuur wordt heel precies opgenomen, d.w.z. de opgeslagen waarde heeft een groot aantal decimale cijfers. Je kunt de waarde afronden tot een aantal decimale cijfers. In het voorbeeld hebben wij het cijfer afgerond tot een decimaal, maar voor een ander niveau van nauwkeurigheid, verander het nummer `1` tot het nummer van decimale cijfers die je wenst te zien.

```python
temp = round( sense.temperature, 1 )
```

\--- /task \---

\--- task \---

Om de huidige temperatuur tentoon te stellen als een scrollende boodschap op het schermbeeld, voeg je deze codelijn toe:

```python
sense.show_message( str(temp) )
```

Het `str()` deel zet de temperatuur om van een nummer naar tekst zodat de Astro Pi het kan laten zien.

\--- /task \---

\--- task \---

Je kunt ook de temperatuur laten zien als deel van een andere boodschap door delen van je boodschap samen te voegen met een `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

De werkelijke Astro Pi zal de temperatuur eromheen meten, maar je kunt de temperatuur schuifknop op de Sense HAT emulator verschuiven om de temperatuurveranderingen te simuleren en je code te testen.

![Temperatuurschuifknop](images/temperature-slider.png)

**Aandacht:** Je vraagt je misschien af waarom de temperatuurschuifknop de temperatuur laat zien als een geheel getal, maar de lezing die je ziet is een decimaal. De emulator simuleert de onnauwkeurigheid van de werkelijke sensor, zodat de temperatuurmeting die je ziet misschien iets groter of kleiner is dan de waarde die je hebt ingesteld met de schuifknop.