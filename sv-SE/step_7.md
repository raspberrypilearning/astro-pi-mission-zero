## Reagera på luftfuktighet

Du kan kombinera din avläsning av luftfuktigheten med en bild för ge en grafisk visning av luftfuktigheten. Till exempel kan du visa ett hav för hög luftfuktighet, och en öken för låg luftfuktighet:

![Våt och torr](images/wet-dry.png)

--- task ---

Skapa fler färgvariabler för alla de färger som du vill använda, i slutet av ditt program. Du kanske redan har definierat några av dem i ett tidigare steg.

```python
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80,80)
g=(0,255,0)
y=(255,255,0)
```

--- /task ---

--- task ---

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

--- /task ---

--- task ---

Lägg till lite kod för att få luftfuktigheten:

```python
humid = sense.get_humidity()
```

--- /task ---

--- task ---

Bestäm nu vilken bild som ska visas. I det här exemplet visar vi `våt` bilden om luftfuktigheten är 40% eller högre och `torr` bilden om fuktigheten är under 40%.

```python
humid = sense.get_humidity()
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

Använd luftfuktighetsreglaget för att sätta en luftfuktighet på emulatorn. Kör ditt program och kontrollera att den bild du har valt för den luftfuktigheten visas korrekt.

--- /task ---

--- task ---

Ändra din kod så att ditt program visar luftfuktigheten för astronauterna på det sätt som du väljer.

--- /task ---

--- task --- Testa din kod med några olika fuktinställningar (med reglaget) för att se till att den alltid fungerar korrekt. Om du har följt exemplet ovan, visas en bild både när luftfuktigheten är inställd på ett värde mindre än 40% och även när den är inställd på mer än 40%?

--- /task ---
