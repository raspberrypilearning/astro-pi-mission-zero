## Meet de temperatuur

De temperatuursensor in de Astro Pi kan de temperatuur van de lucht eromheen meten, een handige functie om je te helpen gegevens te verzamelen over de omstandigheden in de ruimte.

![Bericht over de temperatuur](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

Een deel van je missie is om bij te dragen aan het dagelijks leven van de bemanning aan boord van het ISS, dus ze laten weten dat de temperatuur aan boord van het ruimtestation binnen een normaal bereik ligt, zal hen geruststellen.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Voeg deze code toe om een ​​temperatuurmeting te doen:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- /task \---

\--- task \---

De temperatuur wordt zeer nauwkeurig geregistreerd, d.w.z. de opgeslagen waarde heeft een groot aantal decimalen. Je kunt de waarde naar elk aantal decimalen afronden. In het voorbeeld hebben we afgerond op één plaats achter de komma, maar voor een ander niveau van precisie, wijzig je het cijfer `1` tot het aantal decimalen dat je wilt zien.

```python
temp = round( sense.temperature, 1 )
```

-- /task \---

\--- task \---

Om de huidige temperatuur weer te geven als een scrollend bericht op het display, voeg je deze regel code toe:

```python
sense.show_message( str(temp) )
```

The `str()` part converts the humidity from a number into text so that the Astro Pi can display it.

\--- /task \---

\--- task \---

Het `str()` gedeelte zet de temperatuur van een getal om naar tekst, zodat de Astro Pi het kan weergeven.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

De echte Astro Pi meet de temperatuur om zich heen, maar je kunt de temperatuurschuifregelaar op de Sense HAT-emulator verplaatsen om temperatuurveranderingen te simuleren en je code te testen.

![Humidity slider](images/humidity-slider.png)

**Opmerking:** Je vraagt ​​je misschien af ​​waarom de temperatuurschuifregelaar de temperatuur als een geheel getal weergeeft, maar de waarde die je krijgt is een decimaal. De emulator simuleert de kleine onnauwkeurigheid van de echte sensor, dus de temperatuurmeting die je ziet, is mogelijk iets groter of kleiner dan de waarde die je met de schuifregelaar hebt ingesteld.