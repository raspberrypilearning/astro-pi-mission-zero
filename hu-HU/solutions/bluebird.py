from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255) # fehér
x = (0, 0, 0) # fekete
g = (0,255,0) # zöld
s = (180,180,180) # szürke
r = (255,0,0) # piros
c = (66, 220, 240) # cián
o = (180,100,0) # narancssárga
b = (0, 0,255) # kék

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
