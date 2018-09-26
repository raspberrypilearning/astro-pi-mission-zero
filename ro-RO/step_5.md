## Afișează o imagine

Poți afișa imagini pe matricea LED a Astro Pi. Poate că salutul tău pentru astronauți ar putea include o imagine sau un model, împreună cu mesajul sau în locul mesajului scris?

![Astronaut](images/astronaut-pic.png)

--- task ---

În partea de jos a programului tău, creează câteva variabile de culoare pentru a defini culorile cu care doreşti să desenezi imaginea. Poți folosi cât de multe culori doreşti, dar în acest exemplu vom păstra doar două culori - alb (`w`) și negru (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Notă:** De această dată, este o idee bună să dați variabilelor de culoare câte un nume de o singură literă, deoarece acest lucru va economisi timp la pasul următor, unde le veți tasta de mai multe ori. Mai mult, folosirea literelor unice va face mai ușoară vederea fotografiei pe care o vei desena.

--- /task ---

--- task ---

Sub noile variabile, creează o listă cu 64 de elemente. Fiecare element reprezintă un pixel pe matricea LED și corespunde uneia dintre variabilele de culoare pe care le-ai definit. Desenează fotografia ta introducând o variabilă în locul în care doreşti să apară culoarea atribuită. Am desenat un astronaut folosind pixeli negri (`b`) ca fundal și albi (`w`) pentru a desena costumul astronauților în spațiu:

```python
picture = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
```

--- /task ---

--- task ---

Adaugă o linie de cod pentru a afișa imaginea ta pe afișajul cu LED-uri.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Apasă **Run** (Executare) pentru a vedea afișată imaginea ta.

--- /task ---

--- task ---

S-ar putea să dorești să adaugi cod pentru a include o așteptare scurtă (sau `sleep`) (repaus) după afișarea imaginii. Acest lucru va acorda astronauților timp pentru a vedea imaginea înainte ca următoarea parte a mesajului să apară. În partea de sus a programului, adaugă:

```python
from time import sleep
```

Apoi, pe linia după cea care afișează imaginea, adaugă acest cod pentru a aștepta două secunde:

```python
sleep(2)
```

--- /task ---

--- task ---

Creează propria ta imagine sau model pentru a le afișa astronauților!

--- /task ---