## Mät luftfuktigheten

Luftfuktighetssenorn i Astro Pi kan mäta den omgivande luftfuktighet, en användbar funktion som hjälper dig att samla in data om förhållandena i rymden.

![Trinket Sense HAT -emulatorn som kör ett provprogram som rullar luftfuktighetsvärdet över LED -matrisen med vita bokstäver](images/M0_3.gif)

Astro Pi mäter luftfuktigheten i ISS i procentuell vattenkoncentration i luften.

En del av ditt uppdrag är att bidra till det dagliga livet för besättningen ombord på ISS, så att låta dem veta att luftfuktigheten ombord på rymdstationen är inom ett normalt intervall kommer att lugna dem.

[[[generic-theory-what-is-humidity]]]

--- task ---

Lägg till den här koden för att avläsa luftfuktigheten:

```python
humid = sense.get_humidity()
```

Den här raden med kod mäter den aktuella luftfuktigheten och lagrar det avlästa värdet i variabeln `humid`.

--- /task ---

--- task ---

Luftfuktigheten registreras mycket exakt, dvs. det lagrade värdet har ett stort antal decimaler. Du kan avrunda värdet till valfritt antal decimaler. I exemplet har vi avrundat till en decimal, men för en annan precision, ändra siffran `1` till antalet decimaler du vill se.

```python
humid = round(sense.get_humidity(), 1)
```

--- /task ---

--- task ---

För att visa den aktuella luftfuktigheten som ett rullande meddelande på skärmen, lägger du till den här raden kod:

```python
sense.show_message(str(humid))
```

Delen `str()` omvandlar luftfuktigheten från ett nummer till text så att Astro Pi kan visa den.

--- /task ---

--- task ---

Du kan också visa luftfuktigheten som en del av ett annat meddelande genom att slå samman delarna av meddelandet med ett `+`.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

--- /task ---

Den verkliga Astro Pi kommer att mäta den omgivande luftfuktighet, men du kan testa din kod och simulera luftfuktighetsförändringar genom att flytta luftfuktighetsreglaget på Sense HAT-emulatorn.

![En märkt skärmdump av Sense HAT -emulatorn med kodfönstret till vänster och emulatorn till höger. Reglaget som används för att justera luftfuktigheten är inringat i det övre högra hörnet](images/humidity-slider.png)

**Obs!** Du kanske undrar varför skjutreglaget för luftfuktighet visar luftfuktigheten som ett heltal, men avläsningen du får är ett decimaltal. Emulatorn simulerar den lilla avvikelsen i noggranhet hos den riktiga sensorns, så skjutreglaget för luftfuktighet som du ser kan vara något större eller mindre än det värde du ställer in med skjutreglaget.
