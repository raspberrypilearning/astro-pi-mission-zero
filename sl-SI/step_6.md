## Izmerite vlažnost

Senzor vlažnosti v računalniku Astro Pi lahko izmeri stanje vlažnosti okoli sebe, kar je koristna funkcija pri zbiranju podatkov o razmerah v vesolju.

![Sporočilo o vlagi](images/degrees-message.gif)

Astro Pi meri vlažnost na ISS v odstotkih koncentracije vode v zraku.

Part of your mission is to contribute to the daily lives of the crew aboard the ISS, so letting them know that the humidity aboard the space station is within a normal range will reassure them.

[[[generic-theory-what-is-humidity]]]

--- task ---

Za odčitavanje vlage dodajte to kodo:

```python
humid = sense.humidity
```

Ta vrstica bo izmerila trenutno vlažnost in izmerjeno vrednost shranila v spremenljivki `humid`.

--- /task ---

--- task ---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. You can round the value to any number of decimal places. In the example we have rounded to one decimal place, but for a different level of precision, change the number `1` to the number of decimal places you would like to see.

```python
humid = round( sense.humidity, 1 )
```

--- /task ---

--- task ---

Za prikaz trenutne vlage v obliki premikajočega se sporočila dodajte to vrstico kode:

```python
sense.show_message( str(humid) )
```

Del `str()` vlago pretvori iz številke v besedilo, da jo lahko Astro Pi prikaže.

--- /task ---

--- task ---

Vlažnost lahko prikažete tudi kot del drugega sporočila, kar storite tako, da dele sporočila združite s kodo `+`.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

--- /task ---

Pravi Astro Pi bo izmeril vlago okrog sebe, a vi lahko drsnik za vlago na emulatorju Sense HAT premikate in s tem simulirate spremembe vlage ter preizkusite svojo kodo.

![Drsnik za vlažnost](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.
