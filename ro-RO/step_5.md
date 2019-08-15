## Afișează o imagine

Poți afișa imagini pe matricea LED a Astro Pi. Poate că salutul tău pentru astronauți ar putea include o imagine sau un model, împreună cu mesajul sau în locul mesajului scris?

![Astronaut](images/astronaut-pic.png)

\--- task \---

În partea de jos a programului tău, creează câteva variabile de culoare pentru a defini culorile cu care dorești să desenezi imaginea. Poți folosi cât de multe culori dorești, dar în acest exemplu vom păstra doar două culori — alb (`a`) și negru (`n`).

```python
a = (255, 255, 255)
n = (0, 0, 0)
```

**Notă:** De această dată, este o idee bună să dai variabilelor de culoare câte un nume de o singură literă, deoarece acest lucru va economisi timp la pasul următor, unde le vei tasta de mai multe ori. Mai mult, folosirea literelor unice va face mai ușoară vederea imaginii pe care o vei desena.

\--- /task \---

\--- task \---

Sub noile tale variabile, creează o listă cu 64 de elemente. Fiecare element reprezintă un pixel pe matricea LED și corespunde uneia dintre variabilele de culoare pe care le-ai definit. Desenează imaginea ta introducând o variabilă în locul în care dorești să apară culoarea atribuită. Am desenat un astronaut folosind pixeli negri (`n`) ca fundal și albi (`a`) pentru a desena costumul astronauților în spațiu:

```python
imagine = [
    n, n, a, a, a, a, n, n,
    n, a, n, n, n, n, a, n,
    n, a, n, a, a, n, a, n,
    n, a, n, n, n, n, a, n,
    n, n, a, a, a, a, n, n,
    n, n, a, a, a, a, n, n,
    n, a, a, a, a, a, a, n,
    n, a, a, a, a, a, a, n
]
```

\--- /task \---

\--- task \---

Adaugă o linie de cod pentru a afișa imaginea ta pe afișajul cu LED-uri.

```python
sense.set_pixels(imagine)
```

\--- /task \---

\--- task \---

Apasă **Run** pentru a vedea afișată imaginea ta.

\--- /task \---

\--- task \---

S-ar putea să dorești să adaugi cod pentru a include o așteptare scurtă (sau `sleep`) după afișarea imaginii. Acest lucru va acorda astronauților timp pentru a vedea imaginea înainte ca următoarea parte a mesajului să apară. În partea de sus a programului, adaugă:

```python
from time import sleep
```

Apoi, pe linia după cea care afișează imaginea, adaugă acest cod pentru a aștepta două secunde:

```python
sleep(2)
```

\--- /task \---

\--- task \---

Creează propria ta imagine sau model pentru a le afișa astronauților!

\--- /task \---