from math import pi

print("     *** Area & Volume of Cylinder Calculator ***")
rad = eval(input("Enter radius of Cylinder: "))

while rad < 0:
    print("Wrong input!")
    rad = eval(input("Again, enter radius of Cylinder: "))

area = pi*rad*rad
vol = area*rad

print("Area of Cylinder with Radius {:.2f} is: {:.4f}" .format(rad,area))
print("Volume of Cylinder with Radius {:.2f} is: {:.4f}" .format(rad,vol))