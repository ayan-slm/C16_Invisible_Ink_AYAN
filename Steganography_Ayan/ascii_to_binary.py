message = input("Enter a short message: ")
binary_list = []
for char in message:
    binary_form = format(ord(char),"08b")
    binary_list.append(binary_form)
print(binary_list)
