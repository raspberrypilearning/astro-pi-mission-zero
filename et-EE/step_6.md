## Mõõda niiskust

Astro Pi-l asuv niiskuse sensor mõõdab ümbritseva õhu niiskust, mis on vajalik kosmoses valitsevate tingimuste kohta andmete kogumiseks.

![Sõnum õhuniiskuse kohta](images/degrees-message.gif)

Astro Pi mõõdab ISS-i niiskust protsentides vee kontsentratsiooni kohta õhus.

Osa sinu ülesandest on panustada ISS-i meeskonna igapäevaellu, seetõttu annab nende teavitamine sellest, et õhuniiskus kosmosejaama pardal on normaalses vahemikus, neile suuremat kindlust.

[[[generic-theory-what-is-humidity]]]

--- task ---

Õhuniiskuse mõõtmiseks lisa see kood:

```python
humid = sense.humidity
```

See koodirida mõõdab valitsevat õhuniiskust ja säilitab mõõdetud väärtuse muutujas `humid`.

--- /task ---

--- task ---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. You can round the value to any number of decimal places. In the example we have rounded to one decimal place, but for a different level of precision, change the number `1` to the number of decimal places you would like to see.

```python
humid = round( sense.humidity, 1 )
```

--- /task ---

--- task ---

Valitseva õhuniiskuse kuvamiseks ekraanil keritava sõnumina tuleb lisada see koodirida:

```python
sense.show_message( str(humid) )
```

See `str()` osa konverteerib õhuniiskuse numbri tekstiks selle jaoks, et seda saaks kuvada Astro Pi-l.

--- /task ---

--- task ---

Samuti võid kuvada õhuniiskust mõne teise sõnumi osana, selleks pead oma sõnumi osad ühendama kasutades `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

--- /task ---

Tõeline Astro Pi mõõdab õhuniiskust enda ümber, aga sina võid niiskuse liugurit liigutada Sense HAT-i emulaatoril simuleerimaks niiskuse muutusi ja testimaks oma koodi.

![Niiskuse liugur](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.
