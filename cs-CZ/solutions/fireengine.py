from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255) # bílá
x = (0, 0, 0) # černá
g = (0,255,0) # zelená
s = (180,180,180) # stříbrná
r = (255,0,0) # červená
c = (66, 220, 240) # modrozelená
o = (180,100,0) # oranžová
b = (0, 0,255) # modrá

obrazek = [
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, b, c,
    w, w, w, c, r, r, r, r,
    r, r, r, r, r, r, s, s,
    r, r, r, r, r, r, r, o,
    r, x, r, r, r, r, x, r,
    g, g, g, g, g, g, g, g
    ]
    
sense.set_pixels(obrazek)

