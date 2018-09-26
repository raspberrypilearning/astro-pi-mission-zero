## Prikažite sporočilo

Na matrici LED računalnika Astro Pi lahko prikažete slike. Morda želite, da bi vaš pozdrav astronavtov poleg ali namesto pisnega sporočila vseboval sliko ali vzorec?

![Astronavt](images/astronaut-pic.png)

--- task ---

Na dnu svojega programa določite nekaj barvnih spremenljivk za barve, ki jih želite uporabiti v svojih slikah. Uporabite lahko toliko barv, kot želite, a v tem primeru bomo uporabili le dve — belo (`w`) in črno (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Opomba:** V tem primeru je barvnim spremenljivkam priporočljivo dodeliti imena, sestavljena iz le ene črke, saj vam bo to prihranilo čas v naslednjem koraku, ko jih boste morali večkrat natipkati. Poleg tega bo zaradi uporabe enojnih črk sliko lažje videti.

--- /task ---

--- task ---

Pod svojimi novimi spremenljivkami ustvarite seznam s 64 elementi. Vsak element predstavlja eno slikovno piko na matrici LED in ustreza eni izmed določenih barvnih spremenljivk. Svojo sliko narišete tako, da spremenljivko postavite na mesto, kjer želite, da se pojavi spremenljivki dodeljena barva. S črnimi (`b`) slikovnimi pikami na ozadju in belimi (`w`) slikovnimi pikami smo narisali astronavtovo vesoljsko obleko:

```python
picture = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
```

--- /task ---

--- task ---

Da svojo sliko prikažete na zaslonu LED, dodajte vrstico kode.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Pritisnite **Run** (Zaženi), da bo vaša slika prikazana.

--- /task ---

--- task ---

Dodate lahko kodo, s katero po prikazu slike vključite kratek zamik (ali `sleep`). Tako bodo imeli astronavti več časa, da si ogledajo vašo sliko, preden se pojavi naslednji del vašega sporočila. Na vrhu programa dodajte:

```python
from time import sleep
```

Za dodajanje zamika dveh sekund v vrstici pod tisto, ki prikazuje vašo sliko, dodajte naslednjo kodo:

```python
sleep(2)
```

--- /task ---

--- task ---

Ustvarite svojo sliko ali vzorec in ju prikažite astronavtom!

--- /task ---