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

pilt = [
    c, c, c, c, c, c, c, c,
    c, c, b, b, b, c, c, c,
    c, b, b, x, b, b, c, c,
    c, b, b, b, b, o, o, c,
    c, b, b, b, b, b, c, c,
    b, b, b, b, b, c, c, c,
    b, b, b, b, b, c, c, c,
    b, b, b, b, b, c, c, c
    ]
    
sense.set_pixels(pilt)
