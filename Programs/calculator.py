operator = input('''Enter your desired operator from below:
  1.   +
  2.   -
  3.   *
  4.   /
Your Choice: ''')
if operator == "+":
    print("You've selected \'Addition\'")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    sum=num1+num2
    print("{0} + {1} = {2}" .format(num1, num2, sum))

elif operator == "-":
    print("You've selected \'Subtraction\'")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    minus=num1-num2
    print("{0} - {1} = {2}" .format(num1, num2, minus))

elif operator == "*":
    print("You've selected \'Multiplication\'")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    mul=num1*num2
    print("{0} * {1} = {2}" .format(num1, num2, mul))
    
elif operator == "/":
    print("You've selected \'Division\'")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    div=num1/num2
    print("{0} / {1} = {2}" .format(num1, num2, div))
    
else:
    print("Sorry! Wrong choice.")