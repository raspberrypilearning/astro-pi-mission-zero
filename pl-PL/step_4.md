## Wykrywanie koloru

W tym kroku przygotujesz czujnik jasności koloru i użyjesz go do wykrycia ilości czerwonego, zielonego i niebieskiego docierającego do czujnika. Ten kolor zostanie następnie użyty do pokolorowania wybranego obrazu. Astronauta podchodzący do czujnika w niebieskiej koszuli zobaczy inny obraz niż astronauta w czerwonej koszuli.

![obraz wyświetlany z różowym tłem na matrycy LED](images/colour_background.png)

Niezależnie jaki obrazek wybierzesz, tło używa zmiennej `c`, ustawionej na czerń.

--- task ---

Użyj czujnika koloru, aby pokolorować tło.

Dodaj kod przed listą obrazów, aby uzyskać kolor z czujnika i popraw zmienną koloru tła `c`, aby zamiast czerni użyć kolor wykrywany przez czujnik koloru Sense HAT.

**Wskazówka:** Nie musisz wpisywać komentarzy zaczynających się od '#' (są tam, aby wyjaśnić kod).

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 9-10
---
# Dodaj zmienne kolorów i obraz

c = (0, 0, 0) # Czarny
m = (34, 139, 34) # Leśny zielony
q = (255, 255, 0) # Żółty
t = (255, 140, 0) # Ciemny pomarańczowy
y = (255, 20, 147) # Głęboki różowy

rgb = sense.color # pobierz kolor z czujnika
c = (rgb.red, rgb.green, rgb.blue) # użyj odczytany kolor

obrazek = [
  c, c, y, y, y, y, c, c,
  c, y, y, t, t, y, y, c,
  y, y, t, q, q, t, y, y,
  c, y, y, t, t, y, y, c,
  c, c, y, y, y, y, c, c,
  m, c, c, m, m, c, c, m,
  c, m, m, m, m, m, m, c,
  c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

**Test:** Przesuń suwak koloru na wybrany kolor, a następnie **uruchom** swój kod. Twój kolor tła się zmieni. Powtórz ten test z innym kolorem.

**Wskazówka:** Będziesz musiał kliknąć 'Uruchom' za każdym razem, gdy zmienisz kolor.

--- /task ---

## Zapętl swój program

Program Astro Pi Mission Zero może działać maksymalnie 30 sekund. Wykorzystasz ten czas, aby wielokrotnie sprawdzać czujnik koloru i odświeżać obraz.

Twój kod użyje pętli `for`, aby uruchomić się 28 razy. **Za każdym** razem będzie:
+ odczytywał ostatni kolor
+ odświeżał kolor tła obrazka
+ zatrzymywał się na sekundę

--- task ---

**Znajdź** swoją linię kodu `rgb = sense.color`.

**Dodaj** powyższy kod, aby ustawić pętlę `for` na `28` powtórzeń.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---
for i in range(28):
rgb = sense.color # pobierz kolor z czujnika
c = (rgb.red, rgb.green, rgb.blue)

obrazek = [
  c, c, y, y, y, y, c, c,
  c, y, y, t, t, y, y, c,
  y, y, t, q, q, t, y, y,
  c, y, y, t, t, y, y, c,
  c, c, y, y, y, y, c, c,
  m, c, c, m, m, c, c, m,
  c, m, m, m, m, m, m, c,
  c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

Teraz musisz zrobić wcięcie w całym kodzie poniżej pętli `for`, aby znajdował się **wewnątrz** pętli `for`.

**Wskazówka:** Aby zrobić wcięcie wielu linii, zaznacz linie, które chcesz wciąć, a następnie naciśnij klawisz <kbd>Tab</kbd> na klawiaturze (zazwyczaj powyżej klawisza <kbd>Caps Lock</kbd>).

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 2 - 17
---
for i in range(28):
  rgb = sense.color # pobierz kolor z czujnika
  c = (rgb.red, rgb.green, rgb.blue)

  obrazek = [
    c, c, y, y, y, y, c, c,
    c, y, y, t, t, y, y, c,
    y, y, t, q, q, t, y, y,
    c, y, y, t, t, y, y, c,
    c, c, y, y, y, y, c, c,
    m, c, c, m, m, c, c, m,
    c, m, m, m, m, m, m, c,
    c, c, c, m, m, c, c, c]
    
  # Wyświetl obraz

  sense.set_pixels(obrazek)
 
--- /code ---

--- /task ---

--- task ---

Na dole kodu w swojej pętli dodaj instrukcję `sleep` na jedną sekundę:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 4
---
  # Wyświetl obraz

  sense.set_pixels(obrazek)
  sleep(1)  

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
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 6
---
  # Wyświetl obraz

  sense.set_pixels(obrazek)
  sleep(1) 
  
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

[[[generic-theory-colours]]]

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 6-7
---
  # Wyświetl obraz

  sense.set_pixels(obrazek)
  sleep(1) 

x = (178, 34, 34)  # wybierz własne wartości czerwonego, zielonego i niebieskiego od 0 do 255
sense.clear(x)

--- /code ---

--- /task ---

--- task ---

**Test:** Uruchom kod ponownie. Kiedy Twój projekt zakończy działanie, matryca LED zmieni kolor na wybrany przez Ciebie. Możesz zmienić, a następnie przetestować kolor tyle razy, ile chcesz.

--- /task ---

--- task ---

--- collapse ---

---
title: Ukończony przykład kodu
---

![Siatka 8 x 8 kwadratów przedstawiająca różowy kwiat na zielonej łodydze.](images/flower.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Wczytaj biblioteki
from sense_hat import SenseHat
from time import sleep

# Przygotuj Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Przygotuj czujnik kolorów
sense.color.gain = 60 # Ustaw czułość czujnika
sense.color.integration_cycles = 64 # Okres czasu, w którym będzie dokonywany odczyt

# Dodaj zmienne kolorów i obraz

c = (0, 0, 0) # Czarny
m = (34, 139, 34) # Leśny zielony
q = (255, 255, 0) # Żółty
t = (255, 140, 0) # Ciemny pomarańczowy
y = (255, 20, 147) # Głęboki różowy

for i in range(28):
  rgb = sense.color # pobierz kolor z czujnika
  c = (rgb.red, rgb.green, rgb.blue)

  obrazek = [
    c, c, y, y, y, y, c, c,
    c, y, y, t, t, y, y, c,
    y, y, t, q, q, t, y, y,
    c, y, y, t, t, y, y, c,
    c, c, y, y, y, y, c, c,
    m, c, c, m, m, c, c, m,
    c, m, m, m, m, m, m, c,
    c, c, c, m, m, c, c, c]

  # Wyświetl obraz

  sense.set_pixels(obrazek)
  sleep(1)

x = (178, 34, 34)  # wybierz własne wartości czerwonego, zielonego i niebieskiego od 0 do 255
sense.clear(x)


--- /code ---

--- /collapse ---

--- /task ---
