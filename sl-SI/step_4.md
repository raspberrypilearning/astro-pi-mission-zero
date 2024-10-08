## Zaznajte barve

V tem koraku boste nastavili senzor barvne svetilnosti in ga uporabili za zaznavanje količine rdeče, zelene in modre, ki doseže senzor. Ta barva bo nato uporabljena za barvanje izbrane slike. Astronavt, ki bi stopil do senzorja v modri srajci, bi videl drugačno sliko kot astronavt v rdeči srajci.

![slika, prikazana z rožnatim ozadjem na matriki LED](images/colour_background.png)

Ne glede na to, katero sliko izberete, ozadje uporablja spremenljivko `c`, ki je nastavljena na črno.

--- task ---

Za barvanje ozadja uporabite barvni senzor.

Dodajte kodo pred seznam slik, da dobite barvo s senzorja, in spremenite spremenljivko barve ozadja `c`, da bo namesto črne uporabila barvo, ki jo zazna barvni senzor Sense HAT.

**Nasvet:** Komentarjev, ki se začnejo z '#', vam ni treba vnašati (tam so, da razložijo kodo).

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 9, 10
---

# Doda barvne spremenljivke in sliko

a = (255, 255, 255) # Bela
c = (0, 0, 0) # Črna
f = (25, 25, 112) # Nočno modra
m = (34, 139, 34) # Drevesno zelena

rgb = sense.color # Preberi barvo iz senzorja
c = (rgb.red, rgb.green, rgb.blue) # Uporabi zaznano barvo

slika = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]


--- /code ---

--- /task ---

--- task ---

**Preizkus:** Premaknite barvni drsnik na barvo po vaši izbiri in nato **zaženite** svojo kodo. Vaša barva ozadja se bo spremenila. Ponovno ponovite test z novo barvo.

**Namig:** Vsakič, ko spremenite barvo, boste morali klikniti »Zaženi«.

--- /task ---

## Ponavljajte svoj program

Program Astro Pi Mission Zero lahko deluje do 30 sekund. Ta čas boste porabili za večkratno preverjanje barvnega senzorja in posodobitev slike.

Vaša koda bo uporabila zanko `for`, da se bo zagnala 28-krat. **Vsakič** bo:
+ zaznala najnovejšo barvo
+ posodobite barvo ozadja slike
+ počakala eno sekundo

--- task ---

**Poiščite** svojo `rgb = sense.color` vrstico kode.

Nad njo **dodajte** kodo, da nastavite svojo zanko `for` na `28` ponovitev.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 2
---

for i in range(28):
rgb = sense.color # Preberi barvo iz senzorja
c = (rgb.red, rgb.green, rgb.blue)

slika = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

  
--- /code ---

--- /task ---

--- task ---

Zdaj morate vso svojo kodo pod zanko `for` zamakniti, da se nahaja **znotraj** `for`.

**Namig:** Če želite zamakniti več vrstic, označite vrstice, ki jih želite zamakniti, nato pritisnite tipko <kbd>Tab</kbd> na tipkovnici (običajno nad tipko <kbd>Caps Lock</kbd>).

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
---

for i in range(28):
  rgb = sense.color # Preberi barvo iz senzorja
  c = (rgb.red, rgb.green, rgb.blue)

  slika = [
    m, m, m, m, m, c, c, c,
    m, f, m, f, m, m, m, m,
    m, m, m, m, m, m, m, m,
    m, m, c, a, c, c, c, a,
    m, m, c, c, c ,c ,c ,c,
    m, m, c, c, c, a, c, c,
    m, m, m, m, m, m, m, m,
    m, m, m, m, m, m, m, m]

    
  # Prikaže sliko

  sense.set_pixels(slika)
 
--- /code ---

--- /task ---

--- task ---

Znotraj zanke na dnu vaše kode dodajte enosekundno `čakanje`:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 5
---
  
  # Prikaže sliko

  sense.set_pixels(slika)
  sleep(1)  
  
--- /code ---

**Namig:** Prepričajte se, da je ta vrstica kode zamaknjena znotraj zanke `for`.

--- /task ---

--- task ---

**Preizkus:** Med izvajanjem projekta zaženite kodo in večkrat spremenite izbirnik barv. Preverite, ali se vaša slika posodobi tako, da bo pri naslednjem zagonu uporabila zaznano barvo.

Slika se bo prenehala posodabljati, ko se zanka konča, tako da program ne deluje več kot 30 sekund.

--- /task ---

--- task ---

**Razhroščevanje**

Moja koda ima sintaktično napako ali pa se ne izvaja po pričakovanjih:

- Preverite, ali se vaša koda ujema s kodo v zgornjih primerih
- Preverite, ali ste zamaknili kodo v `for` zanki
- Preverite, ali je vaš seznam obkrožen z `[` in `]`
- Preverite, ali je vsaka barvna spremenljivka na seznamu ločena z vejico

Moja koda se izvaja dlje kot 30 sekund:

- Zmanjšajte število zagonov zanke for iz 28 na 25 ali celo 20.
- Zmanjšajte dolžino spanja z 1 sekunde na 0,5 sekunde.

--- /task ---

--- task ---

Dodajte `sense.clear()` na konec kode, da na koncu zanke počistite sliko. To vam bo pomagalo videti, kdaj se je vaša animacija končala.

**Namig:** Prepričajte se, da **ne** zamaknete vrstice `sense.clear()`, saj želite, da se zažene samo enkrat na koncu vaše animacije.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 7
---
  
  # Prikaže sliko

  sense.set_pixels(slika)
  sleep(1) 
  
sense.clear()
  
--- /code ---

--- /task ---

--- task ---

**Preizkus:** Znova zaženite kodo. Ko se vaš projekt zaključi, se bo LED matrika počistila in vse luči bodo postale črne (izklopljene).

--- /task ---

--- task ---

**Razhroščevanje**

LED matrika vsako sekundo postane črna:

- Preverite, ali niste zamaknili kode `sense.clear()` v `for` zanki

--- /task ---

--- task ---

Dodajte kodo za čiščenje matrike LED na barvo po vaši izbiri. Ustvarite spremenljivko z imenom `x`, da shranite novo barvo.

Lahko zmešate svojo barvo ali uporabite vrednosti s seznama barv, da ustvarite svojo novo barvo `x`.

[[[generic-theory-simple-colours]]] 
[[[ambient-colours]]]

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 7, 8
---
  
  # Prikaže sliko

  sense.set_pixels(slika)
  sleep(1) 

x = (178, 34, 34)  # Izberite svoje rdeče, zelene, modre vrednosti med 0 in 255
sense.clear(x)
  
--- /code ---

--- /task ---

--- task ---

**Preizkus:** Znova zaženite kodo. Ko je vaš projekt končan, se bo LED matrika pobarvala v vašo izbrano barvo. Barvo lahko spremenite in preizkusite tolikokrat, kot želite.

--- /task ---

--- task ---

**Shrani svoj napredek**

Svoj program lahko shranite v projekt Mission Starter tako, da vnesete ime svoje ekipe, imena članov ekipe in kodo učilnice, ki ste jo prejeli. Svoj program lahko znova naložite v katero koli napravo z internetno povezavo, tako da vnesete ime ekipe in kodo učilnice.

![Posnetek zaslona gumba za shranjevanje Mission Zero](images/savebutton_sl.png)

--- /task ---

--- task ---

--- collapse ---

---
title: Primer dokončane kode
---

![Mreža z 8x8 kvadratki, ki prikazujejo krokodila.](images/croc.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Uvozi knjižnice
from sense_hat import SenseHat
from time import sleep

# Nastavi Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Nastavi barvni senzor
sense.color.gain = 60 # Nastavi občutljivost senzorja
sense.color.integration_cycles = 64 # Interval, v katerem bo opravljeno branje

# Doda barvne spremenljivke in sliko

a = (255, 255, 255) # Bela
c = (0, 0, 0) # Črna
f = (25, 25, 112) # Nočno modra
m = (34, 139, 34) # Drevesno zelena

for i in range(28):
  rgb = sense.color # Preberi barvo iz senzorja
  c = (rgb.red, rgb.green, rgb.blue)

  slika = [
    m, m, m, m, m, c, c, c,
    m, f, m, f, m, m, m, m,
    m, m, m, m, m, m, m, m,
    m, m, c, a, c, c, c, a,
    m, m, c, c, c ,c ,c ,c,
    m, m, c, c, c, a, c, c,
    m, m, m, m, m, m, m, m,
    m, m, m, m, m, m, m, m]


  # Prikaže sliko

  sense.set_pixels(slika)
  sleep(1)

x = (178, 34, 34)  # Izberite svoje rdeče, zelene, modre vrednosti med 0 in 255
sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
