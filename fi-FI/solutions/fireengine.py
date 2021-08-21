from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255) # valkoinen
x = (0, 0, 0) # musta
g = (0,255,0) # vihreä
s = (180,180,180) # hopea
r = (255,0,0) # punainen
c = (66, 220, 240) # syaani (sinivihreä)
o = (180,100,0) # oranssi
b = (0, 0,255) # sininen

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

