## Vis en besked

--- opgave ---

Åbn [Sense HAT-emulatoren](https://trinket.io/mission-zero){:target="_blank"} til Mission Zero-projektet.

Her kan du se, at der automatisk er blevet tilføjet tre linjer kode for dig:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![sense hat-emulator](images/sense-hat-emulator2.png)

Denne kode opretter forbindelse til Astro Pi og sørger for, at LED-displayet på Astro Pi vises på korrekt vis. Lad koden stå, for du får brug for den.

--- /opgave ---

--- opgave ---

Måske kunne du efterlade en hyggelig hilsen til de astronauter på ISS, der arbejder i nærheden af Astro Pi? Lad os rulle (scrolle) en besked hen over displayet.

Tilføj denne linje under den anden kode:

```python
sense.show_message("Astro Pi")
```

--- /opgave ---

--- opgave ---

Tryk på knappen **Run** (Kør) og kig på, mens beskeden `Astro Pi` ruller hen over LED-displayet.

![vis kode for besked, klik på kør](images/show-message-code-annotated.PNG)

--- /opgave ---

![Rullende besked](images/scroll-message.gif)

For at få vist en anden besked kan du skrive præcist, hvad du ønsker mellem anførselstegnene (`""`).

--- kollaps ---

---
title: Hvilke tegn kan bruges?
---

Sense HAT kan kun vise tegnsættet Latin 1, hvilket betyder, at kun følgende tegn er tilgængelige. Øvrige tegn vises som `?`.

```
+-*/! "#$><0123456789. =) (

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;: |@%[&_ '] \ ~
```

--- /kollaps ---

--- opgave ---

Du kan også ændre den hastighed, som beskeden ruller med hen over displayet med. Tilføj en `scroll_speed` (Rullehastighed) til den kodelinje, du allerede har, som følger:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Beskedens standardhastighed er `0.1`. Hvis du gør talværdien mindre, ruller beskeden hurtigere, og hvis du gør talværdien større, ruller beskeden langsommere.

--- /opgave ---

### Vælg et navn til de nye Astro Pi -computere

--- opgave --- Hvis du gerne vil deltage i konkurrencen om at vælge navnene på de nye Mark II Astro Pi-computere, skal du starte din besked med ordene "Mit navn skal være" og derefter tilføje dit valg fra denne liste.

Hvis du f.eks. vil stemme på Ada Lovelace, ser din kode således ud:

```python
sense.show_message ("Mit navn skal være Ada Lovelace")
```
--- /opgave ---



