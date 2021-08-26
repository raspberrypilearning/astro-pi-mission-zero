## Mål luftfugtigheden

Luftfugtighedssensoren i Astro Pi kan måle luftfugtigheden i luften omkring den og er en nyttig funktion, der kan hjælpe dig med at indsamle data om forholdene i rummet.

![Trinket Sense HAT-emulatoren kører et prøveprogram, der ruller værdien af luftfugtigheden hen over LED-matricen med hvide bogstaver](images/M0_3.gif)

Astro Pi måler fugtigheden i ISS i procent af vandkoncentrationen i luften.

En del af din mission er at bidrage til det daglige liv for besætningen ombord på ISS, så at lade dem vide, at fugtigheden ombord på rumstationen er inden for et normalt interval, vil berolige dem.

[[[generic-theory-what-is-humidity]]]

--- task ---

Tilføj denne kode for at foretage en fugtighedsaflæsning:

```python
luftfugtighed = sense.humidity()
```

Denne linje måler den aktuelle fugtighed og gemmer den målte værdi i variablen ` luftfugtighed `.

--- /task ---

--- task ---

Luftfugtigheden registreres meget præcist, dvs. at den lagrede værdi har et stort antal decimaler. Du kan afrunde værdien til et vilkårligt antal decimaler. I eksemplet har vi afrundet til én decimal, men for at få en anden grad af præcision skal du ændre tallet `1` til det antal decimaler, du gerne vil se.

```python
luftfugtighed = round(sense.humidity(), 1)
```

--- /task ---

--- task ---

For at få vist den aktuelle luftfugtighed, som rullende besked på displayet skal du tilføje denne kodelinje:

```python
sense.show_message(str(luftfugtighed))
```

Funktionen `str()` konverterer fugtigheden fra et tal til tekst, så Astro Pi kan vise den.

--- /task ---

--- task ---

Du kan også vise luftfugtigheden som en del af en anden besked ved at tilslutte dele af din besked sammen med en `+`.

```python
sense.show_message ("Det er" + str (luftfugtighed) + " %")
```

--- /task ---

Den rigtige Astro Pi måler luftfugtigheden omkring den, men du kan flytte luftfugtighedsskyderen på Sense HAT-emulatoren for at simulere ændring af luftfugtigheden og teste din kode.

![Et opmærket skærmbillede af Sense HAT-emulatoren med kodevinduet til venstre og emulatoren til højre. Skyderen (slideren), der bruges til at justere luftfugtigheden, er markeret med en cirkel i øverste højre hjørne](images/humidity-slider.png)

**Bemærk:** Du undrer dig måske over, hvorfor luftfugtighedsskyderen (slider) viser luftfugtigheden som et helt tal, men den aflæsning, du får, er med decimaler. Emulatoren simulerer en lille unøjagtighed fra den rigtige sensor, så den luftfugtighedsmåling, du ser, kan være en lille smule større eller mindre end den værdi, du har indstillet med skyderen (slideren).
