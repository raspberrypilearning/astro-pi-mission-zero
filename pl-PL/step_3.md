## Wyświetl wiadomość i wybierz nazwę dla nowych komputerów Astro Pi

--- task ---

Otwórz [emulator Sense HAT](https://trinket.io/mission-zero){:target="_blank"} dla projektu Misja Zero.

Zobaczysz, że trzy linie kodu zostały dodane automatycznie:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![Zrzut ekranu emulatora Trinket Sense Hat z trzema liniami początkowego kodu wyświetlanymi w lewym panelu.](images/sense-hat-emulator2.png)

Kod ten łączy się z Astro Pi i zapewnia, że wyświetlacz LED Astro Pi jest pokazany we właściwy sposób. Kod należy zostawić, gdyż będzie on potrzebny.

--- /task ---

--- task ---

Może zamieścisz miłe pozdrowienia dla astronautów z ISS, którzy pracują w pobliżu Astro Pi? Dodajmy przewijaną wiadomość na wyświetlaczu.

Dodaj ten wiersz pod innym kodem:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Po naciśnięciu przycisku **Run** (Uruchom) zobaczysz, jak wiadomość `Astro Pi` przewija się na wyświetlaczu LED.

![Emulator Trinket Sense HAT uruchamiający przykładowy program, który przewija tekst "Astro PI" po matrycy LED białymi literami](images/M0_1.gif)

--- /task ---

Aby wyświetlić inną wiadomość, można napisać dowolną treść między znakami cudzysłowu (`""`).

--- collapse ---
---
title: Jakich znaków można użyć?
---

Sense HAT może wyświetlać tylko zestaw znaków Latin 1, co oznacza, że ​​dostępne będą tylko następujące znaki. Inne znaki będą wyświetlane jako `?`.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

Możesz również zmienić prędkość przewijania wiadomości na ekranie. Dodaj `scroll_speed` (tempo_przewijania) do istniejącego wiersza kodu, na przykład tak:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Domyślna prędkość przewijania wiadomości to `0.1`. Zmniejszenie liczby spowoduje, że wiadomość będzie przewijać się szybciej, a jej zwiększenie spowoduje, że wiadomość będzie przewijać się wolniej.

--- /task ---

### Wybierz nazwę dla nowych komputerów Astro Pi

--- task --- Komputery Astro Pi zostaną nazwane imionami dwóch inspirujących europejskich naukowców. Setki mężczyzn i kobiet przyczyniło się do rozwoju nauki i technologii; uczestnicy mogą sugerować swoje własne nazwy lub wybrać z listy naszych sugestii (upewnij się, że użyto angielskiej wersji imienia):

[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"} 
[Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing){:target="_blank"} 
[Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel){:target="_blank"} 
[Edsger Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra){:target="_blank"} 
[Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr){:target="_blank"} 
[Hypatia](https://en.wikipedia.org/wiki/Hypatia){:target="_blank"} 
[John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone){:target="_blank"} 
[Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie){:target="_blank"} 
[Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla){:target="_blank"} 
[Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe){:target="_blank"}

Aby zagłosować, zacznij swoją wiadomość od słów „My name should be” (po angielsku). Na przykład chcesz głosować na Ada Lovelace, twój kod wyglądałby tak:

```python
sense.show_message("My name should be Ada Lovelace")
```

Jeśli chcesz zagłosować, Twoja wiadomość *musi* zaczynać się od tych słów (w języku angielskim), w przeciwnym razie nie będziemy mogli automatycznie policzyć Twojego wpisu.

--- /task ---



