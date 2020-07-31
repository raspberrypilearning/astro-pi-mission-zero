## Εμφάνιση της θερμοκρασίας

You could combine your humidity reading with a picture to also indicate the humidity in a graphical way. For example, you might display an ocean for high humidity, and a desert for low humidity:

![Ζεστό και κρύο](images/wet-dry.png)

\--- task --

Στο κάτω μέρος του προγράμματός σας, δημιουργήστε μερικές μεταβλητές χρώματος για τα χρώματα που θέλετε να χρησιμοποιήσετε στις εικόνες σας. Ίσως να έχετε ήδη ορίσει κάποιες από αυτές τις μεταβλητές σε προηγούμενο βήμα.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

\--- /task \---

\--- task --

Όπως και προηγουμένως, σχεδιάστε τις εικόνες σας δημιουργώντας πρώτα μια λίστα για κάθε μία, και έπειτα καθορίστε/αντιστοιχίστε τα στοιχεία της λίστας με τα χρώματα που θέλετε να είναι τα pixels σας .

```python
hot = [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g
]


cold = [
  b, b, w, b, b, b, w, b,
  b, b, b, b, b, w, b, b,
  b, w, b, b, b, b, b, w,
  b, b, b, b, w, b, b, b,
  w, b, b, w, b, b, w, b,
  b, b, b, b, b, b, b, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w
]
```

\--- /task \---

\--- task --

Προσθέστε τον κώδικα για τη λήψη της θερμοκρασίας:

```python
temp = sense.temperature
```

\--- /task \---

\--- task --

Τώρα αποφασίστε ποια εικόνα θέλετε να εμφανιστεί. For this example, we will display the `wet` image if the humidity reading is 20% or above, and the `dry` image if the humidity is below 20%.

```python
temp = sense.temperature
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
```

\--- /task \---

\--- task --

Use the humidity slider to set a humidity on the emulator. Run your program and check that the image you've selected for that humidity is correctly displayed.

\--- /task \---

\--- task --

Αλλάξτε τον κώδικά σας έτσι ώστε το πρόγραμμά σας να εμφανίζει τη θερμοκρασία στους αστροναύτες με τον δικό σας τρόπο.

\--- /task \---