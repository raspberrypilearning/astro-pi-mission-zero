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
