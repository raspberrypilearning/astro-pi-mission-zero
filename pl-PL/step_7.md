## Wyświetlanie temperatury

Można połączyć pomiar temperatury z obrazkiem, aby pokazać temperaturę również w postaci graficznej. Można na przykład wyświetlić burzę śnieżną przy niskich temperaturach i słoneczny dzień w przypadku wysokich temperatur:

![Gorąco i zimno](images/hot-and-cold.png)

\--- task \---

U dołu programu utwórz więcej zmiennych kolorów, aby określić dowolne kolory potrzebne do narysowania obrazków. Możliwe, że niektóre z nich zostały już określone w poprzednim kroku. W naszych przykładach zastosujemy kolor biały (`w`), żółty (`y`), zielony (`g`) i czarny/pusty (`b`).

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

Dodaj kod, aby uzyskać temperaturę:

```python
temp = sense.temperature
```

\--- /task \---

\--- task \---

Teraz zdecyduj, który obrazek chcesz wyświetlić. W tym przykładzie wyświetlimy obrazek `hot` (gorąco), jeśli pomiar temperatury wyniesie 20 stopni lub więcej, a obrazek `cold` (zimno), jeśli temperatura będzie poniżej 20 stopni.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /task \---

\--- task \---

Za pomocą suwaka temperatury ustaw temperaturę na emulatorze. Uruchom program i sprawdź, czy obrazek wybrany dla tej temperatury jest wyświetlany poprawnie.

\--- /task \---

\--- task \---

Zmień swój kod tak, aby program wyświetlał astronautom temperaturę w wybrany przez ciebie sposób.

\--- /task \---