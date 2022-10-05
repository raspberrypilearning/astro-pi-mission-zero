from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255) # Weiss
x = (0, 0, 0) # Schwarz
g = (0,255,0) # Grün
s = (180,180,180) # Silber
r = (255,0,0) # Rot
c = (66, 220, 240) # Cyan
o = (180,100,0) # Orange
b = (0, 0,255) # Blau

bild = [
    c, c, c, c, c, c, c, c,
    c, c, b, b, b, c, c, c,
    c, b, b, x, b, b, c, c,
    c, b, b, b, b, o, o, c,
    c, b, b, b, b, b, c, c,
    b, b, b, b, b, c, c, c,
    b, b, b, b, b, c, c, c,
    b, b, b, b, b, c, c, c
    ]
    
sense.set_pixels(bild)
