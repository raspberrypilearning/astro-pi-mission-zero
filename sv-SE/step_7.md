## Visa temperaturen

You could combine your humidity reading with a picture to also indicate the humidity in a graphical way. For example, you might display an ocean for high humidity, and a desert for low humidity:

![Varm och kall](images/wet-dry.png)

\--- task \---

Skapa fler färgvariabler för alla de färger som du vill använda, i slutet av ditt program. Du kanske redan har definierat några av dem i ett tidigare steg.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Precis som tidigare, ritar du dina bilder genom att först skapa en lista för var och en av dem, och sedan ställa in listans objekt med de färger som du vill att pixlarna ska ha.

```python
hot = [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g
]


cold = [
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

\--- /task \---

\--- task \---

Lägg till lite kod för att hämta temperaturen:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Välj nu vilken bild som ska visas. I det här exemplet visar vi ` våt ` bilden om luftfuktigheten är 40% eller högre och ` torr ` bilden om fuktigheten är under 40%.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /task \---

\--- task \---

Use the humidity slider to set a humidity on the emulator. Run your program and check that the image you've selected for that humidity is correctly displayed.

\--- /task \---

\--- task \---

Ändra din kod så att ditt program visar temperaturen för astronauterna på det sätt som du väljer.

\--- /task \---