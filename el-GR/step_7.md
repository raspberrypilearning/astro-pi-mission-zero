## Εμφάνιση της υγρασίας

Μπορείτε να συνδυάσετε τη μέτρηση υγρασίας με μια εικόνα που επίσης θα δείχνει την υγρασία με ένα γραφικό τρόπο. Για παράδειγμα μπορείτε να εμφανίσετε ένα ωκεανό για την υψηλή υγρασία και μια έρημο για τη χαμηλή:

![Ζεστό και κρύο](images/wet-dry.png)

--- task ---

Στο κάτω μέρος του προγράμματός σας, δημιουργήστε μερικές μεταβλητές χρώματος για τα χρώματα που θέλετε να χρησιμοποιήσετε στις εικόνες σας. Ίσως να έχετε ήδη ορίσει κάποιες από αυτές τις μεταβλητές σε προηγούμενο βήμα.

```python
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)
```

--- /task ---

--- task ---

Όπως και προηγουμένως, σχεδιάστε τις εικόνες σας δημιουργώντας πρώτα μια λίστα για κάθε μία, και έπειτα καθορίστε/αντιστοιχίστε τα στοιχεία της λίστας με τα χρώματα που θέλετε να είναι τα pixels σας .

```python
wet = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


dry = [
  c, c, g, g, c, c, c, c,
  c, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, g, g, g, g, g, c, c,
  c, c, g, g, c, c, c, c,
  y, y, y, y, y, y, y, y,
  y, y, y, y, y, y, y, y
]
```

--- /task ---

--- task ---

Προσθέστε τον κώδικα για τη λήψη της υγρασίας:

```python
humid = sense.get_humidity
```

--- /task ---

--- task ---

Τώρα αποφασίστε ποια εικόνα θέλετε να εμφανιστεί. Σε αυτό το παράδειγμα, θα εμφανίσουμε την εικόνα `wet (υγρό)` αν η τιμή της υγρασίας είναι πάνω από 40% και την εικόνα `dry (ξηρό)` αν η τιμή είναι κάτω από 40%.

```python
humid = sense.get_humidity
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

Χρησιμοποποιήστε το ρυθμιστή υγρασίας για να ορίσετε μια υγρασία στον εξομοιωτή. Εκτελέστε το πρόγραμμά σας και ελέγξτε την εικόνα που επιλέξατε ώστε η υγρασία να εμφανίζεται σωστά.

--- /task ---

--- task ---

Αλλάξτε τον κώδικά σας έτσι ώστε το πρόγραμμά σας να εμφανίζει την υγρασία στους αστροναύτες με τον δικό σας τρόπο.

--- /task ---