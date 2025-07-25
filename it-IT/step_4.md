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
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9, 10
---

# Aggiungi variabili di colore e immagine

a = (255, 255, 255) # Bianco c = (0, 0, 0) # Nero f = (25, 25, 112) # Blu notte m = (34, 139, 34) # Verde foresta

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


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
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


--- /code ---

--- /task ---

--- task ---

Ora devi indentare tutto il tuo codice sotto il ciclo `for` in modo che si trovi **dentro** il ciclo `for`.

**Suggerimento:** Per far rientrare più righe, evidenzia le righe che desideri indentare, quindi premi il tasto <kbd>Tab</kbd> sulla tastiera (di solito si trova sopra il tasto <kbd>Maiuscole/1> della tastiera). </p> 

<p spaces-before="0">
  --- code ---
</p>
<hr />

<p spaces-before="0">
  language: python filename: main.py line_numbers: false line_number_start: 1
</p>
<h2 spaces-before="0">
  line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
</h2>

<p spaces-before="0">
  for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)
</p>

<p spaces-before="2">
  image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]
</p>

<p spaces-before="2">
  # Display the image
</p>

<p spaces-before="2">
  sense.set_pixels(image)
</p>

<p spaces-before="0">
  --- /code ---
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Nella parte inferiore del codice, aggiungi uno <code>sleep</code> di un secondo all'interno del tuo ciclo:
</p>

<p spaces-before="0">
  --- code ---
</p>
<hr />

<p spaces-before="0">
  language: python filename: main.py line_numbers: false line_number_start: 1
</p>
<h2 spaces-before="0">
  line_highlights: 5
</h2>

<p spaces-before="2">
  # Display the image
</p>

<p spaces-before="2">
  sense.set_pixels(image) sleep(1)
</p>

<p spaces-before="0">
  --- /code ---
</p>

<p spaces-before="0">
  <strong x-id="1">Suggerimento:</strong> Assicurati che questa riga di codice sia indentata nel tuo ciclo <code>for</code>.
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  <strong x-id="1">Test:</strong> Esegui il tuo codice e cambia il selettore del colore più volte mentre il tuo progetto è in esecuzione. Verifica che l'immagine si aggiorni utilizzando il colore rilevato nell'esecuzione successiva.
</p>

<p spaces-before="0">
  L'immagine smetterà di aggiornarsi al termine del ciclo in modo che il programma non venga eseguito per più di 30 secondi.
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  <strong x-id="1">Debug</strong>
</p>

<p spaces-before="0">
  Il mio codice ha un errore di sintassi o non viene eseguito come previsto:
</p>

<ul>
  <li>
    Verifica che il tuo codice corrisponda al codice degli esempi precedenti
  </li>
  <li>
    Verifica di aver indentato il codice nel tuo ciclo <code>for</code>
  </li>
  <li>
    Verifica che la tua lista sia racchiusa tra <code>[</code> e <code>]</code>
  </li>
  <li>
    Verifica che ogni variabile di colore nell'elenco sia separata da una virgola
  </li>
</ul>

<p spaces-before="0">
  Il mio codice viene eseguito per più di 30 secondi:
</p>

<ul>
  <li>
    Riduci il numero di volte che il ciclo for viene eseguito, da 28 a 25 o anche 20.
  </li>
  <li>
    Riduci la durata della pausa sleep, da 1 secondo a 0.5 secondi.
  </li>
</ul>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Aggiungi <code>sense.clear()</code> alla fine del tuo codice per cancellare l'immagine alla fine del tuo ciclo. Questo ti aiuterà a capire quando l'animazione termina.
</p>

<p spaces-before="0">
  <strong x-id="1">Suggerimento:</strong> Assicurati di <strong x-id="1">non</strong> indentare la riga di codice <code>sense.clear()</code> perché deve essere eseguita solo una volta alla fine dell'animazione.
</p>

<p spaces-before="0">
  --- code ---
</p>
<hr />

<p spaces-before="0">
  language: python filename: main.py line_numbers: false line_number_start: 1
</p>
<h2 spaces-before="0">
  line_highlights: 7
</h2>

<p spaces-before="2">
  # Display the image
</p>

<p spaces-before="2">
  sense.set_pixels(image) sleep(1)
</p>

<p spaces-before="0">
  sense.clear()
</p>

<p spaces-before="0">
  --- /code ---
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  <strong x-id="1">Test:</strong> Esegui di nuovo il codice. Quando il tuo progetto ha terminato l'esecuzione, la matrice LED si pulirà, annerendo tutte le luci (luci spente).
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  <strong x-id="1">Debug</strong>
</p>

<p spaces-before="0">
  La matrice LED diventa nera ogni secondo:
</p>

<ul>
  <li>
    Verifica di non aver indentato il codice <code>sense.clear()</code> all'interno del tuo ciclo <code>for</code>
  </li>
</ul>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Aggiungi il codice per colorare la matrice LED a tua scelta. Crea una variabile chiamata <code>x</code> per memorizzare il tuo nuovo colore.
</p>

<p spaces-before="0">
  Puoi mescolare il tuo colore o utilizzare i valori della lista dei colori per creare il tuo nuovo colore <code>x</code>.
</p>

<p spaces-before="0">
  [[[generic-theory-simple-colours]]] [[[ambient-colours]]]
</p>

<p spaces-before="0">
  --- code ---
</p>
<hr />

<p spaces-before="0">
  language: python filename: main.py line_numbers: false line_number_start: 1
</p>
<h2 spaces-before="0">
  line_highlights: 7, 8
</h2>

<p spaces-before="2">
  # Display the image
</p>

<p spaces-before="2">
  sense.set_pixels(image) sleep(1)
</p>

<p spaces-before="0">
  x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)
</p>

<p spaces-before="0">
  --- /code ---
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  <strong x-id="1">Test:</strong> Esegui di nuovo il codice. Al termine dell'esecuzione del progetto, la matrice LED assumerà il colore scelto. Puoi cambiare e testare il colore tutte le volte che vuoi.
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  <strong x-id="1">Salva i tuoi progressi</strong>
</p>

<p spaces-before="0">
  Puoi salvare il tuo programma sul progetto Mission Starter inserendo il nome della tua squadra, i nomi dei membri del team e il codice classe che ti è stato comunicato. È possibile ricaricare il programma su qualsiasi dispositivo con una connessione internet inserendo il nome del team e il codice aula.
</p>

<p spaces-before="0">
  <img src="images/mz_savebutton_v2.png" alt="Mission Zero Save button screengrab" />
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  --- collapse ---
</p>

<hr />
<h2 spaces-before="0">
  title: Esempio di codice completato
</h2>

<p spaces-before="0">
  <img src="images/fish.png" alt="A grid with 8 x 8 squares showing a fish." />
</p>

<p spaces-before="0">
  --- code ---
</p>
<hr />

<p spaces-before="0">
  language: python filename: main.py
</p>
<h2 spaces-before="0">
  line_numbers: false
</h2>
<h1 spaces-before="0">
  Importare le librerie
</h1>

<p spaces-before="0">
  from sense_hat import SenseHat from time import sleep
</p>

<h1 spaces-before="0">
  Imposta il Sense HAT
</h1>

<p spaces-before="0">
  sense = SenseHat() sense.set_rotation(270)
</p>

<h1 spaces-before="0">
  Configura il sensore di colore
</h1>

<p spaces-before="0">
  sense.color.gain = 60 # Imposta la sensibilità del sensore sense.color.integration_cycles = 64 # L'intervallo a cui verrà eseguita la lettura
</p>

<h1 spaces-before="0">
  Aggiungi variabili di colore e immagine
</h1>

<p spaces-before="0">
  a = (255, 255, 255) # Bianco c = (0, 0, 0) # Nero f = (25, 25, 112) # Blu notte m = (34, 139, 34) # Verde foresta
</p>

<p spaces-before="0">
  for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)
</p>

<p spaces-before="2">
  image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]
</p>

<p spaces-before="2">
  # Visualizza l'immagine
</p>

<p spaces-before="2">
  sense.set_pixels(image) sleep(1)
</p>

<p spaces-before="0">
  x = (178, 34, 34)  # scegli i tuoi valori di rosso, verde e blu compresi tra 0 e 255 sense.clear(x)
</p>

<p spaces-before="0">
  --- /code ---
</p>

<p spaces-before="0">
  --- /collapse ---
</p>

<p spaces-before="0">
  --- /task ---
</p>
