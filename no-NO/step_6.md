## Måle temperaturen

Temperaturføleren i Astro Pi kan måle temperaturen på luften rundt den, en nyttig funksjon som hjelper deg med å samle data om forholdene i rommet.

![Melding om temperaturen](images/degrees-message.gif)

Astro Pi måler temperaturen i ISS i grader Celsius (&deg;C). Fordi temperaturen i rommet varierer mye mer enn på jorden, kan Astro Pi måle temperaturer fra så lavt som -40 grader Celsius opp til +120 grader Celsius.

En del av oppdraget deres er å bidra til dagliglivet til mannskapet ombord på ISS, så når de får vite at temperaturen om bord på romstasjonen ligger innenfor et normalt område, vil de bli beroliget.

--- collapse ---
---
title: Hva er temperatur?
---
Temperatur er måling av hvor varmt noe er. Det kan godt hende dere har fått målt temperaturen med et termometer hos legen.

![Termometer](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} via Wikimedia Commons*

For å være mer presis er temperatur et mål på mengden varmeenergi i et stoff. Dere vet at en isbit er hard, men når den varmes opp, det vil si når den absorberer varmeenergi fra omgivelsene, smelter den og blir til væske. Dette skyldes at når et stoff absorberer eller mister nok varmeenergi, vil stoffet forandre tilstand, for eksempel vil det gå fra å være et fast stoff til å bli en væske.

--- /collapse ---

--- task ---

Legg til denne koden for å ta en temperaturavlesning:

```python
temp = sense.temperature
```

Denne linjen vil måle gjeldende temperatur og lagre den målte verdien i variabelen `temp`.

--- /task ---

--- task ---

Temperaturen registreres svært nøyaktig, dvs. den lagrede verdien vil ha et høyt antall desimaler. Du kan avrunde verdien til et hvilket som helst antall desimaler. I eksemplet har vi avrundet til en desimal, men for et annet presisjonsnivå, endrer dere tallet `1` til så mange desimaler dere ønsker.

```python
temp = round( sense.temperature, 1 )
```

--- /task ---

--- task ---

For å vise gjeldende temperatur som en rullerende melding på skjermen, legg til denne kodelinjen:

```python
sense.show_message( str(temp) )
```

`str()`-delen omdanner temperaturen fra tall til tekst slik at Astro Pi kan vise den.

--- /task ---

--- task ---

Du kan også vise temperaturen som en del av en annen melding ved å slå sammen delene av meldingen med et `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

--- /task ---

Den virkelige Astro Pi måler temperaturen rundt seg, men dere kan flytte temperaturregulatoren på Sense HAT-emulatoren for å simulere temperaturendringer og teste koden.

![Temperaturregulator](images/temperature-slider.png)

**Merk:** Dere lurer kanskje på hvorfor temperaturregulatoren viser temperaturen som et heltall, mens avlesingen dere får er et desimaltall. Emulatoren simulerer den lille unøyaktigheten til den virkelige sensoren, så temperaturmålingene dere ser kan være ørlite større eller mindre enn verdien dere har angitt med skyveknappen.