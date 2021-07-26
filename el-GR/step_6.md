## Μέτρηση της υγρασίας

Ο αισθητήρας υγρασίας στο Astro Pi μπορεί να μετρήσει την υγρασία του αέρα που τον περιβάλλει, μια χρήσιμη δυνατότητα που σας βοηθά να συλλέξετε δεδομένα για τις συνθήκες στο διάστημα.

![Μήνυμα για τη υγρασία](images/degrees-message.gif)

Το Astro Pi μετράει την υγρασία στον ISS σαν ποσοστό συγκέντρωσης νερού στον αέρα.

Μέρος της αποστολής σας είναι να συνεισφέρετε στην καθημερινότητα του πληρώματος του ISS, ώστε να γνωρίζει ότι η υγρασία μέσα στον διαστημικό σταθμό είναι σε ένα κανονικό εύρος που θα τους καθησυχάζει.

[[[generic-theory-what-is-humidity]]]

--- task ---

Προσθέστε αυτόν τον κώδικα για να πάρετε μια μέτρηση υγρασίας:

```python
humid = sense.get_humidity
```

Αυτή η γραμμή θα μετρήσει την τρέχουσα υγρασία, και θα την αποθηκεύσει στην μεταβλητή `humid`.

--- /task ---

--- task ---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. You can round the value to any number of decimal places. In the example we have rounded to one decimal place, but for a different level of precision, change the number `1` to the number of decimal places you would like to see.

```python
humid = round( sense.get_humidity(), 1 )
```

--- /task ---

--- task ---

Για να εμφανίσετε την τρέχουσα υγρασία σαν κυλιόμενο μήνυμα στην οθόνη, προσθέστε την παρακάτω γραμμή κώδικα:

```python
sense.show_message( str(humid) )
```

Το τμήμα `str()` μετατρέπει την υγρασία απο αριθμό σε κείμενο ωστε το Astro Pi να μπορεί να το εμφανίσει.

--- /task ---

--- task ---

Μπορείτε επίσης να εμφανίσετε την υγρασία σαν τμήμα άλλου μηνύματος ενώνοντας τα δύο τμήματα μαζί με το `+`.

```python
sense.show_message( "It is " + str(humid) + " %" )
```

--- /task ---

Το αληθινό Astro Pi θα μετρήσει την υγρασία στο χώρο που βρίσκεται, αλλά μπορείτε να μετακινήσετε τον ρυθμιστή υγρασίας στον εξομοιωτή Sense Hat για να εξομοιώσετε αλλαγές υγρασίας και να ελέγξετε τον κώδικά σας.

![Ρυθμιστής υγρασίας](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.
