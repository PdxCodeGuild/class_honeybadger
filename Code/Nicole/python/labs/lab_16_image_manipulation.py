# lab_16_image_manipulation.py

# Use the formula for converting to greyscale and the code below. Remember that Pillow uses ints for RGB values, in the range of 0-255, whereas your math will often use floats. 'Y' is used to represent the brightness. The following formula get the brightness of an RGB triplet. To convert to greyscale, set R, G, and B to Y.

from PIL import Image

img = Image.open("ashlyn.jpg")
width, height = img.size
pixels = img.load()


for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        
        y = int(0.299*r + 0.587*g + 0.114*b)
        # y = int(0.453*r + 0.123*g + 0.987*b)
        
        pixels[i, j] = (y, y, y)

img.show()