from PIL import Image
import random

im = Image.open(r"C:\Users\YONI\Desktop\me.jpg")
px = im.load()


def disturb(rgbVal):
    newRGBVal = [0,0,0]
    for i, clr in enumerate(rgbVal):
        if clr > 120: newRGBVal[i] = random.randrange(100, 255)
        else: newRGBVal[i] = random.randrange(30, 120)
    return tuple(newRGBVal)

width, height = im.size

for w in range(width):
    for h in range(height):
        px[w, h] = disturb(im.getpixel((w, h)))


newSize = (300, 300)
im1 = im.resize(newSize)
im1 = im1.resize((592, 592), Image.NEAREST)
im1.show()

im.save(r'C:\Users\YONI\Desktop\result.png')
