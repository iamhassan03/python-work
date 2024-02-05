#                   Student Management System
#   Created by Muhammad Hassan Raza (SP23-BCS-056)

# login credentials
#       Username  : Password
stu_login = {  # user login credentials
    "SP21-BCS-006": "genius123",
    "FA20-BSE-010": "pakistan000",
    "FA21-BEE-106": "hacker1234",
    "SP20-BCT-050": "leader123",
    "FA22-BAI-091": "science111",
    "SP23-BDS-013": "humanity343",
    "FA23-BDA-013": "heavens738",
}

adm_login = {                   # admin login credentials
    "umariqbal1": "javaprog01",
    "anwar731": "ppit8310",
    "khurram1": "smart101",
    "majid11": "csdept01",
}

#   code    :   name
courses = {                     # courses
    "HUM101": "Islamic Studies",
    "HUM100": "English Comprehension and Composition",
    "EEE221": "Applied Physics",
    "CSC101": "Intoduction to ICT",
    "CSC102": "Discrete Structures",
    "CSC103": "Programming Fundamentals",
    "CSC110": "Theory of Automata",
    "CSC100": "Data Structures",
    "EEE200": "Digital Logic Design",
    "CSC301": "Design and Analysis of Algorithms",
    "CSC441": "Compiler Construction",
    "CSC462": "Artificial Intelligence",
    "CSC307": "Graph Theory",
    "CSC315": "Theory of Programming Languages",
    "MTH375": "Numerical Computations",
    "CSC241": "Object Oriented Programming",
    "CSC340": "Computer Networks",
    "CSC410": "Professional Practices",
    "MTH104": "Statistics and Probability Theory",
    "MTH262": "Calculus and Analytic Geometry",
    "AIC270": "Programming for Artificial Intelligence",
    "AIC260": "Machine Learning",
    "AIC250": "Pattern Recognition",
    "CSC211": "Web Technologies",
    "CYC101": "Introduction to Cyber Security",
    "CYC110": "Vulnerability Assessment & Reverse Engineering",
    "MGT101": "Introduction to Management",
    "MTH091": "Pre-Calculus",
    "CSC501": "Database Systems",
    "MTH231": "Linear Algebra",
    "HUM111": "Pakistan Studies",
}

#   student id    :  [name , semester]
details = {
    "SP21-BCS-006": ["Khaqan Ali", "3rd"],
    "FA20-BSE-010": ["Muhammad Sarib", "7th"],
    "FA21-BEE-106": ["Muhammad Hassnain", "5th"],
    "SP20-BCT-050": ["Muhammad Huzaifa", "3rd"],
    "FA22-BAI-091": ["Muhammad Hussain", "4th"],
    "SP23-BDS-013": ["Sarim Bajwa", "2nd"],
    "FA23-BDA-013": ["Muhammad Usama", "2nd"],
}
#   student id    :     [registered courses]
reg_courses = {
    "SP21-BCS-006": ["HUM101", "HUM100", "MGT101", "CSC101", "EEE221", "MTH091"],
    "FA20-BSE-010": ["HUM111", "MGT101", "CSC410", "CSC501", "EEE200", "MTH231"],
    "FA21-BEE-106": ["CYC101", "HUM100", "CSC241", "CSC103", "EEE221", "MTH104"],
    "SP20-BCT-050": ["CYC110", "CSC301", "MTH262", "CSC102", "AIC260", "CSC307"],
    "FA22-BAI-091": ["CSC441", "MTH375", "HUM101", "AIC250", "CYC101", "MGT101"],
    "SP23-BDS-013": ["HUM111", "MGT101", "CSC102", "CSC410", "CSC462", "MTH231"],
    "FA23-BDA-013": ["CSC110", "CSC301", "MTH104", "CSC315", "CYC110", "CSC340"],
}


#   student id    :     [attendances]
courses_attend = {
    "SP21-BCS-006": [87, 89, 82, 100, 96, 100],
    "FA20-BSE-010": [81, 86, 88, 90, 91, 93],
    "FA21-BEE-106": [92, 97, 89, 85, 92, 100],
    "SP20-BCT-050": [90, 95, 89, 100, 100, 97],
    "FA22-BAI-091": [100, 89, 82, 93, 96, 83],
    "SP23-BDS-013": [96, 89, 91, 83, 98, 81],
    "FA23-BDA-013": [80, 94, 82, 100, 91, 88],
}

#   student id    :     [course points]
courses_points = {
    "SP21-BCS-006": [76, 80, 77, 83, 82, 90],
    "FA20-BSE-010": [81, 78, 80, 82, 81, 89],
    "FA21-BEE-106": [92, 85, 80, 87, 84, 84],
    "SP20-BCT-050": [86, 91, 83, 75, 83, 92],
    "FA22-BAI-091": [75, 80, 81, 77, 82, 83],
    "SP23-BDS-013": [91, 88, 85, 80, 90, 89],
    "FA23-BDA-013": [80, 92, 82, 81, 92, 88],
}


#   code    :  {instrctor : credit}
instruct_credit = {  
    "HUM101": {"Asifa Tahir": 3},
    "HUM100": {"Ali Aslam": 3},
    "EEE221": {"Dr. Amir": 4},
    "CSC101": {"Khurram Iqbal": 3},
    "CSC102": {"Tanveer Ahmed": 3},
    "CSC103": {"Umar Iqbal": 4},
    "CSC110": {"Dr. Asim Asghar": 3},
    "CSC100": {"Dr. Inayat": 4},
    "EEE200": {"Fahad Shareef": 4},
    "CSC301": {"Tanveer Ahmed": 3},
    "CSC441": {"Akhtar Khawar": 4},
    "CSC462": {"Fahad-ul-Hassan": 3},
    "CSC307": {"Dr. Abid Ali": 3},
    "CSC315": {"Dr. Ishfaq": 3},
    "MTH375": {"Dr. Masood": 3},
    "CSC241": {"Fawad Ali": 4},
    "CSC340": {"Shoukat Khan": 4},
    "CSC410": {"Anwar Shoukat": 3},
    "MTH104": {"Dr. Asghar Khan": 3},
    "MTH262": {"Dr. Sajjad": 3},
    "AIC270": {"Dr. Ahmed Ali": 4},
    "AIC260": {"Dr. Saif-ur-Rehman": 4},
    "AIC250": {"Dr. Kashif": 4},
    "CSC211": {"Kamal Hassan": 4},
    "CYC101": {"Kashan Ahmed": 3},
    "CYC110": {"Mahmood-ul-Hassan": 4},
    "MGT101": {"Nabila Nazir": 3},
    "MTH091": {"Dr. Sajjad": 3},
    "CSC501": {"Shazim Ali": 4},
    "MTH231": {"Dr. Aqsa": 3},
    "HUM111": {"Anwar Ali": 3},
}


def point_gpa(point):
    if point >= 85:
        return 4
    elif point >= 80:
        return 3.66
    elif point >= 75:
        return 3.33
    elif point >= 70:
        return 3.00
    elif point >= 65:
        return 2.5
    elif point >= 60:
        return 2.00
    elif point >= 55:
        return 1.50
    elif point >= 50:
        return
    else:
        return "F"


def grade(gpa):
    if gpa >= 3.67:
        return "A"
    elif gpa >= 3.33:
        return "A-"
    elif gpa >= 3.00:
        return "B+"
    elif gpa >= 2.66:
        return "B"
    elif gpa >= 2.33:
        return "C+"
    elif gpa >= 2.00:
        return "C"
    elif gpa >= 1.50:
        return "D"
    elif gpa >= 1.00:
        return "E"
    else:
        return "F"


def status(cgpa):
    if cgpa >= 2.00:
        return "GAS"
    else:
        return "Prohabation"


def registered_courses(stud_id):
    print("        ----------------------")
    print("          Registered Courses ")
    print("        ----------------------")

    course_names = []
    course_codes = []
    for course in reg_courses[stud_id]:
        course_codes.append(course)
        course_names.append(courses[course])

    print("Sr.  Code             Course Name ")
    print("--------------------------------------------------------------")
    for num, course_ in enumerate(course_names):
        print("{:<3} {:<10} {:<50}".format(num + 1, course_codes[num], course_))

    statement = "Do you again want to view courses?"
    func_name = "registered"
    logged = True
    prompt(statement, func_name, logged, stud_id)


def register(stud_id):
    print("        ------------------------")
    print("          Courses Registration ")
    print("        ------------------------")
    print("Courses Available for Registration: ")

    print("Sr.  Code          Course Name ")
    print("------------------------------------------------------------")
    num = 1
    for code, course in courses.items():
        print("{:<3} {:<10} {:<45}".format(num, code, course))
        num += 1

    success = False
    while True:
        print("Note: You can register Max. 7 Courses!")
        choice = input("Enter Course Code to register: ").strip()  # ask for choice

        for code, name in courses.items():
            if code == choice:
                selected_course = courses.get(choice)

                if len(reg_courses[stud_id]) <= 7:
                    reg_courses[stud_id].append(selected_course)
                    print("'{choice}' has successfully been registered")
                    success = True
                    break
                else:
                    print("You cannot register more courses!")
                    student_menu(stud_id)

        if success:
            break
        else:
            print("Invalid Course Code! Please Again Enter.")

    if success:
        statement = "Do you again want to register another course?"
        func_name = "register"
        logged = True
        prompt(statement, func_name, logged, stud_id)


def result(stud_id):
    print("             ---------------")
    print("               Result Card")
    print("             ---------------")
    course_names = []
    course_codes = []
    course_credits = []

    for course in reg_courses[stud_id]:
        course_codes.append(course)
        course_names.append(courses[course])
        for instructor in instruct_credit[course]:
            course_credits.append(instruct_credit[course].get(instructor))

    name = details[stud_id][0]
    semester = details[stud_id][1]

    points = []
    for marks in courses_points[stud_id]:
        points.append(marks)

    gpas = []
    for mark in points:
        gpas.append(point_gpa(mark))

    grades = []
    for gpa in gpas:
        grades.append(grade(gpa))

    print(
        "\t\tName: {}\t  Student ID: {}\n\t\tSemester: {}\t\t  Program: {}".format(
            name, stud_id, semester, stud_id[5:8]
        )
    )
    print(
        "  Code            Course Name                               Credits    Points      GPA    Grade  "
    )
    print(
        "------------------------------------------------------------------------------------------------"
    )
    for num, course_name in enumerate(course_names):
        print(
            " {:<10} {:<50} {:<9} {:<9} {:<8} {:<8}".format(
                course_codes[num],
                course_name,
                course_credits[num],
                points[num],
                gpas[num],
                grades[num],
            )
        )

    total = 0
    for index, cred_hour in enumerate(course_credits):
        subj_total = cred_hour * gpas[index]
        total += subj_total

    cgpa = round(total / sum(course_credits), 2)
    print("            CGPA: {}".format(cgpa))
    print("            Scholastic Status: {}".format(status(cgpa)))

    statement = "Do you again want to view result?"
    func_name = "result"
    logged = True
    prompt(statement, func_name, logged, stud_id)


def cgpa_cal(stud_id):
    print("        ----------------------------")
    print("          CGPA and Grade Calculator ")
    print("        ----------------------------")
    while True:
        try:
            num_courses = int(input("Enter no. of courses: "))
        except (ValueError, NameError):
            print("Invalid Input!")
            continue
        else:
            break

    gpas = []
    credits = []
    num = 1
    while num <= num_courses:
        try:
            credit = int(input(f"Enter credits of course {num}: "))
            gpa = float(input("Enter GPA of course: "))
        except (ValueError, NameError):
            print("Invalid Input!")
            continue
        else:
            credits.append(credit)
            gpas.append(gpa)
            num += 1

    total = 0
    for index, cred_hour in enumerate(credits):
        course_total = gpas[index] * cred_hour
        total += course_total

    cgpa = round(total / sum(credits), 2)
    print("Your CGPA is: {:.2f}\n Grade: {}".format(cgpa, grade(cgpa)))

    statement = "Do you again want to again calculate CGPA?"
    func_name = "cgpa"
    logged = True
    prompt(statement, func_name, logged, stud_id)


def subject_gpa(stud_id):
    print("        -----------------------------------")
    print("          Course GPA and Grade Calculator ")
    print("        -----------------------------------")

    while True:
        # assignment marks
        try:
            assign = float(input("Enter Assignment Marks (out of 10): "))
        except:
            print("Invalid Input!")
        else:
            if assign > 10.0:
                print("Invalid Marks! Please again enter marks.")
                continue
            else:
                break

    while True:
        # quiz marks
        try:
            quiz = float(input("Enter Quiz Marks (out of 15): "))
        except:
            print("Invalid Input!")
        else:
            if quiz > 15.0:
                print("Invalid Marks! Please again enter marks.")
                continue
            else:
                break

    while True:
        # mids marks
        try:
            mids = float(input("Enter Mids Marks (out of 25): "))
        except:
            print("Invalid Input!")
        else:
            if mids > 25.0:
                print("Invalid Marks! Please again enter marks.")
                continue
            else:
                break

    while True:
        # finals marks
        try:
            finals = float(input("Enter Finals Marks (out of 50): "))
        except:
            print("Invalid Input!")
        else:
            if finals > 50.0:
                print("Invalid Marks! Please again enter marks.")
                continue
            else:
                break

    gpa = finals + mids + assign + quiz
    print("\tYour GPA is: {}\n\tGrade: {}".format(point_gpa(gpa), grade(gpa)))

    statement = "Do you again want to calculate GPA of another course?"
    func_name = "gpa"
    logged = True
    prompt(statement, func_name, logged, stud_id)


def attendance(stud_id):
    print("        ----------------------")
    print("          Attendance Details ")
    print("        -----------------------")

    course_names = []
    course_codes = []

    for course in reg_courses[stud_id]:
        course_codes.append(course)
        course_names.append(courses[course])

    print(" Code              Course Name                           Attendance (%)  ")
    print("-----------------------------------------------------------------------")
    for num, course_name in enumerate(course_names):
        print(
            "{:<10} {:<50} {:<9}".format(
                course_codes[num], course_name, courses_attend[stud_id][num]
            )
        )

    overall_attendance = round(
        sum(courses_attend[stud_id]) / len(courses_attend[stud_id]), 2
    )
    print("           Overall Attendance: {}%".format(overall_attendance))

    statement = "Do you again want to view attendance details?"
    func_name = "details"
    logged = True
    prompt(statement, func_name, logged, stud_id)


def course_details(stud_id):
    print("        -------------------")
    print("          Courses Details ")
    print("        -------------------")

    course_names = []
    course_codes = []
    course_credits = []
    course_instructor = []

    for course in reg_courses[stud_id]:
        course_codes.append(course)
        course_names.append(courses[course])
        for instructor, credit in instruct_credit[course].items():
            course_instructor.append(instructor)
            course_credits.append(credit)

    print(
        "Sr.  Code             Course Name                              Credits      Instructor "
    )
    print(
        "-----------------------------------------------------------------------------------------------"
    )
    for num, course_name in enumerate(course_names):
        print(
            "{:<3} {:<10} {:<50} {:<9} {:<25}".format(
                num + 1,
                course_codes[num],
                course_name,
                course_credits[num],
                course_instructor[num],
            )
        )

    statement = "Do you again want to show courses details?"
    func_name = "details"
    logged = True
    prompt(statement, func_name, logged, stud_id)


def prompt(statement, func_name, logged, stud_id):
    while True:
        print("\nDo you want to:")
        print("   " + statement + " (Enter 'yes')")
        print("   Logout from System (Enter 'logout')")
        if logged:
            print("   Return to Student Menu (Enter 'main')")
        choice = (
            input("Enter your selection: ").lower().strip()
        )  # ask to exit or return to menu or delete account

        if logged and choice == "main":
            print("Redirecting to Student Main Screen.....")
            student_menu(stud_id)

        if choice == "exit":  # exit from system
            print("Exiting from System.....")
            exit()

        elif choice == "logout":
            print("Logging Out.....")
            main()

        elif choice == "yes":  # recall current function
            match func_name:
                case "registered":
                    registered_courses(stud_id)
                case "register":
                    register(stud_id)
                case "cgpa":
                    cgpa_cal(stud_id)
                case "gpa":
                    subject_gpa(stud_id)
                case "details":
                    course_details(stud_id)
                case "attendance":
                    attendance(stud_id)
                case "result":
                    result(stud_id)
        else:
            print("Wrong Choice!")


def student_menu(stud_id):
    stud_name = details[stud_id][0]
    print("             ==========================")
    print("             |    CU Student Portal   |")
    print("             ==========================")
    print(
        f"""Welcome Dear {stud_name}!\n To:
        1. View Registered Courses (Press \'1\')
        2. Register Courses (Press \'2\')
        3. View Result (Press \'3\')
        4. Calculate CGPA and Grade (Press \'4\')
        5. Calculate Subject GPA (Press \'5\')
        6. View Attendance (Press \'6\')
        7. Course Details (Press \'7\')"""
    )
    while True:
        try:
            choice = int(input("Enter your selection: ").strip())  # ask for choice
        except (ValueError, NameError):
            print("Invalid Input! Please enter a valid input.")
            continue

        match choice:
            case 1:
                registered_courses(stud_id)
            case 2:
                register(stud_id)
            case 3:
                result(stud_id)
            case 4:
                cgpa_cal(stud_id)
            case 5:
                subject_gpa(stud_id)
            case 6:
                attendance(stud_id)
            case 7:
                course_details(stud_id)
            case _:
                print("Invalid Choice")


def main():
    print("             --------------------------------------")
    print("             |     CU Student Management System   |")
    print("             --------------------------------------")

    incomplete = True
    stud_id = input("Enter your Student ID: ")
    stud_pass = input("Enter your Password: ")
    for stud, password in stu_login.items():  # check credentials
        if stud == stud_id and stud_pass == password:
            incomplete = False
            student_menu(stud_id)

    if incomplete:
        print("Invalid Login Credentials!")

        statement = "Do you again want to login?"
        func_name = "login"
        logged = False
        incomplete = True
        stud_id = None
        prompt(statement, func_name, logged, stud_id)


if __name__ == "__main__":  # load main function if this file is directly loaded
    main()
