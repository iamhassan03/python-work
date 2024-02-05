def main():
    print("     --- Math Interpreter ---")
    num1, exp, num2 = input("Enter your problem (separate by spaces): ").strip().split(" ")
    num1 , num2 = eval(num1), eval(num2)

    match exp:
        case "+":
            add()
        case "-":
            minus()
        case "*":
            product()
        case "/":
            divide()
        case _:
            print("Invalid Operand")

def add(num1, num2):
    print(f"Sum of {num1} and {num2} is:", num1+num2)

def minus(num1,num2):
    if num2>num1:
        num1, num2= num2, num1

    print(f"Difference of {num1} and {num2} is:", num1-num2)

def product(num1, num2):
    print(f"Product of {num1} and {num2} is:", num1*num2)

def divide(num1, num2):
    print(f"Division of {num1} by {num2} is:", num1*num2)

main()