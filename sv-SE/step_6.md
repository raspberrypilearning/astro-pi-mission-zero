## Mät luftfuktigheten

Luftfuktighetssenorn i Astro Pi kan mäta den omgivande luftfuktighet, en användbar funktion som hjälper dig att samla in data om förhållandena i rymden.

![Meddelande om luftfuktigheten](images/degrees-message.gif)

Astro Pi mäter luftfuktigheten i ISS i procentuell vattenkoncentration i luften.

En del av ditt uppdrag är att bidra till det dagliga livet för besättningen ombord på ISS, så att låta dem veta att luftfuktigheten ombord på rymdstationen är inom ett normalt område kommer att lugna dem.

[[[generic-theory-what-is-humidity]]]

--- task ---

Lägg till den här koden för att avläsa luftfuktigheten:

```python
luftfuktighet = sense.humidity
```

Den här raden med kod mäter den aktuella luftfuktigheten och lagrar det avlästa värdet i variabeln `luftfuktighet`.

--- /task ---

--- task ---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. You can round the value to any number of decimal places. In the example we have rounded to one decimal place, but for a different level of precision, change the number `1` to the number of decimal places you would like to see.

```python
luftfuktighet = round( sense.humidity, 1 )
```

--- /task ---

--- task ---

För att visa den aktuella luftfuktigheten som ett rullande meddelande på skärmen, lägger du till den här raden kod:

```python
sense.show_message( str(humid) )
```

Delen `str()` omvandlar luftfuktigheten från ett nummer till text så att Astro Pi kan visa den.

--- /task ---

--- task ---

Du kan också visa luftfuktigheten som en del av ett annat meddelande genom att slå samman delarna av meddelandet med ett `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

--- /task ---

Den verkliga Astro Pi kommer att mäta den omgivande luftfuktighet, men du kan testa din kod och simulera luftfuktighetsförändringar genom att flytta luftfuktighetsreglaget på Sense HAT-emulatorn.

![Reglage för luftfuktighet](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.
