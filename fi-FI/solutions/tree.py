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
