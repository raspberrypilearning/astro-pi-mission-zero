## Změřte teplotu

The humidity sensor in the Astro Pi can measure the humidity in the air around it, a useful feature to help you gather data about the conditions in space.

![Zpráva s teplotou](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

Part of your mission is to contribute to the daily lives of the crew aboard the ISS, so letting them know that the humidity aboard the space station is within a normal range will reassure them.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Přidejte tento kód pro měření vlhkosti:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- /task \---

\--- task \---

Vlhkost se zaznamenává velmi přesně, proto bude mít uložená hodnota velký počet desetinných míst. Hodnotu můžete zaokrouhlit na libovolný počet desetinných míst. V příkladu zaokrouhlujeme na jedno desetinné místo, ale když číslo `1` změníte na jiné, dostanete jiný počet desetinných míst.

```python
temp = round( sense.temperature, 1 )
```

\--- /task \---

\--- task \---

Abyste aktuální teplotu zobrazili na displeji jako běžící text, přidejte tuhle řádku kódu:

```python
sense.show_message( str(temp) )
```

Část `str()` převádí vlhkost z čísla na text tak, aby ji Astro Pi mohl zobrazit.

\--- /task \---

\--- task \---

To `str()` převádí teplotu z čísla na text, aby ji Astro Pi mohlo zobrazit.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

\--- /task \---

Skutečný Astro Pi bude měřit vlhkost kolem sebe, vy můžete posunout posuvník vlhkosti na emulátoru Sense HAT, abyste simulovali změny vlhkosti a vyzkoušeli váš kód.

![Posuvník vlhkosti](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.