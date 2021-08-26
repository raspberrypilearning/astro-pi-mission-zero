## Meet de vochtigheid

De vochtigheidssensor op de Astro Pi kan de vochtigheid meten van de lucht eromheen, een nuttige eigenschap om je te helpen met het verzamelen van gegevens over de condities in de ruimte.

![De Trinket Sense HAT-emulator waarop een voorbeeldprogramma draait die de vochtigheidswaarde over de LED-matrix laat scrollen in witte letters](images/M0_3.gif)

De Astro Pi meet de vochtigheid in het ISS in percentage waterconcentratie in de lucht.

Een deel van je missie is het bijdragen tot het dagelijkse leven van de bemanning aan boord het ISS, dus hun laten weten dat de vochtigheid aan boord het ruimtestation binnen de normale parameters ligt zal hun geruststellen.

[[[generic-theory-what-is-humidity]]]

--- task ---

Voeg deze code toe om een vochtigheidsmeting te doen:

```python
humid = sense.get_humidity()
```

Deze lijn meet de huidige vochtigheid en slaat de meetwaarde op in de variabele `humid`.

--- /task ---

--- task ---

De vochtigheid wordt heel precies gemeten, d.w.z. dat de opgeslagen waarde een groot aantal decimalen zal hebben. Je kan de waarde afronden op om het even welk aantal decimalen. In ons voorbeeld hebben we het cijfer afgerond op 1 decimaal, maar voor een ander niveau van nauwkeurigheid, verander je het cijfer `1` naar het aantal decimalen dat je wil zien.

```python
humid = round(sense.get_humidity(), 1)
```

--- /task ---

--- task ---

Om de actuele vochtigheid te tonen als een boodschap die over het scherm scrolt, voeg je deze codelijn toe:

```python
sense.show_message(str(humid))
```

Het `str()` deel zet de vochtigheid om van een nummer naar tekst zodat de Astro Pi het kan laten zien.

--- /task ---

--- task ---

Je kan de vochtigheid ook tonen als een deel van een andere boodschap door de delen van je boodschap samen te voegen met een `+`.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

--- /task ---

De echte Astro Pi zal de vochtigheid errond meten, maar je kan de vochtigheid-schuifknop op de Sense HAT-emulator verplaatsen om vochtigheidsveranderingen te simuleren en zo je code te testen.

![Een genummerd screenshot van de Sense HAT-emulator met het codeervenster aan de linkerkant en de emulator aan de rechterkant. De schuifknop die gebruikt wordt om de vochtigheid aan te passen is omcirkeld in de rechter bovenhoek](images/humidity-slider.png)

**Opmerking:** Je vraagt je misschien af waarom de vochtigheidsschuifknop de vochtigheid als een geheel getal weergeeft terwijl de meting die je ontvangt een decimaal is. De emulator simuleert de kleine onnauwkeurigheid van de echte sensor, zodat de vochtigheidsmeting die je ziet een beetje groter of kleiner kan zijn dan de waarde die je instelde met de schuifknop.
