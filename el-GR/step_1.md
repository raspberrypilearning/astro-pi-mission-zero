## Εισαγωγή

Προσφέρετε μια ευχάριστη νότα στην καθημερινή ρουτίνα των αστροναυτών στον Διεθνή Διαστημικό Σταθμό, δείχνοντάς τους ένα μήνυμα και τη θερμοκρασία περιβάλλοντος μέσα στον σταθμό, χρησιμοποιώντας τον υπολογιστή Sense ΗΑΤ του Astro Pi.

Θα χρησιμοποιήσετε τον διαδικτυακό εξομοιωτή Sense HAT για να δημιουργήσετε το πρόγραμμά σας, οπότε δεν θα χρειαστείτε επιπλέον εξοπλισμό — όλα γίνονται σε ένα πρόγραμμα περιήγησης Ιστού (φυλλομετρητή).

Το ολοκληρωμένο πρόγραμμά σας θα εκτελεστεί στο διάστημα στον Διεθνή Διαστημικό Σταθμό (ΔΔΣ)! Θα λάβετε επίσης ένα ειδικό πιστοποιητικό που θα δείχνει πού ακριβώς βρισκόταν ο Διεθνής Διαστημικός Σταθμός κατά την εκτέλεση του προγράμματός σας!

### Τι θα φτιάξεις

Παρακάτω είναι ένα παράδειγμα του προγράμματος που θα μπορούσατε να φτιάξετε. Κάντε κλικ στο «**Run**» (Εκτέλεση) για να δείτε το πρόγραμμα σε δράση. <iframe src="https://trinket.io/embed/python/b92d76c0f3?outputOnly=true&runOption=run&start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- collapse \---

* * *

## title: Τι θα μάθεις

Αυτό το έργο καλύπτει στοιχεία από τις ακόλουθες πτυχές του [Raspberry Pi Digital Curriculum Making](http://rpf.io/curriculum){:target="_blank"}:

+ πώς να εμφανίζετε μηνύματα και χρώματα
+ πώς να δημιουργείτε εικόνες
+ μέτρηση της θερμοκρασίας

Αυτό το έργο καλύπτει στοιχεία από τις ακόλουθες πτυχές του [Raspberry Pi Digital Curriculum Making](http://rpf.io/curriculum){:target="_blank"}:

+ [Χρησιμοποίησε βασικές δομές προγραμματισμού για να δημιουργήσεις απλά προγράμματα](https://curriculum.raspberrypi.org/programming/creator/){:target="_blank"}

\--- /collapse \---

\--- collapse \---

* * *

## title: Τι θα χρειαστείς

### Υλικό (Hardware)

+ Οποιοσδήποτε υπολογιστής με σύνδεση στο Διαδίκτυο

### Λογισμικό

+ Ένα πρόγραμμα περιήγησης Ιστού (π.χ. Google Chrome) για να ανοίξετε το <https://trinket.io/mission-zero>{:target="_blank"}

\--- /collapse \---

## \--- collapse \---

## title: Σημειώσεις για εκπαιδευτικούς και συμβούλους (μέντορες)

Αυτή η δραστηριότητα μπορεί να ολοκληρωθεί μέσα σε ένα απόγευμα. Organise your students into teams of two to four, and let us guide them through writing a short Python program to show a personal message and the relative humidity on the Astro Pi.

Διαβάστε το [επίσημο έγγραφο οδηγιών](https://astro-pi.org/wp-content/uploads/2018/09/Astro_Pi_Mission_Zero_Guidelines_2018_19_V12_pages.pdf){:target="_blank"} για το Mission Zero.

You will need to register for the Mission Zero challenge to allow your team(s) to participate.

+ Μεταβείτε στη [σελίδα Mission Zero του εξομοιωτή Trinket](https://trinket.io/mission-zero/register){:target="_blank"}.

+ Συμπληρώστε τη φόρμα και κάντε κλικ στο «**Submit**»\*.

\* Παρακαλώ, προσέξτε ότι αυτή η φόρμα εγγραφής είναι διαθέσιμη μόνο στα Αγγλικά.

The fields on the form include:  
Teacher/mentor name  
Team name  
Number of team members  
Names and ages of team members  
In which language did you access the Mission Zero guidelines?

+ A Trinket account will be created for you (if you don't already have one, or you're not logged in). You can create one account per email address. Each account has its own **classroom code**, and you will need to tell your team(s) what yours is when they are ready to submit their programs.

+ Προβάλλετε σε κάποιο εμφανές σημείο τον κωδικό τάξης σας, για παράδειγμα σε έναν πίνακα ή χρησιμοποιώντας μια συσκευή προβολής και ξεκινήστε τη δραστηριότητα.
    
    Δημιουργήσαμε [ένα εκτυπώσιμο φυλλάδιο δύο σελίδων](https://astro-pi.org/astro_pi_mission_zero_project_print_out_v10_print/){:target="_blank"} που καλύπτει τα βασικά σημεία του Mission Zero και το οποίο οι μαθητές και οι νέοι μπορούν να χρησιμοποιήσουν μαζί με αυτό το online έργο.

\--- /collapse \---

![Εντοπίζοντας pixel](https://code.org/api/hour/begin_raspberrypi_astropi.png)