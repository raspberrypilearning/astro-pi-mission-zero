## Măsoară umiditatea

Senzorul de umiditate din Astro Pi poate măsura temperatura aerului în jurul acestuia, o funcție utilă care te ajută să obții date despre condițiile din spațiu.

![Mesaj despre umiditate](images/degrees-message.gif)

Astro Pi măsoară umiditatea în cadrul ISS în procentajul concentrației de apă din aer.

O parte din misiunea ta este să contribui la viața de zi cu zi a echipajului de la bordul ISS, informându-i astfel că umiditatea la bordul stației spațiale se află într-un interval normal, fapt ce îi va liniști.

[[[generic-theory-what-is-humidity]]]

--- task ---

Adaugă acest cod pentru a măsura umiditatea:

```python
umiditate = sense.humidity
```

Această linie va măsura umiditatea curentă și va stoca rezultatul în variabila `umiditate`.

--- /task ---

--- task ---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. You can round the value to any number of decimal places. In the example we have rounded to one decimal place, but for a different level of precision, change the number `1` to the number of decimal places you would like to see.

```python
umiditate = round( sense.humidity, 1 )
```

--- /task ---

--- task ---

Pentru a afișa umiditatea curentă ca mesaj derulant pe afișaj, adaugă această linie de cod:

```python
sense.show_message( str(humid) )
```

Partea `str()` convertește umiditatea dintr-un caracter numeric în caracter text astfel încât Astro Pi să o poată afișa.

--- /task ---

--- task ---

De asemenea, poți afișa umiditatea ca parte a unui alt mesaj prin îmbinarea părților mesajului tau împreună cu un `+`.

```python
sense.show_message( "Umiditate de " + str(umiditate) + "%" )
```

--- /task ---

Un Astro Pi real va măsura umiditatea din jurul său, dar poți muta sliderul de umiditate de pe emulatorul Sense HAT pentru a simula schimbări de umiditate și pentru a testa codul tău.

![Slider-ul de umiditate](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.
