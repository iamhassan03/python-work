print("     *** ASCII Code to Character Conversion ***")
code = eval(input("Enter an ASCII Code (0-127): "))

while code <0 and code > 127:
    print("Wrong input!")
    code = input("Again, enter an ASCII Code (0-127): ")

char = chr(code)

print("Character for ASCII Code %d is: %s" %(code,char))