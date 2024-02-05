print("     --- Word Counter --- ")
print("Enter line(s): ")
line = input()

count = dict()

line = line.split()
for word in line:
    # var = get value of (required variable, default value returned if req. var. not matches)
    count[word] = count.get(word, 0) + 1

for word, times in count:
    if word.isnumeric():
        continue
    print("Word: {:<13} Times:{:<5}".format(word, times))