## Lisa värve

Astro Pi LED-ekraanid näitavad ka erinevaid värve. Värvi saad määrata luues muutuja ja andes sellele RGB-värviväärtuse.

Siin saad õppida, kuidas luua kõiki värve kasutades erinevaid punase, rohelise ja sinise proportsioone:

[[[generic-theory-colours]]]

--- task ---

Vali värv ja leia selle värvi RGB-väärtus. Enda abistamiseks võid kasutada [värvi valijat](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"}.

--- /task ---

--- task ---

Oma valitud värvi säilitamiseks loo muutuja. Kui valisid näiteks punase värvi, siis kirjutaksid sellise koodirea:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

Nüüd saad oma teksti kuvada enda valitud värvidega! Selleks, et programm kasutaks sinu poolt loodud värvi, lisa sinu teksti kuvavale koodile `teksti_värvuse` parameeter:

```python
punane = (255,0,0)
sense.show_message("Astro Pi", tekst_värvus=punane)
```

--- /task ---

![näita sõnumit värviliselt](images/show-message-color.gif)

--- task ---

Samuti saad muuta ekraani taustavärvi. Vali mõni teine värv ja loo selle säilitamiseks uus muutuja. Kui soovid programmile öelda, et ta kasutaks sinu valitud taustavärvi, lisa oma koodile `tausta_värvi` parameeter:

```python
punane = (255,0,0)
roheline = (0,255,0)
sense.show_message("Astro Pi", teksti_värv=punane, tausta_värv=roheline)
```

--- /task ---

--- task ---

Muuda tervitusteksti ja värvi — millise sõnumi sa ISS-i astronautidele saadad?

--- /task ---
