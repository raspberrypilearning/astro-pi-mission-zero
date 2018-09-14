## Dodawanie koloru

Diody LED Astro Pi mogą również wyświetlać kolory. Można określić kolor, tworząc zmienną i przypisując mu wartość koloru RGB.

Tutaj można dowiedzieć się, jak tworzy się wszystkie kolory za pomocą różnych proporcji czerwonego, zielonego i niebieskiego:

[[[generic-theory-colours]]]

--- task ---

Wybierz kolor i sprawdź jego wartość RGB. Można użyć [selektora kolorów](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"}.

--- /task ---

--- task ---

Utwórz zmienną, aby zachować wybrany kolor. Na przykład, w przypadku wybrania czerwonego należy napisać ten wiersz kodu:

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

![pokaż wiadomość w kolorze](images/show-message-color.gif)

--- task ---

Można również zmienić kolor tła wyświetlacza. Wybierz inny kolor i utwórz kolejną zmienną, aby zachować ten kolor. Aby w programie dać polecenie użycia wybranego koloru tła, dodaj parametr `back_colour` (koloru_tła) do swojego kodu:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Zmień tekst pozdrowienia i kolor - jaką wiadomość wyślesz do astronautów na pokładzie MSK?

--- /task ---
