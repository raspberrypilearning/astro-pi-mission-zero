## Vis et billede

Du kan vise billeder på Astro Pi'ens LED-matrix. Måske kunne din hilsen til astronauterne indeholde et billede eller et mønster sammen med, eller i stedet for, en skriftlig besked?

![A screenshot of the emulator window showing the Flight Unit with the LED matrix displaying a picture of the Flight Unit itself](images/fu-pic.png)

--- opgave ---

I bunden af dit program skal du oprette nogle farvevariabler til at definere de farver, som du ønsker at tegne dit billede med. Du kan bruge så mange farver, som du vil, men i dette eksempel bruger vi kun få farver - rød (`r`), hvid (`w`), sort (`b`) og to gråtoner (`g` og `s`). Bemærk, at nuancerne opnås ved at reducere mængden af lys i alle tre kanaler, samtidig med at proportionerne beholdes.

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Note:** This time, it's a good idea to give the colour variables single-letter names, because that will save time in the next step, where you are going to be typing them out many times. Moreover, using single letters will make it easier to see the picture you'll draw.

--- /task ---

--- task ---



Below your new variables, create a list of 64 items. Each item represents one pixel on the LED matrix, and corresponds to one of the colour variables you defined. Draw your picture by putting a variable where you want its assigned colour to appear. We have drawn an Astro Pi by using the black (`b`) pixels as the background and the grey (`g`) pixels to draw the metal parts of the Astro Pi flight case:

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

Tryk på **Run** (Kør) for at få dit billede vist.

--- /task ---

--- task ---

You might want to add some code to include a short wait (or `sleep`) after the picture is displayed. This will give the astronauts time to see your picture before the next part of your message appears. At the top of your program, add:

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
