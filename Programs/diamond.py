length = int(input("Enter Length of Diamond: "))

for tri1 in range(length-1):
    for space in range((length-1)-tri1):
        print(" ",end="")
    for right1 in range(tri1+1):
        print("*",end="")
    for left1 in range(tri1):
        print("*", end="")
    print()

for tri2 in range(length):
    for space in range(tri2):
        print(" ",end="")
    for right2 in range(length-tri2):
        print("*", end="")
    for right in range((length-tri2)-1):
        print("*",end="")
    print()