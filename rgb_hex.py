def rgb(r, g, b):
    rgb = [r, g, b]
    for n, x in enumerate(rgb):
        x = max(min(255, x), 0)
        x = hex(x)[2:4].rjust(2,'0').upper()
        rgb[n] = x
    rgb = ''.join(rgb)
    return rgb

print(rgb())
