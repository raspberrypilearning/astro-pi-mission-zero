## Mål temperaturen

Temperatursensoren i Astro Pi kan måle temperaturen i luften omkring den og er en nyttig funktion, der kan hjælpe dig med at indsamle data om forholdene i rummet.

![Besked om temperaturen](images/degrees-message.gif)

Astro Pi måler temperaturen i ISS i grader Celsius (&deg;C). Idet temperaturerne i rummet varierer meget mere end dem på jorden, kan Astro Pi måle temperaturer helt nede fra -40 grader Celsius og op til +120 grader Celsius.

En del af din mission går ud på at bidrage til besætningens dagligdag ombord på ISS, så det vil berolige dem at få at vide, at temperaturen ombord på rumstationen ligger inden for normalområdet.

--- collapse ---
---
title: Hvad er temperatur?
---
Temperatur er en måling af, hvor varmt noget er. Du har sandsynligvis fået taget din temperatur med et termometer under et besøg hos lægen.

![Termometer](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} via Wikimedia Commons*

For at være mere præcis er temperatur en måling af mængden af varmeenergi i et stof. Du ved, at en isterning er fast, men når den varmes op, dvs. optager varmeenergi fra omgivelserne, smelter den og bliver flydende. Det skyldes, at når et stof optager eller afgiver tilstrækkeligt med varmeenergi, ændres stoffets tilstand; det går eksempelvis fra at være fast til at være flydende.

--- /collapse ---

--- task ---

Tilføj denne kode for at foretage en temperaturaflæsning:

```python
temp = sense.temperature
```

Denne linje måler den aktuelle temperatur og lagrer den målte værdi i variablen `temp`.

--- /task ---

--- task ---

Temperaturen registreres meget præcist, dvs., at den lagrede værdi har et stort antal decimaler. Du kan afrunde værdien til et vilkårligt antal decimaler. I eksemplet har vi afrundet til én decimal, men for at få en anden grad af præcision skal du ændre tallet `1` til det antal decimaler, du gerne vil se.

```python
temp = round( sense.temperature, 1 )
```

--- /task ---

--- task ---

For at få vist den aktuelle temperatur som rullende besked på displayet skal du tilføje denne kodelinje:

```python
sense.show_message( str(temp) )
```

Delen `str()` konverterer temperaturen fra et tal til tekst, så Astro Pi kan vise den.

--- /task ---

--- task ---

Du kan også vise temperaturen som en del af en anden besked ved at sætte delene af din besked sammen med et `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

--- /task ---

Den rigtige Astro Pi måler temperaturen omkring den, men du kan flytte temperaturskyderen på Sense HAT-emulatoren for at simulere temperaturændringer og teste din kode.

![Temperaturskyder](images/temperature-slider.png)

**Bemærk:** Du undrer dig måske over, hvorfor temperaturskyderen viser temperaturen som et helt tal, men den aflæsning, du får, er med decimaler. Emulatoren simulerer den lille unøjagtighed fra den rigtige sensor, så den temperaturmåling, du ser, kan være en lille smule større eller mindre end den værdi, du har indstillet med skyderen.