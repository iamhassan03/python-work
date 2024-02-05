print("     *** Greater Number Determination ***\n")

num1 = eval(input("Enter 1st number: "))
num2 = eval(input("Enter 2nd number: "))
num3 = eval(input("Enter 3rd number: "))
num4 = eval(input("Enter 4th number: "))

if (num1 > num2):
    num_chk1 = num1
else:
    num_chk1 = num2

if (num3 > num4):
    num_chk2 = num3
else:
    num_chk2 = num4

if (num_chk1 > num_chk2):
    print(num_chk1, "is greatest!")
else:
    print(num_chk2, "is greatest!")