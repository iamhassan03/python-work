print("     *** Palindrome Checker ***")
string = input("Enter any string: ")
string = string.strip()

high = len(string) - 1
low = 0
while low <= high:
    print(low, " ", high)
    if string[low] == string[high]:
        low +=1 
        high -=1
    else:
        print("Not Palindrome!")
        break

if low > high:
    print("String \"",string,"\" is palindrome!")
