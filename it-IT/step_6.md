## Misura l'umidità

Il sensore di umidità nell'Astro Pi può misurare l'umidità nell'aria circostante, una funzione utile che può aiutarti a raccogliere dati sulle condizioni nello spazio.

![The Trinket Sense HAT emulator running a sample program which scrolls the humidity value across the LED matrix using white letters](images/M0_3.gif)

L'Astro Pi misura l'umidità nell'ISS come percentuale di concentrazione d'acqua nell'aria.

Parte della vostra missione è contribuire positivamente alla vita quotidiana dell’equipaggio a bordo della ISS. Far saper loro che l'umidità a bordo della stazione spaziale si trova fra i valori normali li rassicurerà certamente.

[[[generic-theory-what-is-humidity]]]

--- task ---

Aggiungete questa riga di codice per misurare l'umidità:

```python
umidita = sense.get_humidity()
```

Questa riga di codice misurerà l'umidità attuale e la memorizzerà nella variabile `umidita`.

--- /task ---

--- task ---

L'umidità viene registrata con molta precisione, ovvero il valore memorizzato avrà un numero elevato di cifre decimali. È possibile arrotondare il valore a un numero qualsiasi di cifre decimali. Nell’esempio, abbiamo arrotondato il valore a una cifra decimale, ma per visualizzare un diverso livello di precisione è sufficiente sostituire il numero `1` con il numero di cifre decimali che volete visualizzare.

```python
umidita = round(sense.get_humidity(), 1)
```

--- /task ---

--- task ---

Per visualizzare l'umidità attuale come messaggio scorrevole sul display, aggiungete questa riga di codice:

```python
sense.show_message(str(umidita))
```

L'istruzione `str()` converte l'umidità da numero in testo in modo che l'Astro Pi possa visualizzarla.

--- /task ---

--- task ---

È possibile anche visualizzare l'umidità all’interno di un messaggio più lungo, unendo insieme le varie parti con un `+`.

```python
sense.show_message( "E' al " + str(umidita) + " %" )
```

--- /task ---

In realtà, il vero Astro Pi misurerà l'umidità effettiva intorno ad esso, ma voi, con l’emulatore Sense HAT, potete simulare cambiamenti d'umidità e provare il corretto funzionamento del codice semplicemente spostando il cursore relativo.

![A labelled screenshot of the Sense HAT emulator with the code window on the left and the emulator on the right. The slider used to adjust the humidity is circled in the top right corner](images/humidity-slider.png)

**Nota:** Potreste chiedervi come mai il cursore dell'umidità visualizza l'umidità come un numero intero, ma la lettura ottenuta è un numero decimale. L’emulatore simula anche una leggera imprecisione che è presente sul sensore reale. Quindi la misura dell'umidità che leggerete potrebbe essere leggermente superiore o inferiore al valore impostato con il cursore.
