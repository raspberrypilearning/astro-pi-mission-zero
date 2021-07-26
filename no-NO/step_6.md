## Måle luftfuktigheten

Luftfuktighetsføleren i Astro Pi kan måle luftfuktigheten i luften rundt den, en nyttig funksjon som hjelper deg med å samle data om forholdene i rommet.

![Melding om temperaturen](images/degrees-message.gif)

Astro Pi måler luftfuktigheten i ISS i antall prosent vannkonsentrasjon i luften.

En del av oppdraget deres er å bidra til dagliglivet til mannskapet ombord på ISS, så når de får vite at luftfuktigheten om bord på romstasjonen ligger innenfor et normalt område, vil de bli beroliget.

[[[generic-theory-what-is-humidity]]]

--- task ---

Legg til denne koden for å lese av luftfuktigheten:

```python
humid = sense.humidity
```

Denne linjen vil måle gjeldende luftfuktighet og lagre den målte verdien i variabelen `humid`.

--- /task ---

--- task ---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. You can round the value to any number of decimal places. In the example we have rounded to one decimal place, but for a different level of precision, change the number `1` to the number of decimal places you would like to see.

```python
humid = round( sense.humidity, 1 )
```

--- /task ---

--- task ---

For å vise gjeldende luftfuktighet som en rullende melding på skjermen, legg til denne kodelinjen:

```python
sense.show_message( str(humid) )
```

`str()`-delen gjør om luftfuktigheten fra tall til tekst slik at Astro Pi kan vise den.

--- /task ---

--- task ---

Du kan også vise luftfuktigheten som en del av en annen melding ved å slå sammen delene av meldingen med et `+`.

```python
sense.show_message( "Det er " + str(humid) + " %" )
```

--- /task ---

Den virkelige Astro Pi måler luftfuktigheten rundt seg, men dere kan flytte glidebryteren for luftfuktighet på Sense HAT-emulatoren for å simulere endringer i luftfuktighet og teste koden.

![Luftfuktighet glidebryter](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.
