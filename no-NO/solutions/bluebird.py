from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255) # hvit
x = (0, 0, 0) # svart
g = (0,255,0) # grønn
s = (180 180 180) # sølv
r = (255,0,0) # rød
c = (66, 220, 240) # cyan
o = (180,100,0) # oransje
b = (0, 0,255) # blå

picture = [
    c, c, c, c, c, c, c, c,
    c, c, b, b, b, c, c, c,
    c, b, b, x, b, b, c, c,
    c, b, b, b, b, o, o, c,
    c, b, b, b, b, b, c, c,
    b, b, b, b, b, c, c, c,
    b, b, b, b, b, c, c, c,
    b, b, b, b, b, c, c, c
    ]
    
sense.set_pixels(picture)
