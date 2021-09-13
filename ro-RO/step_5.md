## Afișează o imagine

Poți afișa imagini pe matricea LED a Astro Pi. Poate că salutul tău pentru astronauți ar putea include o imagine sau un model, împreună cu mesajul sau în locul mesajului scris?

![O captură de ecran a ferestrei de emulator care arată Unitatea de zbor cu matricea LED care afișează o poză a Unității de zbor în sine](images/fu-pic.png)

--- task ---

În partea de jos a programului tău, creează câteva variabile de culoare pentru a defini culorile cu care dorești să desenezi imaginea. Poți folosi cât de multe culori dorești, dar în acest exemplu vom folosi doar câteva culori - roșu (`r`), alb (`w`), negru (`b`), și două nuanțe de gri (`g` și `s`). Nu uita că aceste nuanțe se obțin prin reducerea cantității de lumină în toate cele trei canale, menținând în același timp proporțiile.

```python
w = (255, 255, 255)
b = (0, 0, 0)
g = (50,50,50)
s = (200,255,200)
r = (255,0,0)
```

**Notă:** De această dată, este o idee bună să dai variabilelor de culoare câte un nume de o singură literă, deoarece acest lucru va economisi timp la pasul următor, unde le vei tasta de mai multe ori. Mai mult, folosirea literelor unice va face mai ușoară vederea imaginii pe care o vei desena.

--- /task ---

--- task ---

Sub noile tale variabile, creează o listă cu 64 de elemente. Fiecare element reprezintă un pixel pe matricea LED și corespunde uneia dintre variabilele de culoare pe care le-ai definit. Desenează imaginea ta introducând o variabilă în locul în care dorești să apară culoarea atribuită. Am desenat un Astro Pi folosind pixeli negri (`b`) ca fundal și albi (`g`) pentru a-i desena părțile din metal a carcasei:

```python
 picture = [
    g, b, b, b, b, b, b, g,
    b, g, g, g, g, g, g, b,
    b, g, b, b, g, w, g, g,
    b, g, b, b, g, g, g, g,
    b, g, g, g, s, s, g, g,
    b, g, r, g, g, g, g, g,
    b, g, g, g, g, g, g, b,
    g, b, b, b, b, b, b, g
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

Apasă **Run** pentru a vedea afișată imaginea ta.

--- /task ---

--- task ---

S-ar putea să dorești să adaugi cod pentru a include o așteptare scurtă (sau `sleep`) după afișarea imaginii. Acest lucru va acorda astronauților timp pentru a vedea imaginea înainte ca următoarea parte a mesajului să apară. În partea de sus a programului, adaugă:

```python
from time import sleep
```

Apoi, pe linia după cea care afișează imaginea, adaugă acest cod pentru a aștepta două secunde:

```python
sleep(2)
```

--- /task ---

--- task ---

Creează propria ta imagine sau model pentru a o afișa astronauților!

--- /task ---
