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
b = (0,00,255) # blauw

afbeelding = [
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, b, c,
    w, w, w, c, r, r, r, r,
    r, r, r, r, r, r, s, s,
    r, r, r, r, r, r, r, o,
    r, x, r, r, r, r, x, r,
    g, g, g, g, g, g, g, g
    ]
    
sense.set_pixels(afbeelding)

