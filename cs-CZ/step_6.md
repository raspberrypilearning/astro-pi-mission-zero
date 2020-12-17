## Změřte vlhkost

Snímač vlhkosti v Astru Pi dokáže měřit vlhkost okolního vzduchu. To je užitečná funkce, která vám pomůže shromáždit údaje o podmínkách ve vesmíru.

![Zpráva o vlhkosti](images/degrees-message.gif)

Astro Pi měří vlhkost v ISS v procentech koncentrace vody ve vzduchu.

Součástí vaší mise je přispívat k každodennímu životu posádky na palubě ISS, dát jim vědět, že vlhkost na palubě vesmírné stanice je v normálním rozsahu je uklidní.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Přidejte tento kód pro měření vlhkosti:

```python
humid = sense.get_humidity()
```

Tato řádka změří současnou vlhkost a uloží naměřenou hodnotu v proměnné `humid`.

\--- /task \---

\--- task \---

Vlhkost se zaznamenává velmi přesně, proto bude mít uložená hodnota velký počet desetinných míst. Hodnotu můžete zaokrouhlit na libovolný počet desetinných míst. V příkladu zaokrouhlujeme na jedno desetinné místo, ale když číslo `1` změníte na jiné, dostanete jiný počet desetinných míst.

```python
humid = round(sense.get_humidity(), 1)
```

\--- /task \---

\--- task \---

Abyste aktuální vlhkost zobrazili na displeji jako běžící text, přidejte tuhle řádku kódu:

```python
sense.show_message(str(humid))
```

Část `str()` převádí vlhkost z čísla na text tak, aby ji Astro Pi mohl zobrazit.

\--- /task \---

\--- task \---

To `str()` převádí vlhkost z čísla na text, aby ji Astro Pi mohlo zobrazit.

```python
sense.show_message( "Je " + str(humid) + " %" )
```

\--- /task \---

Skutečný Astro Pi bude měřit vlhkost kolem sebe, vy můžete posunout posuvník vlhkosti na emulátoru Sense HAT, abyste simulovali změny vlhkosti a vyzkoušeli váš kód.

![Posuvník vlhkosti](images/humidity-slider.png)

**Poznámka:** Možná se divíte, proč posuvník vlhkosti zobrazuje vlhkost jako celé číslo, zatímco měření, které získáte, má desetinná místa. Emulátor simuluje maličkou míru nepřesnosti skutečného snímače, takže měření vlhkosti, které dostanete, může být nepatrně větší nebo menší než hodnota, kterou jste nastavili pomocí posuvníku.