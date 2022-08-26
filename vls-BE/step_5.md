## Laat een beeld zien

In this step, you will set up the colour sensor and use it to sense the colour in the environment. This colour will then be used to colour in your chosen image.

<mark>add an image with a different background colour not black</mark>

--- task ---

Find the `# Setup the colour sensor` comment.

Onderaan je programma kun je wat kleurvariabelen maken om de kleuren waarmee je je tekening wil maken te definiëren. Je kan zoveel kleuren gebruiken als je wil, maar in dit voorbeeld zullen we maar een paar kleuren gebruiken - rood (`r`), wit (`w`), zwart (`b`), en twee tinten grijs (`g` en `s`). Merk op dat de tinten gemaakt worden door de hoeveelheid licht in alle drie de kanalen te verminderen terwijl de verhoudingen gelijk blijven.

**Opmerking:** Deze keer is het een goed idee om de kleurvariabelen namen met één letter te geven, omdat dit tijd zal besparen in de volgende stap, waar je ze vaak zal moeten typen. Bovendien maakt het gebruik van aparte letters het eenvoudiger om de tekening die je maakt te zien.
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 2,3
---
# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor sense.color.integration_cycles = 64 # The interval at which the reading will be taken --- /code ---

--- /task ---

--- task ---

Use the colour sensor to colour your background.

**Find and update** your existing `c = (0, 0, 0) # Black` colour variable to use the colour sensed by the Sense HAT colour sensor instead of black.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 1
---
Druk op **Run** om je tekening te zien verschijnen.

--- /task ---

--- task ---

**Test:** Move the colour slider to a colour of your choice and run your code. Your background colour will change.

Move the colour slider again to a new colour and run your code again. Your background colour will change to the new colour.

--- /task ---

## Loop your program

The Asto Pi Mission Zero program needs to run for less than 30 seconds. Your image can be run repeatedly and sense the latest colour each time.

--- task ---

**Find** your `sense.set_pixels(image)` line of code.

**Add** code above it to set up your `for` loop for `28` repetitions.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 6
---
# Set LED colours
sense.clear(v) sleep(1) sense.clear(m) sleep(1) for i in range(28): sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

You now need to indent your function call so that it sits **inside** the `for` loop.

To do this, use the **Tab** key on your keyboard at the start of the `sense.set_pixels()` line.

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 7
---
# Set LED colours
sense.clear(v) sleep(1) sense.clear(m) sleep(1) for i in range(28): sense.set_pixels(image)

--- /code ---

--- /task ---

--- task ---

At the bottom of your code, add the following two lines to sense the colour and create a `sleep` of one second inside your loop:

--- code ---
---
language: python filename: main.py line_numbers: false line_number_start: 1
line_highlights: 8,9
---
# Set LED colours
sense.clear(v) sleep(1) sense.clear(m) sleep(1) for i in range(28): sense.set_pixels(image) c = sense.colour.colour[0:3] sleep(1)

--- /code ---

**Tip:** Make sure your last two lines of code are indented within your `for` loop.

--- /task ---

--- task ---

**Test:** Run your code and change the colour picker several times as your project is running. Check that your image updates to use the sensed colour on its next run of the animation.

--- /task ---

--- task ---

**Debug:** My code has a syntax error or doesn't run as expected!

- Check that your code matches the code in the examples above
- Check that you have indented the code in your for loop
- Check that your list is surrounded by `[` and `]`
- Check that each colour variable in the list is separated by a comma

--- /task ---
