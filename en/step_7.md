## Adjust LED brightness for the lighting conditions

The Columbus module where the Astro Pis normally live is used for a variety of different tasks and the internal lighting may be adjusted to match whatever is happening. In order to make sure that your Mission Zero experiments doesn't disturb the conditions by being too bright, you can measure how bright it is using the light sensor and adjust the intensity of the LEDs accordingly.

--- task ---

Calculate a scaling factor to work out how much the brightness of the LEDs should be reduced. To do this, you need to know the maximum possible brightness value that will be recorded by the light sensor which can be retrieved using `sh.color.max_raw`.

Then divide the measured value by that maximum. 

```python
scaling_factor = lux/sh.color.max_raw
```

--- /task ---

--- task ---

Now you can use this scaling factor to adjust the RGB values for the colours that you have defined. This can be achieved cleanly and simply using a list comprehension.

[[[generic-python-simple-list-comprehensions]]]

So to scale all the white values:

```python
 w = [ int(value * scaling_factor) for value in w ]
```
Note that because RGB values need to be integers (whole numbers) we need to convert out scaled value using the `int()` function. 

--- /task ---

--- task ---
Add list comprehensions for every colour definition you have used. Re-arrange your program so that you measure the light levels and adjust your colour definitions before you display any messages or images.

--- /task ---