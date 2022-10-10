from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255)
b = (0, 0, 0)
g = (50,50,50)
s = (180,180,180)
red = (255,0,0)

obrazek = [
    g, b, b, b, b, b, b, g,
    b, g, g, g, g, g, g, b,
    b, g, b, b, g, w, g, s,
    b, g, b, b, g, g, g, s,
    b, g, g, g, s, s, g, s,
    b, g, r, g, g, g, g, s,
    b, g, g, g, g, g, g, b,
    g, b, b, b, b, b, b, g
    ]
    
sense.set_pixels(obrazek)
