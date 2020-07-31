## Misurate la temperatura

Il sensore di temperatura dell’Astro Pi può misurare la temperatura dell’aria circostante. Questa funzione è molto utile per raccogliere dati sulle condizioni nello spazio.

![Messaggio sulla temperatura](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

Parte della vostra missione è contribuire positivamente alla vita quotidiana dell’equipaggio a bordo della ISS. Il far saper loro che la temperatura a bordo della stazione spaziale si trova fra i valori normali li rassicurerà certamente.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Aggiungete questa riga di codice per misurare la temperatura:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- /task \---

\--- task \---

La temperatura viene registrata con molta precisione, ovvero il valore memorizzato avrà un numero elevato di cifre decimali. È possibile arrotondare il valore a un numero qualsiasi di cifre decimali. Nell’esempio, abbiamo arrotondato il valore a una cifra decimale, ma per visualizzare un diverso livello di precisione è sufficiente sostituire il numero `1` con il numero di cifre decimali che volete visualizzare.

```python
temp = round( sense.temperature, 1 )
```

\--- /task \---

\--- task \---

Per visualizzare la temperatura attuale come messaggio scorrevole sul display, aggiungete questa riga di codice:

```python
sense.show_message( str(temp) )
```

The `str()` part converts the humidity from a number into text so that the Astro Pi can display it.

\--- /task \---

\--- task \---

La parte `str()` converte il valore della temperatura da numero a testo, per poterlo visualizzare sull’Astro Pi.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

In realtà, il vero Astro Pi misurerà la temperatura effettiva intorno ad esso, ma voi, con l’emulatore Sense HAT, potete simulare cambiamenti di temperatura e provare il corretto funzionamento del codice semplicemente spostando il cursore della temperatura.

![Humidity slider](images/humidity-slider.png)

**Nota:** Potreste chiedervi come mai il cursore della temperatura visualizza la temperatura come un numero intero, ma la lettura ottenuta è un numero decimale. L’emulatore simula anche una leggera imprecisione che è presente sul sensore reale. Quindi la misura della temperatura che vedete potrebbe essere leggermente superiore o inferiore al valore impostato con il cursore.