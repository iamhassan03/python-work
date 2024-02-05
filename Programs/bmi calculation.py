import os
print("       *** BMI Calculator ***")
weight = eval(input("Enter Your Weight (in kilograms): "))
height = eval(input("Enter Your Height (in meters): "))
bmi=weight/height**2
print("Your BMI is:", round(bmi,4))
os.system("pause")