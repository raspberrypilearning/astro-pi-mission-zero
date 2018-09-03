## Wyświetlanie wiadomości

\--- task \---

Otwórz [emulator Sense HAT](https://trinket.io/mission-zero){:target="_blank"} dla projektu Mission Zero.

Zobaczysz, że trzy wiersze kodu zostały dodane automatycznie:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![emulator sense hat](images/sense-hat-emulator2.png)

Kod ten łączy się z Astro Pi i zapewnia, że wyświetlacz LED Astro Pi jest pokazany we właściwy sposób. Kod należy zostawić, gdyż będzie potrzebny.

\--- /task \---

\--- task \---

Może zamieścisz miłe pozdrowienia dla astronautów z MSK, którzy pracują w pobliżu Astro Pi? Dodajmy przewijaną wiadomość na wyświetlaczu.

Dodaj ten wiersz poniżej drugiego kodu:

```python
sense.show_message("Astro Pi")
```

\--- /task \---

\--- task \---

Po naciśnięciu przycisku **Run** (Uruchom) zobaczysz, jak wiadomość `Astro Pi` przewija się na wyświetlaczu LED.

![pokaż kod wiadomości kliknij uruchom](images/show-message-code-annotated.PNG)

\--- /task \---

![Przewijanie wiadomości](images/scroll-message.gif)

Aby wyświetlić inną wiadomość, można napisać dowolną treść między znakami cudzysłowu (`""`).

\--- collapse \---

* * *

## title: Jakich znaków można użyć?

Sense HAT może wyświetlać tylko zestaw znaków Latin 1, co oznacza, że ​​dostępne będą tylko następujące znaki. Inne znaki będą wyświetlane jako `?`.

    +-*/!"#$><0123456789.=)(
    
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    abcdefghijklmnopqrstuvwxyz
    
    ?,;:|@%[&_']\~
    

\--- /collapse \---

\--- task \---

Można również zmienić tempo przewijania wiadomości na ekranie. Dodaj `scroll_speed` (tempo_przewijania) do istniejącego wiersza kodu, na przykład:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Domyślne tempo przewijania wiadomości to `0.1`. Zmniejszenie liczby spowoduje, że wiadomość będzie przewijać się szybciej, a jej zwiększenie spowoduje, że wiadomość będzie przewijać się wolniej.

\--- /task \---