## Mostra un’immagine

La matrice LED di Astro Pi può visualizzare i colori. In questa fase, visualizzerai le immagini dalla natura sulla matrice LED di Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Una <span style="color: #0faeb0">**matrice LED**</span> è una griglia di LED che può essere controllata individualmente o in gruppo per creare diversi effetti di luce. La matrice LED del Sense HAT ha 64 LED visualizzati in una griglia 8 x 8. I LED possono essere programmati per produrre un'ampia gamma di colori.
</p>

![Uno screenshot della finestra dell'emulatore che mostra l'unità di volo con la matrice LED che visualizza l'immagine di un fiore.](images/fu-pic.png)

--- task ---

Apri [il progetto iniziale Mission Zero](http://rpf.io/mzcode){:target="_blank"}.

Vedrai che alcune righe di codice sono state aggiunte automaticamente per te.

Questo codice esegue il collegamento all'Astro Pi, assicurando che il display a LED dell'Astro Pi sia mostrato nel modo corretto e imposta il sensore di colore. Lasciate stare questo codice, perché è necessario.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Importa le librerie
from sense_hat import SenseHat from time import sleep

# Imposta il Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Configura il sensore di colore
sense.color.gain = 60 # Imposta la sensibilità del sensore sense.color.integration_cycles = 64 # L'intervallo con cui verrà eseguita la lettura

--- /code ---

![Uno screenshot dell'emulatore Sense HAT con linee di codice iniziale visualizzate nel riquadro di sinistra.](images/sense-hat-emulator2.png)

--- /task ---

### Colori RGB

I colori possono essere creati utilizzando diverse proporzioni di rosso, verde e blu. Puoi scoprire i colori RGB qui:

[[[generic-theory-simple-colours]]]

La matrice LED è una griglia 8 x 8. Ciascun LED sulla griglia può essere impostato ad un colore diverso. Ecco un elenco di variabili per 24 diversi colori. Ogni colore ha un valore per rosso, verde e blu:

[[[ambient-colours]]]

### Scegli un'immagine

--- task ---

**Scegli:** Scegli un'immagine da visualizzare tra le seguenti opzioni. Python memorizza le informazioni per un'immagine in una lista. Il codice di ogni immagine include le variabili di colore utilizzate e la lista.

Dovrai **copiare** tutto il codice per l'immagine scelta, quindi **incollarlo** nel tuo progetto sotto la riga che dice `# Aggiungi variabili di colore e immagine`.

--- collapse ---

---
title: Pollo
---

![Una griglia con 8 x 8 quadrati che mostra un pulcino in un uovo.](images/fox_mz3.png)

Created by team i_pupi, Italy

```python
c = (0, 0, 0) # Nero 
m = (34, 139, 34) # Verde bosco 
q = (255, 255, 0) # Giallo 
t = (255, 140, 0) # Arancio scuro 
y = (255, 20, 147) # Rosa scuro
```

--- /collapse ---


--- collapse ---

---
title: Serpente
---

![Una griglia con 8 x 8 quadrati che mostra una rana.](images/elephant.png)

Created by team ILiFanT, Finland

```python
a = (255, 255, 255) # Bianco 
c = (0, 0, 0) # Nero 
v = (255, 0, 0) # Rosso
```

--- /collapse ---

--- collapse ---
---
title: Fiore
---

![Una griglia con 8 x 8 quadrati che mostra un granchio.](images/cactus.png)

Created by team 6TETHASI, The Netherlands

```python
a = (255, 255, 255) # Bianco 
c = (0, 0, 0) # Nero 
e = (0, 0, 205) # Blu Medio 
q = (255, 255, 0) # Giallo 
t = (255, 140, 0) # Arancio scuro
w = (255, 192, 203) # Rosa

```

--- /collapse ---


--- collapse ---
---
title: Coccodrillo
---

![Una griglia con 8 x 8 quadrati che mostra una testa di coccodrillo.](images/croc.png)

```python

a = (255, 255, 255) # Bianco 
c = (0, 0, 0) # Nero 
f = (25, 25, 112) # Blu notte 
m = (34, 139, 34) # Verde bosco

```

--- /collapse ---

--- collapse ---
---
title: Rana
---

![Una griglia con 8 x 8 quadrati che mostra un fiore rosa su uno stelo verde.](images/rainbow.png)

Created by team camrus_6, United Kingdom

```python

c = (0, 0, 0) # Nero 
 m = (34, 139, 34) # Verde bosco 
 q = (255, 255, 0) # Giallo 
 v = (255, 0, 0) # Rosso

```

--- /collapse ---

--- collapse ---
---
title: Granchio
---

![Una griglia con 8 x 8 quadrati che mostra un serpente.](images/dragon.png)

Created by team hwplucyr, United Kingdom

```python

b = (105, 105, 105) # DimGray
c = (0, 0, 0) # Black
d = (100, 149, 237) # CornflowerBlue
v = (255, 0, 0) # Red
z = (153, 50, 204) # DarkOrchid

image = [
    c, c, v, c, v, c, c, c,
    c, z, z, z, z, v, c, c,
    z, b, z, b, z, c, c, c,
    z, z, z, z, z, v, c, c,
    c, c, d, d, d, c, c, z,
    c, z, d, z, z, z, z, c,
    c, c, d, d, z, c, c, c,
    c, c, z, c, z, c, c, c]

```

--- /collapse ---

--- /task ---

--- task ---

**Trova:** la riga che dice `# Visualizza l'immagine` e aggiungi una riga di codice per visualizzare la tua immagine sulla matrice LED:

```python
c = (0, 0, 0) # Nero 
m = (34, 139, 34) # Verde bosco 
q = (255, 255, 0) # Giallo 
v = (255, 0, 0) # Rosso

```

--- /task ---

--- task ---

Premi **Esegui** nella parte inferiore dell'editor per vedere la tua immagine visualizzata sulla matrice LED.

--- /task ---

--- task ---

**Debug**

Il mio codice ha un errore di sintassi:

- Verifica che il tuo codice corrisponda al codice degli esempi sopra
- Verifica di aver indentato il codice nella tua lista
- Verifica che la tua lista sia racchiusa tra `[` e `]`
- Verifica che ogni variabile di colore nell'elenco sia separata da una virgola

La mia immagine non viene visualizzata:

- Verifica che il tuo `sense.set_pixels(image)` non sia indentato

--- /task ---


--- task ---

**Save your progress**

Now that you have displayed an image, you can save your program on the Mission Starter project by entering your team name, team members' names, and the classroom code given to you. You can reload your program on any device with an internet connection by entering your team name and classroom code.

![Mission Zero Save button](images/savebutton.png)

--- /task --- 
