## Zobrazte obrázek

Na LED matici Astra Pi můžete zobrazovat obrázky. Co kdyby váš pozdrav astronautům obsahoval, kromě nebo místo psané zprávy, i obrázek nebo vzor?

![Astronaut](images/astronaut-pic.png)

--- task ---

Na konec programu přidejte nové řádky a na nich si vytvořte nové proměnné s definicemi barev, které budete chtít používat při kreslení svého obrázku. Můžete použít kolik barev budete chtít, ale v našem příkladu zůstaneme u dvou — u černé (`w`) a bílé (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Poznámka:** V tomhle případě se hodí dát proměnným s barvami jednopísmenná jména, protože to ušetří čas v dalším kroku, kde je budeme psát hodněkrát dokola. A kromě toho s jednopísmennými proměnnými lépe uvidíte obrázek, který kreslíte.

--- /task ---

--- task ---

Pod novými proměnnými udělejte seznam s 64 položkami. Každá položka představuje jeden pixel na LED matici a odpovídá jedné z proměnných s barvami, které jste si definovali. Obrázek nakreslíte tak, že proměnnou dáte tam, kde chcete, aby se objevila jí přiřazená barva. Nakreslili jsme astronauta tak, že černé pixely (`b`) tvoří pozadí a bílými pixely (`w`) jsme nakreslili astronautův skafandr:

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

--- /task ---

--- task ---

Přidejte řádek kódu, kterým obrázek zobrazíte na LED displeji.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Podívejte se na svůj obrázek stisknutím tlačítka **Run** (Spustit).

--- /task ---

--- task ---

Možná budete chtít po zobrazení obrázku přidat kus kódu, který vyvolá krátké čekání (říká se mu `sleep` (spánek)). Tak dáte astronautům čas, aby si obrázek prohlédli, než se objeví další část vaší zprávy. Na začátek programu přidejte:

```python
from time import sleep
```

Potom na řádek hned po řádku zobrazujícím obrázek přidejte tento kód, který znamená dvouvteřinové čekání:

```python
sleep(2)
```

--- /task ---

--- task ---

Vytvořte si svůj vlastní obrázek nebo vzor, který chcete astronautům zobrazit!

--- /task ---