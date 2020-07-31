## Μέτρηση της θερμοκρασίας

Ο αισθητήρας θερμοκρασίας στο Astro Pi μπορεί να μετρήσει τη θερμοκρασία του αέρα που τον περιβάλλει, μια χρήσιμη δυνατότητα που σας βοηθά να συλλέξετε δεδομένα για τις διαστημικές συνθήκες.

![Μήνυμα για τη θερμοκρασία](images/degrees-message.gif)

The Astro Pi measures the humidity in the ISS in percentage water concentration in the air.

Part of your mission is to contribute to the daily lives of the crew aboard the ISS, so letting them know that the humidity aboard the space station is within a normal range will reassure them.

[[[generic-theory-what-is-humidity]]]

\--- task \---

Add this code to take a humidity reading:

```python
temp = sense.temperature
```

\--- /collapse \---

\--- /task \---

\--- task \---

The humidity is recorded very precisely, i.e. the stored value will have a large number of decimal places. You can round the value to any number of decimal places. In the example we have rounded to one decimal place, but for a different level of precision, change the number `1` to the number of decimal places you would like to see.

```python
temp = round( sense.temperature, 1 )
```

\--- /task \---

\--- task --

To display the current humidity as a scrolling message on the display, add this line of code:

```python
sense.show_message( str(temp) )
```

The `str()` part converts the humidity from a number into text so that the Astro Pi can display it.

\--- /task \---

\--- task \---

Το τμήμα `str()` μετατρέπει τη θερμοκρασία σπό αριθμό σε κείμενο, ώστε να μπορέσει να προβληθεί από το Astro Pi.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

The real Astro Pi will measure the humidity around it, but you can move the humidity slider on the Sense HAT emulator to simulate humidity changes and test your code.

![Humidity slider](images/humidity-slider.png)

**Note:** You might be wondering why the humidity slider displays the humidity as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the humidity measurement you see may be very slightly larger or smaller than the value you've set with the slider.