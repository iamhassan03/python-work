print("     *** Reverse 4-digit Number ***")
num = input("Enter a 4-digit integer: ")

while not((len(num)) == 4 and num.isdigit()):
    print("Wrong input!")
    num = input("Enter a 4-digit integer: ")

print("Reversed Digit is:" , num[3::-1])