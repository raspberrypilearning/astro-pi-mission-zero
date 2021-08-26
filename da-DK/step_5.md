## Vis et billede

Du kan vise billeder på Astro Pi'ens LED-matrix. Måske kunne din hilsen til astronauterne indeholde et billede eller et mønster sammen med, eller i stedet for, en skriftlig besked?

![Et skærmbillede af emulatorvinduet, der viser Flight Unit'en med LED-matricen, der viser et billede af selve Flight Unit'en](images/fu-pic.png)

--- task ---

I bunden af dit program skal du oprette nogle farvevariabler til at definere de farver, som du ønsker at tegne dit billede med. Du kan bruge så mange farver, som du vil, men i dette eksempel bruger vi kun få farver - rød (`r`), hvid (`w`), sort (`b`) og to gråtoner (`g` og `s`). Bemærk, at nuancerne opnås ved at reducere mængden af lys i alle tre kanaler, samtidig med at proportionerne beholdes.

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Bemærk:** Denne gang er det en god idé at give farvevariablerne enkeltbogstaver som navne, fordi det kommer til at spare dig tid i det næste trin, hvor du skal skrive dem mange gange. Desuden bliver det lettere at se det billede, du vil tegne, hvis du anvender enkeltbogstaver.

--- /task ---

--- task ---



Under dine nye variabler skal du oprette en liste med 64 elementer. Hvert element repræsenterer en pixel på LED-matricen og svarer til én af de farvevariabler, du definerede. Tegn dit billede ved at sætte en variabel dér, hvor du ønsker, at dens tildelte farve skal vises. Vi har tegnet en Astro Pi ved at anvende sorte (`b`) pixels som baggrund og grå (`w`) pixels til at tegne den metaldele:

```python
 billede = [
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

Tilføj en kodelinje for at vise dit billede på LED-displayet.

```python
sense.set_pixels(billede)
```

--- /task ---

--- task ---

Tryk på **Run** (Kør) for at få dit billede vist.

--- /task ---

--- task ---

Det kan være, du vil tilføje noget kode for at lave en kort pause (eller `sleep` (dvale)) efter visning af billedet. På den måde får astronauterne tid til at se dit billede, før næste del af din besked vises. Øverst i dit program skal du tilføje:

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
