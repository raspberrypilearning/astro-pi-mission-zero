## Afișează temperatura

Poți combina citirea temperaturii cu o imagine pentru a indica, de asemenea, temperatura într-un mod grafic. De exemplu, este posibil să afișezi o furtună de zăpadă pentru temperaturi scăzute și o zi însorită pentru temperaturi ridicate:

![Cald și rece](images/hot-and-cold.png)

--- task ---

În partea de jos a programului tău, creează mai multe variabile pentru orice culori pe care vrei sa le folosești în imaginile tale. Este posibil să fi definit deja unele dintre ele într-un pas anterior. În exemplele noastre vom folosi alb (`a`), galben (`g`), verde (`v`) și negru/spațiu gol (`n`).

```python
a = (255, 255, 255)
g = (255, 255, 0)
v = (0, 255, 0)
n = (0, 0, 0)
```

--- /task ---

--- task ---

La fel ca mai devreme, desenează imaginile tale, creând mai întâi o listă pentru fiecare dintre ele, apoi setând elementele listei la culorile pe care dorești să le aibă pixelii.

```python
cald = [
  n, n, n, n, n, g, g, n,
  n, n, n, n, g, g, g, g,
  n, n, n, n, n, g, g, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  v, v, v, v, v, v, v, v,
  v, v, v, v, v, v, v, v
]


rece = [
  n, n, a, n, n, n, a, n,
  n, n, n, n, n, a, n, n,
  n, a, n, n, n, n, n, a,
  n, n, n, n, a, n, n, n,
  a, n, n, a, n, n, a, n,
  n, n, n, n, n, n, n, n,
  a, a, a, a, a, a, a, a,
  a, a, a, a, a, a, a, a
]
```

--- /task ---

--- task ---

Adaugă cod pentru a obține temperatura:

```python
temp = sense.temperature
```

--- /task ---

--- task ---

Acum decide ce imagine vrei să se afișeze. Pentru acest exemplu, vom afișa imaginea `cald` dacă valoarea citită a temperaturii este de 20 de grade sau mai mare și imaginea `rece` dacă temperatura este sub 20 de grade.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(cald)
else:
    sense.set_pixels(rece)
```

--- /task ---

--- task ---

Utilizează sliderul pentru temperatură pentru a seta o temperatură pe emulator. Rulează programul și verifică dacă imaginea pe care ai selectat-o pentru acea temperatură este afișată corect.

--- /task ---

--- task ---

Modifică codul astfel încât programul să afișeze temperatura pentru astronauți în modul ales de tine.

--- /task ---