from sense_hat import SenseHat
sensor = SenseHat()
sense.set_rotation (270)
w = (255, 255, 255) # blanco
x = (0, 0, 0) # negro
g = (0,255,0) # verde
s = (180,180,180) # plateado
r = (255,0,0) # rojo
c = (66, 220, 240) # cian
o = (180,100,0) # naranja
b = (0, 0,255) # azul

imagen = [
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, b, c,
    w, w, w, c, r, r, r, r,
    r, r, r, r, r, r, s, s,
    r, r, r, r, r, r, r, o,
    r, x, r, r, r, r, x, r,
    g, g, g, g, g, g, g, g
    ]
    
sense.set_pixels(imagen)

