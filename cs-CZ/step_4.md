## Získej hodnoty ze senzoru

V tomto kroku nastavíš senzor barev a svítivosti. Tento senzor budeš používat k naměření množství červeného, zeleného a modrého světla, které na něho dopadá. Tyto hodnoty pak budou použity ke změně jedné z barev na tvém obrázku.

To znamená, že obrázek se může měnit podle toho, co senzor vidí. Například astronaut v modrém tričku uvidí jinou verzi obrázku než astronaut v červeném tričku.

Barva pozadí obrázku s velrybou v minulém kroku byla černá. Použili jsme proměnnou `c`, do které jsme uložili kód barvy RGB:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Použij barevný senzor a změň jednu ze svých barev.

Pod řádky, kde definuješ barvy, přidej následující kód:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

--- /code ---

--- /task ---

Tento kód nahrazuje hodnoty RGB uložené v proměnné `c` hodnotami naměřenými barevným senzorem.

Tip: Pokud ve svém obrázku nepoužíváš proměnnou `c`, nahraď `c` jednou z proměnných barev, které používáš. Díky tomu bude moci senzor změnit danou barvu.

--- task ---

**Test:** Pomocí nástroje pro výběr barvy si zvol barvu, která se ti líbí, a pak svůj kód **spusť**. Barva tvého pozadí se změní. Opakuj tento test s novou barvou.

**Tip:** Po každé změně barvy musíš kliknout na tlačítko „Spustit“.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Podařilo se ti zobrazit obrázek, rozpoznat barvu a použít ji ve svém programu, a tvůj kód je tak připraven k odevzdání! 

Program můžeš uložit a odeslat pomocí formuláře v dolní části editoru kódu.
  
Možná však budeš chtít do svého projektu přidat další obrázky nebo ho oživit animacemi. V následujících krocích se dozvíš, jak na to.
</p>

## Naanimuj svůj projekt (nepovinné)

Tvůj program Mission Zero může na Mezinárodní vesmírné stanici (ISS) běžet po dobu až 30 sekund. Tento čas můžeš využít k zobrazení animace na LED matici tak, že budeš přepínat mezi dvěma nebo více obrázky.

--- task ---


Těsně pod řádek `sense.set_pixels(obrazek)` **přidej** svůj druhý obrázek. Pojmenuj proměnnou jako `obrazek2` a změň pár pixelu, aby tvůj snímek animace vypadal jinak. Pak za ním přidej krátkou pauzu.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# Extra images / frames go here:

image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

Na samém konci souboru s kódem nastav smyčku `for` tak, aby se opakovala `14`krát a střídala mezi proměnnými `obrazek` a `obrazek2`, přičemž na každém snímku se zastaví na 1 sekundu.

**Tip:** Ujisti se, že řádky kódu pod `for i in range(14):` jsou odsazeny mezerou, aby se nacházely **uvnitř** bloku smyčky.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1)

--- /code ---

--- /task ---

--- task ---

**Test:** Spusť svůj kód znovu. Tvůj program okamžitě zobrazí naměřenou barvu a poté bude pomocí smyčky přepínat tam a zpátky, čímž vznikne animovaný obrázek.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Pokud ve své animaci chceš mít více než dva snímky, musíš zajistit, aby program běžel po dobu maximálně 30 sekund. Například pokud máš 10 obrázků, z nichž každý se zobrazí na 1 sekundu, musíš smyčku „for“ nastavit tak, aby se opakovala 3krát (10 × 3 = 30 sekund).
</p>

--- task ---

**Zkontroluj chyby**

Můj kód má chyby v syntaxi nebo nemění snímky:
- Zkontroluj, že tvůj kód pro smyčku `for` má stejné odsazení jako v příkladu.
- Ujisti se, že se tvůj druhý obrázek jmenuje `obrazek2` a že je umístěný mimo smyčku a před ní.
- Podívej se, že řádky se `sleep` jsou nastaveny přesně na `1` sekundu, aby nedošlo k překročení 30sekundového limitu na ISS.

--- /task ---

--- task ---

**Ulož si svůj postup**

Svůj program můžeš uložit do startovacího projektu výzvy zadáním názvu týmu, jmen členů týmu a kódu třídy, který ti byl přidělen. Program můžeš načíst na jakémkoli zařízení s připojením k internetu tak, že zadáš název týmu a kód třídy.

--- /task ---

--- task ---

--- collapse ---
---
title: Příklad dokončeného kódu s velrybou
---

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
a = (255, 255, 255) # White c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Příklad dokončeného kódu s velrybou (včetně animace)
---

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
a = (255, 255, 255) # White c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1)

--- /code ---

--- /collapse ---

--- /task ---
