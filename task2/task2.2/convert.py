from PIL import Image
img = Image.open("baseImage.jpg")
img.save("PNGimage.png")
gray = img.convert("L")
gray.save("GrayImage.png")

import os
initialSize = os.path.getsize("baseImage.jpg")
pngSize = os.path.getsize("PNGimage.png")
graySize = os.path.getsize("GrayImage.png")
print(f"Initial size: {initialSize}")
print(f"PNG size: {pngSize}")
print(f"Gray scale size: {graySize}")