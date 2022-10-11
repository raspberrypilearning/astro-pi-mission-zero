from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255) # bela
x = (0, 0, 0) # črna
g = (0,255,0) # zelena
s = (180,180,180) # srebrna
r = (255,0,0) # rdeča
c = (66, 220, 240) # cian
o = (180,100,0) # oranžna
b = (0, 0,255) # morda

slika = [
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, b, c,
    w, w, w, c, r, r, r, r,
    r, r, r, r, r, r, s, s,
    r, r, r, r, r, r, r, o,
    r, x, r, r, r, r, x, r,
    g, g, g, g, g, g, g, g
    ]
    
sense.set_pixels(slika)

