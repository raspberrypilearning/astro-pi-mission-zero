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
    c, c, b, b, b, c, c, c,
    c, b, b, x, b, b, c, c,
    c, b, b, b, b, o, o, c,
    c, b, b, b, b, b, c, c,
    b, b, b, b, b, c, c, c,
    b, b, b, b, b, c, c, c,
    b, b, b, b, b, c, c, c
    ]
    
sense.set_pixels(obrazek)
