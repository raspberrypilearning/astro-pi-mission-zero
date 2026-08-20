## Wykryj kolor

W tym kroku skonfigurujesz czujnik koloru i jasności. Użyjesz tego czujnika do zmierzenia ilości światła czerwonego, zielonego i niebieskiego docierającego do czujnika. Te wartości zostaną następnie użyte do zmiany jednego z kolorów na wybranym przez Ciebie obrazku.

Oznacza to, że obrazek może się zmieniać w zależności od tego, co widzi czujnik. Na przykład astronauta w niebieskiej koszulce zobaczy inną wersję obrazka niż astronauta w czerwonej koszulce.

Na obrazku wieloryba, którego użyliśmy w poprzednim kroku, kolor tła był czarny. Do przechowania jego kodu koloru RGB użyliśmy zmiennej `c`:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Użyj czujnika koloru, aby zmienić jeden ze swoich kolorów.

Pod liniami, w których definiujesz kolory, dodaj następujący kod:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4
---
# Wykryj kolor
rgb = sense.color # pobierz kolor z czujnika
c = (rgb.red, rgb.green, rgb.blue) # użyj odczytany kolor

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
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
obrazek = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(obrazek)

# Dodatkowe obrazki / klatki umieść tutaj:

obrazek2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

Na samym dole pliku z kodem ustaw pętlę `for`, aby powtórzyła się `14` razy i naprzemiennie wyświetlała `obrazek` i `obrazek2`, zatrzymując się na 1 sekundę przy każdej klatce.

**Wskazówka:** Upewnij się, że linie kodu pod `for i in range(14):` są wcięte o spację, dzięki czemu znajdą się **wewnątrz** bloku pętli.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
obrazek2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Powtórz 14 razy (14 * 2 sekundy = 28 sekund całej animacji)
for i in range(14):
  # Wyświetl drugi obrazek
  sense.set_pixels(obrazek2)
  sleep(1)

  # Wyświetl pierwszy obrazek
  sense.set_pixels(obrazek)
  sleep(1)
  
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
sense.color.integration_cycles = 64 # Interwał, w którym będzie wykonywany odczyt

# Dodaj zmienne kolorów i obraz
a = (255, 255, 255) # Biały
c = (0, 0, 0)       # Czarny
f = (36, 128, 200)  # Błękit oceanu
g = (0, 204, 255)   # Błękit nieba

# Wykryj kolor
rgb = sense.color # pobierz kolor z czujnika
c = (rgb.red, rgb.green, rgb.blue)

obrazek = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(obrazek)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Ukończony przykład kodu z wielorybem (z animacją)
---

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
sense.color.integration_cycles = 64 # Interwał, w którym będzie wykonywany odczyt

# Dodaj zmienne kolorów i obraz
a = (255, 255, 255) # Biały
c = (0, 0, 0)       # Czarny
f = (36, 128, 200)  # Błękit oceanu
g = (0, 204, 255)   # Błękit nieba

# Wykryj kolor
rgb = sense.color # pobierz kolor z czujnika
c = (rgb.red, rgb.green, rgb.blue)

obrazek = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(obrazek)

# PODSTAWOWE ZGŁOSZENIE jest już gotowe

# Dodatkowe obrazki / klatki umieść tutaj:
obrazek2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Powtórz 14 razy (14 * 2 sekundy = 28 sekund całej animacji)
for i in range(14):
  # Wyświetl drugi obrazek
  sense.set_pixels(obrazek2)
  sleep(1)

  # Wyświetl pierwszy obrazek
  sense.set_pixels(obrazek)
  sleep(1)
  
--- /code ---

--- /collapse ---

--- /task ---

