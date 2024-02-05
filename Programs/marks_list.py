print("     *** Students Marks Storing ***\n")

stu1 = eval(input("Enter marks of student 1: "))
stu2 = eval(input("Enter marks of student 2: "))
stu3 = eval(input("Enter marks of student 3: "))
stu4 = eval(input("Enter marks of student 4: "))
stu5 = eval(input("Enter marks of student 5: "))
stu6 = eval(input("Enter marks of student 6: "))

marks = [stu1, stu2, stu3, stu4, stu5, stu6]
marks.sort()
print("Marks of students in sorted manner are: {0}" .format(marks))