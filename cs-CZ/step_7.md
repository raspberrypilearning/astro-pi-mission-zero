## Zobrazte teplotu

Naměřenou teplotu můžete zkombinovat s obrázkem, kterým teplotu naznačíte graficky. Například sněhovou vánicí můžete naznačit zimu, obrázkem slunečného dne teplo:

![Teplo a zima](images/hot-and-cold.png)

\--- task \---

Na konci programu vytvořte ještě několik proměnných s barvami, jaké budete chtít použít v obrázcích. Možná jste některé z nich definovali už v předchozím kroku. V našich příkladech budeme používat bílou (`w`), žlutou (`y`), zelenou (`g`) a černou/bezbarvou (`b`).

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Stejně jako předtím nakreslete obrázky tak, že pro každý z nich vytvoříte seznam a potom položky tohoto seznamu nastavíte na barvy, které mají mít jednotlivé pixely.

```python
hot = [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g
]


cold = [
  b, b, w, b, b, b, w, b,
  b, b, b, b, b, w, b, b,
  b, w, b, b, b, b, b, w,
  b, b, b, b, w, b, b, b,
  w, b, b, w, b, b, w, b,
  b, b, b, b, b, b, b, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w
]
```

\--- /task \---

\--- task \---

Přidejte kód pro získání teploty:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Teď rozhodněte, který obrázek se zobrazí. V tomhle příkladu zobrazíme obrázek pro `hot` (teplo) při naměřené teplotě 20 stupňů nebo vyšší a obrázek pro `cold` (zima), když je teplota nižší než 20 stupňů.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /task \---

\--- task \---

Pomocí posuvníku teploty nastavte teplotu na emulátoru. Spusťte svůj program a zkontrolujte, jestli se správně zobrazí obrázek vybraný pro danou teplotu.

\--- /task \---

\--- task \---

Změňte kód tak, aby váš program ukazoval astronautům teplotu tak, jak chcete vy.

\--- /task \---