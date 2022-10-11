from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255) # alb
x = (0, 0, 0) # negru
g = (0, 255, 0) # verde
s = (180, 180, 180) # argintiu
r = (255, 0, 0) # rosu
c = (66, 220, 240) # albastru deschis
o = (180, 100, 0) # portocaliu
b = (0, 0, 255) # albastru
print('bob')
imagine = [
    c, c, g, g, g, g, c, c,
    c, g, g, g, g, g, g, c,
    c, g, g, g, g, g, g, c,
    c, c, g, g, g, g, c, c,
    c, c, c, g, g, c, c, c,
    c, c, c, o, o, c, c, c,
    c, c, c, o, o, c, c, c,
    g, g, g, g, g, g, g, g
    ]
    
sense.set_pixels(imagine)
