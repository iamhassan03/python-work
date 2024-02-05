rows = int(input("Enter rows: "))

for outer in range(rows):
    for inner in range(outer+1):
        print("* ",end = "")
    print("\n")
    