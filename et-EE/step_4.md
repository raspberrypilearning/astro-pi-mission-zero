## Taju värvi

Selles etapis installid värvide helenduse anduri ja kasutad seda andurini jõudva punase, rohelise ja sinise koguse tuvastamiseks. Seda värvi kasutatakse seejärel sinu valitud pildi värvimiseks. Anduri juurde kõndiv sinises särgis astronaut näeks teistsugust pilti kui punases särgis astronaut.

![image displayed with a pink background on the LED matrix](images/colour_background.png)

Mis tahes pildi sa valid, taust kasutab `c` muutujat, mis on seadistatud mustana.

--- task ---

Kasuta oma tausta värvimiseks värviandurit.

Andurilt värvi saamiseks lisa pildiloendi ette kood ja muuda oma `c` taustavärvi muutujat, et musta asemel kasutaks Sense HAT värvianduri tajutavat värvi.

**Näpunäide:** Sa ei pea sisestama "#"-ga algavaid kommentaare (need on koodi selgitamiseks).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9-10
---
# Lisa värvi muutujad ja pilt

c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange y = (255, 20, 147) # DeepPink

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

**Test:** Liiguta värviliugur oma valitud värvile ja seejärel **käivita** enda kood. Sinu taustavärv muutub. Korda seda testi uuesti uue värviga.

**Näpunäide:** Iga kord, kui värvi muudad, pead klõpsama käsul "Käivita".

--- /task ---

## Silmusta oma programm

Astro Pi Mission Zero programmil on lubatud käitada kuni 30 sekundit. Kasutad seda aega värvianduri korduvaks kontrollimiseks ja pildi värskendamiseks.

Sinu kood kasutab `for` tsüklit 28 korda käitamiseks. **Iga** kord see:
+ tajub uusimat värvi
+ värskendab pildi taustavärvi
+ peatub üheks sekundiks

--- task ---

**Leia** oma `rgb = sense.color` koodirida.

**Lisa** kood selle ette, et installida oma `for` tsükkel `28` korduseks.

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

Nüüd pead taandama kogu koodi `for` tsükli alla, nii et see paigutuks `for` tsükli **sisse**.

**Näpunäide:** Mitme rea taandamiseks tõsta esile read, mida soovid taandada, seejärel vajuta oma klaviatuuril <kbd>Tab</kbd> klahvi (reeglina klaviatuuril <kbd>Caps Lock</kbd> klahvi kohal).

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

Lisa koodi allossa oma tsüklisse ühe sekundi pikkune `sleep`:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 4
---
  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Näpunäide:** Veendu, et see koodirida oleks sinu `for` tsüklisse taandatud.

--- /task ---

--- task ---

**Test:** Käita oma kood ja muuda projekti käitamise ajal värvivalijat mitu korda. Kontrolli, kas sinu pilti värskendatakse, et kasutada tajutud värvi järgmisel käitamisel.

Pildi värskendamine lõpetatakse, kui tsükkel lõpeb, nii et programm ei tööta kauem kui 30 sekundit.

--- /task ---

--- task ---

**Silumine**

Minu koodis on süntaksiviga või see ei käivitu ootuspäraselt:

- Kontrolli, kas sinu kood ühtib ülaltoodud näidetes oleva koodiga
- Kontrolli, kas oled oma `for` tsüklis koodi taandanud
- Kontrolli, kas sinu loend on ümbritsetud `[` ja `]`-ga
- Check that each colour variable in the list is separated by a comma

My code runs for longer than 30 seconds:

- Decrease the number of times your for loop runs, from 28 to 25 or even 20.
- Decrease the length of the sleep, from 1 second to 0.5 seconds.

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

**Test:** Run your code again. When your project has finished running the LED matrix will clear, turning all the lights black (off).

--- /task ---

--- task ---

**Debug**

The LED matrix turns black every second:

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

**Test:** Run your code again. When your project has finished running the LED matrix will clear to your chosen colour. You can change then test the colour as many times as you want.

--- /task ---

--- task ---

--- collapse ---

---
title: Completed code example
---

![A grid with 8 x 8 squares showing a pink flower on a green stem.](images/flower.png)

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
