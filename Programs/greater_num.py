print("     *** Greater Number Determination ***\n")

num1 = eval(input("Enter 1st number: "))
num2 = eval(input("Enter 2nd number: "))
num3 = eval(input("Enter 3rd number: "))
num4 = eval(input("Enter 4th number: "))

if (num1>num2 and num1>num3 and num1>num4):
    print("1st number is greatest!")

elif (num2>num1 and num2>num3 and num2>num4):
    print("2nd number is greatest!")

elif (num3>num1 and num3>num2 and num3>num4):
    print("3rd number is greatest!")

else:
    print("4th number is greatest!")
