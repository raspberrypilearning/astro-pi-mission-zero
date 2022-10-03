## Přidej barvy

V tomto kroku nastavíš senzor barev a svítivosti, který ti řekne, kolik červené, zelené a modré dopadá na senzor. Touto barvou se poté vybarví tvůj obrázek. Astronaut, který přijde k senzoru v modrém tričku, uvidí jiný obrázek než astronaut v červeném tričku.

![obrázek zobrazený s růžovým pozadím na LED matici](images/colour_background.png)

Ať už si vybereš jakýkoli obrázek, pozadí používá proměnnou `c`, která je nastavená na černou.

--- task ---

Použij senzor barev k vybarvení pozadí.

Před seznam s obrázkem přidej kód, díky němuž získáš barvu ze senzoru, a změň barvu pozadí proměnné `c` na barvu, kterou zachytil senzor barev desky Sense HAT.

**Tip:** Nemusíš psát komentáře, které začínají „#“ (slouží pouze k vysvětlení daného kódu).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9-10
---
# Přidej proměnné s barvami a obrázek

c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange y = (255, 20, 147) # DeepPink

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

**Test:** Na posuvníku s barvou si vyber barvu, která se ti líbí, a pak svůj kód **spusť**. Barva tvého pozadí se změní. Opakuj tento test s novou barvou.

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
line_highlights: 1
---
for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

Všechen svůj kód teď musíš odsadit pod cyklus `for` tak, aby se nacházel **uvnitř** těla tohoto cyklu.

**Tip:** To indent multiple lines, highlight the lines you want to indent then press the <kbd>Tab</kbd> key on your keyboard (usually above the <kbd>Caps Lock</kbd> key on the keyboard).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2 - 17
---
for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

  # Display the image

  sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

At the bottom of your code, add a `sleep` of one second inside your loop:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 4
---
  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Tip:** Make sure this line of code is indented within your `for` loop.

--- /task ---

--- task ---

**Test:** Run your code and change the colour picker several times as your project is running. Check that your image updates to use the sensed colour on its next run.

The image will stop updating when the loop finishes so that the program doesn't run for more than 30 seconds.

--- /task ---

--- task ---

**Ladění**

Můj kód má chyby v syntaxi nebo neběží, jak by měl:

- Zkontroluj si, jestli tvůj kód odpovídá kódu v příkladech uvedených výše.
- Zkontroluj si, jestli je tvůj kód cyklu `for` správně odsazený.
- Zkontroluj si, jestli je tvůj seznam ohraničený závorkami `[` a `]`.
- Zkontroluj si, jestli je každá proměnná s barvou oddělená čárkou.

Můj kód běží déle než 30 sekund:

- Decrease the number of times your for loop runs, from 28 to 25 or even 20.
- Sniž dobu trvání funkce „sleep“ z 1 sekundy na 0,5 sekundy.

--- /task ---

--- task ---

Add `sense.clear()` at the end of your code to clear the image at the end of your loop. This will help you see when your animation has finished running.

**Tip:** Make sure you **do not** indent the `sense.clear()` line of code as you want this to only run once at the end of your animation.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 6
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

- Check that you have not indented the `sense.clear()` code within your `for` loop

--- /task ---

--- task ---

Add code to clear the LED matrix to a colour of your choice. Create a variable called `x` to store your new colour.

You can mix your own colour or use the values from the list of colours to create your new `x`colour.

\[[[generic-theory-simple-colours]]\] \[[[ambient-colours\]]]

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 6-7
---
  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /task ---

--- task ---

**Test:** Spusť svůj kód znovu. Jakmile tvůj projekt doběhne, LED matice se vyklidí a nastaví tebou zvolenou barvu. Barvu můžeš měnit a testovat, kolikrát jen chceš.

--- /task ---

--- task ---

--- collapse ---

---
title: Příklad dokončeného kódu
---

![Mřížka o velikosti 8 × 8, na které je fialová kytička se zeleným stonkem.](images/flower.png)

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

c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange y = (255, 20, 147) # DeepPink

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
