## Måle luftfuktigheten

Luftfuktighetsføleren i Astro Pi kan måle luftfuktigheten i luften rundt den, en nyttig funksjon som hjelper deg med å samle data om forholdene i rommet.

![Melding om temperaturen](images/degrees-message.gif)

Astro Pi måler luftfuktigheten i ISS i antall prosent vannkonsentrasjon i luften.

En del av oppdraget deres er å bidra til dagliglivet til mannskapet ombord på ISS, så når de får vite at luftfuktigheten om bord på romstasjonen ligger innenfor et normalt område, vil de bli beroliget.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Legg til denne koden for å lese av luftfuktigheten:

```python
humid = sense.humidity
```

Denne linjen vil måle gjeldende luftfuktighet og lagre den målte verdien i variabelen `humid`.

\--- /task \---

\--- task \---

Luftfuktigheten lagres veldig nøyaktig, det vil si at den lagrede verdien har mange desimaler. Du kan avrunde verdien til et hvilket som helst antall desimaler. I eksemplet har vi avrundet til en desimal, men for et annet presisjonsnivå, endrer dere tallet `1` til så mange desimaler dere ønsker.

```python
humid = round( sense.humidity, 1 )
```

\--- /task \---

\--- task \---

For å vise gjeldende luftfuktighet som en rullende melding på skjermen, legg til denne kodelinjen:

```python
sense.show_message( str(humid) )
```

`str()`-delen gjør om luftfuktigheten fra tall til tekst slik at Astro Pi kan vise den.

\--- /task \---

\--- task \---

Du kan også vise luftfuktigheten som en del av en annen melding ved å slå sammen delene av meldingen med et `+`.

```python
sense.show_message( "Det er " + str(humid) + " %" )
```

\--- /task \---

Den virkelige Astro Pi måler luftfuktigheten rundt seg, men dere kan flytte glidebryteren for luftfuktighet på Sense HAT-emulatoren for å simulere endringer i luftfuktighet og teste koden.

![Luftfuktighet glidebryter](images/humidity-slider.png)

**Merk:** Dere lurer kanskje på hvorfor luftfuktighetsinnstillingen viser temperaturen som et heltall, mens avlesingen dere får er et desimaltall. Emulatoren simulerer den lille unøyaktigheten til den virkelige sensoren, så luftfuktighetsmålingene dere ser kan være ørlite større eller mindre enn verdien dere har angitt med skyveknappen.