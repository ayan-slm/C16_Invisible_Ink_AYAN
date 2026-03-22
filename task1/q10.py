def embed_bit (pixel_value,secret_bit):
    pixel_value = pixel_value&~1 
    return pixel_value|secret_bit

pixels = [150, 151, 152, 153, 154,155, 156, 157] 
secretBits = [1, 0, 1, 1, 0, 0, 1, 0]
for x,y in zip(pixels,secretBits):
    print(embed_bit(x,y))