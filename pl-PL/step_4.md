## Dodawanie koloru

Diody LED Astro Pi mogą również wyświetlać kolory. Można określić kolor, tworząc zmienną i przypisując mu wartość kolorów RGB(Red-czerwony, Green- zielony, Blue- niebieski).

Tutaj można dowiedzieć się, jak tworzy się wszystkie kolory za pomocą różnych proporcji czerwonego, zielonego i niebieskiego:

[[[generic-theory-colours]]]

--- task ---

Wybierz kolor i sprawdź jego wartość RGB. Dla ułatwienia, możesz skorzystać z [selektora kolorów](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"}.

--- /task ---

--- task ---

Utwórz zmienną, aby przechować wybrany kolor. Na przykład, w przypadku wybrania czerwonego należy napisać następującą linię kodu:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

Teraz można wyświetlać swój tekst w wybranym kolorze! Aby w programie dać polecenie użycia utworzonego koloru, należy dodać parametr `text_colour` (koloru_tekstu) do kodu, który wyświetla twój tekst:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /task ---

![Emulator Trinket Sense HAT uruchamiający przykładowy program, który przewija tekst \"Astro Pi\" po matrycy LED używając czerwonych literami](images/M0_2.gif)

--- task ---

Można również zmienić kolor tła wyświetlacza. Wybierz inny kolor i utwórz kolejną zmienną, aby zachować ten kolor. Aby w programie dać polecenie użycia wybranego koloru tła, dodaj parametr `back_colour` (kolor_tła) do swojego kodu:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Zmień tekst pozdrowienia i kolor - jaką wiadomość wyślesz do astronautów na pokładzie ISS?

--- /task ---
