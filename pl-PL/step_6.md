## Pomiar temperatury

Czujnik temperatury w Astro Pi może mierzyć temperaturę powietrza w otoczeniu. Jest to przydatna funkcja, która pomoże zebrać dane o warunkach panujących w przestrzeni kosmicznej.

![Wiadomość o temperaturze](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

Częścią waszej misji jest wkład w codzienne życie załogi na pokładzie MSK, więc informacja o tym, że temperatura na stacji kosmicznej mieści się w normalnym zakresie, doda im otuchy.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Dodaj ten kod, aby pobrać pomiar temperatury:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- /task \---

\--- task \---

Temperatura jest rejestrowana bardzo precyzyjnie, tzn. zapisana wartość będzie zawierała dużą liczbę miejsc dziesiętnych. Można zaokrąglić wartość do dowolnej liczby miejsc po przecinku. W tym przykładzie zaokrągliliśmy do jednego miejsca po przecinku, ale aby uzyskać inny poziom dokładności, należy zmienić cyfrę `1` na pożądaną liczbę miejsc po przecinku.

```python
temp = round( sense.temperature, 1 )
```

\--- /task \---

\--- task \---

Aby wyświetlić aktualną temperaturę jako przewijany komunikat na wyświetlaczu, dodaj ten wiersz kodu:

```python
sense.show_message( str(temp) )
```

The `str()` part converts the humidity from a number into text so that the Astro Pi can display it.

\--- /zadanie \---

\--- task \---

Część `str()` konwertuje temperaturę z liczby na tekst, aby Astro Pi mógł ją wyświetlić.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

Prawdziwy Astro Pi mierzy temperaturę w swoim otoczeniu, ale można przesunąć suwak temperatury na emulatorze Sense HAT, aby symulować zmiany temperatury i przetestować kod.

![Humidity slider](images/humidity-slider.png)

**Uwaga:** Być może zastanawiasz się, dlaczego suwak temperatury wyświetla temperaturę jako liczbę całkowitą, ale pomiar podawany jest w postaci liczby dziesiętnej. Emulator symuluje niewielką niedokładność rzeczywistego czujnika, więc uzyskany pomiar temperatury może być nieznacznie większy lub mniejszy niż wartość ustawiona za pomocą suwaka.