number = int (input("Enter any number: "))

factorial = 1
count = 1

while count <= number:
    factorial = factorial*count
    count+=1
    
print("Factorial of {0} is : {1}" .format(number, factorial))