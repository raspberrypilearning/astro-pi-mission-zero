## Mostra un’immagine

L'immagine visualizzata sarà composta da 64 quadrati colorati chiamati **pixel**. I pixel sono disposti in una griglia 8 x 8. Ogni pixel può essere di un colore diverso. Scegliendo attentamente i colori, puoi creare un'immagine. Ecco un esempio di una balena realizzata utilizzando diverse tonalità di blu su sfondo nero.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Una <span style="color: #0faeb0">**matrice LED**</span> è una griglia di LED che può essere controllata individualmente o in gruppo per creare diversi effetti di luce. La matrice LED del Sense HAT ha 64 LED disposti in una griglia 8 x 8. I LED possono essere programmati per produrre un'ampia gamma di colori.
</p>

![un'immagine 8x8 di una balena con lettere che identificano colori diversi](images/whale.png)

Nota che ogni quadrato è etichettato con un codice per rappresentare un colore particolare. In questa immagine vengono utilizzati 3 colori:
+ c = nero
+ f = Blu oceano
+ g = Azzurro cielo


--- task ---

Apri [il progetto iniziale Mission Zero](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"}.

Vedrai che alcune righe di codice sono state aggiunte automaticamente per facilitarti.

Questo codice esegue il collegamento all'Astro Pi, assicurando che il display a LED dell'Astro Pi sia mostrato nel modo corretto e inoltre imposta il sensore di colore. Non modificate questo codice, perché ne avrete bisogno.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
---
# Importa le librerie
from sense_hat import SenseHat
from time import sleep

# Imposta il Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Configura il sensore di colore
sense.color.gain = 60 # Imposta la sensibilità del sensore
sense.color.integration_cycles = 64 # L'intervallo con cui verrà eseguita la lettura

--- /code ---

![Uno screenshot dell'emulatore Sense HAT con linee di codice iniziali visualizzate nel riquadro di sinistra.](images/sense-hat-emulator3.png)

--- /task ---

### Colori RGB

I colori possono essere creati utilizzando diverse quantità di rosso, verde e blu. Puoi scoprire i colori RGB qui:

![Tre cursori che mostrano i valori di colore RGB](images/rgbsliders.gif)

La matrice LED è una griglia 8 x 8. Ciascun LED sulla griglia può essere impostato a un colore diverso. Possiamo usare le lettere dalla a alla z come nomi di variabili per rappresentare 24 colori diversi. Ogni colore ha un valore per il rosso, il verde e il blu.

--- collapse ---

---
title: Elenco delle variabili di colore
---

![Una griglia di 24 quadrati colorati ciascuno etichettato con una diversa lettera dell'alfabeto](images/palette.png)

```python
a = (255, 255, 255) # Bianco
b = (171, 171, 171) # Grigio
c = (0, 0, 0) # Nero
d = (25, 25, 113) # Blu navy
e = (0, 0, 255) # Blu puro
f = (36, 128, 200) # Blu oceano
g = (0, 204, 255) # Azzurro cielo
h = (86, 255, 255) # Ciano elettrico
j = (0, 255, 0) # Verde puro
k = (46, 139, 33) # Verde Foglia
l = (57, 97, 17) # Verde oliva
m = (30, 65, 6) # Verde foresta
n = (126, 88, 25) # Marrone Terra
o = (179, 96, 65) # Marrone terracotta
p = (180, 34, 34) # Rosso mattone
q = (255, 0, 0) # Rosso puro
r = (232, 118, 5) # Arancione
s = (241, 231, 100) # Giallo pallido
t = (255, 255, 0) # Giallo puro
u = (255, 209, 209) # Rosa pallido
v = (255, 177, 177) # Rosa cipria
w = (249, 169, 255) # Rosa chiaro
y = (248, 97, 255) # Magenta
z = (220, 53, 232) # Viola

```

--- /collapse ---

### Scegli un'immagine

--- task ---

**Scegli:** decidi quale immagine visualizzare tra le seguenti opzioni. Python memorizza le informazioni per un'immagine in una lista. Il codice di ogni immagine include le variabili di colore utilizzate e la lista.

Dovrai **copiare** tutto il codice per l'immagine scelta, quindi **incollarlo** nel tuo progetto sotto la riga che dice `# Aggiungi variabili di colore e immagine`.

--- collapse ---

---
title: Balena
---

![Una griglia di 8 x 8 quadrati che mostra una balena.](images/whale.png)

Creato dal Team Naicom, Italia

```python
c = (0, 0, 0)       # Nero
f = (36, 128, 200)  # Blu oceano
g = (0, 204, 255)   # Cielo blu

immagine = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, a,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

```

--- /collapse ---


--- collapse ---

---
title: Limone
---

![Una griglia con 8 x 8 quadrati che mostra un limone.](images/lemon.png)

Creato dal team g4lemoni, Grecia

```python
c = (0, 0, 0)       # Nero
k = (46, 139, 33)   # Verde foglia
t = (255, 255, 0)   # Giallo puro

immagine = [
c, c, c, k, k, c, c, c,
c, c, k, c, k, c, c, c,
c, k, c, t, t, c, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, c, t, t, c, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Maiale
---

![Una griglia con 8 x 8 quadrati che mostra un maiale.](images/pig.png)

Creato da Gary, Regno Unito

```python
a = (255, 255, 255) # Bianco
v = (255, 177, 177) # Rosa cipria
y = (248, 97, 255)  # Magenta
o = (179, 96, 65)   # Marrone terracotta
c = (0, 0, 0)       # Nero

immagine = [
a, a, y, a, a, y, a, a,
a, y, y, y, y, y, y, a,
a, y, c, y, c, y, y, y,
v, v, v, v, v, y, y, y,
v, o, v, o, v, y, y, y,
v, v, v, v, v, y, y, y,
a, y, y, y, y, y, y, y,
a, a, y, a, a, a, y, a]

```

--- /collapse ---


--- collapse ---
---
title: Tempesta
---

![Una griglia con 8 x 8 quadrati che mostra una nuvola temporalesca.](images/storm.png)

Creato dal team hop2p023, Spagna

```python

c = (0, 0, 0)       # Nero
f = (36, 128, 200)  # Blu oceano
g = (0, 204, 255)   # Cielo blu
t = (255, 255, 0)   # Giallo puro

immagine = [
c, c, c, c, c, c, c, c,
c, c, f, f, f, f, c, c,
c, f, f, f, f, f, f, c,
c, g, c, g, t, g, c, c,
c, c, c, t, t, c, c, c,
c, c, t, t, c, c, c, c,
c, c, g, c, c, c, c, g,
c, g, c, c, c, c, c, c]


```

--- /collapse ---

--- collapse ---
---
title: Anatra
---

![Una griglia con 8 x 8 quadrati che mostra un'anatra.](images/duck.png)

Creato da Peter, Irlanda

```python

c = (0, 0, 0) # Nero
l = (57, 97, 17)    # Verde Oliva
m = (30, 65, 6)     # Verde foresta
r = (232, 118, 5)   # Arancia
a = (255, 255, 255) # Bianco
b = (171, 171, 171) # Grigio

immagine = [
c, l, l, c, c, c, c, c,
r, r, m, c, c, c, c, c,
c, l, l, c, c, c, c, c,
c, a, a, l, a, a, c, c,
c, l, l, a, a, a, b, a,
c, a, a, b, b, b, a, a,
c, c, a, a, a, a, c, c,
c, c, c, r, c, r, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Rana
---

![Una griglia con 8 x 8 quadrati che mostra una rana.](images/frog.png)

Creato dal team Jmeno, Repubblica Ceca

```python

a = (255, 255, 255) # Bianco
b = (171, 171, 171) # Grigio
c = (0, 0, 0)       # Nero
q = (255, 0, 0)     # Rosso puro
j = (0, 255, 0)     # Verde puro
k = (46, 139, 33)   # Verde foglia
n = (126, 88, 25)   # Marrone Terra

immagine = [
a, a, a, a, a, a, a, a,
a, a, a, a, a, b, a, b,
a, a, a, a, a, a, c, a,
a, a, c, a, c, a, q, a,
a, a, j, j, j, q, a, a,
a, j, j, k, q, a, a, a,
j, k, j, k, k, a, a, a,
k, k, k, j, k, n, n, n]

```

--- /collapse ---

--- collapse ---
---
title: Albero in fiore
---

![Una griglia di 8 x 8 quadrati che mostra un albero in fiore.](images/blossom.png)

Creato dal team Zssh14, Slovacchia

```python

t = (255, 255, 0)   # Giallo puro
g = (0, 204, 255)   # Cielo blu
w = (249, 169, 255) # Rosa chiaro
y = (248, 97, 255)  # Magenta
z = (220, 53, 232)  # Viola
n = (126, 88, 25)   # Marrone Terra
o = (179, 96, 65)   # Marrone terracotta
k = (46, 139, 33)   # Verde foglia

immagine =  [
t, g, g, w, w, y, g, g,
g, g, w, w, y, y, z, g,
g, w, y, z, y, z, z, z,
w, y, z, z, g, n, w, g,
g, g, o, o, n, w, y, z,
g, g, g, g, n, g, g, g,
g, g, g, o, n, n, g, g,
k, k, o, n, n, n, k, k]

```

--- /collapse ---

--- /task ---

--- task ---

**Trova:** la riga che dice `# Mostra l'immagine` e aggiungi una riga di codice per visualizzare la tua immagine sulla matrice LED:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Nero
f = (36, 128, 200)  # Blu oceano
g = (0, 204, 255)   # Cielo blu

immagine = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, a,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

# Mostra l'immagine
sense.set_pixels(immagine)

--- /code ---

--- /task ---

--- task ---

Premi **Run (esegui)** nella parte inferiore dell'editor per vedere la tua immagine visualizzata sulla matrice LED.

--- /task ---

--- task ---

**Debug**

Il mio codice ha un errore di sintassi:

- Verifica che il tuo codice corrisponda al codice degli esempi sopra
- Verifica di aver indentato il codice nella tua lista
- Verifica che la tua lista sia racchiusa tra `[` e `]`
- Verifica che ogni variabile di colore nell'elenco sia separata da una virgola

La mia immagine non viene visualizzata:

- Verifica che il tuo `sense.set_pixels(immagine)` non sia indentato

--- /task ---


--- task --- 

**Salva i tuoi progressi**

Ora che hai visualizzato un'immagine, puoi salvare il tuo programma sul progetto Mission Starter inserendo il nome della tua squadra, i nomi dei membri del team e il codice dell'aula che ti è stato comunicato. È possibile ricaricare il programma su qualsiasi dispositivo con una connessione internet inserendo il nome del team e il codice aula.

![Pulsante per salvare Mission Zero.](images/mz_savebutton_v2.png)

--- /task --- 

