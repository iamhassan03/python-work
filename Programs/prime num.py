num = int(input("Enter any number: "))

prime = 1
chk = 2

while chk <= int(num ** 0.5):
    if num % chk==0:
        prime = 0
        break
    chk+=1
    
if prime:
    print(num, "is a prime number")
else:
    print(num, "is a not prime number")