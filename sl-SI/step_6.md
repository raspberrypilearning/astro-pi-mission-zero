## Izmerite temperaturo

Senzor temperature v računalniku Astro Pi lahko izmeri temperaturo zraka okrog sebe, kar je koristna funkcija, ki pomaga pri zbiranju podatkov o razmerah v vesolju.

![Sporočilo o temperaturi](images/degrees-message.gif)

Astro Pi temperaturo na postaji ISS meri v stopinjah Celzija (&deg;C). Ker se temperature v vesolju razlikujejo veliko bolj kot tiste na Zemlji, lahko Astro Pi izmeri temperaturo v razponu od –40 stopinj Celzija do +120 stopinj Celzija.

Del vaše misije je izboljšanje vsakdana posadke na postaji ISS. Ko jim boste sporočili, da je temperatura na vesoljski postaji v mejah normale, jih bo to prav gotovo pomirilo.

## \--- collapse \---

## title: Kaj je temperatura?

S temperaturo izmerimo, kako vroče je nekaj. Med obiskom pri zdravniku so vam prav gotovo s termometrom že kdaj izmerili telesno temperaturo.

![Termometer](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} via Wikimedia Commons*

Če smo natančnejši, je temperatura merilo količine toplotne energije snovi. Veste, da je kocka ledu trdna, a ko se segreje (ko absorbira toplotno energijo iz okolja), se stali in postane tekoča. Ko absorbira ali izgubi toplotno energijo, snov namreč spremeni agregatno stanje, npr. iz trdnega v tekoče.

\--- /collapse \---

\--- task \---

Za odčitavanje temperature dodajte to kodo:

```python
temp = sense.get_temperature()
```

Ta vrstica bo izmerila trenutno temperaturo in izmerjeno vrednost shranila v spremenljivki `temp`.

\--- /task \---

\--- task \---

Temperatura je zabeležena zelo natančno, kar pomeni, da bo shranjena vrednost imela veliko število decimalnih mest. Vrednost lahko zaokrožite na poljubno število decimalnih mest. V tem primeru smo vrednost zaokrožili na eno decimalno mesto, a za drugačno stopnjo natančnosti lahko število `1` spremenite v želeno število decimalnih mest.

```python
temp = round( sense.get_temperature(), 1 )
```

\--- /task \---

\--- task \---

Za prikaz trenutne temperature v obliki premikajočega se sporočila dodajte to vrstico kode:

```python
sense.show_message( str(temp) )
```

Del `str()` temperaturo pretvori iz številke v besedilo, da jo lahko Astro Pi prikaže.

\--- /task \---

\--- task \---

Temperaturo lahko prikažete tudi kot del drugega sporočila, kar storite tako, da dele sporočila združite s kodo `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

Pravi Astro Pi bo izmeril temperaturo okrog sebe, a vi lahko drsnik za temperaturo na emulatorju Sense HAT premikate in s tem simulirate temperaturne spremembe ter preizkusite svojo kodo.

![Drsnik za temperaturo](images/temperature-slider.png)

**Opomba:** Morda se sprašujete, zakaj drsnik temperaturo prikaže kot celo število, a dobljen odčitek bo v decimalni obliki. Emulator simulira manjšo nenatančnost pravega senzorja, zato je lahko izmerjena temperatura nekoliko višja ali nižja od vrednosti, ki ste jo nastavili z drsnikom.