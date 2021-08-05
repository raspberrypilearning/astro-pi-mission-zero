## Afficher un message et choisir un nom pour les nouveaux ordinateurs Astro Pi

--- task ---

Ouvre [l'émulateur Sense HAT](https://trinket.io/mission-zero){:target="_blank"} pour le projet Mission Zero.

Tu vas constater que trois lignes de code ont été ajoutées automatiquement :

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![émulateur Sense HAT](images/sense-hat-emulator2.png)

Ce code se connecte à l'Astro Pi et s'assure que l'écran LED de l'Astro Pi est affiché dans le bon sens. Laisse ce code ici car tu en auras besoin.

--- /task ---

--- task ---

Peut-être pourrais-tu laisser un message de bienvenue aux astronautes de l'ISS qui travaillent près de l'Astro Pi ? Faisons défiler un message sur l'écran.

Ajoute cette ligne en-dessous de l'autre ligne de code :

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Appuie sur le bouton **Run** (Exécuter) et regarde le message `Astro Pi` défiler sur l'écran LED.

![afficher le code du message cliquer run (exécuter)](images/show-message-code-annotated.PNG)

--- /task ---

![Message de défilement](images/scroll-message.gif)

Pour afficher un message différent, tu peux écrire ce que tu veux entre les guillemets (`""`).

--- collapse ---

---
title: Quels caractères peuvent être utilisés ?
---

Le Sense HAT ne peut afficher que le jeu de caractères Latin 1, ce qui signifie que seuls les caractères suivants sont disponibles. Les autres caractères s'afficheront sous la forme d'un `?` .

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

Tu peux aussi modifier la vitesse de défilement du message sur l'écran. Ajoute un `scroll_speed` (vitesse de défilement) à ta ligne de code, comme ceci :

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

La vitesse par défaut du message est `0.1`. En réduisant le nombre, tu fais défiler le message plus rapidement et en augmentant le nombre tu fais défiler le message plus lentement.

--- /task ---

### Choisis un nom pour les nouveaux ordinateurs Astro Pi

--- task --- We will name the Astro Pi computers after two inspirational European scientists. There are hundreds of men and women that have contributed to science and technology, and participants can suggest their own names, or pick from our list of suggestions:


[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"}: [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) [Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel) [Edsgar Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra) [Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr) [Hypatia](https://en.wikipedia.org/wiki/Hypatia) [John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone) [Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie) [Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla) [Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe)

To vote, start your message with the words "My name should be". For example, you want to vote for Ada Lovelace, your code would look like this:

```python
sense.show_message("Mon nom doit être Ada Lovelace")
```
--- /task ---



