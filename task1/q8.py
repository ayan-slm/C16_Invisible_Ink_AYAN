def embed_bit (pixel_value,secret_bit):
    pixel_value = pixel_value%~1 
    return pixel_value|secret_bit



