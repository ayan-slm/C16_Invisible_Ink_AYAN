x = input("Input a word: ")
length = len(x)
for i in range(length):
    ASCII = ord(x[i])
    ASCII_bin = bin(ASCII)
    print(ASCII_bin[2: ])