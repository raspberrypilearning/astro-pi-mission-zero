from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255) # biały
x = (0, 0, 0) # czarny
g = (0,255,0) # zielony
s = (180,180,180) # srebny
r = (255,0,0) # czerwony
c = (66, 220, 240) # cyjan
o = (180,100,0) # pomarańczowy
b = (0, 0,255) # niebieski

obrazek = [
    c, c, c, c, c, c, c, c,
    c, c, b, b, b, c, c, c,
    c, b, b, x, b, b, c, c,
    c, b, b, b, b, o, o, c,
    c, b, b, b, b, b, c, c,
    b, b, b, b, b, c, c, c,
    b, b, b, b, b, c, c, c,
    b, b, b, b, b, c, c, c
    ]
    
sense.set_pixels(obrazek)
