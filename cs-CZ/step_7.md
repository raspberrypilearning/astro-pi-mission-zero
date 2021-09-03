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

Stejně jako minule – nakresli obrázky tak, že nejprve vytvoříš seznam a poté nastavíš položky seznamu na barvy, které mají jednotlivé pixely mít.

```python
wet = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


dry = [
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
humid = sense.get_humidity()
```

--- /task ---

--- task ---

Teď se rozhodni, který obrázek se má zobrazit. V tomhle příkladu se obrázek `wet` zobrazí tehdy, jestliže je hodnota vlhkosti 40 % a výš, a pokud je naopak vlhkost nižší než 40 %, zobrazí se obrázek `dry`.

```python
humid = sense.get_humidity()
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

Pomocí posuvníku vlhkosti nastav vlhkost na emulátoru. Spusť svůj program a zkontroluj, jestli se obrázek určený pro danou hodnotu vlhkosti správně zobrazí.

--- /task ---

--- task ---

Změň svůj kód tak, aby program zobrazoval astronautům vlhkost tak, jak chceš ty.

--- /task ---

--- task --- Otestuj svůj kód s různými hodnotami vlhkosti (pomocí posuvníku) a ujisti se, že vždy správně funguje. Pokud postupuješ podle výše uvedeného příkladu, zobrazí se ti obrázek jak v případě, že je vlhkost nastavena na hodnotu nižší než 40 %, tak i v případě, že je nastavena na hodnotu vyšší než 40 %?

--- /task ---
