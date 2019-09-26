#Filename: lab16_img_manip.py

from PIL import Image # thought I was using pillow???

img = Image.open('snek.jpg')

width, height = img.size # width and height set

pixels = img.load() # img as array of pixels??

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

r = int(0.299*r)
g = int(0.587*g)
b = int(0.114*b)


pixels[i, j] = (r, g, b)

print(r,g,b)

img.show()