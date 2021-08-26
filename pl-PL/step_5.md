## Wyświetlanie obrazków

Na matrycy LED Astro Pi można wyświetlać obrazki. Może twoje pozdrowienie dla astronautów mogłoby zawierać obrazek lub wzór, dodatkowo lub też zamiast pisemnej wiadomości?

![Zrzut ekranu okna emulatora pokazujący jednostkę lotu z matrycą LED wyświetlającą obraz tejże jednostki lotu](images/fu-pic.png)

--- task ---

U dołu programu utwórz kilka zmiennych kolorów, aby określić, jakich kolorów chcesz użyć do narysowania obrazka. Można użyć dowolnej ilości kolorów, ale w poniższym przykładzie użyjemy tylko kilku — czerwony(`r`), biały (`w`), czarny (`b`), oraz dwóch odcieni szarego (`g` i `s`). Zwróć uwagę, że odcienie uzyskuje się poprzez zmniejszenie ilości światła we wszystkich trzech kanałach przy zachowaniu tych samych proporcji.

```python
w = (255, 255, 255)
b = (0, 0, 0)
g = (50,50,50)
s = (200,255,200)
r = (255,0,0)
```

**Uwaga:** Tym razem dobrze jest nadać zmiennym kolorów nazwy jednoliterowe, ponieważ pozwoli to zaoszczędzić czas w następnym kroku, w którym będą one wpisywane wiele razy. Ponadto przy użyciu pojedynczych liter łatwiej będzie zobaczyć rysowany obrazek.

--- /task ---

--- task ---



Pod nowymi zmiennymi utwórz 64 elementową listę. Każdy element reprezentuje jeden piksel na matrycy LED i odpowiada jednej z określonych zmiennych kolorów. Narysuj swój obrazek, umieszczając zmienną w miejscu, w którym ma pojawić się przypisany jej kolor. Narysowaliśmy Astro Pi, używając czarnych (`b`) pikseli jako tła i szarych pikseli (`g`) do narysowania obudowy Astro Pi:

```python
 picture = [
    g, b, b, b, b, b, b, g,
    b, g, g, g, g, g, g, b,
    b, g, b, b, g, w, g, g,
    b, g, b, b, g, g, g, g,
    b, g, g, g, s, s, g, g,
    b, g, r, g, g, g, g, g,
    b, g, g, g, g, g, g, b,
    g, b, b, b, b, b, b, g
    ]
```
--- /task ---

--- task ---

Dodaj linię kodu, aby wyświetlić obrazek na wyświetlaczu LED.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Naciśnij **Run** (Uruchom), aby wyświetlić obrazek.

--- /task ---

--- task ---

Można dodać kod, który określi krótki czas odczekania - wait (lub `sleep` - uśpienia) po wyświetleniu obrazka. Da to astronautom czas na zobaczenie twojego obrazka, zanim pojawi się następna część twojej wiadomości. U góry programu dodaj:

```python
from time import sleep
```

Następnie w wierszu po wierszu wyświetlającym rysunek dodaj ten kod, aby odczekać dwie sekundy:

```python
sleep(2)
```

--- /task ---

--- task ---

Stwórz własny obrazek lub wzór do wyświetlenia astronautom!

--- /task ---
