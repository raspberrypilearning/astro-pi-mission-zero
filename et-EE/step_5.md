## Kuva pilt

Pilte saad kuvada Astro Pi LED-maatriksil. Võib-olla võiks sinu tervitus astronautidele sisaldada pilti või mustrit koos kirjaliku sõnumiga või selle asemel?

![A screenshot of the emulator window showing the Flight Unit with the LED matrix displaying a picture of the Flight Unit itself](images/fu-pic.png)

--- task ---

Oma programmi alaosas saad luua värvimuutujaid määramaks piltide joonistamisel kasutatavaid värve. Võid kasutada nii palju värve kui soovid, aga selles näites kasutame vaid mõnd — red (`r`), white (`w`), black (`b`) ja kaks grey tooni (`g` ja `s`). Pane tähele, et toonid saavutatakse valguse vähendamise tulemusena kõigis kolmes kanalis, ent proportsioone ei muudeta.

```python
w = (255, 255, 255)
b = (0, 0, 0)
g = (50,50,50)
s = (200,255,200)
r = (255,0,0)
```

**Märkus:** Seekord oleks hea mõte anda värvi muutujatele ühetähelised nimetused, sest see hoiab järgmises etapis aega kokku, kuna neid on sul vaja kirjutada palju kordi. Lisaks teeb ühetäheliste nimetuste kasutamine joonistatud pildi vaatamise hõlpsamaks.

--- /task ---

--- task ---



Oma uute muutujate alla tee 64-st elemendist koosnev loend. Iga element kujutab ühte pikslit LED-maatriksil ja vastab ühele sinu määratud värvimuutujale. Joonista oma pilt pannes muutuja sinna, kus soovid kasutada sellega määratud värvi. Meie joonistasime Astro Pi kasutades musta värvi (`b`) piksleid tausta määramiseks ja halli värvi (`g`) piksleid Astro Pi lennukikohvri metallosade joonistamiseks:

```python
 pilt = [
    g, b, b, b, b, b, b, g,
    b, g, g, g, g, g, g, b,
    b, g, b, b, g, w, g, g,
    b, g, b, b, g, g, g, g,
    b, g, g, g, s, s, g, g,
    b, g, r, g, g, g, g, g,
    b, g, g, g, g, g, g, b,
    g, b, b, b, b, b, b, g
    ]
```
--- /task ---

--- task ---

Oma pildi kuvamiseks LED-ekraanil lisa koodirida.

```python
sense.set_pixels(pilt)
```

--- /task ---

--- task ---

Klõpsa **Käivita** nägemaks, kuidas sinu pilti kuvatakse.

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
