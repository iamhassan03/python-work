l = int(input("Enter Length of Box: "))
h = int(input("Enter Height of Box: "))

for length in range(l):
    print("* ", end="")
print()
spaces = 2*(l-2)+1
for height in range(h-2):
    print("*",end="")
    for space in range(spaces):
        print(" ",end="")
    print("*")

for length in range(l):
    print("* ", end="")