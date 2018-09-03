## Misurate la temperatura

Il sensore di temperatura dell’Astro Pi può misurare la temperatura dell’aria circostante. Questa funzione è molto utile per raccogliere dati sulle condizioni nello spazio.

![Messaggio sulla temperatura](images/degrees-message.gif)

L’Astro Pi misura la temperatura nella ISS in gradi centigradi (&deg;C). Poiché le temperature nello spazio variano molto più di quelle sulla Terra, l’Astro Pi può misurare temperature da un minimo di -40 gradi centigradi fino a un massimo di +120 gradi centigradi.

Parte della vostra missione è contribuire positivamente alla vita quotidiana dell’equipaggio a bordo della ISS. Il far saper loro che la temperatura a bordo della stazione spaziale si trova fra i valori normali li rassicurerà certamente.

## \--- collapse \---

## title: Cosa è la temperatura?

La temperatura è la misura di quanto sia caldo un qualcosa. Certamente avranno misurato la temperatura anche a voi con un termometro, magari se siete dovuti andare dal dottore.

![Termometro](images/thermometer.JPG) *Foto Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} tramite Wikimedia Commons*

Per essere più precisi, la temperatura è una misura della quantità di energia termica di una sostanza. Sapete che un cubetto di ghiaccio è solido, ma mentre si riscalda, cioè mentre assorbe l’energia termica dal suo ambiente, si scioglie e diventa liquido. Questo perché, quando una sostanza assorbe o perde abbastanza energia termica, si verifica un cambiamento di stato nella sostanza. Ad esempio la sostanza passa dallo stato solido allo stato liquido.

\--- /collapse \---

\--- task \---

Aggiungete questa riga di codice per misurare la temperatura:

```python
temp = sense.get_temperature()
```

Questa riga di codice misurerà la temperatura attuale e la memorizzerà nella variabile `temp`.

\--- /task \---

\--- task \---

La temperatura viene registrata con molta precisione, ovvero il valore memorizzato avrà un numero elevato di cifre decimali. È possibile arrotondare il valore a un numero qualsiasi di cifre decimali. Nell’esempio, abbiamo arrotondato il valore a una cifra decimale, ma per visualizzare un diverso livello di precisione è sufficiente sostituire il numero `1` con il numero di cifre decimali che volete visualizzare.

```python
temp = round( sense.get_temperature(), 1 )
```

\--- /task \---

\--- task \---

Per visualizzare la temperatura attuale come messaggio scorrevole sul display, aggiungete questa riga di codice:

```python
sense.show_message( str(temp) )
```

La parte `str()` converte il valore di temperatura da numero a testo, per poterlo visualizzare sull’Astro Pi.

\--- /task \---

\--- task \---

È possibile anche visualizzare la temperatura all’interno di un altro messaggio, unendo insieme le varie parti del messaggio con un `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

In realtà, il vero Astro Pi misurerà la temperatura effettiva intorno ad esso, ma voi, con l’emulatore Sense HAT, potete simulare cambiamenti di temperatura e provare il corretto funzionamento del codice semplicemente spostando il cursore della temperatura.

![Cursore della temperatura](images/temperature-slider.png)

**Nota:** Potreste chiedervi come mai il cursore della temperatura visualizza la temperatura come un numero intero, ma la lettura ottenuta è un numero decimale. L’emulatore simula anche una leggera imprecisione che è presente sul sensore reale. Quindi la misura della temperatura che vedete potrebbe essere leggermente superiore o inferiore al valore impostato con il cursore.