## Mostra un'immagine

La matrice di LED dell’Astro Pi consente anche di visualizzare immagini. Forse volete che il vostro saluto agli astronauti includa un’immagine o un motivo, insieme ad un messaggio o al posto di un testo?

![Uno screenshot della finestra dell'emulatore che mostra l'Unità di volo e sulla matrice LED un'immagine dell'Unità di volo stessa](images/fu-pic.png)

--- task ---

Alla fine del programma, create delle variabili di colore per definire i colori con i quali potete disegnare la vostra immagine. Potete utilizzare tutti i colori che volete ma, in questo esempio, ci limiteremo a questi: rosso (`r`), bianco (`b`), nero (`x`) e due sfumature di grigio (`g` e `s`). Attenzione che le sfumature si ottengono riducendo la quantità di luce in tutti e tre i canali mantenendo le stesse proporzioni.

```python
w = (255, 255, 255)
b = (0, 0, 0)
g = (50,50,50)
s = (200,255,200)
r = (255,0,0)
```

**Nota:** In questo caso è una buona idea assegnare alle variabili di colore nomi abbreviati di una sola lettera per risparmiare tempo nella fase seguente, in cui dovrete scriverli ripetutamente molte volte. Inoltre, usando nomi di una sola lettera, diventa molto più facile vedere l’immagine disegnata.

--- /task ---

--- task ---



Sotto alle vostre nuove variabili, create una lista con 64 voci. Ciascuna voce rappresenta un pixel nella matrice di LED e corrisponde ad una delle variabili di colore che avete definito. Per disegnare l’immagine è sufficiente inserire una variabile nel punto in cui volete che appaia il colore ad essa assegnato. Abbiamo disegnato un Astro Pi utilizzando i pixel neri (`b`) come sfondo e i pixel grigi (`g`) per disegnare le parti metalliche per la sua "tuta spaziale":

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

Aggiungete una linea di codice per visualizzare il disegno sul display LED.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Premete **Run** (Esegui) per vedere come viene visualizzato il disegno.

--- /task ---

--- task ---

Se volete, potreste aggiungere del codice per introdurre una breve pausa (`sleep`) dopo la visualizzazione del disegno. Ciò consentirà agli astronauti di vedere il disegno prima che venga visualizzata la parte successiva del messaggio. All’inizio del programma, aggiungete:

```python
from time import sleep
```

Quindi, sulla riga successiva a quella che visualizza il disegno, aggiungete la seguente riga di codice per inserire un’attesa di due secondi:

```python
sleep(2)
```

--- /task ---

--- task ---

Adesso potete creare il vostro disegno o motivo grafico da mostrare agli astronauti!

--- /task ---
