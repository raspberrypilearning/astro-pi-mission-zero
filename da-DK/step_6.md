## Mål luftfugtigheden

Luftfugtighedssensoren i Astro Pi kan måle luftfugtigheden i luften omkring den og er en nyttig funktion, der kan hjælpe dig med at indsamle data om forholdene i rummet.

![Besked om luftfugtigheden](images/degrees-message.gif)

Astro Pi måler fugtigheden i ISS i procent af vandkoncentrationen i luften.

En del af din mission er at bidrage til det daglige liv for besætningen ombord på ISS, så at lade dem vide, at fugtigheden ombord på rumstationen er inden for et normalt interval, vil berolige dem.

[[[generic-theory-what-is-humidity]]]

--- task ---

Tilføj denne kode for at foretage en fugtighedsaflæsning:

```python
humid = sense.humidity
```

Denne linje måler den aktuelle fugtighed og gemmer den målte værdi i variablen `humid` (luftfugtighed).

--- /task ---

--- task ---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. You can round the value to any number of decimal places. In the example we have rounded to one decimal place, but for a different level of precision, change the number `1` to the number of decimal places you would like to see.

```python
humid = round( sense.humidity, 1 )
```

--- /task ---

--- task ---

For at få vist den aktuelle luftfugtighed, som rullende besked på displayet skal du tilføje denne kodelinje:

```python
sense.show_message( str(humid) )
```

Funktionen `str()` konverterer fugtigheden fra et tal til tekst, så Astro Pi kan vise den.

--- /task ---

--- task ---

Du kan også vise luftfugtigheden som en del af en anden besked ved at tilslutte dele af din besked sammen med en `+`.

```python
sense.show_message ("Det er" + str (humid) + "%")
```

--- /task ---

Den rigtige Astro Pi måler luftfugtigheden omkring den, men du kan flytte luftfugtighedsskyderen på Sense HAT-emulatoren for at simulere ændring af luftfugtigheden og teste din kode.

![Luftfugtighedsskyder](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.
