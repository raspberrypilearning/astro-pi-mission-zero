## Mål luftfugtigheden

Temperatursensoren i Astro Pi kan måle temperaturen i luften omkring den og er en nyttig funktion, der kan hjælpe dig med at indsamle data om forholdene i rummet.

![Besked om luftfugtigheden](images/degrees-message.gif)

Astro Pi måler fugtigheden i ISS i procent af vandkoncentrationen i luften.

En del af din mission er at bidrage til det daglige liv for besætningen ombord på ISS, så at lade dem vide, at fugtigheden ombord på rumstationen er inden for et normalt interval, vil berolige dem.

[[[generic-theory-what-is-humidity]]]

\--- opgave \---

Tilføj denne kode for at foretage en temperaturaflæsning:

```python
luftfugtighed = sense.humidity
```

Denne linje måler den aktuelle fugtighed og gemmer den målte værdi i variablen ` humid `.

\--- /opgave \---

\--- opgave \---

Temperaturen registreres meget præcist, dvs., at den lagrede værdi har et stort antal decimaler. Du kan afrunde værdien til et vilkårligt antal decimaler. I eksemplet har vi afrundet til én decimal, men for at få en anden grad af præcision skal du ændre tallet `1` til det antal decimaler, du gerne vil se.

```python
humid = round( sense.humidity, 1 )
```

\--- /opgave \---

\--- opgave \---

For at få vist den aktuelle temperatur som rullende besked på displayet skal du tilføje denne kodelinje:

```python
sense.show_message( str(humid) )
```

Funktionen `str()` konverterer temperaturen fra et tal til tekst, så Astro Pi kan vise den.

\--- /opgave \---

\--- opgave \---

Delen `str()` konverterer temperaturen fra et tal til tekst, så Astro Pi kan vise den.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

\--- /opgave \---

Den rigtige Astro Pi måler temperaturen omkring den, men du kan flytte temperaturskyderen på Sense HAT-emulatoren for at simulere temperaturændringer og teste din kode.

![Fugtighedsskyder](images/humidity-slider.png)

**Bemærk:** Du undrer dig måske over, hvorfor temperaturskyderen viser temperaturen som et helt tal, men den aflæsning, du får, er med decimaler. Emulatoren simulerer den lille unøjagtighed fra den rigtige sensor, så den temperaturmåling, du ser, kan være en lille smule større eller mindre end den værdi, du har indstillet med skyderen.