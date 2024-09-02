## Získej hodnoty ze senzoru

V tomto kroku nastavíš senzor barev a svítivosti, který ti řekne, kolik červené, zelené a modré dopadá na senzor. Touto barvou se poté vybarví tvůj obrázek. Astronaut, který přijde k senzoru v modrém tričku, uvidí jiný obrázek než astronaut v červeném tričku.

![Obrázek zobrazený s růžovým pozadím na LED matici.](images/colour_background.png)

Ať už si vybereš jakýkoli obrázek, pozadí používá proměnnou `c`, která je nastavená na černou.

--- task ---

Použij senzor barev k vybarvení pozadí.

Před seznam s obrázkem přidej kód, díky němuž získáš naměřenou barvu ze senzoru, a změň proměnnou `c` s pozadím na barvu, kterou zachytil senzor barev desky Sense HAT.

**Tip:** Nemusíš psát komentáře, které začínají „#“ (slouží pouze k vysvětlení daného kódu).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9, 10
---

# Přidej proměnné s barvami a obrázek

a = (255, 255, 255) # White c = (0, 0, 0) # Black f = (25, 25, 112) # MidnightBlue m = (34, 139, 34) # ForestGreen

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ m, m, m, m, m, c, c, c, m, f, m, f, m, m, m, m, m, m, m, m, m, m, m, m, m, m, c, a, c, c, c, a, m, m, c, c, c ,c ,c ,c, m, m, c, c, c, a, c, c, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]


--- /code ---

--- /task ---

--- task ---

**Test:** Pomocí nástroje pro výběr barvy si zvol barvu, která se ti líbí, a pak svůj kód **spusť**. Barva tvého pozadí se změní. Opakuj tento test s novou barvou.

**Tip:** Po každé změně barvy musíš kliknout na tlačítko „Spustit“.

--- /task ---

## Přidej do svého programu cyklus

Program výzvy Astro Pi Mission Zero může běžet po dobu až 30 sekund. Využij této doby a opakovaně kontroluj senzor barev, a aktualizuj tak svůj obrázek.

Tvůj kód použije cyklus `for`, aby se spustil 28krát. Během **každého** opakování:
+ naměří poslední barvu,
+ aktualizuje pozadí obrázku,
+ se zastaví na jednu sekundu.

--- task ---

**Najdi** řádek kódu obsahující `rgb = sense.color`.

**Přidej** kód nad něj a nastav cyklus `for` na `28` opakování.

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

Všechen svůj kód teď musíš odsadit pod cyklus `for` tak, aby se nacházel **uvnitř** těla tohoto cyklu.

**Tip:** Pokud chceš odsadit více řádků, označ dané řádky a stiskni klávesu <kbd>Tab</kbd> (většinou nad klávesou <kbd>Caps Lock</kbd>).

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

Na konec cyklu přidej funkci `sleep` s délkou trvání jedné sekundy:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 5
---

  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Tip:** Ujisti se, že tento řádek kódu je v cyklu `for` odsazený.

--- /task ---

--- task ---

**Test:** Spusť svůj kód a pomocí nástroje pro výběr barvy několikrát změn barvu. Zkontroluj, jestli se tvůj obrázek změnil a jestli používá při dalším opakování naměřenou barvu.

Po dokončení cyklu se obrázek přestane aktualizovat, aby tvůj program neběžel déle než 30 sekund.

--- /task ---

--- task ---

**Ladění**

Můj kód má chyby v syntaxi nebo neběží, jak by měl:

- Zkontroluj si, jestli tvůj kód odpovídá kódu v příkladech uvedených výše.
- Zkontroluj si, jestli je tvůj kód uvnitř cyklu `for` správně odsazený.
- Zkontroluj si, jestli je tvůj seznam ohraničený závorkami `[` a `]`.
- Zkontroluj si, jestli je každá proměnná s barvou oddělená čárkou.

Můj kód běží déle než 30 sekund:

- Sniž počet opakování cyklu `for` z 28 na 25 nebo třeba na 20.
- Sniž dobu trvání funkce `sleep` z 1 sekundy na 0,5 sekundy.

--- /task ---

--- task ---

Na konec svého kódu přidej řádek `sense.clear()`, který po dokončení cyklu obrázek vyklidí. Díky němu uvidíš, kdy tvoje animace skončila.

**Tip:** Ujisti se, že řádek `sense.clear()` **není** odsazený, protože ho chceš spustit pouze jednou, a to na konci své animace.

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

**Test:** Spusť svůj kód znovu. Jakmile tvůj projekt doběhne, LED matice se vyklidí, čímž všechna světla zčernají (vypnou se).

--- /task ---

--- task ---

**Ladění**

LED matice každou sekundu zčerná:

- Zkontroluj si, jestli řádek `sense.clear()` není odsazený, a nenachází se tak v cyklu `for`.

--- /task ---

--- task ---

Přidej kód, který vyklidí LED matici na barvu dle tvého výběru. Vytvoř proměnnou `x`, do které uložíš novou barvu.

K vytvoření proměnné `x` si můžeš namíchat svoji vlastní barvu nebo použít hodnoty ze seznamu barev.

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

**Test:** Spusť svůj kód znovu. Jakmile tvůj projekt doběhne, LED matice se vyklidí na tebou zvolenou barvu. Barvu můžeš měnit a testovat, kolikrát jen chceš.

--- /task ---


--- task ---

**Ulož si svůj postup**

Svůj program můžeš uložit do startovacího projektu výzvy zadáním názvu týmu, jmen členů týmu a kódu třídy, který ti byl přidělen. Program můžeš načíst na jakémkoli zařízení s připojením k internetu tak, že zadáš název týmu a kód třídy.

![Snímek obrazovky z výzvy Mission Zero s tlačítkem pro uložení.](images/mz_savebutton_v2.png)

--- /task ---


--- task ---

--- collapse ---

---
title: Příklad dokončeného kódu
---

![Mřížka o velikosti 8 × 8, na které je krokodýl.](images/croc.png)

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
