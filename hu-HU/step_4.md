## Adj hozzá egy kis színt!

Az Astro Pi LED-jei színeket is meg tudnak jeleníteni. Egy színt egy változó létrehozásával, majd egy RGB színérték hozzárendelésével határozhatsz meg.

Itt megtanulhatod, hogyan hozhatsz létre bármilyen színt a vörös, a zöld és a kék különböző arányainak használatával:

[[[generic-theory-colours]]]

--- task ---

Válassz ki egy színt, és keresd ki annak a színnek az RGB értékét. Egy [színválasztót](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} is segítségül hívhatsz.

--- /task ---

--- task ---

Hozz létre egy változót a válaszott színed tárolására. Például, ha a vöröset választottad volna, ezt a kódsort írnád:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

Mást már meg tudod jeleníteni az üzeneteted az általad választott színben! Utasítsd a programot, hogy az általad létrehozott színben jelenítse meg az üzenetedet a `text_colour` paraméter hozzádásával:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /task ---

![színes üzenetek megjelenítése](images/show-message-color.gif)

--- task ---

Még a kijelző háttérszínét is megváltoztathatod. Válassz ki egy másik színt, és hozz létre még egy változót annak a színnek a tárolásához. Utasítsd a programot, hogy az általad választott háttérszínt használja, add a `back_colour` paramétert a kódodhoz:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Változtasd meg az üdvözlő szöveget és a színt — milyen üzenetet küldesz majd a Nemzetközi Űrállomás űrhajósainak?

--- /task ---