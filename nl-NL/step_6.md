## Meet de luchtvochtigheid

De luchtvochtigheidssensor in de Astro Pi kan de vochtigheid van de lucht eromheen meten, een handige functie om je te helpen gegevens te verzamelen over de omstandigheden in de ruimte.

![Bericht over de luchtvochtigheid](images/degrees-message.gif)

De Astro Pi meet de luchtvochtigheid in het ISS in procentuele waterconcentratie in de lucht.

Een deel van je missie is om bij te dragen aan het dagelijks leven van de bemanning aan boord van het ISS, dus ze laten weten dat de luchtvochtigheid aan boord van het ruimtestation binnen een normaal bereik ligt, zal hen geruststellen.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Voeg deze code toe om een luchtvochtigheidsmeting te doen:

```python
humid = sense.humidity
```

Deze regel meet de huidige luchtvochtigheid en slaat de gemeten waarde op in de variabele `humid`.

\---/task\---

\--- task \---

De luchtvochtigheid wordt zeer nauwkeurig geregistreerd, d.w.z. de opgeslagen waarde heeft een groot aantal decimalen. Je kunt de waarde naar elk aantal decimalen afronden. In het voorbeeld hebben we afgerond op één plaats achter de komma, maar voor een ander niveau van precisie, wijzig je het cijfer `1` in het aantal decimalen dat je wilt zien.

```python
humid = round( sense.humidity, 1 )
```

-- /task \---

\--- task \---

Om de huidige luchtvochtigheid weer te geven als een scrollend bericht op het display, voeg je deze regel code toe:

```python
sense.show_message( str(humid) )
```

Het `str()` gedeelte zet de luchtvochtigheid van een getal om naar tekst, zodat de Astro Pi het kan weergeven.

\---/task\---

\--- task \---

Je kunt de luchtvochtigheid ook weergeven als onderdeel van een ander bericht door de delen van je bericht samen te voegen met een `+`.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

\--- /task \---

De echte Astro Pi meet de luchtvochtigheid om zich heen, maar je kunt de luchtvochtigheidsschuifregelaar op de Sense HAT-emulator verplaatsen om luchtvochtigheidsveranderingen te simuleren en je code te testen.

![Luchtvochtigheidsschuifregelaar](images/humidity-slider.png)

**Opmerking:** Je vraagt ​​je misschien af ​​waarom de luchtvochtigheidsschuifregelaar de luchtvochtigheid als een geheel getal weergeeft, maar de waarde die je krijgt is een decimaal. De emulator simuleert de kleine onnauwkeurigheid van de echte sensor, dus de luchtvochtigheidsmeting die je ziet, is mogelijk iets groter of kleiner dan de waarde die je met de schuifregelaar hebt ingesteld.