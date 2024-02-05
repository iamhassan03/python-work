print("         *** Even / odd numbers print ***")
low = int(input("Enter lower limit: "))
up = int(input("Enter higher limit: "))

print("Even numbers from {0} to {1} (inclusive) are: " .format(low,up))
count = low
while count <= up:
    if count % 2 == 0:
        print("  ",count)
    count+=1
    
print("\nOdd numbers from {0} to {1} (inclusive) are: " .format(low,up))
count = low

while count <= up:
    if count % 2 != 0:
        print("  ",count)
    count+=1