## Măsoară temperatura

Senzorul de temperatură din Astro Pi poate măsura temperatura aerului în jurul acestuia, o funcție utilă care te ajută să obții date despre condițiile din spațiu.

![Mesaj despre temperatură](images/degrees-message.gif)

Astro Pi măsoară temperatura în ISS în grade Celsius (&deg;C). Deoarece temperaturile în spațiu variază mult mai mult decât cele de pe Pământ, Astro Pi poate măsura temperaturi de la -40 grade Celsius până la +120 grade Celsius.

O parte din misiunea ta este să contribui la viața de zi cu zi a echipajului de la bordul ISS, informându-i astfel că temperatura la bordul stației spațiale se află într-un interval normal, fapt ce îi va liniști.

## \--- collapse \---

## title: Ce este temperatura?

Temperatura este măsura a cât de cald este ceva. S-ar putea ca temperatura ta să fi fost luată cu un termometru în timpul unei vizite la medic.

![Termometru](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} via Wikimedia Commons*

Mai precis, temperatura este o măsură a cantității de energie termică a unei substanțe. Știi că un cub de gheață este solid, dar pe măsură ce se încălzește, adică în timp ce absoarbe energia termică din mediul său, se topește și devine lichid. Acest lucru se datorează faptului că, atunci când o substanță absoarbe sau pierde suficientă energie termică, substanța îşi va schimba starea, de exemplu va trece de la stare solidă la cea lichidă.

\--- /collapse \---

\--- task \---

Adaugă acest cod pentru a măsura temperatura:

```python
temp = sense.get_temperature()
```

Această linie va măsura temperatura curentă și va stoca valoarea măsurată în variabila `temp`.

\--- /task \---

\--- task \---

Temperatura este înregistrată foarte precis, adică valoarea stocată va avea un număr mare de zecimale. Poți rotunji valoarea la orice număr de zecimale. În exemplul dat, am rotunjit la o zecimală, dar pentru un alt nivel de precizie, schimbă numărul `1` la numărul de zecimale pe care doreşti să le vezi.

```python
temp = round( sense.get_temperature(), 1 )
```

\--- /task \---

\--- task \---

Pentru a afișa temperatura curentă ca mesaj derulant pe afișaj, adaugă această linie de cod:

```python
sense.show_message( str(temp) )
```

Partea `str()` convertește temperatura dintr-un caracter numeric în caracter text astfel încât Astro Pi să poată afișa.

\--- /task \---

\--- task \---

De asemenea, poți afișa temperatura ca parte a unui alt mesaj prin îmbinarea părților mesajului tau împreună cu un `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

Astro Pi real va măsura temperatura din jurul său, dar poți muta sliderul de temperatură de pe emulatorul Sense HAT pentru a simula schimbări de temperatură și pentru a testa codul tău.

![Cursor pentru temperatură](images/temperature-slider.png)

**Notă:** S-ar putea să te întrebi de ce sliderul de temperatură afișează temperatura ca număr întreg, dar citirea pe care o primești este un număr cu zecimale. Emulatorul simulează o ușoară inexactitate a senzorului real, astfel încât temperatura măsurată pe care o vezi poate fi puțin mai mică sau mai mare decât valoarea pe care ai setat-o cu ajutorul cursorului.