## Ανίχνευση ενός χρώματος

Σε αυτό το βήμα, θα ρυθμίσεις τον αισθητήρα φωτεινότητας χρώματος και θα τον χρησιμοποιήσεις για να ανιχνεύσεις την ποσότητα του κόκκινου, πράσινου και μπλε που φτάνει στον αισθητήρα. Αυτό το χρώμα θα χρησιμοποιηθεί στη συνέχεια για να χρωματίσεις την εικόνα που έχεις επιλέξει. Ένας αστροναύτης που θα περπατούσε προς τον αισθητήρα με μπλε πουκάμισο θα έβλεπε μια διαφορετική εικόνα από έναν αστροναύτη με κόκκινο πουκάμισο.

![εικόνα που εμφανίζεται με ροζ φόντο στην οθόνη LED](images/colour_background.png)

Για όποια εικόνα επέλεξες, το φόντο χρησιμοποιεί τη μεταβλητή `c` η οποία είναι αρχικά ορισμένη ως μαύρο.

--- task ---

Χρησιμοποίησε τον αισθητήρα χρώματος για να χρωματίσεις το φόντο σου.

Πρόσθεσε κώδικα πριν τη λίστα εικόνων για να πάρεις το χρώμα από τον αισθητήρα και να αλλάξεις το χρώμα της μεταβλητής φόντου `c` για να χρησιμοποιήσεις το χρώμα που ανίχνευσε ο αισθητήρας χρωμάτων Sense HAT αντί για το μαύρο.

**Συμβουλή:** Δεν χρειάζεται να πληκτρολογήσεις τα σχόλια που ξεκινούν με '#' (βρίσκονται εκεί για να εξηγήσουν τον κώδικα).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 9-10
---

# Προσθήκη μεταβλητών χρωμάτων και εικόνας

c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange y = (255, 20, 147) # DeepPink

rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

**Δοκιμή:** Μετακίνησε τη γραμμή κύλισης χρώματος προς ένα χρώμα της επιλογής σου και μετά κάνε **run** τον κώδικά σου. Το χρώμα του φόντου σου θα αλλάξει. Επανάλαβε αυτή τη δοκιμή ξανά με ένα νέο χρώμα.

**Συμβουλή:** Θα πρέπει να κάνεις κλικ στο «Run» κάθε φορά που αλλάζεις το χρώμα.

--- /task ---

## Επανάληψη του προγράμματός σου

Το πρόγραμμα Astro Pi Mission Zero επιτρέπεται να εκτελεστεί έως και για 30 δευτερόλεπτα. Θα χρησιμοποιήσεις αυτό το χρονικό διάστημα για να ελέγχεις επανειλημμένα τον αισθητήρα χρώματος και να ενημερώνεις την εικόνα.

Ο κώδικάς σου θα χρησιμοποιήσει ένα βρόχο `for` που θα εκτελεστεί 28 φορές. **Κάθε** φορά θα:
+ ανιχνεύεις το πιο πρόσφατο χρώμα
+ ενημερώνεις το χρώμα φόντου της εικόνας
+ κάνεις παύση για ένα δευτερόλεπτο

--- task ---

**Βρες** τη δική σου γραμμή κώδικα `rgb = sense.color`.

**Πρόσθεσε** κώδικα από πάνω για να ορίσεις τον βρόχο `for` στις `28` επαναλήψεις.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 1
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

--- /code ---

--- /task ---

--- task ---

Τώρα πρέπει να κάνεις εσοχή σε όλο τον κώδικά σου κάτω από τον βρόχο `for`, έτσι ώστε να βρίσκεται **μέσα** στον βρόχο `for`.

**Συμβουλή:** Για να δημιουργήσεις εσοχές σε πολλές γραμμές, επισήμανε τις γραμμές που θέλεις να βάλεις σε εσοχή και στη συνέχεια, πάτα το πλήκτρο <kbd>Tab</kbd> στο πληκτρολόγιό σου (συνήθως πάνω από το πλήκτρο <kbd>Caps Lock</kbd> στο πληκτρολόγιο).

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2 - 17
---

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

  # Display the image

  sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Στο κάτω μέρος του κώδικά σου, πρόσθεσε ένα `sleep` του ενός δευτερολέπτου στον βρόχο σου:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 4
---

  # Display the image

  sense.set_pixels(image) sleep(1)

--- /code ---

**Συμβουλή:** Βεβαιώσου ότι αυτή η γραμμή κώδικα έχει εσοχές μέσα στον βρόχο `for`.

--- /task ---

--- task ---

**Δοκιμή:** Εκτέλεσε τον κώδικά σου και άλλαξε τον επιλογέα χρώματος πολλές φορές καθώς εκτελείται το έργο σου. Έλεγξε ότι η εικόνα σου ενημερώνεται για να χρησιμοποιηθεί το χρώμα που ανιχνεύθηκε στην επόμενη εκτέλεση.

Η εικόνα θα σταματήσει να ενημερώνεται όταν τελειώσει ο βρόχος, έτσι ώστε το πρόγραμμα να μην εκτελείται για περισσότερο από 30 δευτερόλεπτα.

--- /task ---

--- task ---

**Εντοπισμός σφαλμάτων**

Ο κώδικάς μου έχει συντακτικό λάθος ή δεν εκτελείται όπως αναμένεται:

- Έλεγξε ότι ο κώδικάς σου ταιριάζει με τον κώδικα στα παραπάνω παραδείγματα
- Βεβαιώσου ότι έχεις κάνει εσοχή στον κώδικα μέσα στον βρόχο `for`
- Έλεγξε ότι η λίστα σου περιβάλλεται από `[` και `]`
- Έλεγξε ότι κάθε μεταβλητή για τα χρώματα στη λίστα διαχωρίζεται με κόμμα

Ο κώδικάς μου εκτελείται για περισσότερο από 30 δευτερόλεπτα:

- Μείωσε τον αριθμό των φορών που εκτελείται ο βρόχος, από 28 σε 25 ή ακόμη και 20.
- Μείωσε τη διάρκεια του sleep, από 1 δευτερόλεπτο σε 0,5 δευτερόλεπτα.

--- /task ---

--- task ---

Πρόσθεσε `sense.clear()` στο τέλος του κώδικά σου για να καθαρίσεις την εικόνα στο τέλος του βρόχου σου. Αυτό θα σε βοηθήσει να δεις πότε θα τελειώσει η εκτέλεση της κινούμενης εικόνας σου.

**Συμβουλή:** Βεβαιώσου ότι **δεν κάνεις** εσοχή στη γραμμή κώδικα `sense.clear()`, καθώς θέλεις να εκτελείται μόνο μία φορά στο τέλος της κινούμενης εικόνας σου.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 6
---

  # Display the image

  sense.set_pixels(image) sleep(1)

sense.clear()

--- /code ---

--- /task ---

--- task ---

**Δοκιμή:** Εκτέλεσε τον κώδικά σου πάλι. Όταν το έργο σου έχει τελειώσει την εκτέλεσή του, η οθόνη LED θα καθαρίσει, κάνοντας όλα τα φώτα μαύρα (σβηστά).

--- /task ---

--- task ---

**Εντοπισμός σφαλμάτων**

Ο οθόνη LED γίνεται μαύρη κάθε δευτερόλεπτο:

- Έλεγξε ότι δεν έχεις βάλει σε εσοχή τον κώδικα `sense.clear()` μέσα στον βρόχο `for`

--- /task ---

--- task ---

Πρόσθεσε κώδικα για να καθαρίσεις την οθόνη LED σε ένα χρώμα της επιλογής σου. Δημιούργησε μια μεταβλητή που ονομάζεται `x` για να αποθηκεύσεις το νέο σου χρώμα.

Μπορείς να αναμίξεις το δικό σου χρώμα ή να χρησιμοποιήσεις τις τιμές από τη λίστα χρωμάτων για να δημιουργήσεις το νέο σου χρώμα `x`.

\[[[generic-theory-simple-colours]]\] \[[[ambient-colours\]]]

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 6-7
---

  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /task ---

--- task ---

**Δοκιμή:** Εκτέλεσε τον κώδικά σου πάλι. Όταν ολοκληρωθεί η εκτέλεση του έργου σου, η οθόνη LED θα καθαρίσει στο χρώμα που έχεις επιλέξει. Μπορείς να αλλάξεις και στη συνέχεια να δοκιμάσεις το χρώμα όσες φορές θέλεις.

--- /task ---

--- task ---

--- collapse ---

---
title: Παράδειγμα ολοκληρωμένου κώδικα
---

![Ένα πλέγμα με 8 x 8 τετράγωνα που δείχνει ένα ροζ λουλούδι σε ένα πράσινο μίσχο.](images/flower.png)

--- code ---
---
language: python filename: main.py
line_numbers: false
---
# Import the libraries
from sense_hat import SenseHat from time import sleep

# Set up the Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image

c = (0, 0, 0) # Black m = (34, 139, 34) # ForestGreen q = (255, 255, 0) # Yellow t = (255, 140, 0) # DarkOrange y = (255, 20, 147) # DeepPink

for i in range(28): rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

  image = [ c, c, y, y, y, y, c, c, c, y, y, t, t, y, y, c, y, y, t, q, q, t, y, y, c, y, y, t, t, y, y, c, c, c, y, y, y, y, c, c, m, c, c, m, m, c, c, m, c, m, m, m, m, m, m, c, c, c, c, m, m, c, c, c]

  # Display the image

  sense.set_pixels(image) sleep(1)

x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255 sense.clear(x)

--- /code ---

--- /collapse ---

--- /task ---
