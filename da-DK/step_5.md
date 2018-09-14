## Vis et billede

Du kan vise billeder på LED-matrix på Astro Pi. Måske kunne din hilsen til astronauterne indeholde et billede eller et mønster sammen med eller i stedet for en skriftlig besked?

![Astronaut](images/astronaut-pic.png)

--- task ---

I bunden af dit program skal du oprette nogle farvevariabler til at definere de farver, som du ønsker at tegne dit billede med. Du kan anvende ligeså mange farver, du har lyst til, men i dette eksempel holder vi os til kun to — hvid (`w`) og sort (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Bemærk:** Denne gang er det en god idé at give farverne enkeltbogstaver som navne, fordi det kommer til at spare dig tid i det næste trin, hvor du skal skrive dem mange gange. Desuden bliver det lettere at se det billede, du vil tegne, hvis du anvender enkeltbogstaver.

--- /task ---

--- task ---

Under dine nye variabler skal du oprette en liste med 64 elementer. Hvert element repræsenterer en pixel på LED-matrix og svarer til én af de farvevariabler, du definerede. Tegn dit billede ved at sætte en variabel dér, hvor du ønsker, at dens tildelte farve vises. Vi har tegnet en astronaut ved at anvende sorte (`b`) pixels som baggrund og hvide (`w`) pixels til at tegne astronautens rumdragt:

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

Tilføj en kodelinje for at vise dit billede på LED-displayet.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Tryk på **Run** (Kør) for at se dit billede vist.

--- /task ---

--- task ---

Det kan være, du vil tilføje en kode for at lave en kort ventetid (eller `sleep` (dvale)) efter visning af billedet. På den måde får astronauterne tid til at se dit billede, før næste del af din besked vises. Øverst i dit program skal du tilføje:

```python
from time import sleep
```

Dernæst på linjen efter den, der viser dit billede, skal du tilføje denne kode for at vente i to sekunder:

```python
sleep(2)
```

--- /task ---

--- task ---

Lav dit eget billede eller mønster, du kan vise til astronauterne!

--- /task ---