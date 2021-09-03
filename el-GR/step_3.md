## Εμφάνιση μηνύματος και επιλογή ονόματος για τους νέους υπολογιστές Astro Pi

--- task ---

Άνοιξε τον [εξομοιωτή Sense HAT](https://trinket.io/mission-zero){:target="_blank"} για το έργο Mission Zero.

Θα δεις τρεις γραμμές κώδικα που έχουν προστεθεί αυτόματα:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![Ένα στιγμιότυπο οθόνης του εξομοιωτή Trinket Sense Hat με τρεις γραμμές κώδικα που εμφανίζονται στο αριστερό παράθυρο.](images/sense-hat-emulator2.png)

Ο κώδικας αυτός συνδέεται στο Astro Pi και εξασφαλίζει ότι η οθόνη LED του Astro Pi εμφανίζεται στη σωστή κατεύθυνση. Άφησε αυτόν τον κώδικα εκεί, γιατί θα τον χρειαστείς.

--- /task ---

--- task ---

Μήπως θέλεις να στείλεις έναν χαιρετισμό στους αστροναύτες στον Διεθνή Διαστημικό Σταθμό που εργάζονται κοντά στον Astro Pi; Ας κυλήσουμε ένα μήνυμα στην οθόνη.

Πρόσθεσε αυτή τη γραμμή κάτω από τον υπόλοιπο κώδικα:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

Πάτησε το κουμπί «**Run**» (Εκτέλεση) και παρακολούθησε το κυλιόμενο μήνυμα «`Astro Pi`» στην οθόνη LED.

![Ο εξομοιωτής Trinket Sense HAT εκτελεί ένα δείγμα προγράμματος το οποίο μετακινεί το κείμενο "Astro PI" στη οθόνη LED με λευκά γράμματα](images/M0_1.gif)

--- /task ---

Για να εμφανίσεις ένα διαφορετικό μήνυμα, μπορείτε να γράψεις ότι άλλο θέλεις μεταξύ των εισαγωγικών (`" "`).

--- collapse ---
---
title: Τι χαρακτήρες μπορούν να χρησιμοποιηθούν;
---

Το Sense HAT μπορεί να εμφανίσει μόνο το σύνολο χαρακτήρων Latin 1, που σημαίνει ότι διατίθενται μόνο οι ακόλουθοι χαρακτήρες. Οποιοσδήποτε άλλος χαρακτήρας θα εμφανίζεται ως `?`.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

Μπορείς επίσης να αλλάξεις την ταχύτητα κύλισης του μηνύματος στην οθόνη. Πρόσθεσε την παράμετρο `scroll_speed` στη γραμμή κώδικα που έχεις ήδη, ως εξής:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Η προεπιλεγμένη ταχύτητα του μηνύματος είναι `0.1`. Αν μειώσεις τον αριθμό, το μήνυμα θα κυλάει πιο γρήγορα. Αν τον αυξήσεις, το μήνυμα θα κυλάει πιο αργά.

--- /task ---

### Επίλεξε ένα όνομα για τους νέους υπολογιστές Astro Pi

--- task --- Θα ονομάσουμε τους υπολογιστές Astro Pi με ονόματα από δύο εμπνευσμένους Ευρωπαίους επιστήμονες. Υπάρχουν εκατοντάδες άνδρες και γυναίκες που έχουν συμβάλει στην επιστήμη και την τεχνολογία. Οι συμμετέχοντες μπορούν να προτείνουν τα δικά τους ονόματα ή να επιλέξουν από τη λίστα προτάσεών μας (βεβαιώσου ότι χρησιμοποιείς την αγγλική εκδοχή του ονόματος):


[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace){:target="_blank"} 
[Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing){:target="_blank"} 
[Caroline Herschel](https://en.wikipedia.org/wiki/Caroline_Herschel){:target="_blank"} 
[Edsger Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra){:target="_blank"} 
[Hedy Lamarr](https://en.wikipedia.org/wiki/Hedy_Lamarr){:target="_blank"} 
[Hypatia](https://en.wikipedia.org/wiki/Hypatia){:target="_blank"} 
[John Edmonstone](https://en.wikipedia.org/wiki/John_Edmonstone){:target="_blank"} 
[Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie){:target="_blank"} 
[Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla){:target="_blank"} 
[Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe){:target="_blank"}

Για να ψηφίσεις, ξεκίνα το μήνυμά σου με τις λέξεις "My name should be". Για παράδειγμα, αν ένας συμμετέχων ή μια ομάδα θα ήθελε να ψηφίσει για την Ada Lovelace, ο κώδικάς τους θα μοιάζει κάπως έτσι:

```python
sense.show_message("My name should be Ada Lovelace")
```

Εάν θέλεις να ψηφίσεις, το μήνυμά σου *πρέπει* να ξεκινά με αυτές τις λέξεις, διαφορετικά δεν θα μπορούμε να μετρήσουμε αυτόματα την καταχώρισή σου.

--- /task ---



