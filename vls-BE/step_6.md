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

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. You can round the value to any number of decimal places. In the example we have rounded to one decimal place, but for a different level of precision, change the number `1` to the number of decimal places you would like to see.

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

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.
