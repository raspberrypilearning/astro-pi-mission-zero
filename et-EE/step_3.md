## Kuva sõnum ja vali uutele Astro Pi arvutitele nimi

--- task ---

Ava [Sense HAT-i emulaator](https://trinket.io/mission-zero){:target="_blank"} Mission Zero projekti jaoks.

Näed, et sulle on automaatselt lisatud kolm rida koodi:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![sense hat-i emulaator](images/sense-hat-emulator2.png)

See kood ühendub Astro Pi-ga ja tagab, et Astro Pi LED-ekraan kuvatakse õigesti. Jäta kood sinna, sest sul läheb seda vaja.

--- /task ---

--- task ---

Võib-olla jätaksid toreda tervituse neile ISS-i astronautidele, kes töötavad Astro Pi läheduses? Kerime sõnumit tervel ekraanil.

Lisa see rida teise koodi alla:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Vajuta **Käivita** nuppu ja vaata sõnumit `Astro Pi` LED-ekraanil.

![näita sõnumi koodi klõpsa käivita](images/show-message-code-annotated.PNG)

--- /task ---

![Sõnumi kerimine](images/scroll-message.gif)

Teistsuguse sõnumi kuvamiseks kirjuta jutumärkide vahele, mida iganes sa soovid (`""`).

--- collapse ---

---
title: Milliseid tähemärke saab kasutada?
---

Sense HAT-iga saab kuvada ainult Latin 1 tähemärke, seetõttu saab kasutada ainult järgmisi tähemärke. Kõiki teisi tähemärke kuvataks nii `?`.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

Samuti saad muuta ekraanil keritava sõnumi kiirust. Lisa `scroll_speed` olemasolevale koodireale, nagu näidatud:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Sõnumi kerimise vaikekiirus on `0.1`. Numbri vähendamine muudab sõnumi kerimise kiiremaks ja numbri suurendamine muudab selle aeglasemaks.

--- /task ---

### Valige uutele Astro Pi arvutitele nimi

--- task --- Kui soovite uute Mark II Astro Pi arvutite nimevalimise konkursil osaleda, alustage oma sõnumit sõnadega "Minu nimi peaks olema" ja lisage seejärel valik sellest loetelust.

Näiteks juhul, kui soovite hääletada Ada Lovelace'i poolt, näeks teie kood välja selline:

```python
sense.show_message("Minu nimi peaks olema Ada Lovelace")
```
--- /task ---



