## Leggi il colore

In this step, you will set up the colour and brightness sensor. In questo passaggio, imposterai il sensore di luminosità del colore e lo utilizzerai per rilevare la quantità di rosso, verde e blu letta dal sensore. Questo colore verrà quindi utilizzato per colorare l'immagine scelta.

This means that the image can change depending on what the sensor sees. Un astronauta che si avvicina al sensore con una maglietta blu vedrebbe un'immagine diversa rispetto a un astronauta con una maglietta rossa.

In the whale image we used in the previous step, the background colour was black. We used the variable `c` to store its RGB colour code:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0) --- /code ---


--- task ---

Usa il sensore di colore per colorare il tuo sfondo.

Underneath the lines where you define the colours, add the following code:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---
# Sense a colour
rgb = sense.color # ottenere il colore dal sensore c = (rgb.red, rgb.green, rgb.blue) # usa il colore rilevato

This code replaces the RGB values stored in `c` with the values for the colour detected by the sensor.

Tip: If you didn't use the variable `c` in your own image, replace `c` with one of the colour variables that you did use. This will allow the sensor to change that colour instead.

--- task ---

**Test:** Sposta il cursore del colore su un colore a tua scelta e poi **esegui** il tuo codice. Il colore dello sfondo cambierà. Ripeti questo test di nuovo con un colore differente.

**Suggerimento:** Dovrai fare clic su "Run (esegui)" ogni volta che cambi il colore.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Now you have displayed an image and sensed a colour and used it in your program, and your code is ready for submission! 

You can save and submit your program using the form at the bottom of the code editor.
  
However, you may wish to add more images to your project, or make it come to life with animation. The next steps show you how to do this.
</p>

## Animate your project (optional)

Il programma Astro Pi Mission Zero può funzionare per un massimo di 30 secondi. Utilizzerai questo tempo per controllare ripetutamente il sensore di colore e aggiornare l'immagine.

--- task ---


**Trova** la tua riga di codice `rgb = sense.color`. Give it the variable name `image2` and change a few pixels to make your animation frame look different. Then add a short pause after it.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
---
immagine = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

sense.set_pixels(image)

# Extra images / frames go here:

immagine = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /code ---

--- /task ---

--- task ---

At the very bottom of your code file, set up your `for` loop to repeat `14` times and alternate between displaying `image` and `image2` pausing for 1 second on each frame.

**Suggerimento:** Per far rientrare più righe, evidenzia le righe che desideri indentare, quindi premi il tasto <kbd>Tab</kbd> sulla tastiera (di solito si trova sopra il tasto <kbd>Maiuscole</kbd> della tastiera).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7, 8
---
images/colour_background.png

sense.set_pixels(immagine) sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  sense.set_pixels(immagine) sleep(1)

--- /task ---

--- task ---

**Test:** Esegui di nuovo il codice. Quando il tuo progetto ha terminato l'esecuzione, la matrice LED si pulirà, annerendo tutte le luci (luci spente).

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
If you would like to have more than two frames in your animation, you must make sure that the program will run for no more than 30 seconds. For example, if you have 10 images that each display for 1 second, you must change your `for` loop to repeat 3 times (10 * 3 = 30 seconds)
</p>

**Test:** Esegui di nuovo il codice.

Il mio codice ha un errore di sintassi o non viene eseguito come previsto:
- Verifica di aver indentato il codice nel tuo ciclo `for`
- Make sure you named your second image matrix `image2` and that it is placed outside and before the loop begins.
- Check that your `sleep` times are set to exactly `1` second to avoid running past the strict 30-second execution cutoff on the ISS.

--- /task ---

--- task ---

**Salva i tuoi progressi**

Puoi salvare il tuo programma sul progetto Mission Starter inserendo il nome della tua squadra, i nomi dei membri del team e il codice classe che ti è stato comunicato. È possibile ricaricare il programma su qualsiasi dispositivo con una connessione internet inserendo il nome del team e il codice aula.

--- /task ---

--- collapse ---
---
title: Completed Whale code example
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
z = (153, 50, 204) # Orchidea scura q = (255, 255, 0) # Giallo d = (51, 153, 255) # Blu c = (0, 0, 0) # Nero

# Sense a colour
for i in range(28): rgb = sense.color # ottenere il colore dal sensore c = (rgb.red, rgb.green, rgb.blue)

immagine = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /collapse ---
---
title: Esempio di codice completato
---

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Importa le librerie
from sense_hat import SenseHat from time import sleep

# Imposta il Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Aggiungi il codice prima della lista contenente le immagini per ottenere il colore dal sensore e modifica la variabile del colore di sfondo `c` per utilizzare il colore rilevato dal sensore di colore Sense HAT, al posto del nero.
for i in range(28): rgb = sense.color # ottenere il colore dal sensore c = (rgb.red, rgb.green, rgb.blue)

# Add colour variables and image
z = (153, 50, 204) # Orchidea scura q = (255, 255, 0) # Giallo d = (51, 153, 255) # Blu c = (0, 0, 0) # Nero

# Sense a colour
for i in range(28): rgb = sense.color # ottenere il colore dal sensore c = (rgb.red, rgb.green, rgb.blue)

immagine = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

sense.set_pixels(immagine)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
images/savebutton_it.png

sense.set_pixels(immagine) sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  sense.set_pixels(immagine) sleep(1)
