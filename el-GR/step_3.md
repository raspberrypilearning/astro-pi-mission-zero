## Εμφάνιση εικόνας

Ο πίνακας LED του Astro Pi μπορεί να εμφανίζει χρώματα. Σε αυτό το βήμα, θα εμφανίσεις εικόνες από τη φύση στη οθόνη LED του Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Ένα <span style="color: #0faeb0">**LED matrix**</span> είναι ένα πλέγμα από LED που μπορούν να ελεγχθούν μεμονωμένα ή ως ομάδα για να δημιουργήσουν διαφορετικά εφέ φωτισμού. Ο πίνακας LED matrix στο Sense HAT έχει 64 LED που εμφανίζονται σε ένα πλέγμα 8 x 8. Τα LED μπορούν να προγραμματιστούν ώστε να παραγάγουν μεγάλη γκάμα χρωμάτων.
</p>

![Ένα στιγμιότυπο οθόνης του παραθύρου εξομοιωτή που δείχνει τη Μονάδα Πτήσης με την οθόνη LED να εμφανίζει μια εικόνα ενός λουλουδιού.](images/fu-pic.png)

--- task ---

Άνοιξε το [αρχικό έργο Mission Zero](https://missions.astro-pi.org/el/mz/code_submissions/new){:target="_blank"}.

Θα δεις ότι μερικές γραμμές κώδικα έχουν ήδη προστεθεί αυτόματα για σένα.

Αυτός ο κώδικας συνδέεται με το Astro Pi, εξασφαλίζει ότι η οθόνη LED του Astro Pi εμφανίζεται με τον σωστό τρόπο και ρυθμίζει τον αισθητήρα χρώματος. Άφησε αυτόν τον κώδικα εκεί, γιατί θα τον χρειαστείς.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 
---
# Εισαγωγή βιβλιοθηκών
from sense_hat import SenseHat 
from time import sleep

# Ρύθμιση του Sense HAT
sense = SenseHat() 
sense.set_rotation(270)

# Ρύθμιση του αισθητήρα χρωμάτων
sense.color.gain = 60 # Ρύθμιση της ευαισθησίας του αισθητήρα
sense.color.integration_cycles = 64 # Το μεσοδιάστημα κατά το οποίο θα γίνεται η ανάγνωση

--- /code ---

![Ένα στιγμιότυπο οθόνης του εξομοιωτή Sense HAT με γραμμές του αρχικού κώδικα να εμφανίζονται στο αριστερό παράθυρο.](images/sense-hat-emulator2.png)

--- /task ---

### Χρώματα RGB

Τα χρώματα μπορούν να δημιουργηθούν χρησιμοποιώντας διαφορετικές αναλογίες κόκκινου, πράσινου και μπλε. Μπορείς να μάθεις για τα χρώματα RGB εδώ:

[[[generic-theory-simple-colours]]]

Ο πίνακας LED matrix είναι ένα πλέγμα 8 x 8. Κάθε LED στο πλέγμα μπορεί να ρυθμιστεί σε διαφορετικό χρώμα. Εδώ είναι μια λίστα μεταβλητών για 24 διαφορετικά χρώματα. Κάθε χρώμα έχει μια τιμή για το κόκκινο, το πράσινο και το μπλε:

[[[ambient-colours]]]

### Επίλεξε μια εικόνα

--- task ---

**Επίλεξε:** Από τις παρακάτω επιλογές διάλεξε μια εικόνα για να την εμφανίσεις. Η Python αποθηκεύει τις πληροφορίες για μια εικόνα σε μια λίστα. Ο κώδικας για κάθε εικόνα περιλαμβάνει τις μεταβλητές για τα χρώματα που χρησιμοποιούνται και τη λίστα.

Θα χρειαστεί να **αντιγράψεις** όλο τον κώδικα για την εικόνα που επέλεξες και στη συνέχεια να τον **επικολλήσεις** στο έργο σου κάτω από τη γραμμή που λέει `# Προσθήκη μεταβλητών χρώματος και εικόνας`.

--- collapse ---

---
title: Κοτόπουλο
---

![Ένα πλέγμα με τετράγωνα 8 x 8 που δείχνει ένα κοτόπουλο σε ένα αυγό.](images/chick.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Άσπρο
c = (0, 0, 0) # Μαύρο
e = (0, 0, 205) # Μεσαίο Μπλε
q = (255, 255, 0) # Κίτρινο
t = (255, 140, 0) # Σκούρο Πορτοκαλί
w = (255, 192, 203) # Ροζ

image = [
  c, c, c, q, q, q, c, c,
  c, c, t, q, e, q, c, c,
  c, c, c, q, q, q, c, c,
  c, w, w, w, w, w, w, c,
  c, w, a, a, a, a, w, c,
  c, w, a, a, a, a, w, c,
  c, c, w, a, a, w, c, c,
  c, c, c, w, w, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Λουλούδι
---

![Ένα πλέγμα με 8 x 8 τετράγωνα που δείχνει ένα ροζ λουλούδι σε ένα πράσινο μίσχο.](images/flower.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
c = (0, 0, 0) # Μαύρο
m = (34, 139, 34) # Πράσινο του Δάσους
q = (255, 255, 0) # Κίτρινο
t = (255, 140, 0) # Σκούρο Πορτοκαλί
y = (255, 20, 147) # Σκούρο Ροζ

image = [
  c, c, y, y, y, y, c, c,
  c, y, y, t, t, y, y, c,
  y, y, t, q, q, t, y, y,
  c, y, y, t, t, y, y, c,
  c, c, y, y, y, y, c, c,
  m, c, c, m, m, c, c, m,
  c, m, m, m, m, m, m, c,
  c, c, c, m, m, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Κάβουρας
---

![Ένα πλέγμα με 8 x 8 τετράγωνα που δείχνουν έναν κάβουρα.](images/crab.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Άσπρο
c = (0, 0, 0) # Μαύρο
v = (255, 0, 0) # Κόκκινο

image = [
  c, a, a, c, a, a, c, c,
  c, a, c, c, a, c, c, c,
  c, v, c, c, v, c, c, c,
  c, v, c, c, v, c, c, c,
  v, v, v, v, v, c, v, v,
  v, v, c, c, v, v, v, c,
  v, v, v, v, v, c, v, v,
  v, c, v, c, v, c, c, c]

--- /code ---

--- /collapse ---


--- collapse ---
---
title: Κροκόδειλος
---

![Ένα πλέγμα με τετράγωνα 8 x 8 που δείχνει ένα κεφάλι κροκόδειλου.](images/croc.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
a = (255, 255, 255) # Άσπρο
c = (0, 0, 0) # Μαύρο
f = (25, 25, 112) # Μπλε του Μεσονυκτίου
m = (34, 139, 34) # Πράσινο του Δάσους

image = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

--- /code ---


--- /collapse ---

--- collapse ---
---
title: Φίδι
---

![Ένα πλέγμα με τετράγωνα 8 x 8 που δείχνει ένα φίδι.](images/snake.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
 c = (0, 0, 0) # Μαύρο
 m = (34, 139, 34) # Πράσινο του Δάσους
 q = (255, 255, 0) # Κίτρινο
 v = (255, 0, 0) # Κόκκινο

image = [
  c, c, c, c, c, c, c, m,
  c, m, m, m, m, m, m, m,
  c, m, c, c, c, c, c, c,
  c, m, m, m, m, m, c, c,
  c, c, c, c, c, m, c, c,
  q, m, q, m, m, m, c, c,
  m, m, m, c, c, c, c, c,
  v, c, c, c, c, c, c, c]

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Βάτραχος
---

![Ένα πλέγμα με τετράγωνα 8 x 8 που δείχνει έναν βάτραχο.](images/frog.png)

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
c = (0, 0, 0) # Μαύρο
m = (34, 139, 34) # Πράσινο του Δάσους
q = (255, 255, 0) # Κίτρινο
v = (255, 0, 0) # Κόκκινο

image = [
  c, m, m, m, c, m, m, m,
  c, m, q, m, c, m, q, m,
  m, m, m, m, m, m, m, m,
  m, v, v, v, v, v, v, v,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, m, m, m, c, m]

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Βρες:**τη γραμμή που λέει `# Εμφάνιση εικόνας` και πρόσθεσε μια γραμμή κώδικα για να εμφανίσει την εικόνα σου στην οθόνη LED:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 12
---
image = [
  c, c, c, q, q, q, c, c,
  c, c, t, q, e, q, c, c,
  c, c, c, q, q, q, c, c,
  c, w, w, w, w, w, w, c,
  c, w, a, a, a, a, w, c,
  c, w, a, a, a, a, w, c,
  c, c, w, a, a, w, c, c,
  c, c, c, w, w, c, c, c]

# Display the image 
sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

Πάτα **Run (Εκτέλεση)** στο κάτω μέρος του προγράμματος επεξεργασίας επεξεργαστή, για να δεις την εικόνα σου να εμφανίζεται στην οθόνη LED.

--- /task ---

--- task ---

**Εντοπισμός σφαλμάτων**

Ο κώδικάς μου έχει ένα συντακτικό σφάλμα:

- Έλεγξε ότι ο κώδικάς σου ταιριάζει με τον κώδικα στα παραπάνω παραδείγματα
- Έλεγξε ότι έχεις βάλει εσοχές στον κώδικα στη λίστα σου
- Έλεγξε ότι η λίστα σου περιβάλλεται από `[` και `]`
- Έλεγξε ότι κάθε μεταβλητή για τα χρώματα στη λίστα διαχωρίζεται με κόμμα

Η εικόνα μου δεν εμφανίζεται:

- Έλεγξε μήπως το `sense.set_pixels(image)` δεν είναι σε εσοχή

--- /task ---



