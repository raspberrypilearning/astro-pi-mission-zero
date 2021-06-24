## Measure the Lighting conditions

The light/colour sensor in the Astro Pi can measure the lighting conditions around it, a useful feature to help you gather data about the conditions in space.

![Message about the humidity](images/degrees-message.gif)

 As well as measuring the overall brightness, the Astro Pi can also work out the contributions form red, blue and green light as described in the SenseHAT library documentation. 

The Columbus module where the Astro Pis are normally kept is used for a variety of different tasks and the internal lighting may be adjusted to match whatever is happening. In order to make sure that the Mission Zero experiments don't disturb the conditions by being too bright, you can measure how bright it is using the light sensor and adjust the intensity of the LEDs accordingly. 


--- task ---

Add this code to take a light reading:

```python
sh.color.gain = 4
lux = sh.color.clear_raw
```

The first line sets the sensitivity of the light sensor using the gain parameter to a value useful for indoor conditions. The second line will actually measure the current brightness, and store the measured value in the variable `lux`.

--- /task ---

--- task ---

To display the brightness as a scrolling message on the display, add this line of code:

```python
sense.show_message(str(lux))
```

The `str()` part converts the brightness value from a number into text so that the Astro Pi can display it.

--- /task ---

--- task ---

You can also display the brightness as part of another message by joining the parts of your message together with a `+`.

```python
sense.show_message( "It is " + str(lux) + " %" )
```

--- /task ---

The real Astro Pi will measure the brightness around it, but you can move the brightness slider on the Sense HAT emulator to simulate lighting changes and test your code.

![Humidity slider](images/humidity-slider.png)

