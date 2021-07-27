from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255,255,255) # wit
x = (0,0,0) # zwart
g = (0,255,0) # groen
s = (180,180,180) # zilver
r = (255,0,0) # rood
c = (66,220,240) # cyaan
o = (180,100,0) # oranje
b = (0,0,255) # blauw
print('bob')
afbeelding = [
    c, c, g, g, g, g, c, c,
    c, g, g, g, g, g, g, c,
    c, g, g, g, g, g, g, c,
    c, c, g, g, g, g, c, c,
    c, c, c, g, g, c, c, c,
    c, c, c, o, o, c, c, c,
    c, c, c, o, o, c, c, c,
    g, g, g, g, g, g, g, g
    ]
    
sense.set_pixels(afbeelding)
