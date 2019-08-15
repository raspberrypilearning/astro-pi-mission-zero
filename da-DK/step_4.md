## Tilføj noget farve

Lysdioderne på Astro Pi kan også vise farver. Du kan angive en farve ved at oprette en variabel og tildele den en RGB-farveværdi.

Du kan lære, hvordan alle farver kan laves ved hjælp af forskellige kombinationer af rød, grøn og blå, her:

[[[generic-theory-colours]]]

\--- opgave \---

Vælg en farve og find uden pågældende farves RGB-værdi. Du kan benytte en [farvevælger](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} til at hjælpe dig.

\--- /opgave \---

\--- opgave \---

Opret en variabel for at gemme din valgte farve. Hvis du eksempelvis valgte rød, ville du skrive denne kodelinje:

```python
red = (255,0,0)
```

\--- /opgave \---

\--- opgave \---

Du kan nu få vist din tekst i den farve, du ønsker! For at bede programmet om at anvende den farve, du oprettede, skal du tilføje parameteren `text_colour` (tekst_farve) til den kode, der viser din tekst:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

\--- /opgave \---

![vis besked i farve](images/show-message-color.gif)

\--- opgave \---

Du kan også ændre baggrundsfarve på displayet. Vælg en anden farve, og opret en anden variabel for at gemme den farve. For at bede programmet om at anvende din valgte baggrundsfarve skal du føje parameteren `back_colour` (bag_farve) til din kode:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

\--- /opgave \---

\--- opgave \---

Skift tekst og farve på hilsenen — hvilken besked vil du sende til astronauterne ombord på ISS?

\--- /opgave \---