## Wyświetl wilgotność

Można połączyć pomiar wilgotności z obrazkiem, aby pokazać wilgotność również w postaci graficznej. Na przykład możesz wyświetlić ocean dla wysokiej wilgotności i pustynię dla niskiej wilgotności:

![Mokro i sucho](images/wet-dry.png)

--- task ---

U dołu programu utwórz więcej zmiennych kolorów, aby określić dowolne kolory potrzebne do narysowania obrazków. Możliwe, że niektóre z nich zostały już określone w poprzednim kroku.

```python
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)
```

--- /task ---

--- task ---

Tak jak wcześniej, narysuj swoje obrazki, najpierw tworząc dla każdego z nich listę, a następnie ustawiając kolory pikseli elementów listy.

```python
wet = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


dry = [
  c, c, g, g, c, c, c, c,
  c, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, g, g, g, g, g, c, c,
  c, c, g, g, c, c, c, c,
  y, y, y, y, y, y, y, y,
  y, y, y, y, y, y, y, y
]
```

--- /task ---

--- task ---

Dodaj kod, aby uzyskać wilgotność:

```python
humid = sense.humidity
```

--- /task ---

--- task ---

Teraz zdecyduj, który obrazek chcesz wyświetlić. Dla tego przykładu wyświetlmy obrazek `wet`, jeśli odczyt wilgotności wynosi 40% lub więcej, i obrazek `dry` jeśli wilgotność jest poniżej 40%.

```python
humid = sense.humidity
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

Użyj suwaka wilgotności, aby ustawić wilgotność na emulatorze. Uruchom swój program i sprawdź, czy obrazek wybrany dla danej wilgotności jest poprawnie wyświetlany.

--- /task ---

--- task ---

Zmień swój kod, aby Twój program wyświetlał wilgotność dla astronautów w wybrany przez Ciebie sposób.

--- /task ---

--- task --- Test your code with a few different humidity settings (using the slider) to make sure it always runs correctly. If you've followed the example above, is an image displayed both when the humidity is set to a value less than 40% and also when it is set to more than 40%?

--- /task ---
