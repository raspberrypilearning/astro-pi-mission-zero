## Nasnímanie farby

V tomto kroku nastavíš senzor farieb a jasu. Tento senzor použiješ na odmeranie množstva červeného, zeleného a modrého svetla dopadajúceho na senzor. Tieto hodnoty sa potom použijú na zmenu jednej z farieb v tvojom obrázku.

To znamená, že obrázok sa môže meniť v závislosti od hodnôt odmeraných senzorom. Napríklad astronaut v modrej košeli by videl inú verziu obrázka ako astronaut v červenej košeli.

Na obrázku veľryby, ktorý sme použili v predchádzajúcom kroku, bola farba pozadia čierna. Na uloženie jej RGB farebného kódu sme použili premennú `c`:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Pomocou senzora farieb zmeň jednu z farieb.

Pod riadky, kde definuješ farby, pridaj tento kód:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4
---
# Zistenie farby
rgb = sense.color # získajte farbu zo snímača
c = (rgb.red, rgb.green, rgb.blue) # použite nasnímanú farbu

--- /code ---

--- /task ---

Tento kód nahradí hodnoty RGB uložené v `c` hodnotami farby zistenej senzorom.

Tip: Ak vo svojom obrázku nemáš použitú premennú `c`, nahraď `c` jednou z premenných farieb, ktoré si použil/-a. To umožní senzoru zmeniť túto farbu.

--- task ---

**Test:** Posuň posúvač farieb na farbu podľa vlastného výberu a potom **spusti**. Farba pozadia sa zmení. Zopakuj tento test s novou farbou.

**Tip:** Pri každej zmene farby treba kliknúť na „Spustiť“.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Teraz s zobrazil/-a obrázok, zistil/-a farbu a použil/-a ju vo svojom programe a tvoj kód je pripravený na odoslanie! 

Program môžeš uložiť a odoslať pomocou formulára v dolnej časti editora kódu.
  
Možno však budeš chcieť do svojho projektu pridať viac obrázkov alebo ho oživiť animáciou. Nasledujúce kroky ti ukážu, ako to urobiť.
</p>

## Animuj svoj projekt (voliteľné)

Tvoj program Mission Zero môže byť na Medzinárodnej vesmírnej stanici (ISS) spustený až 30 sekúnd. Tento čas spustenia môžeš využiť na zobrazenie animácie na LED matrici prepínaním medzi dvoma alebo viacerými rôznymi obrázkami.

--- task ---


**Pridaj** druhý obrázok hneď pod riadok kódu `sense.set_pixels(image)`. Daj mu názov premennej `image2` a zmeň niekoľko pixelov, aby tvoja animačná snímka vyzerala inak. Potom za ním pridaj krátku pauzu.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
image = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# Sem sa pridávajú ďalšie obrázky/snímky:

image2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

Úplne na konci súboru s kódom nastavte slučku `for` tak, aby sa opakovala `14` krát a striedavo zobrazovala `image` a `image2` s 1-sekundovou pauzou na každej snímke.

**Tip:** Uisti sa, že riadky kódu pod `for i in range(14):` sú odsadené medzerou, aby sa nachádzali **vnútri** bloku slučky.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
image2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Zopakujte 14-krát (14 x 2 sekundy = celkový čas animácie 28 sekúnd)
for i in range(14):
  # Zobraziť druhý obrázok
  sense.set_pixels(image2)
  sleep(1)

  # Zobraziť prvý obrázok
  sense.set_pixels(image)
  sleep(1)
  
--- /code ---

--- /task ---

--- task ---

**Test:** Znova spusti kód. Tvoj program okamžite zobrazí nasnímanú farbu a potom sa bude v slučke prepínať tam a späť pre animované zobrazenie.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Ak chceš mať v animácii viac ako dve snímky, musíš dbať na to, aby program nebežal dlhšie ako 30 sekúnd. Ak máš napríklad 10 obrázkov, ktoré sa zobrazujú 1 sekundu, musíš zmeniť slučku ‚for‘ tak, aby sa opakovala 3-krát (10 x 3 = 30 sekúnd)
</p>

--- task ---

**Kontrola chýb**

Môj kód má chybu syntaxe alebo nemení snímky:
- Skontroluj, či tvoj kód slučky `for` zodpovedá odsadeniu v príklade.
- Uisti sa, že druhá matica obrázka má názov `image2` a že sa nachádza mimo a pred začiatkom slučky.
- Skontroluj, či sú tvoje časy `sleep` nastavené presne na `1` sekundu, aby sa predišlo prekročeniu prísneho 30-sekundového limitu pre spustenie na ISS.

--- /task ---

--- task ---

**Ukladaj si priebeh**

Svoj program si môžeš uložiť do projektu Mission Starter zadaním názvu tímu, mien členov tímu a kódu triedy, ktorý si dostal/-a. Svoj program môžeš znova načítať na akomkoľvek zariadení s internetovým pripojením zadaním názvu tímu a kódu triedy.

--- /task ---

--- task ---

--- collapse ---
---
title: Príklad hotového kódu veľryby
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importujte knižnice
from sense_hat import SenseHat
from time import sleep

# Nastavte Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Nastavte snímač farieb
sense.color.gain = 60 # Nastavte citlivosť snímača
sense.color.integration_cycles = 64 # Interval, v ktorom sa bude vykonávať snímanie

# Pridajte farebné premenné a obrázok
a = (255, 255, 255) # Biela
c = (0, 0, 0)       # Čierna
f = (36, 128, 200)  # Morská modrá
g = (0, 204, 255)   # Nebeská modrá

# Zistenie farby
rgb = sense.color # získajte farbu zo snímača
c = (rgb.red, rgb.green, rgb.blue)

image = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(image)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Príklad hotového kódu veľryby (s animáciou)
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importujte knižnice
from sense_hat import SenseHat
from time import sleep

# Nastavte Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Nastavte snímač farieb
sense.color.gain = 60 # Nastavte citlivosť snímača
sense.color.integration_cycles = 64 # Interval, v ktorom sa bude vykonávať snímanie

# Pridajte farebné premenné a obrázok
a = (255, 255, 255) # Biela
c = (0, 0, 0)       # Čierna
f = (36, 128, 200)  # Morská modrá
g = (0, 204, 255)   # Nebeská modrá

# Zistenie farby
rgb = sense.color # získajte farbu zo snímača
c = (rgb.red, rgb.green, rgb.blue)

image = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# ZÁKLADNÉ ODOSLANIE je hotové

# Sem sa pridávajú ďalšie obrázky/snímky:
image2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# Zopakujte 14-krát (14 x 2 sekundy = celkový čas animácie 28 sekúnd)
for i in range(14):
  # Zobraziť druhý obrázok
  sense.set_pixels(image2)
  sleep(1)

  # Zobraziť prvý obrázok
  sense.set_pixels(image)
  sleep(1)
  
--- /code ---

--- /collapse ---

--- /task ---
