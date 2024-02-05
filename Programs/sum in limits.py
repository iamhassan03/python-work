print("         *** Sum of series in a range ***")
low = int(input("Enter lower limit: "))
up = int(input("Enter higher limit: "))

sum = 0
count = low
while count <= up:
    sum = sum + count
    count+=1
print(sum)