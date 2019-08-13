## Measure the temperature

The temperature sensor in the Astro Pi can measure the temperature of the air around it, a useful feature to help you gather data about the conditions in space.

![Message about the temperature](images/degrees-message.gif)

The Astro Pi measures the temperature in the ISS in degrees Celsius (&deg;C). Because temperatures in space vary much more than those on Earth, the Astro Pi can measure temperatures from as low as -40 degrees Celsius up to +120 degrees Celsius.

Part of your mission is to contribute to the daily lives of the crew aboard the ISS, so letting them know that the temperature aboard the space station is within a normal range will reassure them.

## - - 自動隱藏選單 - -

## title: What is temperature?

Temperature is the measure of how hot something is. You may well have had your temperature taken with a thermometer on a visit to the doctor.

![Thermometer](images/thermometer.JPG) *By Menchi [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/){:target="_blank"} via Wikimedia Commons*

To be more precise, temperature is a measure of the amount of heat energy of a substance. You know that an ice cube is solid, but as it warms up, i.e. as it absorbs heat energy from its environment, it melts and becomes liquid. This is because, when a substance absorbs or loses enough heat energy, the substance will change state, e.g. it will go from being a solid to being a liquid.

- - 自動隱藏選單 - -

\--- task \---

Add this code to take a temperature reading:

```python
temp = sense.temperature
```

This line will measure the current temperature, and store the measured value in the variable `temp`.

\--- /task \---

\--- task \---

The temperature is recorded very precisely, i.e. the stored value will have a large number of decimal places. You can round the value to any number of decimal places. In the example we have rounded to one decimal place, but for a different level of precision, change the number `1` to the number of decimal places you would like to see.

```python
temp = round( sense.temperature, 1 )
```

\--- /task \---

\--- task \---

To display the current temperature as a scrolling message on the display, add this line of code:

```python
sense.show_message( str(temp) )
```

The `str()` part converts the temperature from a number into text so that the Astro Pi can display it.

\--- /task \---

\--- task \---

You can also display the temperature as part of another message by joining the parts of your message together with a `+`.

```python
sense.show_message( "It is " + str(temp) + " degrees" )
```

\--- /task \---

The real Astro Pi will measure the temperature around it, but you can move the temperature slider on the Sense HAT emulator to simulate temperature changes and test your code.

![Temperature slider](images/temperature-slider.png)

**Note:** You might be wondering why the temperature slider displays the temperature as a whole number, but the reading you get is a decimal. The emulator simulates the slight inaccuracy of the real sensor, so the temperature measurement you see may be very slightly larger or smaller than the value you've set with the slider.