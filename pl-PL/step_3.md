## Wyświetl obrazek

Obrazek, który wyświetlisz, będzie się składał z 64 kolorowych kwadratów zwanych **pikselami**. Piksele są ułożone w siatkę 8 x 8. Każdy piksel może mieć inny kolor. Dobierając kolory starannie, możesz stworzyć obrazek. Oto przykład wieloryba stworzonego przy użyciu różnych odcieni niebieskiego na czarnym tle.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Matryca LED**</span> to siatka diod LED, które mogą być kontrolowane pojedynczo lub jako grupa, aby tworzyć różne efekty wyświetlania. Matryca LED na Sense HAT ma 64 diody LED wyświetlane w siatce 8 x 8. Diody LED mogą być zaprogramowane w celu uzyskania szerokiej gamy kolorów.
</p>

![obrazek wieloryba o rozmiarze 8x8 z literami oznaczającymi różne kolory](images/whale.png)

Zwróć uwagę, że każdy kwadrat jest oznaczony kodem reprezentującym określony kolor. Na tym obrazku użyto 3 kolorów:
+ c = czarny
+ f = błękit oceanu
+ g = błękit nieba


--- task ---

Otwórz [Projekt startowy Mission Zero](https://missions.astro-pi.org/pl/mz/code_submissions/){:target="_blank"}.

Zobaczysz, że kilka linijek kodu zostało dla Ciebie dodanych automatycznie.

Kod ten łączy się z Astro Pi, zapewnia odpowiedni sposób pracy wyświetlacza LED Astro Pi i przygotowuje czujnik koloru. Pozostaw ten kod, ponieważ będziesz go potrzebować.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Wczytaj biblioteki
from sense_hat import SenseHat from time import sleep

# Przygotuj Sense HAT
sense = SenseHat() sense.set_rotation(270, False)

# Przygotuj czujnik kolorów
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Zrzut ekranu emulatora Sense HAT z wierszami kodu startowego wyświetlanymi w lewym panelu.](images/sense-hat-emulator3.png)

--- /task ---

### Kolory RGB

Kolory można tworzyć przy użyciu różnych proporcji czerwieni, zieleni i niebieskiego. Dowiedz się więcej o kolorach RGB tutaj:

![Trzy suwaki pokazujące wartości kolorów RGB](images/rgbsliders.gif)

Matryca LED to siatka 8 x 8. Każda dioda świecąca na siatce może być ustawiona na inny kolor. Możemy używać liter od a do z jako nazw zmiennych reprezentujących 24 różne kolory. Każdy kolor ma wartość dla czerwonego, zielonego i niebieskiego.

--- collapse ---

---
title: Lista zmiennych kolorów
---

![Siatka 24 kolorowych kwadratów, z których każdy jest oznaczony inną literą alfabetu](images/palette.png)

```python
a = (255, 255, 255) # Biały
b = (171, 171, 171) # Szary
c = (0, 0, 0)       # Czarny
d = (25, 25, 113)   # Granatowy
e = (0, 0, 255)     # Czysty niebieski
f = (36, 128, 200)  # Błękit oceanu
g = (0, 204, 255)   # Błękit nieba
h = (86, 255, 255)  # Jaskrawy cyjan
j = (0, 255, 0)     # Czysta zieleń
k = (46, 139, 33)   # Zieleń liści
l = (57, 97, 17)    # Zieleń oliwkowa
m = (30, 65, 6)     # Zieleń lasu
n = (126, 88, 25)   # Brąz ziemisty
o = (179, 96, 65)   # Brąz terakotowy
p = (180, 34, 34)   # Czerwień ceglana
q = (255, 0, 0)     # Czysta czerwień
r = (232, 118, 5)   # Pomarańczowy
s = (241, 231, 100) # Bladożółty
t = (255, 255, 0)   # Czysta żółć
u = (255, 209, 209) # Blady róż
v = (255, 177, 177) # Pudrowy róż
w = (249, 169, 255) # Jasnoróżowy
y = (248, 97, 255)  # Magenta
z = (220, 53, 232)  # Fioletowy

```

--- /collapse ---

### Wybierz obraz

--- task ---

You can either choose one of the example images below or create your own original design. Feel free to draw anything you like - such as an animal, plant, or imaginary creature - as long as it follows the Mission Zero guidelines.

**Wybór:** Wybierz obraz do wyświetlenia spośród poniższych opcji. Python przechowuje informacje o obrazie na liście. Kod każdego obrazu zawiera użyte zmienne kolorów i listę.

Będziesz musiał **skopiować** cały kod wybranego obrazu, a następnie **wkleić** go do swojego projektu poniżej linii, która mówi `# Dodaj zmienne kolorów i obraz`.

--- collapse ---

---
title: Wieloryb
---

![Siatka 8 x 8 kwadratów przedstawiająca wieloryba.](images/whale.png)

Stworzone przez zespół Naicom, Włochy

```python
c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue

image = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, a,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

```

--- /collapse ---


--- collapse ---

---
title: Cytryna
---

![Siatka 8 x 8 kwadratów przedstawiająca cytrynę.](images/lemon.png)

Stworzone przez zespół g4lemoni, Grecja

```python
c = (0, 0, 0)       # Black
k = (46, 139, 33)   # Leaf Green
t = (255, 255, 0)   # Pure Yellow

image = [
c, c, c, k, k, c, c, c,
c, c, k, c, k, c, c, c,
c, k, c, t, t, c, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, t, t, t, t, c, c,
c, c, c, t, t, c, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Świnka
---

![Siatka 8 x 8 kwadratów przedstawiająca świnkę.](images/pig.png)

Stworzone przez Gary'ego, Wielka Brytania

```python
a = (255, 255, 255) # White
v = (255, 177, 177) # Blush Pink
y = (248, 97, 255)  # Magenta
o = (179, 96, 65)   # Terracotta Brown
c = (0, 0, 0)       # Black

image = [
a, a, y, a, a, y, a, a,
a, y, y, y, y, y, y, a,
a, y, c, y, c, y, y, y,
v, v, v, v, v, y, y, y,
v, o, v, o, v, y, y, y,
v, v, v, v, v, y, y, y,
a, y, y, y, y, y, y, y,
a, a, y, a, a, a, y, a]

```

--- /collapse ---


--- collapse ---
---
title: Burza
---

![Siatka 8 x 8 kwadratów przedstawiająca chmurę burzową.](images/storm.png)

Stworzone przez zespół hop2p023, Hiszpania

```python

c = (0, 0, 0)       # Black
f = (36, 128, 200)  # Ocean Blue
g = (0, 204, 255)   # Sky Blue
t = (255, 255, 0)   # Pure Yellow

image = [
c, c, c, c, c, c, c, c,
c, c, f, f, f, f, c, c,
c, f, f, f, f, f, f, c,
c, g, c, g, t, g, c, c,
c, c, c, t, t, c, c, c,
c, c, t, t, c, c, c, c,
c, c, g, c, c, c, c, g,
c, g, c, c, c, c, c, c]


```

--- /collapse ---

--- collapse ---
---
title: Kaczka
---

![Siatka 8 x 8 kwadratów przedstawiająca kaczkę.](images/duck.png)

Stworzone przez Petera, Irlandia

```python

c = (0, 0, 0) # Black
l = (57, 97, 17)    # Olive Green
m = (30, 65, 6)     # Forest Green
r = (232, 118, 5)   # Orange
a = (255, 255, 255) # White
b = (171, 171, 171) # Grey

image = [
c, l, l, c, c, c, c, c,
r, r, m, c, c, c, c, c,
c, l, l, c, c, c, c, c,
c, a, a, l, a, a, c, c,
c, l, l, a, a, a, b, a,
c, a, a, b, b, b, a, a,
c, c, a, a, a, a, c, c,
c, c, c, r, c, r, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Żaba
---

![Siatka 8 x 8 kwadratów przedstawiająca żabę.](images/frog.png)

Stworzone przez zespół Jmeno, Czechy

```python

a = (255, 255, 255) # White
b = (171, 171, 171) # Grey
c = (0, 0, 0)       # Black
q = (255, 0, 0)     # Pure Red
j = (0, 255, 0)     # Pure Green
k = (46, 139, 33)   # Leaf Green
n = (126, 88, 25)   # Earth Brown

image = [
a, a, a, a, a, a, a, a,
a, a, a, a, a, b, a, b,
a, a, a, a, a, a, c, a,
a, a, c, a, c, a, q, a,
a, a, j, j, j, q, a, a,
a, j, j, k, q, a, a, a,
j, k, j, k, k, a, a, a,
k, k, k, j, k, n, n, n]

```

--- /collapse ---

--- collapse ---
---
title: Kwitnące drzewo
---

![Siatka 8 x 8 kwadratów przedstawiająca kwitnące drzewo.](images/blossom.png)

Stworzone przez zespół Zssh14, Słowacja

```python

t = (255, 255, 0)   # Pure Yellow
g = (0, 204, 255)   # Sky Blue
w = (249, 169, 255) # Light Pink
y = (248, 97, 255)  # Magenta
z = (220, 53, 232)  # Purple
n = (126, 88, 25)   # Earth Brown
o = (179, 96, 65)   # Terracotta Brown
k = (46, 139, 33)   # Leaf Green

image =  [
t, g, g, w, w, y, g, g,
g, g, w, w, y, y, z, g,
g, w, y, z, y, z, z, z,
w, y, z, z, g, n, w, g,
g, g, o, o, n, w, y, z,
g, g, g, g, n, g, g, g,
g, g, g, o, n, n, g, g,
k, k, o, n, n, n, k, k]

```

--- /collapse ---

--- /task ---

--- task ---

**Znajdź:** linię, która mówi `# Wyświetl obraz` i dodaj linię kodu, aby wyświetlić obraz na matrycy LED:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 17, 18
---
c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, a, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

# Wyświetl obraz
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Naciśnij **Uruchom** na dole edytora, aby zobaczyć obraz wyświetlany na matrycy LED.

--- /task ---

--- task ---

**Debugowanie (usuwanie błędów)**

Mój kod zawiera błąd składni:

- Sprawdź, czy Twój kod pasuje do kodu w powyższych przykładach
- Sprawdź, czy masz wcięcia w kodzie na swojej liście
- Sprawdź, czy Twoja lista jest otoczona przez `[` i `]`
- Sprawdź, czy każda zmienna koloru na liście jest oddzielona przecinkiem

Mój obraz się nie pojawia:

- Sprawdź, czy Twój `sense.set_pixels(obrazek)` nie ma wciącia

--- /task ---


--- task ---

**Zapisz swoje postępy**

Teraz, gdy wyświetliłeś obraz, możesz zapisać swój program w projekcie Mission Starter, wpisując nazwę swojego zespołu, imiona członków zespołu i otrzymany kod klasy. Możesz ponownie załadować swój program na dowolnym urządzeniu z dostępem do Internetu, wpisując nazwę swojego zespołu i kod klasy.

![Przycisk „Zapisz” w Mission Zero.](images/mz_savebutton_v2.png)

--- /task --- 
