## Wykryj kolor

W tym kroku skonfigurujesz czujnik koloru i jasności. Użyjesz tego czujnika do zmierzenia ilości światła czerwonego, zielonego i niebieskiego docierającego do czujnika. Te wartości zostaną następnie użyte do zmiany jednego z kolorów na wybranym przez Ciebie obrazku.

Oznacza to, że obrazek może się zmieniać w zależności od tego, co widzi czujnik. Na przykład astronauta w niebieskiej koszulce zobaczy inną wersję obrazka niż astronauta w czerwonej koszulce.

Na obrazku wieloryba, którego użyliśmy w poprzednim kroku, kolor tła był czarny. Do przechowania jego kodu koloru RGB użyliśmy zmiennej `c`:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Użyj czujnika koloru, aby zmienić jeden ze swoich kolorów.

Pod liniami, w których definiujesz kolory, dodaj następujący kod:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

--- /code ---

--- /task ---

Ten kod zastępuje wartości RGB przechowywane w zmiennej `c` wartościami koloru wykrytego przez czujnik.

Wskazówka: Jeśli nie użyłeś zmiennej `c` na swoim obrazku, zastąp `c` jedną ze zmiennych kolorów, których użyłeś. Dzięki temu czujnik zmieni zamiast niej ten kolor.

--- task ---

**Test:** Przesuń suwak koloru na wybrany kolor, a następnie **uruchom** swój kod. Twój kolor tła się zmieni. Powtórz ten test z innym kolorem.

**Wskazówka:** Będziesz musiał kliknąć 'Uruchom' za każdym razem, gdy zmienisz kolor.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Wyświetliłeś już obrazek, odczytałeś kolor i wykorzystałeś go w swoim programie — Twój kod jest gotowy do przesłania! 

Możesz zapisać i przesłać swój program za pomocą formularza znajdującego się na dole edytora kodu.
  
Możesz jednak dodać do swojego projektu więcej obrazków lub ożywić go animacją. Kolejne kroki pokażą Ci, jak to zrobić.
</p>

## Animuj swój projekt (opcjonalnie)

Twój program Mission Zero może działać na Międzynarodowej Stacji Kosmicznej (ISS) maksymalnie przez 30 sekund. Możesz wykorzystać ten czas działania do wyświetlenia animacji na matrycy LED, przełączając się między dwoma lub więcej różnymi obrazkami.

--- task ---


**Dodaj** drugi obrazek bezpośrednio pod linią kodu `sense.set_pixels(obrazek)`. Nadaj mu nazwę zmiennej `obrazek2` i zmień kilka pikseli, aby klatka animacji wyglądała inaczej. Następnie dodaj po nim krótką pauzę.

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

Na samym dole pliku z kodem ustaw pętlę `for`, aby powtórzyła się `14` razy i naprzemiennie wyświetlała `obrazek` i `obrazek2`, zatrzymując się na 1 sekundę przy każdej klatce.

**Wskazówka:** Upewnij się, że linie kodu pod `for i in range(14):` są wcięte o spację, dzięki czemu znajdą się **wewnątrz** bloku pętli.

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

**Test:** Uruchom kod ponownie. Twój program natychmiast wyświetli wykryty kolor, a następnie będzie przełączał się tam i z powrotem, tworząc animację.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Jeśli chcesz mieć w swojej animacji więcej niż dwie klatki, musisz upewnić się, że program nie będzie działał dłużej niż 30 sekund. Na przykład, jeśli masz 10 obrazków, z których każdy wyświetla się przez 1 sekundę, musisz zmienić pętlę `for` tak, aby powtórzyła się 3 razy (10 * 3 = 30 sekund)
</p>

--- task ---

**Sprawdzanie błędów**

Mój kod ma błąd składni lub nie zmienia klatek:
- Sprawdź, czy kod Twojej pętli `for` ma takie same wcięcia jak w przykładzie.
- Upewnij się, że nazwałeś swoją drugą matrycę obrazka `obrazek2` i że znajduje się ona poza pętlą, przed jej rozpoczęciem.
- Sprawdź, czy Twoje czasy `sleep` są ustawione na dokładnie `1` sekundę, aby nie przekroczyć ścisłego 30-sekundowego limitu wykonania na ISS.

--- /task ---

--- task ---

**Zapisz swoje postępy**

Możesz zapisać swój program w projekcie Mission Starter, wpisując nazwę swojego zespołu, imiona członków zespołu i otrzymany kod klasy. Możesz ponownie załadować swój program na dowolnym urządzeniu z dostępem do Internetu, wpisując nazwę swojego zespołu i kod klasy.

--- /task ---

--- task ---

--- collapse ---
---
title: Ukończony przykład kodu z wielorybem
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
title: Ukończony przykład kodu z wielorybem (z animacją)
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
