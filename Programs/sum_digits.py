print("     *** Self Number Sum ***")
num = eval(input("Enter an integer (between 0 and 1000, exlusive): "))

while (not(num > 0 and num < 1000)) or (not(isinstance(num,int))):
    print("Wrong input!")
    num = eval(input("Again enter an integer (between 0 and 1000, exlusive): "))

dig = map(int,str(num))
print(dig)
sum = sum(dig)
print("The sum of digits in {0} is: {1}" .format(num, sum))