## Změřte teplotu

Teplotní snímač v Astru Pi dokáže měřit teplotu okolního vzduchu. To je užitečná funkce, která vám pomůže shromáždit údaje o podmínkách ve vesmíru.

![Zpráva s teplotou](images/degrees-message.gif)

Astro Pi měří teplotu v ISS ve stupních Celsia (&deg;C). Protože teploty ve vesmíru mají mnohem větší výkyvy než teploty na Zemi, umí Astro Pi měřit široké rozmezí teplot – od -40 stupňů Celsia až do +120 stupňů Celsia.

Součástí vaší mise je přispět ke každodennímu životu posádky ISS. Když jim dáte vědě, že teplota na palubě vesmírné stanice je v normálu, uklidní ji to.

--- collapse ---
---
title: Co je teplota?
---
Teplota je měřítko toho, jak je něco teplé. Dost možná vám pan doktor měřil teplotu teploměrem.

![Teploměr](images/thermometer.JPG) Foto: *Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"}, zdroj: Wikimedia Commons*

Přesněji řečeno, teplota je měřítkem množství tepelné energie nějaké látky. Jak víte, kostka ledu je pevná, ale jak se potupně ohřívá (tj. absorbuje tepelnou energii z prostředí), roztává se a stává se kapalnou. Je to proto, že když látka absorbuje nebo ztratí dostatečné množství tepelné energie, změní skupenství, např. z pevného na kapalné.

--- /collapse ---

--- task ---

Přidejte tento kód k odečtení teploty:

```python
temp = sense.temperature
```

Tato řádka změří současnou teplotu a uloží naměřenou hodnotu v proměnné `temp`.

--- /task ---

--- task ---

Teplota je měřena s velikou přesností, takže uložená hodnota bude mít mnoho desetinných míst. Hodnotu můžete zaokrouhlit na libovolný počet desetinných míst. V příkladu zaokrouhlujeme na jedno desetinné místo, ale když číslo `1` změníte na jiné, dostanete jiný počet desetinných míst.

```python
temp = round( sense.temperature, 1 )
```

--- /task ---

--- task ---

Abyste aktuální teplotu zobrazili na displeji jako běžící text, přidejte tuhle řádku kódu:

```python
sense.show_message( str(temp) )
```

To `str()` převádí teplotu z čísla na text, aby ji Astro Pi mohlo zobrazit.

--- /task ---

--- task ---

Teplotu můžete zobrazit také jako součást jiné zprávy. Části zprávy pospojujte znaky `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

--- /task ---

Skutečné Astro Pi měří teplotu kolem sebe, ale k otestování kódu na emulátoru Sense HAT můžete změny teploty simulovat posuvníkem teploty.

![Posuvník teploty](images/temperature-slider.png)

**Poznámka:** Možná se divíte, proč posuvník teploty zobrazuje teplotu jako celé číslo, zatímco měření, které získáte, má desetinná místa. Emulátor simuluje maličkou míru nepřesnosti skutečného snímače, takže měření teploty, které dostanete, může být nepatrně větší nebo menší než hodnota, kterou jste nastavili pomocí posuvníku.