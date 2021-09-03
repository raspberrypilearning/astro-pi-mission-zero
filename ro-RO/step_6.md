## Măsoară umiditatea

Senzorul de umiditate din Astro Pi poate măsura umiditatea aerului din jurul acestuia, o funcție utilă care te ajută să obții date despre condițiile din spațiu.

![Emulatorul Trinket Sense HAT care rulează un program eșantion care derulează valoarea umidității prin matricea LED folosind litere albe](images/M0_3.gif)

Astro Pi măsoară umiditatea în cadrul ISS în procentajul concentrației de apă din aer.

O parte din misiunea ta este să contribui la viața de zi cu zi a echipajului de la bordul ISS, informându-i astfel că umiditatea la bordul stației spațiale se află într-un interval normal, fapt ce îi va liniști.

[[[generic-theory-what-is-humidity]]]

--- task ---

Adaugă acest cod pentru a măsura umiditatea:

```python
humid = sense.get_humidity()
```

Această linie va măsura umiditatea curentă și va stoca rezultatul în variabila `humid`.

--- /task ---

--- task ---

Umiditatea este înregistrată foarte precis, adică valoarea stocată va avea un număr mare de zecimale. Poți rotunji valoarea la orice număr de zecimale. În exemplul dat, am rotunjit la o zecimală, dar pentru un alt nivel de precizie, schimbă numărul `1` la numărul de zecimale pe care dorești să le vezi.

```python
humid = round(sense.get_humidity(), 1)
```

--- /task ---

--- task ---

Pentru a afișa umiditatea curentă ca mesaj derulant pe afișaj, adaugă această linie de cod:

```python
sense.show_message(str(humid))
```

Partea `str()` convertește umiditatea dintr-un caracter numeric în caracter text astfel încât Astro Pi să o poată afișa.

--- /task ---

--- task ---

De asemenea, poți afișa umiditatea ca parte a unui alt mesaj prin îmbinarea părților mesajului tau împreună cu un `+`.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

--- /task ---

Un Astro Pi real va măsura umiditatea din jurul său, dar poți muta glisorul de umiditate de pe emulatorul Sense HAT pentru a simula schimbări de umiditate și pentru a testa codul tău.

![O captură de ecran etichetată a emulatorului Sense HAT cu fereastra de cod din stânga și emulatorul din dreapta. Cursorul folosit pentru a ajusta umiditatea este înconjurat în colțul din dreapta sus](images/humidity-slider.png)

**Notă:** S-ar putea să te întrebi de ce sliderul de umiditate afișează umiditatea ca număr întreg, dar citirea pe care o primești este un număr cu zecimale. Emulatorul simulează ușoara inexactitate a senzorului real, astfel încât umiditatea măsurată pe care o vezi poate fi puțin mai mică sau mai mare decât valoarea pe care ai setat-o cu ajutorul glisorului.
