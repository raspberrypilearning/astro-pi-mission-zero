## Snímanie farby

V tomto kroku nastavíte snímač farebnej svietivosti a použijete ho na snímanie množstva červenej, zelenej a modrej, ktoré sa dostane na snímač. Táto farba sa potom použije na vyfarbenie zvoleného obrázka. Kozmonaut kráčajúci k snímaču v modrej košeli by videl iný obraz ako kozmonaut v červenej košeli.

![obrázok zobrazený s ružovým pozadím na matici LED](images/colour_background.png)

Bez ohľadu na to, ktorý obrázok vyberiete, pozadie používa premennú `c`, ktorá je nastavená na čiernu.

--- task ---

Na vyfarbenie pozadia použite farebný snímač.

Pridajte kód pred zoznam obrázkov, aby ste získali farbu zo snímača, a zmeňte premennú farby pozadia `c` tak, aby namiesto čiernej používala farbu snímanú farebným snímačom Sense HAT.

**Tip:** Nemusíte písať komentáre, ktoré začínajú znakom „#“ (sú tu na vysvetlenie kódu).

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 9-10
---
# Pridajte farebné premenné a obrázok

c = (0, 0, 0) # Čierna
m = (34, 139, 34) # Lesná zelená
q = (255, 255, 0) # Žltá
t = (255, 140, 0) # Tmavo oranžová
y = (255, 20, 147) # Tmavo ružová

rgb = sense.color # získajte farbu zo snímača
c = (rgb.red, rgb.green, rgb.blue) # použite nasnímanú farbu

obrazok = [
  c, c, y, y, y, y, c, c,
  c, y, y, t, t, y, y, c,
  y, y, t, q, q, t, y, y,
  c, y, y, t, t, y, y, c,
  c, c, y, y, y, y, c, c,
  m, c, c, m, m, c, c, m,
  c, m, m, m, m, m, m, c,
  c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

**Test:** Posuňte posúvač farieb na farbu podľa vlastného výberu a potom **spustite**. Vaša farba pozadia sa zmení. Zopakujte tento test s novou farbou.

**Tip:** pri každej zmene farby budete musieť kliknúť na „Spustiť“.

--- /task ---

## Zopakujte svoj program v slučke

Program Astro Pi Mission Zero môže bežať až 30 sekúnd. Tento čas využijete na opakovanú kontrolu farebného snímača a aktualizáciu snímky.

Váš kód použije slučku `for`, a spustí program 28-krát. **Zakaždým**:
+ snímajte najnovšiu farbu
+ aktualizujte farbu obrázka
+ pozastavte na jednu sekundu

--- task ---

**Nájdite** svoj riadok kódu `rgb = sense.color`.

**Pridajte** kód nad ním a nastavte slučku `for` pre `28` opakovaní.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---
for i in range(28):
rgb = sense.color # získajte farbu zo snímača
c = (rgb.red, rgb.green, rgb.blue)

obrazok = [
  c, c, y, y, y, y, c, c,
  c, y, y, t, t, y, y, c,
  y, y, t, q, q, t, y, y,
  c, y, y, t, t, y, y, c,
  c, c, y, y, y, y, c, c,
  m, c, c, m, m, c, c, m,
  c, m, m, m, m, m, m, c,
  c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

Teraz musíte odsadiť celý kód pod slučkou `for` tak, aby sa nachádzal **vnútri** slučky `for`.

**Tip:** ak chcete odsadiť viacero riadkov, zvýraznite riadky, ktoré chcete odsadiť, a potom stlačte kláves <kbd>Tabulátor</kbd> na klávesnici (zvyčajne nad <kbd>Kláves Caps Lock</kbd> na klávesnici).

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 2 - 17
---
for i in range(28):
  rgb = sense.color # získajte farbu zo snímača
  c = (rgb.red, rgb.green, rgb.blue)

  obrazok = [
    c, c, y, y, y, y, c, c,
    c, y, y, t, t, y, y, c,
    y, y, t, q, q, t, y, y,
    c, y, y, t, t, y, y, c,
    c, c, y, y, y, y, c, c,
    m, c, c, m, m, c, c, m,
    c, m, m, m, m, m, m, c,
    c, c, c, m, m, c, c, c]
    
  # Zobrazte obrázok

  sense.set_pixels(obrazok)

--- /code ---

--- /task ---

--- task ---

V spodnej časti kódu pridajte do cyklu `sleep` v dĺžke jednej sekundy:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 4
---
  # Zobrazte obrázok

  sense.set_pixels(obrazok)
  sleep(1)

--- /code ---

**Tip:** uistite sa, že tento riadok kódu je v rámci cyklu `for` odsadený.

--- /task ---

--- task ---

**Test:** Spustite svoj kód a niekoľkokrát zmeňte výber farby počas behu projektu. Skontrolujte, či sa váš obrázok aktualizuje, aby pri ďalšom spustení použil nasnímanú farbu.

Po dokončení cyklu sa obraz prestane aktualizovať, takže program nebude bežať dlhšie ako 30 sekúnd.

--- /task ---

--- task ---

**Ladenie**

Môj kód má chybu syntaxe alebo nefunguje podľa očakávania:

- Skontrolujte, či sa váš kód zhoduje s kódom v príkladoch vyššie
- Skontrolujte, či ste odsadili kód v slučke `for`
- Skontrolujte, či je váš zoznam obklopený znakmi `[` a `]`
- Skontrolujte, či sú jednotlivé farebné premenné v zozname oddelené čiarkou

Môj kód beží dlhšie ako 30 sekúnd:

- Znížte počet spustení slučky z 28 na 25 alebo dokonca na 20.
- Znížte dĺžku spánku z 1 sekundy na 0,5 sekundy.

--- /task ---

--- task ---

Pridajte `sense.clear()` na koniec kódu, aby ste vymazali obrázok na konci cyklu. To vám pomôže zistiť, kedy vaša animácia skončila.

**Tip:** uistite sa, že ste **neodsadili** riadok `sense.clear()` kódu, pretože chcete, aby sa to spustilo iba raz na konci vašej animácie.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 6
---
  # Zobrazte obrázok

  sense.set_pixels(obrazok)
  sleep(1) 
  
sense.clear()

--- /code ---

--- /task ---

--- task ---

**Test:** znova spustite kód. Keď váš projekt skončí, matica LED sa vymaže a všetky svetlá budú čierne (vypnuté).

--- /task ---

--- task ---

**Ladenie**

Matrica LED každú sekundu sčernie:

- Skontrolujte, či ste v slučke `for` neodsadili kód `sense.clear()`

--- /task ---

--- task ---

Pridajte kód na vymazanie matice LED na farbu podľa vášho výberu. Vytvorte premennú s názvom `x` na uloženie novej farby.

Môžete si namiešať vlastnú farbu alebo použiť hodnoty zo zoznamu farieb na vytvorenie novej farby `x`.

[[[generic-theory-simple-colours]]] 
[[[ambient-colours]]]

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 6-7
---
  # Zobrazte obrázok

  sense.set_pixels(obrazok)
  sleep(1) 

x = (178, 34, 34)  # vyberte si vlastné hodnoty červenej, zelenej a modrej medzi 0 - 255
sense.clear(x)

--- /code ---

--- /task ---

--- task ---

**Test:** znova spustite kód. Po dokončení vášho projektu sa matica LED zobrai vo vami zvolenej farbe. Farbu môžete zmeniť a potom otestovať toľkokrát, koľkokrát chcete.

--- /task ---

--- task ---

--- collapse ---

---
title: Dokončený príklad kódu
---

![Mriežka s 8 x 8 štvorcami zobrazujúca ružový kvet na zelenej stonke.](images/flower.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importujte knižnice
from sense_hat import SenseHat
from time import sleep

# Nastavte Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Nastavte snímač farieb
sense.color.gain = 60 # Nastavte snímač farieb
sense.color.integration_cycles = 64 # Interval, v ktorom sa bude realizovať snímanie

# Pridajte farebné premenné a obrázok

c = (0, 0, 0) # Čierna
m = (34, 139, 34) # Lesná zelená
q = (255, 255, 0) # Žltá
t = (255, 140, 0) # Tmavo oranžová
y = (255, 20, 147) # Tmavo ružová

for i in range(28):
  rgb = sense.color # získajte farbu zo snímača
  c = (rgb.red, rgb.green, rgb.blue)

  obrazok = [
    c, c, y, y, y, y, c, c,
    c, y, y, t, t, y, y, c,
    y, y, t, q, q, t, y, y,
    c, y, y, t, t, y, y, c,
    c, c, y, y, y, y, c, c,
    m, c, c, m, m, c, c, m,
    c, m, m, m, m, m, m, c,
    c, c, c, m, m, c, c, c]

  # Zobrazte obrázok

  sense.set_pixels(obrazok)
  sleep(1)

x = (178, 34, 34)  # vyberte si vlastné hodnoty červenej, zelenej a modrej medzi 0 - 255
sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
