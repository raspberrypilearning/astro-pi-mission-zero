## Sanse en farge

I dette trinnet konfigurerer du farge- og lysstyrkesensoren. Du skal bruke denne sensoren til å måle mengden rødt, grønt og blått lys som når sensoren. Disse verdiene vil deretter bli brukt til å endre en av fargene i det valgte bildet.

Dette betyr at bildet kan endre seg avhengig av hva sensoren ser. For eksempel ville en astronaut som har på seg en blå skjorte se en annen versjon av bildet enn en astronaut som har på seg en rød skjorte.

I hvalbildet vi brukte i forrige trinn, var bakgrunnsfargen svart. Vi brukte variabelen `c` til å lagre RGB-fargekoden:

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

Bruk fargesensoren til å endre en av fargene dine.

Legg til følgende kode under linjene der du definerer fargene:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 3, 4
---
# Detekter en farge
rgb = sense.color # hent fargen fra sensoren
c = (rgb.red, rgb.green, rgb.blue) # bruke den sansede fargen

--- /code ---

--- /task ---

Denne koden erstatter RGB-verdiene som er lagret i `c`, med verdiene for fargen som oppdages av sensoren.

Tips: Hvis du ikke brukte variabelen `c` i ditt eget bilde, kan du erstatte `c` med en av fargevariablene du brukte. Dette lar sensoren endre den fargen i stedet.

--- task ---

**Test:** Flytt fargegjenryteren til en farge du velger, og deretter **kjør** koden din. Bakgrunnsfargen din endres. Gjenta denne testen igjen med en ny farge.

**Tips:** Du må klikke 'Run (Kjør)' hver gang du endrer fargen.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Nå har du vist et bilde og registrert en farge og brukt den i programmet ditt, og koden din er klar til innsending! 

Du kan lagre og sende inn programmet ditt ved hjelp av skjemaet nederst i koderedigeringsverktøyet.
  
Du kan imidlertid ønske å legge til flere bilder i prosjektet ditt, eller gjøre det levende med animasjon. De neste trinnene viser deg hvordan du gjør dette.
</p>

## Animer prosjektet ditt (valgfritt)

Mission Zero-programmet ditt kan kjøre på den internasjonale romstasjonen (ISS) i opptil 30 sekunder. Du kan bruke denne kjøretiden til å vise en animasjon på LED-matrisen ved å veksle mellom to eller flere forskjellige bilder.

--- task ---


**Legg til** et bilde til rett under kodelinjen `sense.set_pixels(bilde)`. Gi den variabelnavnet `bilde2` og endre noen piksler for å få animasjonsrammen til å se annerledes ut. Legg så til en kort pause etterpå.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
bilde = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(bilde)

# Ekstra bilder/rammer kommer her:

bilde2 = [
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

Helt nederst i kodefilen setter du opp `for` -løkken din til å gjenta `14` ganger og veksler mellom å vise `bilde` og `bilde2` med 1 sekunds pause på hver billedramme.

**Tips:** Sørg for at kodelinjene under `for i i range(14):` er innrykket med et mellomrom slik at de sitter **inni** løkkeblokken.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
bilde2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# I sløyfe 14 ganger (14 * 2 sekunder = 28 sekunder total animasjon)
for i in range(14):
  # Vis det andre bildet
  sense.set_pixels(bilde2)
  sleep(1)

  # Vis det første bildet
  sense.set_pixels(bilde)
  sleep(1)
  
--- /code ---

--- /task ---

--- task ---

**Test:** Kjør koden din igjen. Programmet ditt vil vise den registrerte fargen umiddelbart, og deretter gå frem og tilbake i en animert visning.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Hvis du ønsker å ha mer enn to bilder i animasjonen, må du sørge for at programmet kjører i ikke mer enn 30 sekunder. Hvis du for eksempel har 10 bilder som hvert vises i 1 sekund, må du endre `for`-løkken til å gjentas 3 ganger (10 * 3 = 30 sekunder).
</p>

--- task ---

**Sjekk om det finnes feil**

Koden min har en syntaksfeil eller endrer ikke billedramme:
- Sjekk at `for`-løkkekoden samsvarer med innrykket i eksemplet.
- Sørg for at du har kalt den andre bildematrisen `bilde2` og at den er plassert utenfor og før løkken begynner.
- Sjekk at `sleep-`-tidene dine er satt til nøyaktig `1` sekund for å unngå å overskride ISS' strenge frist på 30 sekunders utførelse.

--- /task ---

--- task ---

**Lagre fremgangen din**

Du kan lagre programmet ditt på Mission Starter-prosjektet ved å skrive inn lagnavnet ditt, lagmedlemmenes navn og klasseromskoden du har fått. Du kan laste inn programmet på nytt på en hvilken som helst enhet med internettforbindelse ved å skrive inn lagnavnet og klasseromskoden.

--- /task ---

--- task ---

--- collapse ---
---
title: Kodeeksempel for ferdig hval
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importer bibliotekene
from sense_hat import SenseHat
from time import sleep

# Sett opp Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Sett opp fargesensoren
sense.color.gain = 60 # Angi følsomheten til sensoren
sense.color.integration_cycles = 64 # Intervallet som avlesningens skal utføres i

# Legg til fargevariabler og bilde
a = (255, 255, 255) # Hvit
c = (0, 0, 0)       # Svart
f = (36, 128, 200)  # Havblå
g = (0, 204, 255)   # Himmelblå

# Detekter en farge
rgb = sense.color # hent fargen fra sensoren
c = (rgb.red, rgb.green, rgb.blue)

bilde = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(bilde)

--- /code ---

--- /collapse ---

--- collapse ---
---
tittel: Kodeeksempel for ferdig hval (med animasjon)
---

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
# Importer bibliotekene
from sense_hat import SenseHat
from time import sleep

# Sett opp Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Sett opp fargesensoren
sense.color.gain = 60 # Angi følsomheten til sensoren
sense.color.integration_cycles = 64 # Intervallet som avlesningens skal utføres i

# Legg til fargevariabler og bilde
a = (255, 255, 255) # Hvit
c = (0, 0, 0)       # Svart
f = (36, 128, 200)  # Havblå
g = (0, 204, 255)   # Himmelblå

# Detekter en farge
rgb = sense.color # hent fargen fra sensoren
c = (rgb.red, rgb.green, rgb.blue)

bilde = [
c, g, c, g, c, c, c, c,
c, c, g, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sense.set_pixels(bilde)

# GRUNNLEGGENDE INNSENDING er over nå

# Ekstra bilder/rammer kommer her:
bilde2 = [
c, c, c, c, c, c, c, c,
c, c, c, c, c, f, f, f,
c, f, f, f, c, c, f, c,
f, f, c, f, f, c, f, c,
f, f, f, f, f, c, f, c,
g, f, f, f, f, f, f, c,
g, g, g, g, g, g, c, c,
c, g, g, g, g, c, c, c]

sleep(1)

# I sløyfe 14 ganger (14 * 2 sekunder = 28 sekunder total animasjon)
for i in range(14):
  # Vis det andre bildet
  sense.set_pixels(bilde2)
  sleep(1)

  # Vis det første bildet
  sense.set_pixels(bilde)
  sleep(1)
  
--- /code ---

--- /collapse ---

--- /task ---
