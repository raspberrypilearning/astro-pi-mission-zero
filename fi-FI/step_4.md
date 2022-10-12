## Tunnista väri

Tässä vaiheessa määrität värin kirkkausanturin ja käytät sitä tunnistaaksesi punaisen, vihreän ja sinisen määrät anturissa. Tätä väriä käytetään sitten valitsemasi kuvan värittämiseen. Astronautti, joka kävelee anturin luo sinisessä paidassa, näkisi erilaisen kuvan kuin punaisessa paidassa oleva astronautti.

![kuva näkyy vaaleanpunaisella taustalla LED-matriisissa](images/colour_background.png)

Riippumatta valitsemastasi kuvasta, tausta käyttää `c` muuttujaa, joka on asetettu mustaksi.

--- task ---

Käytä värianturia värittääksesi taustasi.

Lisää koodi kuvalistasi eteen saadaksesi värin anturilta ja muuta taustavärisi muuttuja `c` käyttääksesi Sense HATin värianturin tunnistamaa väriä mustan sijasta.

**Vinkki:** Sinun ei tarvitse kirjoittaa #-alkuisia kommentteja (ne ovat siellä koodin selittämiseksi).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9-10
---
# Lisää värimuuttujia ja kuva

c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange y = (255, 20, 147) # DeepPink

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

**Kokeile:** Siirrä värin liukusäädin valitsemaasi väriin ja sitten **aja** koodisi. Taustavärisi muuttuu. Toista tämä kokeilu uudella värillä.

**Vinkki:** Sinun on napsautettava 'Aja' aina, kun muutat väriä.

--- /task ---

## Aja ohjelmaasi silmukassa

Astro Pi Mission Zero -ohjelma saa olla ajossa enintään 30 sekuntia. Käytät tämän ajan toistuvasti värianturin tarkastamiseen ja kuvan päivittämiseen.

Koodisi käyttää `for`-silmukkaa ajaakseen 28 kertaa. **Joka** kerta se:
+ tunnistaa uusimman värin
+ päivittää kuvan taustavärin
+ odottaa yhden sekunnin

--- task ---

**Etsi** sinun `rgb = sense.color` koodirivi.

**Lisää** koodi sen yläpuolelle määrittääksesi `for` -silmukan `28` toistolle.

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

Sinun on nyt sisennettävä kaikki `for`-silmukan alapuolella oleva koodi niin, että se sijoittuu `for`-silmukan **sisälle**.

**Vinkki:** Sisentääksesi useita rivejä, ensin valitse sisennettävät rivit, sitten paina näppäimistösi <kbd>Tab</kbd>-näppäintä (yleensä <kbd>Caps Lock</kbd>-näppäimen yläpuolella).

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

**Debug**

My code has a syntax error or doesn't run as expected:

- Check that your code matches the code in the examples above
- Check that you have indented the code in your `for` loop
- Check that your list is surrounded by `[` and `]`
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

![8 x 8 neliön ruudukko esittämässä vaaleanpunaista kukkaa vihreässä varressa.](images/flower.png)

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
