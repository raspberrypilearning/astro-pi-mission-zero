## Pomiar wilgotności

Czujnik wilgotności w Astro Pi może mierzyć wilgotność powietrza wokół niego, co jest przydatną funkcją, która pomaga zbierać dane o warunkach w przestrzeni.

![Wiadomość o wilgotności](images/degrees-message.gif)

Astro Pi mierzy wilgotność w ISS w procentowym stężeniu wody w powietrzu.

Część misji polega na przyczynianiu się do codziennego życia załogi na pokładzie ISS, aby mogli wiedzieć, że wilgotność na pokładzie stacji kosmicznej mieści się w normalnym zakresie, co ich uspokoi.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Dodaj ten kod, aby odczytać wilgotność:

```python
humid = sense.humidity
```

Ta linia zmierzy aktualną wilgotność i zapisze zmierzoną wartość w zmiennej `humid`.

\--- /task \---

\--- task \---

Wilgotność jest zapisywana bardzo precyzyjnie, tj. zapisana wartość będzie miała dużą liczbę miejsc po przecinku. Można zaokrąglić wartość do dowolnej liczby miejsc po przecinku. W tym przykładzie zaokrągliliśmy do jednego miejsca po przecinku, ale aby uzyskać inny poziom dokładności, należy zmienić cyfrę `1` na pożądaną liczbę miejsc po przecinku.

```python
humid = round( sense.humidity, 1 )
```

\--- /task \---

\--- task \---

Aby wyświetlić bieżącą wilgotność jako komunikat przewijający się na wyświetlaczu, dodaj tą linijkę kodu:

```python
sense.show_message( str(humid) )
```

Część `str()` przekształca wilgotność z liczby na tekst, tak aby Astro Pi mogło ją wyświetlić.

\--- /task \---

\--- task \---

Możesz również wyświetlić wilgotność jako część innej wiadomości, dołączając do części swojej wiadomości używając `+`.

```python
sense.show_message( "Jest " + str(humid) + " %" )
```

\--- /task \---

Prawdziwy Astro Pi mierzy temperaturę w swoim otoczeniu, ale możesz przesunąć suwak wilgotności na emulatorze Sense HAT, aby symulować zmiany wilgotności i przetestować kod.

![Suwak wilgotności](images/humidity-slider.png)

**Uwaga:** Być może zastanawiasz się, dlaczego suwak wilgotności wyświetla wilgotność jako liczbę całkowitą, ale pomiar podawany jest w postaci liczby dziesiętnej. Emulator symuluje niewielką niedokładność rzeczywistego czujnika, więc uzyskany pomiar wilgotności może być nieznacznie większy lub mniejszy niż wartość ustawiona za pomocą suwaka.