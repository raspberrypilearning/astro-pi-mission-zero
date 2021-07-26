from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255) # white
x = (0, 0, 0) # black
g = (0,255,0) # green
s = (180,180,180) # silver
r = (255,0,0) # red
c = (66, 220, 240) # cyan
o = (180,100,0) # orange
b = (0, 0,255) # blue

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
    
sense.set_pixels(imagine)

