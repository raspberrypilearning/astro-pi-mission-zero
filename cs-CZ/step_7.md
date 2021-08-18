## Zobraz vlhkost

Naměřenou vlhkost můžeš zkombinovat s obrázkem, tudíž ji můžeš naznačit graficky. Můžeš například nechat zobrazit oceán, když je vlhkost vysoká, a poušť, když je naopak nízká:

![Vlhko a sucho](images/wet-dry.png)

--- task ---

Na konci programu vytvoř ještě několik proměnných s takovými barvami, které budeš chtít použít při kreslení obrázků. Možná máš už některé z nich definované z předchozího kroku.

```python
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)
```

--- /task ---

--- task ---

Stejně jako minule – nakresli obrázky tak, že jim nejprve vytvoříš seznam a poté nastavíš položky seznamu na barvy, které mají jednotlivé pixely mít.

```python
vlhko = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


sucho = [
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

Přidej kód pro změření vlhkosti:

```python
vlhkost = sense.get_humidity()
```

--- /task ---

--- task ---

Teď se rozhodni, který obrázek se má zobrazit. V tomhle příkladu se obrázek `vlhko` zobrazí tehdy, jestliže je hodnota vlhkosti 40 % a výš, a pokud je naopak vlhkost nižší než 40 %, zobrazí se obrázek `sucho`.

```python
vlhkost = sense.get_humidity()
if vlhkost >= 40:
    sense.set_pixels(vlhko)
else:
    sense.set_pixels(sucho)
```

--- /task ---

--- task ---

Pomocí posuvníku vlhkosti nastav vlhkost na emulátoru. Spusť svůj program a zkontroluj, jestli se obrázek vybraný pro danou vlhkost správně zobrazí.

--- /task ---

--- task ---

Změňte kód tak, aby váš program ukazoval astronautům vlhkost tak, jak chcete vy.

--- /task ---

--- task --- Otestuj svůj kód s různými hodnotami vlhkosti (pomocí posuvníku) a ujisti se, že vždy správně funguje. Pokud postupuješ podle výše uvedeného příkladu, zobrazí se ti obrázek jak v případě, že je vlhkost nastavena na hodnotu nižší než 40 %, tak i v případě, že je nastavena na hodnotu vyšší než 40 %?

--- /task ---
