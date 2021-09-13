## Zobraz obrázek

Na LED matici Astro Pi můžeš zobrazovat obrázky. Co kdyby tvůj pozdrav astronautům obsahoval kromě psané zprávy i obrázek nebo vzor?

![Snímek obrazovky emulátoru, který zobrazuje letovou jednotku s LED maticí zobrazující obrázek samotné letové jednotky](images/fu-pic.png)

--- task ---

Na konci svého programu vytvoř nové proměnné s barvami a definuj tak barvy, které chceš při kreslení svého obrázku použít. Můžeš použít libovolný počet barev, ale v tomhle příkladu použijeme pouze několik barev: červenou (`r`), bílou (`w`), černou (`b`) a dva odstíny šedé (`g` a `s`). Všimni si, že tyto odstíny dostaneme snížením množství světla ve všech třech kanálech a přitom máme stále stejné poměry.

```python
w = (255, 255, 255)
b = (0, 0, 0)
g = (50,50,50)
s = (200,255,200)
r = (255,0,0)
```

**Poznámka:** V tomhle případě se hodí dát všem proměnným s barvami jednopísmenné názvy, protože to ušetří čas v dalším kroku, kdy je budeš mnohokrát vypisovat. A kromě toho s jednopísmennými proměnnými lépe uvidíš obrázek, který právě kreslíš.

--- /task ---

--- task ---

Pod novými proměnnými vytvoř seznam s 64 položkami. Každá položka představuje jeden pixel na LED matici a odpovídá jedné z proměnných s barvami, které už máš definované. Svůj obrázek nakreslíš tak, že umístíš proměnnou tam, kde se má objevit barva, která jí byla přiřazena. Nakreslili jsme Astro Pi tak, že černé (`b`) pixely tvoří pozadí, kdežto šedými (`g`) pixely jsme nakreslili kovové části jeho letového pouzdra:

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

Přidej řádek kódu, kterým svůj obrázek zobrazíš na LED displeji.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Podívej se na svůj obrázek stisknutím tlačítka **Run** (spustit).

--- /task ---

--- task ---

Možná budeš chtít přidat kód, který po zobrazení obrázku bude chvilku čekat (neboli `sleep`). Astronauti si tak stihnou prohlédnout tvůj obrázek dřív, než se objeví další část tvé zprávy. Na začátek svého programu přidej:

```python
from time import sleep
```

Potom pod řádek, jenž zobrazuje tvůj obrázek, přidej tenhle kód, který bude čekat dvě sekundy:

```python
sleep(2)
```

--- /task ---

--- task ---

Vytvoř si vlastní obrázek nebo vzor, který chceš astronautům ukázat!

--- /task ---
