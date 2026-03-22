def ASCII (x):
    ASCII = ord(x)
    bin_ASCII = bin(ASCII)
    bin_ASCII = bin_ASCII[2: ].zfill(8)
    return bin_ASCII

print(ASCII('A'))