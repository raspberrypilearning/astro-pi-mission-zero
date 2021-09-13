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
print('bob')
bild = [
    c, c, g, g, g, g, c, c,
    c, g, g, g, g, g, g, c,
    c, g, g, g, g, g, g, c,
    c, c, g, g, g, g, c, c,
    c, c, c, g, g, c, c, c,
    c, c, c, o, o, c, c, c,
    c, c, c, o, o, c, c, c,
    g, g, g, g, g, g, g, g
    ]
    
sense.set_pixels(bild)
