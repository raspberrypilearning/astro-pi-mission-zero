## Pomiar temperatury

Czujnik temperatury w Astro Pi może mierzyć temperaturę powietrza w otoczeniu. Jest to przydatna funkcja, która pomoże zebrać dane o warunkach panujących w przestrzeni kosmicznej.

![Wiadomość o temperaturze](images/degrees-message.gif)

Astro Pi mierzy temperaturę na MSK w stopniach Celsjusza (&deg;°C). Ponieważ temperatury w kosmosie różnią się znacznie od tych na Ziemi, Astro Pi może mierzyć temperaturę w zakresie od -40 stopni Celsjusza do +120 stopni Celsjusza.

Częścią waszej misji jest wkład w codzienne życie załogi na pokładzie MSK, więc informacja o tym, że temperatura na stacji kosmicznej mieści się w normalnym zakresie, doda im otuchy.

--- collapse ---
---
title: Co to jest temperatura?
---
Temperatura to miara stopnia nagrzania substancji. Możliwe, że podczas wizyty u lekarza mierzono ci temperaturę za pomocą termometru.

![Termometr](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} via Wikimedia Commons*

Mówiąc bardziej precyzyjnie, temperatura jest miarą ilości energii cieplnej substancji. Wiesz, że kostka lodu jest ciałem stałym, ale gdy się nagrzewa, tzn. gdy pochłania energię cieplną z otoczenia, topi się i staje się płynem. Dzieje się tak dlatego, że gdy dana substancja pochłonie lub straci wystarczającą ilość energii cieplnej, substancja ta zmienia swój stan, np. przechodzi od ciała stałego do cieczy.

--- /collapse ---

--- task ---

Dodaj ten kod, aby pobrać pomiar temperatury:

```python
temp = sense.temperature
```

Wiersz ten będzie mierzyć aktualną temperaturę i przechowywać zmierzoną wartość w zmiennej `temp`.

--- /task ---

--- task ---

Temperatura jest rejestrowana bardzo precyzyjnie, tzn. zapisana wartość będzie zawierała dużą liczbę miejsc dziesiętnych. Można zaokrąglić wartość do dowolnej liczby miejsc po przecinku. W tym przykładzie zaokrągliliśmy do jednego miejsca po przecinku, ale aby uzyskać inny poziom dokładności, należy zmienić cyfrę `1` na pożądaną liczbę miejsc po przecinku.

```python
temp = round( sense.temperature, 1 )
```

--- /task ---

--- task ---

Aby wyświetlić aktualną temperaturę jako przewijany komunikat na wyświetlaczu, dodaj ten wiersz kodu:

```python
sense.show_message( str(temp) )
```

Część `str()` konwertuje temperaturę z liczby na tekst, aby Astro Pi mógł ją wyświetlić.

--- /task ---

--- task ---

Można również wyświetlić temperaturę jako część innej wiadomości, łącząc części wiadomości za pomocą `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

--- /task ---

Prawdziwy Astro Pi mierzy temperaturę w swoim otoczeniu, ale można przesunąć suwak temperatury na emulatorze Sense HAT, aby symulować zmiany temperatury i przetestować kod.

![Suwak temperatury](images/temperature-slider.png)

**Uwaga:** Być może zastanawiasz się, dlaczego suwak temperatury wyświetla temperaturę jako liczbę całkowitą, ale pomiar podawany jest w postaci liczby dziesiętnej. Emulator symuluje niewielką niedokładność rzeczywistego czujnika, więc uzyskany pomiar temperatury może być nieznacznie większy lub mniejszy niż wartość ustawiona za pomocą suwaka.