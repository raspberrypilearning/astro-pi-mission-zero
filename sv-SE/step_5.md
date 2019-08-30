## Visa en bild

Du kan visa bilder på Astro Pis LED-matris. Din hälsning till astronauterna kanske ska innehålla en bild eller ett mönster, tillsammans med eller istället för ett skrivet meddelande?

![Astronaut](images/astronaut-pic.png)

--- task ---

Längst ner i programmet skapar du några färgvariabler för att definiera de färger du vill rita din bild med. Du kan använda hur många färger du vill, men i det här exemplet använder vi bara två - vit (`w`) och svart (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Obs!** Den här gången är det en bra idé att ge färgvariablerna enstaviga namn, eftersom det sparar tid i nästa steg, där du ska skriva in dem många gånger. Användning av enstaka bokstäver gör det dessutom lättare att se den bild du ska rita.

--- /task ---

--- task ---

Skapa en lista med 64 objekt, nedanför dina nya variabler. Varje objekt representerar en pixel i LED-matrisen och motsvarar en av de färgvariabler du definierade. Rita din bild genom att placera en variabel där du vill att den tilldelade färgen ska visas. Vi har ritat en astronaut genom att använda de svarta (`s`) pixlarna som bakgrund och de vita (`v`) pixlarna för att rita astronautens rymddräkt:

```python
picture = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
```

--- /task ---

--- task ---

Lägg till en kodrad för att visa din bild på LED-displayen.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Tryck på **Run** (Kör) för att se din bild visas.

--- /task ---

--- task ---

Du kanske vill lägga till lite kod för att inkludera en kort väntetid (eller `sleep`) efter att bilden har visats. Det ger astronauterna lite tid att hinna se din bild innan nästa del av ditt meddelande visas. Överst i programmet, lägger du till:

```python
from time import sleep
```

Lägg sedan till koden för att vänta i två sekunder på raden efter den som visar din bild:

```python
sleep(2)
```

--- /task ---

--- task ---

Skapa din egen bild eller mönster för att visa för astronauterna!

--- /task ---