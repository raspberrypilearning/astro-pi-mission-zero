## Ανίχνευση ενός χρώματος

Σε αυτό το βήμα, θα ρυθμίσετε τον αισθητήρα χρώματος και φωτεινότητας. Θα χρησιμοποιήσετε αυτόν τον αισθητήρα για να μετρήσετε την ποσότητα κόκκινου, πράσινου και μπλε φωτός που φτάνει στον αισθητήρα. Αυτές οι τιμές θα χρησιμοποιηθούν στη συνέχεια για να αλλάξετε ένα από τα χρώματα στην εικόνα που έχετε επιλέξει.

Αυτό σημαίνει ότι η εικόνα μπορεί να αλλάξει ανάλογα με το τι βλέπει ο αισθητήρας. Για παράδειγμα, ένας αστροναύτης που φοράει μπλε πουκάμισο θα έβλεπε μια διαφορετική εκδοχή της εικόνας από έναν αστροναύτη που φοράει κόκκινο πουκάμισο.

Στην εικόνα της φάλαινας που χρησιμοποιήσαμε στο προηγούμενο βήμα, το χρώμα φόντου ήταν μαύρο. Χρησιμοποιήσαμε τη μεταβλητή `c` για να αποθηκεύσουμε τον κωδικό χρώματος RGB:

--- code ---
---
language: python filename: main.py line_numbers: false
line_number_start: 1
---
c = (0, 0, 0)

--- /code ---


--- task ---

Χρησιμοποιήστε τον αισθητήρα χρώματος για να αλλάξετε ένα από τα χρώματά σας.

Κάτω από τις γραμμές όπου ορίζετε τα χρώματα, προσθέστε τον ακόλουθο κώδικα:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 3, 4
---
# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

--- /code ---

--- /task ---

Αυτός ο κώδικας αντικαθιστά τις τιμές RGB που είναι αποθηκευμένες στο `c` με τις τιμές για το χρώμα που ανιχνεύεται από τον αισθητήρα.

Συμβουλή: Εάν δεν χρησιμοποιήσατε τη μεταβλητή `c` στη δική σας εικόνα, αντικαταστήστε την `c` με μία από τις μεταβλητές χρώματος που χρησιμοποιήσατε. Αυτό θα επιτρέψει στον αισθητήρα να αλλάξει αυτό το χρώμα.

--- task ---

**Δοκιμή:** Μετακίνησε τη γραμμή κύλισης χρώματος προς ένα χρώμα της επιλογής σου και μετά κάνε **εκτέλεση(run)** τον κώδικά σου. Το χρώμα του φόντου σου θα αλλάξει. Επανάλαβε αυτή τη δοκιμή ξανά με ένα νέο χρώμα.

**Συμβουλή:** Θα πρέπει να κάνεις κλικ στο «Run» κάθε φορά που αλλάζεις το χρώμα.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Τώρα έχετε εμφανίσει μια εικόνα και έχετε ανιχνεύσει ένα χρώμα και το έχετε χρησιμοποιήσει στο πρόγραμμά σας, και ο κώδικάς σας είναι έτοιμος για υποβολή! 

Μπορείτε να αποθηκεύσετε και να υποβάλετε το πρόγραμμά σας χρησιμοποιώντας τη φόρμα στο κάτω μέρος του προγράμματος code editor.
  
Ωστόσο, ίσως θελήσετε να προσθέσετε περισσότερες εικόνες στο έργο σας ή να το ζωντανέψετε με κινούμενα σχέδια. Τα επόμενα βήματα σας δείχνουν πώς να το κάνετε αυτό.
</p>

## Δώστε κίνηση στο έργο σας (προαιρετικό)

Το πρόγραμμα Mission Zero μπορεί να εκτελεστεί στον Διεθνή Διαστημικό Σταθμό (ISS) για έως και 30 δευτερόλεπτα. Μπορείτε να χρησιμοποιήσετε αυτόν τον χρόνο εκτέλεσης για να εμφανίσετε μια κινούμενη εικόνα στην οθόνη LED, εναλλάσσοντας δύο ή περισσότερες διαφορετικές εικόνες.

--- task ---


**Προσθέστε** μια δεύτερη εικόνα ακριβώς κάτω από τη γραμμή κώδικα `sense.set_pixels(image)`. Δώστε στη μεταβλητή το όνομα `image2` και αλλάξτε μερικά εικονοστοιχεία για να κάνετε το πλαίσιο της κινούμενης εικόνας να φαίνεται διαφορετικό. Στη συνέχεια, προσθέστε μια σύντομη παύση μετά από αυτό.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
---
image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# Extra images / frames go here:

image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

--- /code ---

--- /task ---

--- task ---

Στο κάτω μέρος του αρχείου σας με τον κώδικα, ρυθμίστε τον βρόχο `for` ώστε να επαναλαμβάνεται ο βρόχος `14` φορές και εναλλάξ να εμφανίζει την εικόνα `image` και την εικόνα `image2` κάνοντας παύση για 1 δευτερόλεπτο σε κάθε καρέ.

**Συμβουλή:** Βεβαιωθείτε ότι οι γραμμές κώδικα κάτω από το `for i in range(14):` έχουν εσοχή με κενό, ώστε να βρίσκονται **μέσα στο** μπλοκ του βρόχου.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 14, 15, 16, 17, 18, 19, 20, 21, 22
---
image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1)

--- /code ---

--- /task ---

--- task ---

**Δοκιμή:** Εκτέλεσε τον κώδικά σου πάλι. Το πρόγραμμά σας θα εμφανίσει αμέσως το χρώμα που ανιχνεύσατε και στη συνέχεια θα κάνει επανάληψη μπρος-πίσω για μια κινούμενη οθόνη.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Αν θέλετε να έχετε περισσότερα από δύο καρέ στην κινούμενη εικόνα σας, πρέπει να βεβαιωθείτε ότι το πρόγραμμα θα εκτελεστεί για όχι περισσότερο από 30 δευτερόλεπτα. Για παράδειγμα, αν έχετε 10 εικόνες που η καθεμία εμφανίζεται για 1 δευτερόλεπτο, πρέπει να αλλάξετε τον βρόχο `for` ώστε να επαναλαμβάνεται 3 φορές (10 * 3 = 30 δευτερόλεπτα)
</p>

--- task ---

**Έλεγχος για σφάλματα**

Ο κώδικάς μου έχει ένα συντακτικό σφάλμα ή δεν αλλάζει τα καρέ:
- Ελέγξτε ότι ο κώδικας βρόχου `for` ταιριάζει με την εσοχή στο παράδειγμα.
- Βεβαιωθείτε ότι έχετε ονομάσει τον δεύτερο πίνακα εικόνων `image2` και ότι βρίσκεται έξω και πριν από την έναρξη του βρόχου.
- Ελέγξτε ότι οι χρόνοι `sleep` έχουν οριστεί ακριβώς σε `1` δευτερόλεπτο για να αποφύγετε την υπέρβαση του αυστηρού ορίου εκτέλεσης των 30 δευτερολέπτων στον ISS.

--- /task ---

--- task ---

**Αποθήκευσε την πρόοδό σου**

Μπορείς να αποθηκεύσεις το πρόγραμμά σου στο έργο Mission Starter εισάγοντας το όνομα της ομάδας σου, τα ονόματα των μελών της ομάδας και τον κωδικό της τάξης που σου έχει δοθεί. Μπορείς να φορτώσεις ξανά το πρόγραμμά σου σε οποιαδήποτε συσκευή με σύνδεση στο Διαδίκτυο εισάγοντας το όνομα της ομάδας και τον κωδικό της τάξης σου.

--- /task ---

--- task ---

--- collapse ---
---
title: Παράδειγμα ολοκληρωμένου κώδικα γα τη Φάλαινα
---

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
a = (255, 255, 255) # White c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Παράδειγμα ολοκληρωμένου κώδικα γα τη Φάλαινα (με κινούμενη εικόνα)
---

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
a = (255, 255, 255) # White c = (0, 0, 0)       # Black f = (36, 128, 200)  # Ocean Blue g = (0, 204, 255)   # Sky Blue

# Sense a colour
rgb = sense.color # get the colour from the sensor c = (rgb.red, rgb.green, rgb.blue)

image = [ c, g, c, g, c, c, c, c, c, c, g, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sense.set_pixels(image)

# BASIC SUBMISSION is done by now

# Extra images / frames go here:
image2 = [ c, c, c, c, c, c, c, c, c, c, c, c, c, f, f, f, c, f, f, f, c, c, f, c, f, f, c, f, f, c, f, c, f, f, f, f, f, c, f, c, g, f, f, f, f, f, f, c, g, g, g, g, g, g, c, c, c, g, g, g, g, c, c, c]

sleep(1)

# Loop 14 times (14 * 2 seconds = 28 seconds total animation)
for i in range(14): # Display the second image sense.set_pixels(image2) sleep(1)

  # Display the first image sense.set_pixels(image) sleep(1)

--- /code ---

--- /collapse ---

--- /task ---
