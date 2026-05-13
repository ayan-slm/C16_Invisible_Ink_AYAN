from PIL import Image
im = Image.open("output.png")

pixel = im.load()
width,height = im.size
bin_string = ""
finished = False
for y in range(height):
    if finished:
        break
    for x in range(width):
        r,g,b = pixel[x,y]
        bin_r = format(r,"08b")
        bin_g = format(g,"08b")
        bin_b = format(b,"08b")
        bin_string += bin_r[7] + bin_g[7] + bin_b[7]
        if(bin_string[-8:] == "11111111"):
            finished = True
            break

message = ""   
for i in range(0,len(bin_string),8):
    bin_letter = bin_string[i:i+8]
    if(bin_letter == "11111111"):
        break
    Ascii_letter = int(bin_letter,2)
    message += chr(Ascii_letter)
    
print(message)

