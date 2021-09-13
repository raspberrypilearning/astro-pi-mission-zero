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
print('bob')
immagine = [
    c, c, g, g, g, g, c, c,
    c, g, g, g, g, g, g, c,
    c, g, g, g, g, g, g, c,
    c, c, g, g, g, g, c, c,
    c, c, c, g, g, c, c, c,
    c, c, c, g, g, c, c, c,
    c, c, c, o, o, c, c, c,
    g, g, g, g, g, g, g, g
    ]
    
sense.set_pixels(immagine)
