import colorsys
from PIL import Image

img = Image.open("Lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r = int(r*115)
        g = int(g*300)
        b = int(b*115)
        pixels[i, j] = (r, g, b)

img.show()
