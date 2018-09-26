## Afișează temperatura

Poți combina citirea temperaturii cu o imagine pentru a indica, de asemenea, temperatura într-un mod grafic. De exemplu, este posibil să afișezi o furtună de zăpadă pentru temperaturi scăzute și o zi însorită pentru temperaturi ridicate:

![Cald şi rece](images/hot-and-cold.png)

--- task ---

În partea de jos a programului tău, creează câteva variabile de culoare pentru a defini culorile cu care doreşti să desenezi imaginile tale. Este posibil să fi definit deja unele dintre ele într-un pas anterior. În exemplele noastre vom folosi alb (`w`), galben (`y`), verde (`g`), şi negru/spaţiu gol (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

--- /task ---

--- task ---

La fel ca și mai devreme, desenează imaginile, creând mai întâi o listă pentru fiecare dintre ele, apoi setând elementele listate pentru culorile pe care dorești să le aibă pixelii.

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

--- /task ---

--- task ---

Adaugă cod pentru a obține temperatura:

```python
temp = sense.get_temperature()
```

--- /task ---

--- task ---

Acum decide ce imagine vrei să se afișeze. Pentru acest exemplu, vom afișa imaginea `hot` (cald) dacă valoarea citită a temperaturii este de 20 de grade sau mai mare și imaginea `cold` (rece) dacă temperatura este sub 20 de grade.

```python
temp = sense.get_temperature()
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

--- /task ---

--- task ---

Utilizează sliderul pentru temperatură pentru a seta o temperatură pe emulator. Rulează programul şi verifică dacă imaginea pe care ai selectat-o pentru acea temperatură este afişată corect.

--- /task ---

--- task ---

Modifică codul astfel încât programul să afișeze temperatura pentru astronauți în modul ales de tine.

--- /task ---