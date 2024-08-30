## Leggi il colore

In questo passaggio, imposterai il sensore di luminosità del colore e lo utilizzerai per rilevare la quantità di rosso, verde e blu letta dal sensore. Questo colore verrà quindi utilizzato per colorare l'immagine scelta. Un astronauta che si avvicina al sensore con una maglietta blu vedrebbe un'immagine diversa rispetto a un astronauta con una maglietta rossa.

![immagine visualizzata con sfondo rosa sulla matrice LED](images/colour_background.png)

Qualunque sia l'immagine che hai scelto, lo sfondo utilizza la variabile `c` impostata sul nero.

--- task ---

Usa il sensore di colore per colorare il tuo sfondo.

Aggiungi il codice prima della lista contenente le immagini per ottenere il colore dal sensore e modifica la variabile del colore di sfondo `c` per utilizzare il colore rilevato dal sensore di colore Sense HAT, al posto del nero.

**Suggerimento:** Non è necessario digitare i commenti che iniziano con '#' (sono inseriti per spiegare il codice).

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 9, 10
---

# Aggiungi variabili per il colore e l'immagine

a = (255, 255, 255) # Bianco
c = (0, 0, 0) # Nero
f = (25, 25, 112) # Blu notte
m = (34, 139, 34) # Verde foresta

rgb = sense.color # ottenere il colore dal sensore
c = (rgb.red, rgb.green, rgb.blue) # usa il colore rilevato

immagine = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]


--- /code ---

--- /task ---

--- task ---

**Test:** Sposta il cursore del colore su un colore a tua scelta e poi **esegui** il tuo codice. Il colore dello sfondo cambierà. Ripeti questo test di nuovo con un colore differente.

**Suggerimento:** Dovrai fare clic su "Esegui" ogni volta che cambi il colore.

--- /task ---

## Ripeti il tuo programma

Il programma Astro Pi Mission Zero può funzionare per un massimo di 30 secondi. Utilizzerai questo tempo per controllare ripetutamente il sensore di colore e aggiornare l'immagine.

Il tuo codice utilizzerà un ciclo `for` per essere eseguito 28 volte. **Ogni** volta:
+ leggerà l'ultimo colore
+ aggiornerà il colore di sfondo dell'immagine
+ si fermerà per un secondo

--- task ---

**Trova** la tua riga di codice `rgb = sense.color`.

**Aggiungi** codice al di sopra per impostare il tuo ciclo `for` a `28` ripetizioni.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 2
---

for i in range(28):
rgb = sense.color # ottenere il colore dal sensore
c = (rgb.red, rgb.green, rgb.blue)

immagine = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

  
--- /code ---

--- /task ---

--- task ---

Ora devi indentare tutto il tuo codice sotto il ciclo `for` in modo che si trovi **dentro** il ciclo `for`.

**Suggerimento:** Per far rientrare più righe, evidenzia le righe che desideri indentare, quindi premi il tasto <kbd>Tab</kbd> sulla tastiera (di solito si trova sopra il tasto <kbd>Caps Lock</kbd> della tastiera).

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
---

for i in range(28):
  rgb = sense.color # ottenere il colore dal sensore
  c = (rgb.red, rgb.green, rgb.blue)

  immagine = [
    m, m, m, m, m, c, c, c,
    m, f, m, f, m, m, m, m,
    m, m, m, m, m, m, m, m,
    m, m, c, a, c, c, c, a,
    m, m, c, c, c ,c ,c ,c,
    m, m, c, c, c, a, c, c,
    m, m, m, m, m, m, m, m,
    m, m, m, m, m, m, m, m]

    
  # Mostra l'immagine

  sense.set_pixels(immagine)
 
--- /code ---

--- /task ---

--- task ---

Nella parte inferiore del codice, aggiungi uno `sleep` di un secondo all'interno del tuo ciclo:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 5
---
  
  # Mostra l'immagine

  sense.set_pixels(immagine)
  sleep(1)  
  
--- /code ---

**Suggerimento:** Assicurati che questa riga di codice sia indentata nel tuo ciclo `for`.

--- /task ---

--- task ---

**Test:** Esegui il tuo codice e cambia il selettore del colore più volte mentre il tuo progetto è in esecuzione. Verifica che l'immagine si aggiorni utilizzando il colore rilevato nell'esecuzione successiva.

L'immagine smetterà di aggiornarsi al termine del ciclo in modo che il programma non venga eseguito per più di 30 secondi.

--- /task ---

--- task ---

**Debug**

Il mio codice ha un errore di sintassi o non viene eseguito come previsto:

- Verifica che il tuo codice corrisponda al codice degli esempi precedenti
- Verifica di aver indentato il codice nel tuo ciclo `for`
- Verifica che la tua lista sia racchiusa tra `[` e `]`
- Verifica che ogni variabile di colore nell'elenco sia separata da una virgola

Il mio codice viene eseguito per più di 30 secondi:

- Riduci il numero di volte che il ciclo for viene eseguito, da 28 a 25 o anche 20.
- Riduci la durata della pausa sleep, da 1 secondo a 0,5 secondi.

--- /task ---

--- task ---

Aggiungi `sense.clear()` alla fine del tuo codice per cancellare l'immagine alla fine del tuo ciclo. Questo ti aiuterà a capire quando l'animazione termina.

**Suggerimento:** Assicurati di **non** indentare la riga di codice `sense.clear()` perché deve essere eseguita solo una volta alla fine dell'animazione.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 7
---
  
  # Mostra l'immagine

  sense.set_pixels(immagine)
  sleep(1) 
  
sense.clear()
  
--- /code ---

--- /task ---

--- task ---

**Test:** Esegui di nuovo il codice. Quando il tuo progetto ha terminato l'esecuzione, la matrice LED si pulirà, annerendo tutte le luci (luci spente).

--- /task ---

--- task ---

**Debug**

La matrice LED diventa nera ogni secondo:

- Verifica di non aver indentato il codice `sense.clear()` all'interno del tuo ciclo `for`

--- /task ---

--- task ---

Aggiungi il codice per colorare la matrice LED a tua scelta. Crea una variabile chiamata `x` per memorizzare il tuo nuovo colore.

Puoi mescolare il tuo colore o utilizzare i valori della lista dei colori per creare il tuo nuovo colore `x`.

[[[generic-theory-simple-colours]]]
[[[ambient-colours]]]

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 7, 8
---
  
  # Mostra l'immagine

  sense.set_pixels(immagine)
  sleep(1) 

x = (178, 34, 34)  # scegli i tuoi valori di rosso, verde e blu compresi tra 0 e 255
sense.clear(x)
  
--- /code ---


--- /task ---

--- task ---

**Test:** Esegui di nuovo il codice. Al termine dell'esecuzione del progetto, la matrice LED assumerà il colore scelto. Puoi cambiare e testare il colore tutte le volte che vuoi.

--- /task ---

--- task ---

--- collapse ---

---
title: Esempio di codice completato
---

![Una griglia con 8 x 8 quadrati che mostra un coccodrillo.](images/flower.png)

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

# Imposta il Sense HAT
sense.color.gain = 60 # Imposta la sensibilità del sensore
sense.color.integration_cycles = 64 # L'intervallo con cui verrà eseguita la lettura

# Aggiungi variabili per il colore e l'immagine

a = (255, 255, 255) # Bianco
c = (0, 0, 0) # Nero
f = (25, 25, 112) # Blu notte
m = (34, 139, 34) # Verde foresta

for i in range(28):
  rgb = sense.color # ottenere il colore dal sensore
  c = (rgb.red, rgb.green, rgb.blue)

  immagine = [
    m, m, m, m, m, c, c, c,
    m, f, m, f, m, m, m, m,
    m, m, m, m, m, m, m, m,
    m, m, c, a, c, c, c, a,
    m, m, c, c, c ,c ,c ,c,
    m, m, c, c, c, a, c, c,
    m, m, m, m, m, m, m, m,
    m, m, m, m, m, m, m, m]


  # Mostra l'immagine

  sense.set_pixels(immagine)
  sleep(1)

x = (178, 34, 34)  # scegli i tuoi valori di rosso, verde e blu compresi tra 0 e 255
sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
