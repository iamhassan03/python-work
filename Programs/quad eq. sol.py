import cmath

a = int(input("Enter a: "))
b= int(input("Enter b: "))
c= int (input("Enter c: "))

disc = (b**2 - 4*a*c)**0.5

sol1 = (-b+cmath.sqrt(disc))/2*a
sol2 = (-b-cmath.sqrt(disc))/2*a

print("Solution of equation are: {0} and {1}" .format(sol1,sol2))