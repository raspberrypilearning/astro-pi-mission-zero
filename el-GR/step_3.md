## Εμφάνιση εικόνας

Ο πίνακας LED του Astro Pi μπορεί να εμφανίζει χρώματα. Σε αυτό το βήμα, θα εμφανίσεις εικόνες από τη φύση στη οθόνη LED του Astro Pi.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Ένα <span style="color: #0faeb0">**LED matrix**</span> είναι ένα πλέγμα από LED που μπορούν να ελεγχθούν μεμονωμένα ή ως ομάδα για να δημιουργήσουν διαφορετικά εφέ φωτισμού. Ο πίνακας LED matrix στο Sense HAT έχει 64 LED που εμφανίζονται σε ένα πλέγμα 8 x 8. Τα LED μπορούν να προγραμματιστούν ώστε να παράγουν μεγάλη γκάμα χρωμάτων.
</p>

![Ένα στιγμιότυπο οθόνης του παραθύρου προσομοιωτή που δείχνει τη Μονάδα Πτήσης με την οθόνη LED να εμφανίζει μια εικόνα ενός λουλουδιού.](images/fu-pic.png)

--- task ---

Άνοιξε το [αρχικό έργο Mission Zero](https://missions.astro-pi.org/mz/code_submissions/){:target="_blank"}.

Θα δεις ότι μερικές γραμμές κώδικα έχουν ήδη προστεθεί αυτόματα για σένα.

Αυτός ο κώδικας συνδέεται με το Astro Pi, εξασφαλίζει ότι η οθόνη LED του Astro Pi εμφανίζεται με τον σωστό τρόπο και ρυθμίζει τον αισθητήρα χρώματος. Άφησε αυτόν τον κώδικα εκεί, γιατί θα τον χρειαστείς.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights:
---
# Εισαγωγή βιβλιοθηκών
from sense_hat import SenseHat from time import sleep

# Ρύθμιση του Sense HAT
sense = SenseHat() sense.set_rotation(270)

# Ρύθμιση του αισθητήρα χρωμάτων
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken

--- /code ---

![Ένα στιγμιότυπο οθόνης του προσομοιωτή Sense HAT με γραμμές του αρχικού κώδικα να εμφανίζονται στο αριστερό παράθυρο.](images/sense-hat-emulator2.png)

--- /task ---

### Χρώματα RGB

Τα χρώματα μπορούν να δημιουργηθούν χρησιμοποιώντας διαφορετικές αναλογίες κόκκινου, πράσινου και μπλε. Μπορείς να μάθεις για τα χρώματα RGB εδώ:

[[[generic-theory-simple-colours]]]

The LED matrix is an 8 x 8 grid. Κάθε LED στο πλέγμα μπορεί να ρυθμιστεί σε διαφορετικό χρώμα. Εδώ είναι μια λίστα μεταβλητών για 24 διαφορετικά χρώματα. Κάθε χρώμα έχει μια τιμή για το κόκκινο, το πράσινο και το μπλε:

[[[ambient-colours]]]

### Επίλεξε μια εικόνα

--- task ---

**Επίλεξε:** Από τις παρακάτω επιλογές διάλεξε μια εικόνα για να την εμφανίσεις. Η Python αποθηκεύει τις πληροφορίες για μια εικόνα σε μια λίστα. Ο κώδικας για κάθε εικόνα περιλαμβάνει τις μεταβλητές για τα χρώματα που χρησιμοποιούνται και τη λίστα.

Θα χρειαστεί να **αντιγράψεις** όλο τον κώδικα για την εικόνα που επέλεξες και στη συνέχεια να τον **επικολλήσεις** στο έργο σου κάτω από τη γραμμή που λέει `# Προσθήκη μεταβλητών χρώματος και εικόνας`.

--- collapse ---

---
title: Fish
---

![A grid with 8 x 8 squares showing a fish.](images/fish.png)

Created by team chalka, Poland

```python
z = (204, 0, 204) # magenta
q = (255, 255, 0) # yellow
d = (51, 153, 255) # blue
c = (0, 0, 0) # black

image = [
d, d, z, d, d, d, d, d,
d, d, d, z, z, d, d, d,
z, d, q, q, q, q, d, d,
z, z, q, q, q, c, q, d,
z, z, z, q, q, q, q, d,
z, z, q, q, q, q, q, d,
z, d, q, z, z, q, d, d,
d, d, d, z, d, d, d, d]

```

--- /collapse ---


--- collapse ---

---
title: Walrus
---

![A grid with 8 x 8 squares showing a walrus.](images/walrus.png)

Created by team Walrus, Finland

```python
h = (0, 255, 255)
c = (0, 0, 0)
s = (139, 69, 19)
a = (255, 255, 255)
r = (184, 134, 11)   

image = [
h, h, h, h, h, h, h, h,
h, h, s, s, s, h, h, h,
h, s, s, s, s, s, h, h,
h, s, c, s, c, s, s, s,
h, r, r, r, r, r, s, s,
h, h, a, s, a, s, s, s,
h, h, a, s, a, s, s, s,
r, r, s, s, s, s, s, s]

```

--- /collapse ---

--- collapse ---
---
title: Paxi
---

![A grid with 8 x 8 squares showing paxi.](images/paxi.png)

Created by team tony_pi, Italy

```python
v = (255, 0, 0) # Red
j = (34, 139, 34) # ForestGreen
c = (0, 0, 0) # Black 
e = (100, 149, 237) # CornflowerBlue
l = (0, 255, 0) # Green

image = [
    c, v, j, c, c, j, v, c,
    c, c, v, v, v, v, c, c,
    c, v, c, e, l, e, v, c,
    c, v, c, l, l, l, v, c,
    c, v, c, l, c, l, v, c,
    c, c, v, v, v, v, c, c,
    c, c, l, c, c, l, c, c,
    c, j, j, c, c, j, j, c]

```

--- /collapse ---


--- collapse ---
---
title: Dog
---

![A grid with 8 x 8 squares showing a dog head.](images/dog.png)

Created by team ptpr_07, Spain
```python

c = (0, 0, 0) # Black
r = (86, 71, 0) # Light Brown
s = (123, 61, 0) # Orange Brown
y = (155, 0, 134) # Deep Pink

image = [
    c, r, r, c, c, r, r, c,
    c, r, s, s, s, s, r, c,
    c, r, c, s, s, c, r, c,
    c, s, s, s, s, s, s, c,
    c, s, s, s, s, s, s, c,
    c, s, s, c, c, s, s, c,
    c, c, s, y, y, s, c, c,
    c, c, c, y, y, c, c, c]


```

--- /collapse ---

--- collapse ---
---
title: Chameleon
---

![A grid with 8 x 8 squares showing a rainbow coloured chameleon.](images/chameleon.png)

Created by team The_ETs, United Kingdom

```python

c = (0, 0, 0) # Black
s = (95, 65, 0) # Brown
a = (255, 255, 255) # white
v = (255, 0, 0) # Red
t = (255, 153, 28) # Orange
q = (255, 255, 0) # Yellow
m = (0, 255, 0) # Green
h = (0, 255, 255) # Cyan
z = (128, 0, 255) # Purple
y = (191, 0, 255) # Magenta

image = [
    a, a, v, v, t, a, a, a,
    a, v, v, t, t, q, a, a,
    v, c, t, t, q, q, m, a,
    v, t, t, q, q, m, m, h,
    s, s, q, s, s, m, s, h,
    a, a, a, a, a, a, a, z,
    a, a, a, a, y, a, a, z,
    a, a, a, a, a, y, z, a]

```

--- /collapse ---

--- collapse ---
---
title: Δράκος
---

![A grid with 8 x 8 squares showing a kite.](images/kite.png)

Created by team Val, Greece

```python

b = (105, 105, 105) # Αχνό Γκρι
c = (0, 0, 0) # Μαύρο
d = (100, 149, 237) # Μπλε του Άνθους Αραβοσίτου
v = (255, 0, 0) # Κόκκινο
z = (153, 50, 204) # Σκοτεινή Ορχιδέα

image = [
    c, c, v, c, v, c, c, c,
    c, z, z, z, z, v, c, c,
    z, b, z, b, z, c, c, c,
    z, z, z, z, z, v, c, c,
    c, c, d, d, d, c, c, z,
    c, z, d, z, z, z, z, c,
    c, c, d, d, z, c, c, c,
    c, c, z, c, z, c, c, c]

```

--- /collapse ---

--- collapse ---
---
title: Chicken
---

![A grid with 8 x 8 squares showing a Chicken.](images/chicken.png)

Created by team Slepicky, Czech Republic

```python

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

# Εμφάνιση της εικόνας
sense.set_pixels(image)

```

--- /collapse ---

--- /task ---

--- task ---

**Βρες:**τη γραμμή που λέει `# Εμφάνιση εικόνας` και πρόσθεσε μια γραμμή κώδικα για να εμφανίσει την εικόνα σου στην οθόνη LED:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 18, 19
---
Η εικόνα μου δεν εμφανίζεται:

image = [ d, d, z, d, d, d, d, d, d, d, d, z, z, d, d, d, z, d, q, q, q, q, d, d, z, z, q, q, q, c, q, d, z, z, z, q, q, q, q, d, z, z, q, q, q, q, q, d, z, d, q, z, z, q, d, d, d, d, d, z, d, d, d, d]

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


--- task ---

**Αποθήκευσε την πρόοδό σου**

Τώρα που εμφάνισες μια εικόνα, μπορείς να αποθηκεύσεις το πρόγραμμά σου στο έργο Mission Starter εισάγοντας το όνομα της ομάδας σου, τα ονόματα των μελών της ομάδας και τον κωδικό της τάξης που σου έχει δοθεί. Μπορείς να φορτώσεις ξανά το πρόγραμμά σου σε οποιαδήποτε συσκευή με σύνδεση στο Διαδίκτυο εισάγοντας το όνομα της ομάδας και τον κωδικό της τάξης σου.

![Κουμπί Αποθήκευσης Mission Zero](images/mz_savebutton_v2.png)

--- /task --- 
