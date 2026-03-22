#Brute force
X = "10011100"
length = len(X)
decX = 0
for i in range(length):
    decX += int(X[length - i - 1]) * (2**(i))
print(decX)



# inbuilt function
y = "10011100"
decY = int(X,2)
print(decY)