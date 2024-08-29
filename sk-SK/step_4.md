## Nasnímanie farby

V tomto kroku nastavíš snímač farebnej svietivosti a použiješ ho na nasnímanie množstva červenej, zelenej a modrej, ktoré sa dostáva na snímač. Táto farba sa potom použije na vyfarbenie zvoleného obrázka. Astronaut kráčajúci k snímaču v modrej košeli by videl iný obrázok ako astronaut v červenej košeli.

![Obrázok zobrazený s ružovým pozadím na LED matrici](images/colour_background.png)

Bez ohľadu na to, ktorý obrázok vyberieš, pozadie používa premennú `c`, ktorá je nastavená na čiernu.

--- task ---

Na vyfarbenie pozadia použi snímač farieb.

Pridaj kód pred zoznam obrázkov, aby si získal/-a farbu zo snímača, a zmeň premennú farby pozadia `c` tak, aby namiesto čiernej používala farbu nasnímanú snímačom farieb modulu Sense HAT.

**Tip:** Nemusíš písať komentáre, ktoré sa začínajú znakom „#“ (sú tu na vysvetlenie kódu).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9, 10
---

# Pridajte farebné premenné a obrázok

a = (255, 255, 255) # White c = (0, 0, 0) # Black f = (25, 25, 112) # MidnightBlue m = (34, 139, 34) # ForestGreen

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ m, m, m, m, m, c, c, c, m, f, m, f, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, a, c, c, c, a, m, m, c, c, c ,c ,c ,c, m, m, c, c, c, a, c, c, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]


--- /code ---

--- /task ---

--- task ---

**Test:** Posuň posúvač farieb na farbu podľa vlastného výberu a potom **spusti**. Farba pozadia sa zmení. Zopakuj tento test s novou farbou.

**Tip:** Pri každej zmene farby treba kliknúť na „Spustiť“.

--- /task ---

## Zopakuj svoj program v slučke

Program Astro Pi Mission Zero môže bežať až 30 sekúnd. Tento čas využiješ na opakovanú kontrolu snímača farieb a aktualizáciu obrázka.

Tvoj kód použije slučku `for` a spustí sa 28-krát. **Zakaždým**:
+ Nasníma najnovšiu farbu
+ Aktualizuje farbu obrázka
+ Pozastaví sa na jednu sekundu

--- task ---

**Nájdi** riadok kódu`rgb = sense.color`.

**Pridaj** kód nadeň a nastav slučku `for` na `28` opakovaní.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ m, m, m, m, m, c, c, c, m, f, m, f, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, a, c, c, c, a, m, m, c, c, c ,c ,c ,c, m, m, c, c, c, a, c, c, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]


--- /code ---

--- /task ---

--- task ---

Teraz musíš odsadiť celý kód pod slučkou `for` tak, aby sa nachádzal **vnútri** slučky `for`.

**Tip:** Ak chceš odsadiť viacero riadkov, zvýrazni riadky, ktoré chceš odsadiť, a potom stlač kláves <kbd>Tab</kbd> na klávesnici (zvyčajne nad klávesom <kbd>Caps Lock</kbd> na klávesnici).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ m, m, m, m, m, c, c, c, m, f, m, f, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, a, c, c, c, a, m, m, c, c, c ,c ,c ,c, m, m, c, c, c, a, c, c, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]


  # Display the image

  sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

V spodnej časti kódu pridaj do slučky príkaz `sleep` v dĺžke jednej sekundy:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 5
---

  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Tip:** Uisti sa, že tento riadok kódu je odsadený v rámci slučky `for`.

--- /task ---

--- task ---

**Test:** Spusti svoj kód a niekoľkokrát zmeň výber farby počas behu projektu. Skontroluj, či sa obrázok aktualizuje a pri ďalšom spustení použije nasnímanú farbu.

Po dokončení slučky sa obrázok prestane aktualizovať, aby program nebežal dlhšie ako 30 sekúnd.

--- /task ---

--- task ---

**Ladenie**

Môj kód má chybu syntaxe alebo nefunguje podľa očakávania:

- Skontroluj, či sa kód zhoduje s kódom v príkladoch vyššie
- Skontroluj, či je kód v slučke `for` odsadený
- Skontroluj, či je zoznam uzavretý v znakoch `[` a `]`
- Skontroluj, či sú jednotlivé farebné premenné v zozname oddelené čiarkou

Môj kód beží dlhšie ako 30 sekúnd:

- Zníž počet spustení slučky z 28 na 25 alebo dokonca na 20.
- Skráť pauzu z 1 sekundy na 0,5 sekundy.

--- /task ---

--- task ---

Pridaj príkaz `sense.clear()` na koniec kódu, aby sa na konci cyklu obrázok vymazal. Vďaka tomu zistíš, kedy sa animácia skončila.

**Tip:** Dávaj pozor, aby riadok kódu `sense.clear()` **nebol odsadený**, pretože chceš, aby sa spustil iba raz na konci animácie.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7
---

  # Display the image

  sense.set_pixels(image) sleep(1)

sense.clear()

--- /code ---

--- /task ---

--- task ---

**Test:** Znova spusti kód. Keď sa projekt skončí, LED matrica sa vymaže a všetky svetlá budú čierne (zhasnuté).

--- /task ---

--- task ---

**Ladenie**

LED matrica každú sekundu sčernie:

- Skontroluj, či v slučke `for` nie je kód `sense.clear()` odsadený

--- /task ---

--- task ---

Pridaj kód na vymazanie LED matrice na farbu podľa svojho výberu. Vytvor premennú s názvom `x` na uloženie novej farby.

Môžeš si namiešať vlastnú farbu alebo použiť hodnoty zo zoznamu farieb na vytvorenie novej farby `x`.

\[[[generic-theory-simple-colours]]\] \[[[ambient-colours\]]]

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7, 8
---

  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /task ---

--- task ---

**Test:** Znova spusti kód. Po dokončení projektu sa LED matrica zobrazí v tebou zvolenej farbe. Farbu môžete zmeniť a potom otestovať, koľkokrát chcete.

--- /task ---


--- task ---

**Ukladaj si priebeh**

Svoj program si môžeš uložiť do projektu Mission Starter zadaním názvu tímu, mien členov tímu a kódu triedy, ktorý si dostal/-a. Svoj program môžeš znova načítať na akomkoľvek zariadení s internetovým pripojením zadaním názvu tímu a kódu triedy.

![Snímka obrazovky tlačidla Uložiť v Mission Zero](images/save_button.png)

--- /task ---


--- task ---

--- collapse ---

---
title: Príklad hotového kódu
---

![Mriežka s 8 x 8 štvorcami zobrazujúcimi krokodíla.](images/croc.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Import the libraries
from sense_hat import SenseHat from time import sleep

# Set up the Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image

a = (255, 255, 255) # White c = (0, 0, 0) # Black f = (25, 25, 112) # MidnightBlue m = (34, 139, 34) # ForestGreen

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ m, m, m, m, m, c, c, c, m, f, m, f, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, a, c, c, c, a, m, m, c, c, c ,c ,c ,c, m, m, c, c, c, a, c, c, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]


  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
