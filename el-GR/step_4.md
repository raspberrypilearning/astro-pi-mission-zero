## Προσθήκη χρώματος

Τα LED του Astro Pi μπορούν επίσης να εμφανίζουν χρώματα. Μπορείτε να προσδιορίσετε ένα χρώμα δημιουργώντας μια μεταβλητή στην οποία θα ορίσετε μια τιμή χρώματος RGB.

Μπορείτε να μάθετε πώς να δημιουργείτε όλα τα χρώματα χρησιμοποιώντας διαφορετικές αναλογίες κόκκινου, πράσινου και μπλε εδώ:

[[[generic-theory-colours]]]

--- task ---

Επιλέξτε ένα χρώμα και δείτε την τιμή RGB του χρώματος. Μπορείτε να χρησιμοποιήσετε έναν [επιλογέα χρώματος](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} για να σας βοηθήσει.

--- /task ---

--- task ---

Δημιουργήστε μια μεταβλητή για να αποθηκεύσετε το επιλεγμένο χρώμα σας. Για παράδειγμα, αν επιλέξατε το κόκκινο, θα γράφατε την ακόλουθη γραμμή κώδικα:

```python
red = (255,0,0)
```

--- /task ---

--- task ---

Τώρα μπορείτε να εμφανίσετε το κείμενό σας στο χρώμα της επιλογής σας! Για να δώσετε εντολή στο πρόγραμμα να χρησιμοποιήσει το χρώμα που δημιουργήσατε, προσθέστε την παράμετρο `text_colour` στον κώδικα εμφάνισης του κειμένου σας:

```python
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
```

--- /task ---

![εμφάνιση μηνύματος με χρώμα](images/show-message-color.gif)

--- task ---

Μπορείτε επίσης να αλλάξετε το χρώμα φόντου της οθόνης. Επιλέξτε ένα άλλο χρώμα και δημιουργήστε μια άλλη μεταβλητή για να το αποθηκεύσετε. Για να δώσετε εντολή στο πρόγραμμα να χρησιμοποιήσει το επιλεγμένο σας χρώμα φόντου, προσθέστε την παράμετρο `back_colour` στον κώδικά σας:

```python
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

--- /task ---

--- task ---

Αλλάξτε το κείμενο και το χρώμα του χαιρετισμού — τι μήνυμα θα στείλετε στους αστροναύτες που βρίσκονται στον Διεθνή Διαστημικό Σταθμό;

--- /task ---