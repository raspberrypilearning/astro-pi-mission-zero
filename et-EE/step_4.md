## Lisa värve

Astro Pi LED-ekraanid näitavad ka erinevaid värve. Värvi saad määrata luues muutuja ja andes sellele RGB-värviväärtuse.

Siin saad õppida, kuidas luua kõiki värve kasutades siin erinevaid punase, rohelise ja sinise proportsioone:

[[[generic-theory-colours]]]

\--- task \---

Vali värv ja leia selle värvi RGB-väärtus. Enda abistamiseks võid kasutada [värvi valijat](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"}.

\--- /task \---

\--- task \---

Oma valitud värvi säilitamiseks loo muutuja. Kui sa näiteks punase värvi valisid, siis kirjutaksid sellise koodirea:

```python
red = (255,0,0)
```

\--- /task \---

\--- task \---

Nüüd saad oma teksti kuvada enda valitud värvidega! Ütlemaks programmile, et ta kasutaks sinu poolt loodud värvi, lisa sinu teksti kuvavale koodile `text_colour` parameeter:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

\--- /task \---

![näita sõnumit värviliselt](images/show-message-color.gif)

\--- task \---

Samuti saad muuta ekraani taustavärvi. Vali mõni teine värv ja selle säilitamiseks loo uus muutuja. Kui soovid programmile öelda, et ta kasutaks sinu valitud taustavärvi, siis lisa oma koodile `back_colour` parameeter:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

\--- /task \---

\--- task \---

Muuda tervitusteksti ja värvi; millise sõnumi sa rahvusvahelise ISS-i astronautidele saadad?

\--- /task \---