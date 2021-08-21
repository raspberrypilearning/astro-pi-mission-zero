## Visa en bild

Du kan visa bilder på Astro Pis LED-matris. Din hälsning till astronauterna kanske ska innehålla en bild eller ett mönster, tillsammans med eller istället för ett skrivet meddelande?

![En skärmdump av emulatorfönstret som visar flygenheten med LED-matrisen som visar en bild av själva flygenheten](images/fu-pic.png)

--- task ---

Längst ner i programmet, skapa några färgvariabler för att definiera de färger du vill rita din bild med. Du kan använda så många färger som du vill, men i det här exemplet använder vi bara några färger - röd (`r`), vit (`w`), svart (`b`) och två nyanser av grått (`g` och `s`). Observera att nyanserna uppnås genom att minska mängden ljus i alla tre kanalerna samtidigt behålla samma proportioner.

```python
w = (255, 255, 255)
b = (0, 0, 0)
g = (50,50,50)
s = (200,255,200)
r = (255,0,0)
```

**Obs!** Den här gången är det en bra idé att ge färgvariablerna enstaviga namn, eftersom det sparar tid i nästa steg, där du ska skriva in dem många gånger. Användning av enstaka bokstäver gör det dessutom lättare att se den bild du ska rita.

--- /task ---

--- task ---



Skapa en lista med 64 objekt, nedanför dina nya variabler. Varje objekt representerar en pixel i LED-matrisen och motsvarar en av de färgvariabler du definierade. Rita din bild genom att placera en variabel där du vill att den tilldelade färgen ska visas. Vi har ritat en Astro Pi genom att använda de svarta (`b`) pixlarna som bakgrund och de grå (`g`) pixlarna för att rita metalldelarna i Astro Pi flygfodralet:

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
--- /uppgift ---

--- uppgift ---

Lägg till en kodrad för att visa din bild på LED-displayen.

```python
sense.set_pixels(picture)
```

--- /uppgift ---

--- uppgift ---

Tryck på **Run** (Kör) för att se din bild visas.

--- /uppgift ---

--- uppgift ---

Du kanske vill lägga till lite kod för att inkludera en kort väntetid (eller `sleep`) efter att bilden har visats. Det ger astronauterna lite tid att hinna se din bild innan nästa del av ditt meddelande visas. Överst i programmet, lägger du till:

```python
from time import sleep
```

Lägg sedan till koden för att vänta i två sekunder på raden efter den som visar din bild:

```python
sleep(2)
```

--- /uppgift ---

--- uppgift ---

Skapa din egen bild eller mönster för att visa för astronauterna!

--- /uppgift ---
