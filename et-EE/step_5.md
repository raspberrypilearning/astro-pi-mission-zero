## Kuva pilt

Pilte saad kuvada Astro Pi LED-maatriksil. Võib-olla võiks sinu tervitus astronautidele sisaldada pilti või mustrit koos kirjaliku sõnumiga või selle asemel?

![Astronaut](images/astronaut-pic.png)

--- task ---

Oma programmi alaosas saad luua värvimuutujaid määramaks piltide joonistamisel kasutatavaid värve. Saad kasutada nii palju värve kui soovid, aga selles näites me kasutame ainult kahte värvi, valget (`w`) ja musta (`b`).

```python
w = (255, 255, 255)
b = (0, 0, 0)
```

**Märkus:** Seekord oleks hea mõte anda värvi muutujatele ühetähelisi nimetusi, sest see hoiab järgmises etapis aega kokku, kuna neid on sul vaja kirjutada palju kordi. Lisaks teeb ühetäheliste nimetuste kasutamine joonistatud pildi vaatamise hõlpsamaks.

--- /task ---

--- task ---

Oma uute muutujate alla tee 64-st elemendist koosnev loend. Iga element kujutab ühte pikslit LED-maatriksil ja vastab ühele sinu määratud värvimuutujale. Joonista oma pilt pannes muutuja sinna, kus soovid kasutada sellega määratud värvi. Meie joonistasime astronaudi kasutades musta värvi (`b`) piksleid tausta määramiseks ja valge värvi (`w`) piksleid astronaudi skafandri joonistamiseks:

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

Oma pildi kuvamiseks LED-ekraanil lisa koodirida.

```python
sense.set_pixels(picture)
```

--- /task ---

--- task ---

Klõpsa **Run** (Käivita) nägemaks, kuidas sinu pilti kuvatakse.

--- /task ---

--- task ---

Kui soovid, võid lisada veidi koodi selle jaoks, et peale pildi kuvamist oleks lühike paus (või `sleep`). See annab astronautidele aega vaadata sinu pilti enne, kui sinu sõnumi järgmine osa neile kuvatakse. Oma programmi ülaossa lisa:

```python
from time import sleep
```

Seejärel lisa reale, mis on peale sinu pilti kuvavat rida, see kood, et anda kaks sekundit ooteaega:

```python
sleep(2)
```

--- /task ---

--- task ---

Loo astronautidele näitamiseks oma pilt või muster!

--- /task ---