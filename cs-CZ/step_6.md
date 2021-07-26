## Změřte vlhkost

The humidity sensor in the Astro Pi can measure the humidity in the air around it, a useful feature to help you gather data about the conditions in space.

![Zpráva o vlhkosti](images/degrees-message.gif)

Astro Pi měří vlhkost v ISS v procentech koncentrace vody ve vzduchu.

Součástí vaší mise je přispívat k každodennímu životu posádky na palubě ISS, dát jim vědět, že vlhkost na palubě vesmírné stanice je v normálním rozsahu je uklidní.

[[[generic-theory-what-is-humidity]]]

--- task ---

Přidejte tento kód pro měření vlhkosti:

```python
humid = sense.humidity
```

Tato řádka změří současnou vlhkost a uloží naměřenou hodnotu v proměnné `humid`.

--- /task ---

--- task ---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. You can round the value to any number of decimal places. In the example we have rounded to one decimal place, but for a different level of precision, change the number `1` to the number of decimal places you would like to see.

```python
humid = round( sense.humidity, 1 )
```

--- /task ---

--- task ---

Abyste aktuální vlhkost zobrazili na displeji jako běžící text, přidejte tuhle řádku kódu:

```python
sense.show_message( str(humid) )
```

Část `str()` převádí vlhkost z čísla na text tak, aby ji Astro Pi mohl zobrazit.

--- /task ---

--- task ---

To `str()` převádí vlhkost z čísla na text, aby ji Astro Pi mohlo zobrazit.

```python
sense.show_message( "Je " + str(humid) + " %" )
```

--- /task ---

Skutečný Astro Pi bude měřit vlhkost kolem sebe, vy můžete posunout posuvník vlhkosti na emulátoru Sense HAT, abyste simulovali změny vlhkosti a vyzkoušeli váš kód.

![Posuvník vlhkosti](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.
