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
print('bob')
slika = [
    c, c, g, g, g, g, c, c,
    c, g, g, g, g, g, g, c,
    c, g, g, g, g, g, g, c,
    c, c, g, g, g, g, c, c,
    c, c, c, g, g, c, c, c,
    c, c, c, o, o, c, c, c,
    c, c, c, o, o, c, c, c,
    g, g, g, g, g, g, g, g
    ]
    
sense.set_pixels(slika)
