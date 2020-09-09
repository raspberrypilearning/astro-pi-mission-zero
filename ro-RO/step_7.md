## Afișează umiditatea

Poți combina citirea umidității cu o imagine pentru a indica umiditatea într-un mod grafic. De exemplu, ai putea afișa un ocean pentru o umiditate mare și un deșert pentru umiditate scăzută:

![Umed și uscat](images/wet-dry.png)

--- task ---

În partea de jos a programului tău, creează mai multe variabile pentru orice culori pe care vrei sa le folosești în imaginile tale. Este posibil să fi definit deja unele dintre ele într-un pas anterior.

```python
o = (255,130,0)
b = (0,0,255)
c = (0,150,255)
e = (80,80,80)
g = (0,255,0)
y = (255,255,0)
```

--- /task ---

--- task ---

La fel ca mai devreme, desenează imaginile tale, creând mai întâi o listă pentru fiecare dintre ele, apoi setând elementele listei la culorile pe care dorești să le aibă pixelii.

```python
ud = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


uscat = [
  c, c, g, g, c, c, c, c,
  c, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, g, g, g, g, g, c, c,
  c, c, g, g, c, c, c, c,
  y, y, y, y, y, y, y, y,
  y, y, y, y, y, y, y, y
]
```

--- /task ---

--- task ---

Adaugă cod pentru a obține umiditatea:

```python
umiditate = sense.humidity
```

--- /task ---

--- task ---

Acum decide ce imagine vrei să se afișeze. Pentru acest exemplu, vom afișa imaginea `ud` dacă valoarea citită a umidității este de 40% sau mai mare și imaginea `uscat` dacă umiditatea este sub 40%.

```python
umiditate = sense.humidity
if umiditate >= 40:
    sense.set_pixels(ud)
else:
    sense.set_pixels(uscat)
```

--- /task ---

--- task ---

Utilizează glisorul pentru umiditate pentru a seta o umiditate pe emulator. Rulează programul și verifică dacă imaginea pe care ai selectat-o pentru acea umiditate este afișată corect.

--- /task ---

--- task ---

Modifică codul astfel încât programul să afișeze umiditatea pentru astronauți în modul ales de tine.

--- /task ---