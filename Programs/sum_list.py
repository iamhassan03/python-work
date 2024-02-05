print("     *** Numbers Sum using List ***\n")

num1 = eval(input("Enter number 1: "))
num2 = eval(input("Enter number 2: "))
num3 = eval(input("Enter number 3: "))
num4 = eval(input("Enter number 4: "))

sum_num = [num1, num2, num3, num4]

# sum(list): sums list of any length
print ("Sum of all entered numbers is: {0} " .format(sum(sum_num)))