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
print('bob')
picture = [
    c, c, g, g, g, g, c, c,
    c, g, g, g, g, g, g, c,
    c, g, g, g, g, g, g, c,
    c, c, g, g, g, g, c, c,
    c, c, c, g, g, c, c, c,
    c, c, c, o, o, c, c, c,
    c, c, c, o, o, c, c, c,
    g, g, g, g, g, g, g, g
    ]
    
sense.set_pixels(picture)
