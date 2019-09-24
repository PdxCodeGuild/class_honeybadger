
from PIL import Image


Y = 0.299*R + 0.587*G + 0.114*B

img = Image.open("Lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        r, g, b = y
        # your code here

        pixels[i, j] = (r, g, b)

img.show()
