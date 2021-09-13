from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255) # biały
x = (0, 0, 0) # czarny
g = (0,255,0) # zielony
s = (180,180,180) # srebrny
r = (255,0,0) # czerwony
c = (66, 220, 240) # cyjan
o = (180,100,0) # pomarańczowy
b = (0, 0,255) # niebieski
print('bob')
obrazek = [
    c, c, g, g, g, g, c, c,
    c, g, g, g, g, g, g, c,
    c, g, g, g, g, g, g, c,
    c, c, g, g, g, g, c, c,
    c, c, c, g, g, c, c, c,
    c, c, c, o, o, c, c, c,
    c, c, c, o, o, c, c, c,
    g, g, g, g, g, g, g, g
    ]
    
sense.set_pixels(obrazek)
