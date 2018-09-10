## Geef de temperatuur weer

Je kunt je temperatuurmeting combineren met een afbeelding om ook de temperatuur op een grafische manier aan te geven. Je kunt bijvoorbeeld een sneeuwstorm weergeven voor koude temperaturen en een zonnige dag voor warme temperaturen:

![Warm en koud](images/hot-and-cold.png)

\--- task \---

Maak onder aan het programma meer kleurvariabelen voor alle kleuren die je in je afbeeldingen wilt gebruiken. Mogelijk heb je sommige ervan al in een vorige stap gedefinieerd. In onze voorbeelden gebruiken we wit (`w`), geel (`y`), groen (`g`) en zwart / blanco (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Teken net als eerder je foto's door eerst een lijst voor elk van deze te maken en vervolgens de lijstitems in te stellen op de kleuren die je wilt dat je pixels zijn.

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

Voeg een code toe om de temperatuur te krijgen:

```python
temp = sense.get_temperature()
```

\--- /task \---

\--- task \---

Bepaal nu welke afbeelding moet worden weergegeven. Voor dit voorbeeld zullen we de `hot` weergeven afbeelding als de temperatuurwaarde 20 graden of meer is, en de `cold` (koude) afbeelding als de temperatuur lager is dan 20 graden.

```python
temp = sense.get_temperature()
if temp >= 20:
sense.set_pixels(hot)
else:
sense.set_pixels(cold)
```

\--- /task \---

\--- task \---

Gebruik de schuifregelaar voor temperatuur om een ​​temperatuur op de emulator in te stellen. Voer je programma uit en controleer of de afbeelding die je voor die temperatuur hebt geselecteerd correct wordt weergegeven.

\--- /task \---

\--- task \---

Wijzig je code zodat je programma de temperatuur op je eigen gekozen manier aan de astronauten weergeeft.

\--- /task \---