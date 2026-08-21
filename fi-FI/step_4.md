## Tunnista väri

Tässä vaiheessa alustat väri- ja kirkkausanturin. Käytät tätä anturia mittaamaan anturiin saapuvan punaisen, vihreän ja sinisen valon määrää. Sitten niitä arvoja käytetään yhden värin muuttamiseen valitsemassasi kuvassa.

Tämä tarkoittaa, että kuva voi muuttua sen mukaan, mitä anturi näkee. Esimerkiksi siniseen paitaan pukeutunut astronautti näkisi kuvan eri version kuin punaiseen paitaan pukeutunut astronautti.

Edellisessä vaiheessa käyttämässämme valaskuvassa taustaväri oli musta. Käytimme muuttujaa `c` tallentaaksemme sen RGB-värikoodin:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Käytä värianturia muuttaaksesi yhtä väreistäsi.

Lisää seuraava koodi niiden rivien alle, joilla määrität värit:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

--- /code ---

--- /task ---

Tämä koodi korvaa `c` -kohtaan tallennetut RGB-arvot anturin havaitseman värin arvoilla.

Vinkki: Jos et käyttänyt muuttujaa `c` omassa kuvassasi, korvaa `c` jollakin käyttämistäsi värimuuttujista. Näin anturi voi vaihtaa kyseisen värin.

--- task ---

**Kokeile:** Siirrä värin liukusäädin valitsemaasi väriin ja sitten **aja** koodisi. Taustavärisi muuttuu. Toista tämä kokeilu uudella värillä.

**Vinkki:** Sinun on napsautettava 'Aja' aina, kun muutat väriä.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Nyt olet näyttänyt kuvan sekä tunnistanut värin ja käyttänyt sitä ohjelmassasi, joten koodisi on valmis lähetettäväksi! 

Voit tallentaa ja lähettää ohjelmasi koodieditorin alareunassa olevalla lomakkeella.
  
Voit kuitenkin halutessasi lisätä projektiisi lisää kuvia tai herättää sen eloon animaatioilla. Seuraavat vaiheet näyttävät, miten se tehdään.
</p>

## Animoi projektisi (valinnainen)

Mission Zero -ohjelmaasi ajetaan Kansainvälisellä avaruusasemalla (ISS) enintään 30 sekuntia. Voit käyttää tätä suoritusaikaa animaation näyttämiseen LED-matriisissa vaihtamalla kahden tai useamman eri kuvan välillä.

--- task ---


**Lisää** toinen kuva suoraan `sense.set_pixels(image)` -rivisi alle. Anna sille muuttujan nimi `image2` ja muuta joitain pikseleitä, jotta animaatiokehyksesi näyttää erilaiselta. Lisää sitten lyhyt tauko sen jälkeen.

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

Aseta kooditiedostosi aivan loppuun `for` -silmukka toistumaan `14` kertaa ja näyttämään vuorotellen `image` ja `image2` pysähtyen 1 sekunniksi jokaisen ruudun kohdalla.

**Vinkki:** Varmista, että rivin `for i in range(14):` alla olevat koodirivit ovat sisennetty välilyönnillä, jotta ne ovat silmukkalohkon **sisällä**.

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

**Kokeile:** Aja koodisi uudelleen. Ohjelmasi näyttää tunnistetun värisi välittömästi, ja toistaa sitten väriä edestakaisin animoituaa näkymää varten.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Jos haluat animaatiossasi olevan enemmän kuin kaksi ruutua, varmista, että ohjelma kestää enintään 30 sekuntia. Jos esimerkiksi sinulla on 10 kuvaa, joita kutakin näytetään 1 sekunnin ajan, sinun on muutettava `for`-silmukka toistumaan 3 kertaa (10 * 3 = 30 sekuntia)
</p>

--- task ---

**Tarkista virheet**

Koodissani on syntaksivirhe tai se ei vaihda ruutuja:
- Tarkista, että `for` -silmukan sisennys vastaa esimerkin sisennystä.
- Varmista, että toisen kuvamatriisin nimi on `image2` ja että se on sijoitettu silmukan ulkopuolelle ja ennen sen alkua.
- Tarkista, että `sleep` -aika on asetettu täsmälleen `1` sekunniksi, jotta vältytään ylittämästä tiukkaa 30 sekunnin suoritusaikarajaa ISS:llä.

--- /task ---

--- task ---

**Tallenna kehityksesi**

Voit tallentaa ohjelmasi tehtävän aloitusprojektissa syöttämällä joukkueesi nimen, joukkueen jäsenten nimet ja saamasi luokkahuonekoodin. Voit ladata ohjelman uudelleen millä tahansa laitteella, jossa on Internet-yhteys, syöttämällä joukkuenimen ja luokkahuonekoodin.

--- /task ---

--- task ---

--- collapse ---
---
title: Valmis valaskoodiesimerkki
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
title: Valmis valaskoodiesimerkki (animoituna)
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
