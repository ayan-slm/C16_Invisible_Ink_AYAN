from PIL import Image
im = Image.open("carrier.png")
message = input("Enter a secret message: ")

bin_msg = ""
for char in message:
    bin_form = format(ord(char),"08b")
    bin_msg += bin_form
bin_msg += "11111111"

    
i = 0
finished = False
pixel = im.load()
width, height = im.size
for y in range(height):
    if finished:
         break
    for x in range(width):
          r,g,b = pixel[x,y]
          bin_r = format(r,"08b")
          bin_g = format(g,"08b")
          bin_b = format(b,"08b")
          if(i>=len(bin_msg)):
               
                    finished = True
                    pixel[x,y] = r,g,b
                    break
                    
          bin_r = bin_r[0:-1] + bin_msg[i]
          r = int(bin_r,2)
          i += 1
          if(i>=len(bin_msg)):
               
                    finished = True
                    pixel[x,y] = r,g,b
                    break
                    
          bin_g = bin_g[0:-1] + bin_msg[i]
          g = int(bin_g,2)
          i += 1
          if(i>=len(bin_msg)):
               
                    finished = True
                    pixel[x,y] = r,g,b
                    break
                    
          bin_b = bin_b[0:-1] + bin_msg[i]
          b = int(bin_b,2)
          i += 1
          pixel[x,y] = r,g,b
        
im.save("output.png")
               