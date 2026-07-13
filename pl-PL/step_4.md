## Wykryj kolor

In this step, you will set up the colour and brightness sensor. W tym kroku przygotujesz czujnik jasności koloru i użyjesz go do wykrycia ilości czerwonego, zielonego i niebieskiego docierającego do czujnika. Ten kolor zostanie następnie użyty do pokolorowania wybranego obrazu.

This means that the image can change depending on what the sensor sees. Astronauta podchodzący do czujnika w niebieskiej koszuli zobaczy inny obraz niż astronauta w czerwonej koszuli.

In the whale image we used in the previous step, the background colour was black. We used the variable `c` to store its RGB colour code:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0) --- /code ---


--- task ---

Użyj czujnika koloru, aby pokolorować tło.

Underneath the lines where you define the colours, add the following code:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---
# odświeżał kolor tła obrazka
rgb = sense.color # pobierz kolor z czujnika c = (rgb.red, rgb.green, rgb.blue) # użyj odczytany kolor

This code replaces the RGB values stored in `c` with the values for the colour detected by the sensor.

Niezależnie od wybranego obrazu tło używa zmiennej `c`, ustawionej na kolor czarny. This will allow the sensor to change that colour instead.

--- task ---

**Test:** Przesuń suwak koloru na wybrany kolor, a następnie **uruchom** swój kod. Twój kolor tła się zmieni. Powtórz ten test z innym kolorem.

**Wskazówka:** Będziesz musiał kliknąć 'Uruchom' za każdym razem, gdy zmienisz kolor.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Now you have displayed an image and sensed a colour and used it in your program, and your code is ready for submission! 

You can save and submit your program using the form at the bottom of the code editor.
  
However, you may wish to add more images to your project, or make it come to life with animation. The next steps show you how to do this.
</p>

## Animate your project (optional)

Program Astro Pi Mission Zero może działać maksymalnie 30 sekund. Wykorzystasz ten czas, aby wielokrotnie sprawdzać czujnik koloru i odświeżać obraz.

--- task ---


**Wskazówka:** Upewnij się, że ten wiersz kodu jest wcięty w pętli `for`. Give it the variable name `image2` and change a few pixels to make your animation frame look different. Then add a short pause after it.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
---
obrazek = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

sense.set_pixels(image)

# Extra images / frames go here:

obrazek = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /code ---

--- /task ---

--- task ---

At the very bottom of your code file, set up your `for` loop to repeat `14` times and alternate between displaying `image` and `image2` pausing for 1 second on each frame.

**Wskazówka:** Aby zrobić wcięcie wielu linii, zaznacz linie, które chcesz wciąć, a następnie naciśnij klawisz <kbd>Tab</kbd> na klawiaturze (zazwyczaj powyżej klawisza <kbd>Caps Lock</kbd>).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7, 8
---
images/fish.png

sense.set_pixels(obrazek) sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  sense.set_pixels(obrazek) sleep(1)

--- /task ---

--- task ---

**Test:** Uruchom kod ponownie. Po zakończeniu pracy projekt wyczyści matrycę LED, wyłączając (off) wszystkie diody.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
If you would like to have more than two frames in your animation, you must make sure that the program will run for no more than 30 seconds. For example, if you have 10 images that each display for 1 second, you must change your `for` loop to repeat 3 times (10 * 3 = 30 seconds)
</p>

**Test:** Uruchom kod ponownie.

Mój kod zawiera błąd składni lub nie działa tak jak powinien:
- Sprawdź, czy masz wcięcia w kodzie pętli `for`
- Make sure you named your second image matrix `image2` and that it is placed outside and before the loop begins.
- Check that your `sleep` times are set to exactly `1` second to avoid running past the strict 30-second execution cutoff on the ISS.

--- /task ---

--- task ---

**Zapisz swoje postępy**

Możesz zapisać swój program w projekcie Mission Starter, wpisując nazwę swojego zespołu, imiona członków zespołu i otrzymany kod klasy. Możesz ponownie załadować swój program na dowolnym urządzeniu z dostępem do Internetu, wpisując nazwę swojego zespołu i kod klasy.

--- /task ---

--- collapse ---
---
title: Completed Whale code example
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
z = (153, 50, 204) # Ciemna orchidea q = (255, 255, 0) # Żółty d = (51, 153, 255) # Niebieski c = (0, 0, 0) # Czarny

# odczytywał ostatni kolor
for i in range(28): rgb = sense.color # pobierz kolor z czujnika c = (rgb.red, rgb.green, rgb.blue)

obrazek = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

--- /collapse ---
---
title: Ukończony przykład kodu
---

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Zapętl swój program
from sense_hat import SenseHat from time import sleep

# Przygotuj Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Dodaj kod przed listą obrazów, aby uzyskać kolor z czujnika i popraw zmienną koloru tła `c`, aby zamiast czerni użyć kolor wykrywany przez czujnik koloru Sense HAT.
for i in range(28): rgb = sense.color # pobierz kolor z czujnika c = (rgb.red, rgb.green, rgb.blue)

# Add colour variables and image
z = (153, 50, 204) # Ciemna orchidea q = (255, 255, 0) # Żółty d = (51, 153, 255) # Niebieski c = (0, 0, 0) # Czarny

# Wykryj kolor
for i in range(28): rgb = sense.color # pobierz kolor z czujnika c = (rgb.red, rgb.green, rgb.blue)

obrazek = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

sense.set_pixels(obrazek) sleep(1)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
images/savebutton_pl.png

sense.set_pixels(obrazek) sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1) --- /code --- --- /collapse --- --- /task ---
