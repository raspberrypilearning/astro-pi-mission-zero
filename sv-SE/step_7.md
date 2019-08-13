## Visa temperaturen

Du kan kombinera din temperaturavläsning med en bild för att även visa temperaturen grafiskt. Du kan exempelvis visa en snöstorm för kalla temperaturer, och en solig dag för varma temperaturer:

![Varm och kall](images/hot-and-cold.png)

\--- uppgift \---

Skapa fler färgvariabler för alla de färger som du vill använda, i slutet av ditt program. Du kanske redan har definierat några av dem i ett tidigare steg. I vårt exempel kommer vi att använda vitt (`w`), gult (`y`), grönt (`g`), och svart/tom (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- uppgift \---

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

\--- uppgift \---

Lägg till lite kod för att hämta temperaturen:

```python
temp = sense.temperature
```

\--- /task \---

\--- uppgift \---

Välj nu vilken bild som ska visas. I det här exemplet kommer vi att visa bilden `hot` om temperaturavläsningen är 20 grader eller högre, och bilden `cold` om temperaturen är under 20 grader.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /task \---

\--- uppgift \---

Använd skjutreglaget för temperatur för att ställa in en temperatur på emulatorn. Kör ditt program och kontrollera att den bild du har valt för den temperaturen visas korrekt.

\--- /task \---

\--- uppgift \---

Ändra din kod så att ditt program visar temperaturen för astronauterna på det sätt som du väljer.

\--- /task \---