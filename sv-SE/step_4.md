## Lägg till lite färg

Lysdioderna i Astro Pi kan även visa färger. Du kan ange en färg genom att skapa en variabel och tilldela den ett värde för en RGB-färg.

Du kan lära dig hur alla färger kan skapas med olika proportioner av rött, grönt och blått här:

[[[generic-theory-colours]]]

--- task ---

Välj en färg och ta reda på färgens RGB-värde. Du kan använda en [färgväljare](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} för att hjälpa dig.

--- /task ---

--- task ---

Skapa en variabel för att lagra den färg du valt. Om du exempelvis valde röd, kan du skriva den här kodraden:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

Du kan nu visa din text i den färg du valt! För att tala om för programmet att det ska använda den färg du skapat, lägger du till parametern `text_colour` till den kod som visar din text:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /task ---

![Trinket Sense HAT emulatorn kör ett exempelprogram som rullar texten \"Astro Pi\" över LED-matrisen med röda bokstäver](images/M0_2.gif)

--- task ---

Du kan även ändra bakgrundsfärgen på displayen. Välj en annan färg, och skapa ytterligare en variabel för att lagra den färgen. För att tala om för programmet att det ska använda din valda bakgrundsfärg lägger du till parametern `back_colour` till din kod:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Ändra hälsningstexten och färgen - vilket meddelande vill du skicka till astronauterna ombord på ISS?

--- /task ---
