## Dodajte barve

Diode LED računalnika Astro Pi lahko prikazujejo tudi barve. Barvo lahko določite tako, da ustvarite spremenljivko in ji dodelite vrednost RGB.

O tem, kako lahko s pomočjo različnih razmerij rdeče, zelene in modre ustvarite različne barve, se lahko poučite tukaj:

[[[generic-theory-colours]]]

--- task ---

Izberite barvo in ugotovite, kakšna je njena vrednost RGB. Pri tem vam lahko pomaga [izbirnik barv](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"}.

--- /task ---

--- task ---

Ustvarite spremenljivko za shranjevanje izbrane barve. Če ste, na primer, izbrali rdečo barvo, morate napisati naslednjo vrstico kode:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

Zdaj lahko besedilo prikažete v barvi po vaši izbiri! Če želite programu ukazati, naj uporabi barvo, ki ste jo ustvarili, morate kodi, ki prikazuje vaše besedilo, dodati parameter `text_colour`:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /task ---

![Prikaži sporočilo v barvah](images/show-message-color.gif)

--- task ---

Spremenite lahko tudi barvo ozadja zaslona. Izberite drugo barvo in za njeno shranjevanje ustvarite novo spremenljivko. Če želite programu ukazati, naj uporabi izbrano barvo ozadja, morate kodi dodati parameter `back_colour`:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Spremenite besedilo in barvo pozdravnega sporočila — kakšno sporočilo boste poslali astronavtom na postaji ISS?

--- /task ---
