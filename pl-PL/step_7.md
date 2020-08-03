## Wyświetlanie temperatury

Można połączyć pomiar temperatury z obrazkiem, aby pokazać temperaturę również w postaci graficznej. Można na przykład wyświetlić burzę śnieżną przy niskich temperaturach i słoneczny dzień w przypadku wysokich temperatur:

![Gorąco i zimno](images/wet-dry.png)

\--- task \---

U dołu programu utwórz więcej zmiennych kolorów, aby określić dowolne kolory potrzebne do narysowania obrazków. Możliwe, że niektóre z nich zostały już określone w poprzednim kroku.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task \---

Tak jak wcześniej, narysuj swoje obrazki, najpierw tworząc dla każdego z nich listę, a następnie ustawiając kolory pikseli elementów listy.

```python
hot = [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g
]


cold = [
  b, b, w, b, b, b, w, b,
  b, b, b, b, b, w, b, b,
  b, w, b, b, b, b, b, w,
  b, b, b, b, w, b, b, b,
  w, b, b, w, b, b, w, b,
  b, b, b, b, b, b, b, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w
]
```

\--- /task \---

\--- task \---

Dodaj kod, aby odczytać temperaturę:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Teraz zdecyduj, który obrazek chcesz wyświetlić. For this example, we will display the `wet` image if the humidity reading is 40% or above, and the `dry` image if the humidity is below 40%.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /task \---

\--- task \---

Za pomocą suwaka temperatury ustaw temperaturę na emulatorze. Uruchom program i sprawdź, czy obrazek wybrany dla tej temperatury jest poprawnie wyświetlany.

\--- /task \---

\--- task \---

Zmień swój kod tak, aby program wyświetlał astronautom temperaturę w wybrany przez ciebie sposób.

\--- /task \---