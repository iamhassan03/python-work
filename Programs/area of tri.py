side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

s = ((side1+side2+side3)/2)      # s = semi perimeter = (a+b+c)/2
area = (s*(s-side1)*(s-side2)*(s-side3)) ** 0.5  # Hero's Formula
print("Area of triangle is:",area)