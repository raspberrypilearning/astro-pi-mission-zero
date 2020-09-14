## Meet de vochtigheid

De vochtigheidssensor op de Astro Pi kan de vochtigheid meten van de lucht eromheen, een nuttige eigenschap om je te helpen met het verzamelen van gegevens over de condities in de ruimte.

![Boodschap over de vochtigheid](images/degrees-message.gif)

De Astro Pi meet de vochtigheid in het ISS in percentage waterconcentratie in de lucht.

Een deel van je missie is het bijdragen tot het dagelijkse leven van de bemanning aan boord het ISS, dus hun laten weten dat de vochtigheid aan boord het ruimtestation binnen de normale parameters ligt zal hun geruststellen.

[[[generic-theory-what-is-humidity]]]

--- task ---

Voeg deze code toe om een vochtigheidsmeting te doen:

```python
humid = sense.humidity
```

Deze lijn meet de huidige vochtigheid en slaat de meetwaarde op in de variabele `humid`.

--- /task ---

--- task ---

De vochtigheid wordt heel precies gemeten, d.w.z. dat de opgeslagen waarde een groot aantal decimalen zal hebben. Je kunt de waarde afronden tot een aantal decimale cijfers. In het voorbeeld hebben wij het cijfer afgerond tot één decimaal, maar voor een ander niveau van nauwkeurigheid, verander het nummer `1` tot het nummer van decimale cijfers die je wenst te zien.

```python
humid = round( sense.humidity, 1 )
```

--- /task ---

--- task ---

Om de actuele vochtigheid te tonen als een scrollende boodschap op het scherm, voeg je deze codelijn toe:

```python
sense.show_message( str(humid) )
```

Het `str()` deel zet de vochtigheid om van een nummer naar tekst zodat de Astro Pi het kan laten zien.

--- /task ---

--- task ---

Je kan de vochtigheid ook tonen als een deel van een andere boodschap door de delen van je boodschap samen te voegen met een `+`.

```python
sense.show_message("Het is " + str(humid) + " %")
```

--- /task ---

De echte Astro Pi zal de vochtigheid errond meten, maar je kan de vochtigheid-schuifknop op de Sense HAT-emulator verplaatsen om vochtigheidsveranderingen te simuleren en zo je code te testen.

![Vochtigheids-schuifknop](images/humidity-slider.png)

**Opmerking:** Je vraagt je misschien af waarom de vochtigheid-schuifknop de vochtigheid als een geheel getal weergeeft, maar de meting die je ontvangt een decimaal is. De emulator simuleert de kleine onnauwkeurigheid van de echte sensor, zodat de vochtigheidsmeting die je ziet een beetje groter of kleiner kan zijn dan de waarde die je instelde met de schuifknop.