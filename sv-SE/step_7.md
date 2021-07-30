## Visa luftfuktigheten

Du kan kombinera din avläsning av luftfuktigheten med en bild för ge en grafisk visning av luftfuktigheten. Till exempel kan du visa ett hav för hög luftfuktighet, och en öken för låg luftfuktighet:

![Våt och torr](images/wet-dry.png)

--- uppgift ---

Skapa fler färgvariabler för alla de färger som du vill använda, i slutet av ditt program. Du kanske redan har definierat några av dem i ett tidigare steg.

```python
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80,80)
g=(0,255,0)
y=(255,255,0)
```

--- /uppgift ---

--- uppgift ---

Precis som tidigare, ritar du dina bilder genom att först skapa en lista för var och en av dem, och sedan ställa in listans objekt med de färger som du vill att pixlarna ska ha.

```python
wet= [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g
]


dry= [
  b, b, w, b, b, b, w, b,
  b, b, b, b, b, w, b, b,
  b, w, b, b, b, b, b, w,
  b, b, b, b, w, b, b, b,
  w, b, b, w, b, b, w, b,
  b, b, b, b, b, b, b, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w
]
```

--- /uppgift ---

--- uppgift ---

Lägg till lite kod för att få luftfuktigheten:

```python
luftfuktighet = sense.humidity
```

--- /uppgift ---

--- uppgift ---

Bestäm nu vilken bild som ska visas. I det här exemplet visar vi `våt` bilden om luftfuktigheten är 40% eller högre och `torr` bilden om fuktigheten är under 40%.

```python
luftfuktighet = sense.humidity
if luftfuktighet >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /uppgift ---

--- uppgift ---

Använd luftfuktighetsreglaget för att sätta en luftfuktighet på emulatorn. Kör ditt program och kontrollera att den bild du har valt för den luftfuktigheten visas korrekt.

--- /uppgift ---

--- uppgift ---

Ändra din kod så att ditt program visar luftfuktigheten för astronauterna på det sätt som du väljer.

--- /uppgift ---

--- uppgift --- Testa din kod med några olika fuktighetsinställningar (med skjutreglaget) för att se till att den alltid körs korrekt. Om du har följt exemplet ovan, visas en bild både när luftfuktigheten är inställd på ett värde mindre än 40% och även när den är inställd på mer än 40%?

--- /uppgift ---
