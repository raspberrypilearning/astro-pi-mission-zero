from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255) # bianco
x = (0, 0, 0) # nero
g = (0,255,0) # verde
s = (180,180,180) # argento
r = (255,0,0) # rosso
c = (66, 220, 240) # ciano
o = (180,100,0) # arancione
b = (0, 0,255) # blu

immagine = [
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, b, c,
    w, w, w, c, r, r, r, r,
    r, r, r, r, r, r, s, s,
    r, r, r, r, r, r, r, o,
    r, x, r, r, r, r, x, r,
    g, g, g, g, g, g, g, g
    ]
    
sense.set_pixels(immagine)

