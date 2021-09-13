## Jeleníts meg egy képet

Az Astro Pi LED mátrixán képeket is megjeleníthetsz. Az űrhajósoknak szóló üdvözleted akár még egy képet vagy mintát is tartalmazhat, egy írott üzenettel együtt vagy ahelyett!

![Képernyőkép az emulátorról, amely a Repülési Egységet mutatja, a LED-mátrixon magának a Repülési Egységnek a képével](images/fu-pic.png)

--- task ---

A programod alján hozz létre néhány színváltozót, hogy meghatározd azokat a színeket, amelyekkel meg szeretnéd rajzolni a képedet. Bármennyi színt használhatsz, de ebben a példában csak egy pár színt fogunk használni - vörös (`r`), fehér (`w`), fekete (`b`), és két szürkeárnyalat (`g` és `s`). Figyeld meg, hogy az árnyalatokat úgy érjük el, hogy csökkentjük a fény erejét mindhárom csatornán, miközben megtartjuk az arányukat.

```python
w = (255, 255, 255)
b = (0, 0, 0)
g = (50,50,50)
s = (200,255,200)
r = (255,0,0)
```

**Megjegyzés:** Azt javasoljuk, hogy a színváltozóknak egybetűs nevet adj, mert azzal időt takaríthatsz meg a következő lépésben, amikor sokszor be kell majd őket gépelned. Továbbá, ha egyjegyű betűket használsz, akkor könnyebben láthatod a képet, amit rajzolsz.

--- /task ---

--- task ---

Az új változóid alatt hozz létre egy 64 elemből álló listát. Minden egyes elem egy pixelt képvisel a LED mátrixban, és az egyik általad meghatározott színváltozónak felel majd meg. Rajzold meg a képedet úgy, hogy a színváltozó nevét írod arra a helyre, ahol szeretnéd, hogy a szín megjelenjen. Mi egy Astro Pi-t rajzoltunk úgy, hogy a fekete (`b`) pixeleket háttérként használtuk, a szürke (`g`) pixelekkel pedig megrajzoltuk az Astro Pi fémvázát:

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

Adj hozzá egy kódsort, hogy a képed megjelenjen a LED kijelzőn!

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Nyomd meg a **Run** (Futtatás) gombot, hogy megláthasd a képed!

--- /task ---

--- task ---

Akár hozzáadhatsz egy olyan kódot is, amellyel egy rövid szünetet vagy „szundit” (angolul `sleep`) tarthatsz a kép megjelenítése után. Ezzel egy kis időt hagysz az űrhajósok számára, hogy láthassák a képedet, mielőtt az üzeneted következő része megjelenik. A programod elejéhez add hozzá:

```python
from time import sleep
```

Majd az után a sor után, amelyik megjeleníti a képedet, gépeld be ezt egy két másodperces szünetért:

```python
sleep(2)
```

--- /task ---

--- task ---

Hozd létre a saját képedet vagy mintádat, hogy megmutathasd az űrhajósoknak!

--- /task ---
