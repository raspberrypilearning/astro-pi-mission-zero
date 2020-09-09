## Zobrazit vlhkost

Naměřenou vlhkost můžete zkombinovat s obrázkem, kterým vlhkost naznačíte graficky. Můžete například zobrazit oceán pro vysokou vlhkost a poušť pro nízkou vlhkost:

![Mokrá a suchá](images/wet-dry.png)

--- task ---

Na konci programu vytvořte ještě několik proměnných s barvami, jaké budete chtít použít v obrázcích. Možná jste některé z nich definovali už v předchozím kroku.

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

Stejně jako předtím nakreslete obrázky tak, že pro každý z nich vytvoříte seznam a potom položky tohoto seznamu nastavíte na barvy, které mají mít jednotlivé pixely.

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

Přidejte kód pro získání vlhkosti:

```python
temp = sense.temperature
```

--- /task ---

--- task ---

Teď rozhodněte, který obrázek se zobrazí. V tomhle příkladu zobrazíme obrázek pro `wet` při naměřené vlhkosti 40% nebo vyšší a obrázek pro `dry`, když je vlhkost nižší než 40%.

```python
humid = sense.humidity
if humid &gt;= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

Pomocí posuvníku vlhkosti nastavte vlhkost na emulátoru. Spusťte svůj program a zkontrolujte, jestli se správně zobrazí obrázek vybraný pro danou vlhkost.

--- /task ---

--- task ---

Změňte kód tak, aby váš program ukazoval astronautům vlhkost tak, jak chcete vy.

--- /task ---