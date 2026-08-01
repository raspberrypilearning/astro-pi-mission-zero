## Leggi il colore

In questo passaggio configurerai il sensore di colore e luminosità. Utilizzerai questo sensore per misurare la quantità di luce rossa, verde e blu che raggiunge il sensore. Questi valori verranno quindi utilizzati per modificare uno dei colori nell'immagine scelta.

Ciò significa che l'immagine può cambiare a seconda di ciò che vede il sensore. Ad esempio, un astronauta che indossa una maglietta blu vedrebbe una versione diversa dell'immagine rispetto a un astronauta che indossa una maglietta rossa.

Nell'immagine della balena utilizzata nel passaggio precedente, il colore di sfondo era nero. Abbiamo utilizzato la variabile `c` per memorizzare il suo codice colore RGB:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Usa il sensore di colore per cambiare uno dei tuoi colori.

Sotto le righe in cui definisci i colori, aggiungi il seguente codice:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

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


**Aggiungi** una seconda immagine proprio sotto la riga di codice `sense.set_pixels(image)`. Assegnagli il nome della variabile `image2` e modifica alcuni pixel per rendere diverso il fotogramma dell'animazione. Quindi aggiungi una breve pausa subito dopo.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# Extra images / frames go here:

image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

Nella parte inferiore del file di codice, imposta il ciclo `for` in modo che si ripeta `14` volte e alterni la visualizzazione di `image` e `image2` facendo una pausa per 1 secondo su ciascun fotogramma.

**Suggerimento:** assicurati che le righe di codice sotto `for i in range(14):` siano rientrate con uno spazio in modo che si trovino **all'interno** del blocco loop.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1)

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
- Assicurati di aver chiamato la tua seconda matrice immagine `image2` e che sia posizionata all'esterno e prima dell'inizio del ciclo.
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
language: python filename: main.py
line_numbers: false
---
# Import the libraries
from sense_hat import SenseHat from time import sleep

# Set up the Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image
a = (255, 255, 255) # White c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Esempio di codice Whale completato (con animazione)
---

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Import the libraries
from sense_hat import SenseHat from time import sleep

# Set up the Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image
a = (255, 255, 255) # White c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1)

--- /code ---

--- /collapse ---

--- /task ---
