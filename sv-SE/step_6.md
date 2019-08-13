## Mät temperaturen

Temperatursensorn i Astro Pi kan mäta den omgivande luftens temperatur, en användbar funktion som hjälper dig att samla data om förhållandena i rymden.

![Meddelande om temperaturen](images/degrees-message.gif)

Astro Pi mäter temperaturen ombord på ISS i grader Celsius (&deg;C). Eftersom temperaturen i rymden varierar mycket mer än på jorden, kan Astro Pi mäta så låga temperaturer som -40 grader Celsius ända upp till +120 grader Celsius.

En del av ditt uppdrag är att bidra till vardagslivet för besättningen ombord på ISS, så att låta dem få reda på att temperaturen ombord på rymdstationen ligger inom ett normalt intervall kommer att muntra upp dem.

## \--- collapse \---

## title: Vad är temperatur?

Temperatur är ett mått på hur varmt något är. En doktor kanske har tagit din temperatur med en termometer.

![Termometer](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} via Wikimedia Commons*

För att vara mer exakt, är temperatur ett mått på mängden värmeenergi i ett ämne. Du vet att en isbit är hård, men när den värms upp, dvs. när den absorberar värmeenergi ur sin omgivning, så smälter den och blir till vätska. Detta beror på att när ett ämne absorberar eller förlorar tillräckligt med värmeenergi, kommer ämnet att ändra form, t.ex. övergå från fast form till att bli en vätska.

\--- /collapse \---

\--- uppgift \---

Lägg till den här koden för att göra en temperaturavläsning:

```python
temp = sense.temperature
```

Den här raden mäter den aktuella temperaturen och lagrar det uppmätta värdet i variabeln `temp`.

\--- /task \---

\--- uppgift \---

Temperaturen lagras väldigt noggrant, dvs. det lagrade värdet kommer att ha många decimaler. Du kan avrunda värdet till valfritt antal decimaler. I exemplet har vi avrundat till en decimal, men för en annan nivå av noggrannhet, ändrar du talet `1` till det antal decimaler du vill se.

```python
temp = round( sense.temperature, 1 )
```

\--- /task \---

\--- uppgift \---

För att visa aktuell temperatur som ett rullande meddelande på skärmen, lägger du till den här raden kod:

```python
sense.show_message( str(temp) )
```

Delen med `str()` konverterar temperaturen från ett tal till text så att Astro Pi kan visa den.

\--- /task \---

\--- uppgift \---

Du kan också visa temperaturen som en del av ett annat meddelande genom att slå samman delarna av ditt meddelande med ett `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

Den riktiga Astro Pi mäter omgivningstemperaturen, men du flyttar skjutreglaget för temperatur på Sense HAT-emulatorn för att simulera temperaturförändringar och testa din kod.

![Skjutreglage för temperatur](images/temperature-slider.png)

**Obs!** Du kanske undrar varför skjutreglaget för temperatur visar temperaturen som ett heltal, men avläsningen du får är ett decimaltal. Emulatorn simulerar den lilla bristen på noggrannhet hos den riktiga sensorn, så skjutreglaget för temperatur som du ser kan vara något större eller mindre än det värde du ställer in med skjutreglaget.