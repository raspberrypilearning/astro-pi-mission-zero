## Izmerite vlažnost

Senzor vlažnosti v računalniku Astro Pi lahko izmeri stanje vlažnosti okoli sebe, kar je koristna funkcija pri zbiranju podatkov o razmerah v vesolju.

![Sporočilo o vlagi](images/degrees-message.gif)

Astro Pi meri vlažnost na ISS v odstotkih koncentracije vode v zraku.

Del vaše misije je izboljšanje vsakdana posadke na postaji ISS. Ko jim boste sporočili, da je vlaga na vesoljski postaji v mejah normale, jih bo to prav gotovo pomirilo.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Za odčitavanje vlage dodajte to kodo:

```python
humid = sense.humidity
```

\--- /collapse \---

\--- /task \---

\--- task \---

Vlaga je zabeležena zelo natančno, kar pomeni, da bo shranjena vrednost imela veliko število decimalnih mest. Vrednost lahko zaokrožite na poljubno število decimalnih mest. V tem primeru smo vrednost zaokrožili na eno decimalno mesto, a za drugačno stopnjo natančnosti lahko število `1` spremenite v želeno število decimalnih mest.

```python
humid = round( sense.humidity, 1 )
```

\--- /task \---

\--- task \---

Za prikaz trenutne vlage v obliki premikajočega se sporočila dodajte to vrstico kode:

```python
sense.show_message( str(humid) )
```

Del `str()` vlago pretvori iz številke v besedilo, da jo lahko Astro Pi prikaže.

\--- /task \---

\--- task \---

Vlažnost lahko prikažete tudi kot del drugega sporočila, kar storite tako, da dele sporočila združite s kodo `+`.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

\--- /task \---

Pravi Astro Pi bo izmeril vlago okrog sebe, a vi lahko drsnik za vlago na emulatorju Sense HAT premikate in s tem simulirate spremembe vlage ter preizkusite svojo kodo.

![Drsnik za vlažnost](images/humidity-slider.png)

**Opomba:** Morda se sprašujete, zakaj drsnik vlago prikaže kot celo število, a dobljen odčitek bo v decimalni obliki. Emulator simulira manjšo nenatančnost pravega senzorja, zato je lahko izmerjena vlaga nekoliko višja ali nižja od vrednosti, ki ste jo nastavili z drsnikom.