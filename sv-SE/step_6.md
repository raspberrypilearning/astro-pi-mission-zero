## Mäta temperaturen

Temperatursensorn i Astro Pi kan mäta den omgivande luftens temperatur, en användbar funktion som hjälper dig att samla data om förhållandena i rymden.

![Meddelande om temperaturen](images/degrees-message.gif)

Astro Pi mäter luftfuktigheten i ISS i procentuell vattenkoncentration i luften.

En del av ditt uppdrag är att bidra till det dagliga livet för besättningen ombord på ISS, så att låta dem veta att temperaturen ombord på rymdstationen är inom ett normalt område kommer att lugna dem.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Lägg till den här koden för att göra en luftfuktighetsavläsning:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- /task \---

\--- task \---

Luftfuktigheten registreras mycket exakt, dvs det lagrade värdet har ett stort antal decimaler. Du kan avrunda värdet till valfritt antal decimaler. I exemplet har vi avrundat till en decimal, men för en annan precision, ändra siffran ` 1 ` till antalet decimaler du vill se.

```python
temp = round( sense.temperature, 1 )
```

\--- /task \---

\--- task \---

För att visa aktuell luftfuktigheten som ett rullande meddelande på skärmen, lägger du till den här raden kod:

```python
sense.show_message( str(humid) )
```

Delen `str()` omvandlar fuktigheten från ett nummer till text så att Astro Pi kan visa den.

\--- /task \---

\--- task \---

Delen med `str()` konverterar temperaturen från ett tal till text så att Astro Pi kan visa den.

```python
sense.show_message ("Det är " + str (humid) + "%")
```

\--- /task \---

Den verkliga Astro Pi kommer att mäta luftfuktigheten runt den, men du kan flytta luftfuktighetsreglaget på Sense HAT-emulatorn för att simulera luftfuktighetsförändringar och testa din kod.

![Reglage för fuktighet](images/humidity-slider.png)

**Obs!** Du kanske undrar varför skjutreglaget för luftfuktighet visar luftfuktigheten som ett heltal, men avläsningen du får är ett decimaltal. Emulatorn simulerar den lilla bristen på noggrannhet hos den riktiga sensorn, så skjutreglaget för luftfuktighet som du ser kan vara något större eller mindre än det värde du ställer in med skjutreglaget.