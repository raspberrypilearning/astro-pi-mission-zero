## Leggi il colore

In questo passaggio configurerai il sensore di colore e luminosità. Utilizzerai questo sensore per misurare la quantità di luce rossa, verde e blu che raggiunge il sensore. Questi valori verranno quindi utilizzati per modificare uno dei colori nell'immagine scelta.

Ciò significa che l'immagine può cambiare a seconda di ciò che vede il sensore. Ad esempio, un astronauta che indossa una maglietta blu vedrebbe una versione diversa dell'immagine rispetto a un astronauta che indossa una maglietta rossa.

Nell'immagine della balena utilizzata nel passaggio precedente, il colore di sfondo era nero. Abbiamo utilizzato la variabile `c` per memorizzare il suo codice colore RGB:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Usa il sensore di colore per cambiare uno dei tuoi colori.

Sotto le righe in cui definisci i colori, aggiungi il seguente codice:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4
---
# Leggi un colore
rgb = sense.color # ottenere il colore dal sensore
c = (rgb.red, rgb.green, rgb.blue) # usa il colore rilevato

--- /code ---

--- /task ---

Questo codice sostituisce i valori RGB memorizzati in `c` con i valori del colore rilevato dal sensore.

Suggerimento: se non hai utilizzato la variabile `c` nella tua immagine, sostituisci `c` con una delle variabili di colore che hai utilizzato. Ciò consentirà invece al sensore di cambiare quel colore.

--- task ---

**Test:** Sposta il cursore del colore su un colore a tua scelta e poi **esegui** il tuo codice. Il colore dello sfondo cambierà. Ripeti questo test di nuovo con un colore differente.

**Suggerimento:** Dovrai fare clic su "Run (esegui)" ogni volta che cambi il colore.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Ora che hai visualizzato un'immagine, rilevato un colore e utilizzato nel tuo programma, il tuo codice è pronto per l'invio! 

Puoi salvare e inviare il tuo programma utilizzando il modulo nella parte inferiore dell'editor di codice.
  
Tuttavia, potresti voler aggiungere più immagini al tuo progetto o dargli vita con un'animazione. I passaggi successivi mostrano come eseguire questa operazione.
</p>

## Anima il tuo progetto (facoltativo)

Il tuo programma Mission Zero può essere eseguito sulla Stazione Spaziale Internazionale (ISS) per un massimo di 30 secondi. È possibile utilizzare questo tempo di esecuzione per visualizzare un'animazione sulla matrice LED passando da due o più immagini diverse.

--- task ---


**Aggiungi** una seconda immagine proprio sotto la riga di codice `sense.set_pixels(immagine)`. Assegnagli il nome della variabile `immagine2` e modifica alcuni pixel per rendere diverso il fotogramma dell'animazione. Quindi aggiungi una breve pausa subito dopo.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
immagine = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(immagine)

# Immagini/cornici extra vanno qui:

immagine2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

Nella parte inferiore del file di codice, imposta il ciclo `for` in modo che si ripeta `14` volte e alterni la visualizzazione di `immagine` e `immagine2` facendo una pausa per 1 secondo su ciascun fotogramma.

**Suggerimento:** assicurati che le righe di codice sotto `for i in range(14):` siano rientrate con uno spazio in modo che si trovino **all'interno** del blocco loop.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
immagine2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Ripeti 14 volte (14 * 2 secondi = 28 secondi di animazione totale)
for i in range(14):
  # Visualizza la seconda immagine
  sense.set_pixels(immagine2)
  sleep(1)

  # Visualizza la prima immagine
  sense.set_pixels(immagine)
  sleep(1)
  
--- /code ---

--- /task ---

--- task ---

**Test:** Esegui di nuovo il codice. Il tuo programma visualizzerà immediatamente il colore rilevato, quindi andrà avanti e indietro per eseguire un'animazione.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Se desideri avere più di due fotogrammi nella tua animazione, devi assicurarti che il programma venga eseguito per non più di 30 secondi. Ad esempio, se hai 10 immagini visualizzate ciascuna per 1 secondo, devi modificare il ciclo "for" in modo che si ripeta 3 volte (10 * 3 = 30 secondi)
</p>

--- task ---

**Verifica la presenza di errori**

Il mio codice ha un errore di sintassi o non cambia frame:
- Controlla che il codice del ciclo `for` corrisponda al rientro nell'esempio.
- Assicurati di aver chiamato la tua seconda matrice immagine `immagine2` e che sia posizionata all'esterno e prima dell'inizio del ciclo.
- Controlla che i tuoi tempi di `sleep` siano impostati esattamente su `1` secondo per evitare di superare il rigido limite di esecuzione di 30 secondi sulla ISS.

--- /task ---

--- task ---

**Salva i tuoi progressi**

Puoi salvare il tuo programma sul progetto Mission Starter inserendo il nome della tua squadra, i nomi dei membri del team e il codice classe che ti è stato comunicato. È possibile ricaricare il programma su qualsiasi dispositivo con una connessione internet inserendo il nome del team e il codice aula.

--- /task ---

--- task ---

--- collapse ---
---
title: Esempio di codice Whale completato
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importa le librerie
from sense_hat import SenseHat
from time import sleep

# Imposta il Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Imposta il sensore di colore
sense.color.gain = 60 # Imposta la sensibilità del sensore
sense.color.integration_cycles = 64 # L'intervallo con cui verrà eseguita la lettura

# Aggiungi variabili per il colore e l'immagine
a = (255, 255, 255) # Bianco
c = (0, 0, 0)       # Nero
f = (36, 128, 200)  # Blu oceano
g = (0, 204, 255)   # Cielo blu

# Leggi un colore
rgb = sense.color # ottenere il colore dal sensore
c = (rgb.red, rgb.green, rgb.blue)

immagine = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(immagine)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Esempio di codice Whale completato (con animazione)
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importa le librerie
from sense_hat import SenseHat
from time import sleep

# Imposta il Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Imposta il sensore di colore
sense.color.gain = 60 # Imposta la sensibilità del sensore
sense.color.integration_cycles = 64 # L'intervallo con cui verrà eseguita la lettura

# Aggiungi variabili per il colore e l'immagine
a = (255, 255, 255) # Bianco
c = (0, 0, 0)       # Nero
f = (36, 128, 200)  # Blu oceano
g = (0, 204, 255)   # Cielo blu

# Leggi un colore
rgb = sense.color # ottenere il colore dal sensore
c = (rgb.red, rgb.green, rgb.blue)

immagine = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(immagine)

# L'INVIO DI BASE è ormai terminato

# Immagini/cornici extra vanno qui:
immagine2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Ripeti 14 volte (14 * 2 secondi = 28 secondi di animazione totale)
for i in range(14):
  # Visualizza la seconda immagine
  sense.set_pixels(immagine2)
  sleep(1)

  # Visualizza la prima immagine
  sense.set_pixels(immagine)
  sleep(1)
  
--- /code ---

--- /collapse ---

--- /task ---

