## Mesurer l'humidité

Le capteur d'humidité de l'Astro Pi peut mesurer l'humidité de l'air qui l'entoure, c'est une fonction utile pour t'aider à collecter des données sur les conditions dans l'espace.

![Message relatif à la température](images/degrees-message.gif)

L'Astro Pi mesure l'humidité dans l'ISS en pourcentage de concentration d'eau dans l'air.

Une partie de ta mission est de contribuer à la vie quotidienne de l'équipage à bord de l'ISS, afin de leur faire savoir que l'humidité à bord de la station spatiale est dans les limites normales les rassurera.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Ajoute ce code pour mesurer l'humidité :

```python
humid = sense.humidity
```

\--- /collapse \---

\--- /task \---

\--- task \---

La température est enregistrée très précisément, c’est-à-dire que la valeur stockée a un grand nombre de décimales. Tu peux arrondir la valeur à n'importe quel nombre de décimales. Dans l'exemple, nous avons arrondi à une décimale, mais pour avoir un autre niveau de précision remplace le nombre `1` par le nombre de décimales que tu souhaites.

```python
temp = round( sense.temperature, 1 )
```

\--- /task \---

\--- task \---

Pour afficher la température actuelle sous la forme d'un message défilant à l'écran, ajoute cette ligne de code :

```python
sense.show_message( str(temp) )
```

The `str()` part converts the humidity from a number into text so that the Astro Pi can display it.

\--- /task \---

\--- task \---

La partie `str()` convertit la température d'un nombre en texte pour que l'Astro Pi puisse l'afficher.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

Le vrai Astro Pi mesure la température autour de lui, mais toi tu peux déplacer le curseur de température sur l'émulateur Sense HAT pour simuler des changements de température et tester ton code.

![Humidity slider](images/humidity-slider.png)

**Remarque :** Tu te demandes peut-être pourquoi le curseur de température affiche la température sous forme d'un nombre entier, mais le résultat de la mesure de la température est donnée avec des décimales. L'émulateur simule la légère imprécision du capteur réel, de sorte que le résultat de la mesure de la température que tu vois peut être très légèrement supérieure ou inférieure à la valeur que tu as définie avec le curseur.