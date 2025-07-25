## Wykryj kolor

W tym kroku przygotujesz czujnik jasności koloru i użyjesz go do wykrycia ilości czerwonego, zielonego i niebieskiego docierającego do czujnika. Ten kolor zostanie następnie użyty do pokolorowania wybranego obrazu. Astronauta podchodzący do czujnika w niebieskiej koszuli zobaczy inny obraz niż astronauta w czerwonej koszuli.

![obraz wyświetlany z różowym tłem na matrycy LED](images/colour_background.png)

Niezależnie jaki obrazek wybierzesz, tło używa zmiennej `c`, ustawionej na czerń.

--- task ---

Użyj czujnika koloru, aby pokolorować tło.

Dodaj kod przed listą obrazów, aby uzyskać kolor z czujnika i popraw zmienną koloru tła `c`, aby zamiast czerni użyć kolor wykrywany przez czujnik koloru Sense HAT.

**Wskazówka:** Nie musisz wpisywać komentarzy zaczynających się od '#' (są tam, aby wyjaśnić kod).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9, 10
---

# Dodawanie koloru

a = (255, 255, 255) # Biały c = (0, 0, 0) # Czarny f = (25, 25, 112) # Nocny niebieski m = (34, 139, 34) # Leśny zielony

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


--- /code ---

--- /task ---

--- task ---

**Test:** Przesuń suwak koloru na wybrany kolor, a następnie **uruchom** swój kod. Twój kolor tła się zmieni. Powtórz ten test z innym kolorem.

**Wskazówka:** Będziesz musiał kliknąć 'Uruchom' za każdym razem, gdy zmienisz kolor.

--- /task ---

## Zapętl swój program

Program Astro Pi Misja Zero może działać maksymalnie 30 sekund. Wykorzystasz ten czas, aby wielokrotnie sprawdzać czujnik koloru i odświeżać obraz.

Twój kod użyje pętli `for`, aby uruchomić się 28 razy. **Za każdym** razem będzie:
+ odczytywał ostatni kolor
+ odświeżał kolor tła obrazka
+ zatrzymywał się na sekundę

--- task ---

**Znajdź** swoją linię kodu `rgb = sense.color`.

**Dodaj** powyższy kod, aby ustawić pętlę `for` na `28` powtórzeń.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


--- /code ---

--- /task ---

--- task ---

Teraz musisz zrobić wcięcie w całym kodzie poniżej pętli `for`, aby znajdował się **wewnątrz** pętli `for`.

**Wskazówka:** Aby zrobić wcięcie wielu linii, zaznacz linie, które chcesz wciąć, a następnie naciśnij klawisz <kbd>Tab</kbd> na klawiaturze (zazwyczaj powyżej klawisza <kbd>Caps Lock</kbd>).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


  # Display the image

  sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Na dole kodu w swojej pętli dodaj instrukcję `sleep` na jedną sekundę:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 5
---

  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Wskazówka:** Upewnij się, że ten wiersz kodu jest wcięty w pętli `for`.

--- /task ---

--- task ---

**Test:** Uruchom swój kod i zmieniaj wybór kolorów kilkakrotnie w trakcie działania projektu. Sprawdź, czy obraz zmienił się, aby użyć wykrytego koloru przy następnym uruchomieniu.

Obraz przestanie się odświeżać po zakończeniu pętli, aby program nie działał dłużej niż 30 sekund.

--- /task ---

--- task ---

**Debugowanie (usuwanie błędów)**

Mój kod zawiera błąd składni lub nie działa tak jak powinien:

- Sprawdź, czy Twój kod pasuje do kodu w powyższych przykładach
- Sprawdź, czy masz wcięcia w kodzie pętli `for`
- Sprawdź, czy Twoja lista jest otoczona przez `[` i `]`
- Sprawdź, czy każda zmienna koloru na liście jest oddzielona przecinkiem

Mój kod działa dłużej niż 30 sekund:

- Zmniejsz liczbę uruchomień pętli for z 28 do 25, a nawet 20.
- Zmniejsz długość opóźnienia (sleep) z 1 sekundy do 0.5 sekundy.

--- /task ---

--- task ---

Dodaj `sense.clear()` na końcu kodu, aby wyczyścić obraz na końcu pętli. Pomoże ci to zobaczyć, kiedy twoja animacja się zakończyła.

**Wskazówka:** Upewnij się, że **nie** wciąłeś linii kodu `sense.clear()`, ponieważ chcesz uruchomić tą funkcję tylko raz na końcu animacji.

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

**Test:** Uruchom kod ponownie. Po zakończeniu pracy projekt wyczyści matrycę LED, wyłączając (off) wszystkie diody.

--- /task ---

--- task ---

**Debugowanie**

Matryca LED staje się czarna co sekundę:

- Sprawdź, czy nie masz wcięcia w kodzie `sense.clear()` w pętli `for`

--- /task ---

--- task ---

Dodaj kod, aby wyczyścić matrycę LED na wybrany kolor. Utwórz zmienną o nazwie `x`, aby przechować nowy kolor.

Możesz mieszać własny kolor lub użyć wartości z listy kolorów, aby utworzyć swój nowy kolor `x`.

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

**Test:** Uruchom kod ponownie. Kiedy Twój projekt zakończy działanie, matryca LED zmieni kolor na wybrany przez Ciebie. Możesz zmienić, a następnie przetestować kolor tyle razy, ile chcesz.

--- /task ---


--- task ---

**Zapisz swoje postępy**

Możesz zapisać swój program w projekcie Mission Starter, wpisując nazwę swojego zespołu, imiona członków zespołu i otrzymany kod klasy. Możesz ponownie załadować swój program na dowolnym urządzeniu z dostępem do Internetu, wpisując nazwę swojego zespołu i kod klasy.

![Zrzut ekranu z przyciskiem „Zapisz” w Mission Zero](images/mz_savebutton_v2.png)

--- /task ---


--- task ---

--- collapse ---

---
title: Ukończony przykład kodu
---

![Siatka złożona z kwadratów 8 x 8 przedstawiających krokodyla.](images/fish.png)

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

# Zmień tekst pozdrowienia i kolor - jaką wiadomość wyślesz do astronautów na pokładzie ISS?

a = (255, 255, 255) # Biały c = (0, 0, 0) # Czarny f = (25, 25, 112) # Nocny niebieski m = (34, 139, 34) # Leśny zielony

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]


  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # wybierz własne wartości czerwonego, zielonego i niebieskiego od 0 do 255 sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
