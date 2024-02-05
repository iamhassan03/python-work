
marks = float(input("Enter marks of student: "))
t_mark = 0
t_stud = 0

while marks >= 0:
    marks = float(input("Enter marks of student: "))
    t_stud+=1
    t_mark = t_mark + marks

if t_stud > 0:
    avg = t_mark/t_stud
    print("Average of",t_stud,"students is:",avg)
else:
    print("No student!")