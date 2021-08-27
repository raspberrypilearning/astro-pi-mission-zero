## Adaugă culoare

LED-urile Astro Pi pot afișa și culori. Poți specifica o culoare creând o variabilă și atribuindu-i o valoare de culoare RGB.

Poți afla cum pot fi create toate culorile folosind diferite proporții de roșu, verde și albastru aici:

[[[generic-theory-colours]]]

--- task ---

Alege o culoare și află valoarea RGB a culorii. Ai putea folosi un [selector de culoare](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} pentru a te ajuta.

--- /task ---

--- task ---

Creează o variabilă pentru a stoca culoarea aleasă. De exemplu, dacă ai selecta roșu, ai scrie această linie de cod:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

Acum poți afișa textul tău în culoarea dorită! Pentru a spune programului să utilizeze culoarea pe care ai creat-o, adaugă un parametru `text_colour` la codul care afișează textul tău:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /task ---

![Emulatorul Trinket Sense HAT care rulează un program de probă care derulează textul \"Astro Pi\" prin matricea LED folosind litere roșii](images/M0_2.gif)

--- task ---

De asemenea, poți schimba culoarea de fundal a afișajului. Alege o altă culoare și creează o altă variabilă pentru a stoca acea culoare. Pentru a spune programului să utilizeze culoarea de fundal aleasă, adaugă parametrul `back_colour` la codul tău:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Modifică textul de salut și culoarea — ce mesaj vei trimite astronauților de la bordul ISS?

--- /task ---
