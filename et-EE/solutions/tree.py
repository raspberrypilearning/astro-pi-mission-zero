from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255) # valge
x = (0, 0, 0) # must
g = (0,255,0) # roheline
s = (180,180,180) # hõbedane
r = (255,0,0) # punane
c = (66, 220, 240) # tsüaan
o = (180,100,0) # oranž
b = (0, 0,255) # sinine
print('bob')
pilt = [
    c, c, g, g, g, g, c, c,
    c, g, g, g, g, g, g, c,
    c, g, g, g, g, g, g, c,
    c, c, g, g, g, g, c, c,
    c, c, c, g, g, c, c, c,
    c, c, c, o, o, c, c, c,
    c, c, c, o, o, c, c, c,
    g, g, g, g, g, g, g, g
    ]
    
sense.set_pixels(pilt)
