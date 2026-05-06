#Editing textfile
with open("testfile.txt","r+") as txt:
    txt.write("Hello! \nThis is a test \nBye")
    txt.seek(0)
    print(txt.read())


#Image
from PIL import Image
im = Image.open("image1.jpg")
print(f"Format: {im.format}")
print(f"Mode: {im.mode}")
print(f"Size: {im.size}")