## Wyświetlanie obrazków

Na matrycy LED Astro Pi można wyświetlać obrazki. Może twoje pozdrowienie dla astronautów mogłoby zawierać obrazek lub wzór, dodatkowo lub też zamiast pisemnej wiadomości?

![A screenshot of the emulator window showing the Flight Unit with the LED matrix displaying a picture of the Flight Unit itself](images/fu-pic.png)

--- task ---

U dołu programu utwórz kilka zmiennych kolorów, aby określić, jakich kolorów chcesz użyć do narysowania obrazka. Można użyć dowolnej ilości kolorów, ale w poniższym przykładzie użyjemy tylko dwóch - białego (`w`) i czarnego (`b`). Notice that the shades are achieved by reducing the amount of light in all three channels while keeping the proportions the same.

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Uwaga:** Tym razem dobrze jest nadać zmiennym kolorów nazwy jednoliterowe, ponieważ pozwoli to zaoszczędzić czas w następnym kroku, w którym będą one wpisywane wiele razy. Ponadto przy użyciu pojedynczych liter łatwiej będzie zobaczyć rysowany obrazek.

--- /task ---

--- task ---



Pod nowymi zmiennymi utwórz listę 64 elementów. Każdy element reprezentuje jeden piksel na matrycy LED i odpowiada jednej z określonych zmiennych kolorów. Narysuj swój obrazek, umieszczając zmienną w miejscu, w którym ma pojawić się przypisany jej kolor. Narysowaliśmy astronautę, używając czarnych pikseli (`b`) jako tła i białych pikseli (`w`) do narysowania skafandra astronauty:

```python
 picture = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
```
--- /task ---

--- task ---

Dodaj wiersz kodu, aby wyświetlić obrazek na wyświetlaczu LED.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Naciśnij **Run** (Uruchom), aby wyświetlić obrazek.

--- /task ---

--- task ---

Można dodać kod, który określi krótki czas odczekania (lub `sleep` (uśpienia)) po wyświetleniu obrazka. Da to astronautom czas na zobaczenie twojego obrazka, zanim pojawi się następna część twojej wiadomości. U góry programu dodaj:

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
