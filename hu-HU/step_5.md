## Jeleníts meg egy képet!

Az Astro Pi LED mátrixán képeket is megjeleníthetsz. Az űrhajósoknak szóló üdvözleted akár még egy képet vagy mintát is tartalmazhat, egy írott üzenettel együtt vagy a helyett!

![Űrhajós](images/astronaut-pic.png)

\--- task \---

A programod alján hozz létre néhány színváltozót, hogy meghatározd azokat a színeket, amelyekkel meg szeretnéd rajzolni a képedet. Annyi színt használhatsz, amennyit csak szeretnél, de ebben a példában mi csak kettőt fogunk: fehéret (`w`) és feketetét (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Megjegyzés:** Azt javasoljuk, hogy a színváltozóknak egybetűs nevet adj, mert azzal időt takaríthatsz meg a következő lépésben, amikor sokszor be kell majd őket gépelned. Továbbá, ha egyjegyű betűket használsz, akkor könnyebben láthatod a képet, amit rajzolsz.

\--- /task \---

\--- task \---

Az új változóid alatt hozz létre egy 64 elemből álló listát. Minden egyes elem egy pixelt képvisel a LED mátrixban, és az egyik általad meghatározott színváltozónak felel majd meg. Rajzold meg a képedet egy változó hozzáadásával arra a helyre, ahol szeretnéd, hogy a hozzárendelt szín megjelenjen. Mi egy űrhajóst rajzoltunk úgy, hogy a fekete (`b`) pixeleket háttérként használtuk, a fehér (`w`) pixelekkel pedig megrajzoltuk az űrhajós szkafanderét:

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

\--- /task \---

\--- task \---

Adj hozzá egy kódsort, hogy a képed megjelenjen a LED kijelzőn!

```python
sense.set_pixels(picture)
```

\--- /task \---

\--- task \---

Nyomd meg a **Run** (Futtatás) gombot, hogy megláthasd a képed!

\--- /task \---

\--- task \---

Akár hozzáadhatsz egy olyan kódot is, amellyel egy rövid szünetet vagy „szundit” (angolul `sleep`) tarthatsz a kép megjelenítése után. Ezzel egy kis időt hagysz az űrhajósok számára, hogy láthassák a képedet, mielőtt az üzeneted következő része megjelenik. A programod elejéhez add hozzá:

```python
from time import sleep
```

Majd az után a sor után, amelyik megjeleníti a képedet, gépeld be ezt egy két másodperces szünetért:

```python
sleep(2)
```

\--- /task \---

\--- task \---

Hozd létre a saját képedet vagy mintádat, hogy megmutathasd az űrhajósoknak!

\--- /task \---