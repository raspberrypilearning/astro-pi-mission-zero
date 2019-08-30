## Mõõda õhutemperatuur

Astro Pi´l asuv õhutemperatuuri sensor mõõdab ümbritseva õhu temperatuuri, mis on vajalik kosmoses valitsevate tingimuste kohta andmete kogumiseks.

![Sõnum õhutemperatuuri kohta](images/degrees-message.gif)

Astro Pi mõõdab rahvusvahelise kosmosejaama õhutemperatuuri Celsiuse kraadides (&deg;C). Kuna kosmose õhutemperatuur kõigub palju rohkem kui Maa oma, võib Astro Pi mõõta temperatuuri vahemikus -40°C...+120°C.

Osa sinu ülesandest on panustada rahvusvahelise kosmosejaama meeskonna igapäeva ellu, seetõttu nende teavitamine sellest, et õhutemperatuur kosmosejaama pardal on normaalses vahemikus annab neile suuremat kindlust.

--- collapse ---
---
title: Mis on õhutemperatuur?
---
Temperatuur mõõdab millegi soojust. Arsti juures käies on ilmselt sinu kehatemperatuuri mõõdetud kraadiklaasiga.

![Termomeeter](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} via Wikimedia Commons*

Täpsemalt öeldes on temperatuur mingi aine soojusenergia hulga mõõt. Sa tead seda, et jääkuubik on tahke, aga selle soojenemisel, st ümbritsevast keskkonnast soojusenergia absorbeerimisel, hakkab see sulama ja muutub vedelikuks. Seda seetõttu, et kui aine absorbeerib või kaotab piisavalt palju soojusenergiat muudab aine oma olekut, st muutub tahkest olekust vedelikuks.

--- /collapse ---

--- task ---

Õhutemperatuuri mõõtmiseks lisa see kood:

```python
temp = sense.temperature
```

See koodirida mõõdab valitsevat õhutemperatuuri ja säilitab mõõdetud väärtuse muutujas `temp`.

--- /task ---

--- task ---

Õhutemperatuuri mõõdetakse väga täpselt, st säilitataval väärtusel on suur kümnendkohtade arv. Sina võid väärtuse ümardada mistahes kümnendkohtadega arvuks. Meie ümardasime näite ühe kümnendkohaga arvuks, aga teistsuguse täpsuse saavutamiseks muuda numbrit `1` selliseks kümnendkoha arvuks, mida soovid näha.

```python
temp = round( sense.temperature, 1 )
```

--- /task ---

--- task ---

Õhutemperatuuri kuvamiseks keriva sõnumina ekraanil tuleb lisada see koodirida:

```python
sense.show_message( str(temp) )
```

See `str()` osa konverteerib õhutemperatuuri numbri tekstiks selle jaoks, et seda saaks kuvada Astro Pi´l.

--- /task ---

--- task ---

Samuti võid kuvada õhutemperatuuri mõne teise sõnumi osana, selleks pead oma sõnumi osad ühendama kasutades `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

--- /task ---

Tõeline Astro Pi mõõdab õhutemperatuuri enda ümber, aga sina võid temperatuuri liugurit liigutada Sense HAT´i emulaatoril simuleerimaks temperatuuri muutusi ja testimaks oma koodi.

![Õhutemperatuuri liugur](images/temperature-slider.png)

**Märkus:** Sa võid mõelda, et miks õhutemperatuuri liugur näitab õhutemperatuuri ühe numbrina, aga need mõõtmise tulemused mis sina saad näitavad kümnendkohti. Emulaator simuleerib tõelise sensori väikest ebatäpsust, seetõttu võib sinu poolt nähtav õhutemperatuuri mõõtmise tulemus olla natuke suurem või väiksem sellest väärtusest, mis sa liuguriga tegelikult määrasid.