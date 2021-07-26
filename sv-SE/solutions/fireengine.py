from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255) # vit
x = (0, 0, 0) # svart
g = (0,255,0) # grön
s = (180,180,180) # silver
r = (255,0,0) # röd
c = (66, 220, 240) # cyan
o = (180,100,0) # orange
b = (0, 0,255) # blå

picture = [
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, b, c,
    w, w, w, c, r, r, r, r,
    r, r, r, r, r, r, s, s,
    r, r, r, r, r, r, r, o,
    r, x, r, r, r, r, x, r,
    g, g, g, g, g, g, g, g
    ]
    
sense.set_pixels(picture)

