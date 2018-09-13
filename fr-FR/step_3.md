## Afficher un message

--- task ---

Ouvre [l'émulateur Sense HAT](https://trinket.io/mission-zero){:target="_blank"} pour le projet Mission Zero.

Tu vas constater que trois lignes de code ont été ajoutées automatiquement:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![émulateur Sense HAT](images/sense-hat-emulator2.png)

Ce code établit la connexion à l'Astro Pi et assure que l'affichage LED de l'Astro Pi s'effectue dans le bon sens. Laisse là ce code car tu en auras besoin.

--- /task ---

--- task ---

Peut-être tu pourrais laisser un message de salutation amical pour les astronautes de la station spatiale internationale (ISS) qui travaillent près de l'Astro Pi ? On va faire défiler un message sur l’écran.

Ajoute cette ligne en-dessous de l'autre ligne de code :

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Appuie sur le bouton **Run** (Exécuter) et regarde comme le message `Astro Pi` défile sur l'écran LED.

![montrer le code du message cliquer run (exécuter)](images/show-message-code-annotated.PNG)

--- /task ---

![Message de défilement](images/scroll-message.gif)

Pour afficher un autre message tu peux écrire ce que tu veux entre les guillemets (`""`).

--- collapse ---
---
title: Quels caractères peuvent être utilisés ?
---
Le Sense HAT ne peut afficher que le jeu de caractères Latin 1, ce qui signifie que seuls les caractères suivants sont disponibles. Les autres caractères s'afficheront sous la forme d'un `?` .

    +-*/!"#$><0123456789.=)(
    
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    abcdefghijklmnopqrstuvwxyz
    
    ?,;:|@%[&_']~
    

--- /collapse ---

--- task ---

Tu peux aussi modifier la vitesse de défilement du message sur l'écran. Ajoute un `scroll_speed` (vitesse de défilement) à ta ligne de code, comme cela :

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

La vitesse par défaut du message est `0.1` . En réduisant le nombre, tu fais défiler le message plus rapidement et en augmentant le nombre tu fais défiler le message plus lentement.

--- /task ---
