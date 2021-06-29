## Measure the lighting conditions

The light/colour sensor in the Astro Pi can measure the lighting conditions around it, a useful feature to help you gather data about the conditions in space.

![Message about the brightness](images/degrees-message.gif)

As well as measuring the overall brightness, the Astro Pi can also work out the contributions form red, blue and green light as described in the SenseHAT library documentation. 



--- task ---

Add this code to take a light reading:

```python
sense.color.gain = 4
brightness = sense.color.clear
sense.show_message(str(brightness))
```
The first line sets the sensitivity of the light sensor using the gain parameter to a value useful for indoor conditions. The second line will measure the current brightness, and store the measured value in the variable `brightness`. 

What does the number you obtain actually mean? 

The maximum possible value is 256 with the sensor's current settings. So if your measurement was a value of 100, that would represent 100/256 of the maximum amount of light that could be detected by the sensor. 

Finally, the `str()` part converts the brightness value from a number into text so that the Astro Pi can display it with `show_message()`.

--- /task ---

--- task ---

Previously you were mixing red, green and blue to make different colours for the LEDs. You can now do the reverse and use the sensor to measure the red, green and blue components of the light that it can detect. For the red component:

```python

red_light = sense.color.red
sense.show_message(str(red_light))
```

--- /task ---

--- task ---
You go do the same thing for the green and blue components individually. Or use a single line to retrieve all the values and store them in appropriately named variables:

```python

red_light, green_light, blue_light, brightness = sense.color.color
```

--- /task ---


--- task ---

You can also display the values as part of another message by joining the parts of your message together with a `+`.

```python
sense.show_message( "Red: " + str(red_light), ", Green: " + str(green_light), ", Blue: " + str(blue_light) )
```

--- /task ---

The real Astro Pi will measure the brightness around it, but you can move the brightness slider on the Sense HAT emulator to simulate lighting changes and test your code. Experiment with different values for each of the 3 colours. 

![Humidity slider](images/humidity-slider.png)

