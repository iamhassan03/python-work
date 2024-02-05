from math import ceil
def fuel_percentage():
    while True:
        try:
            numer, denom = input("Fuel Fraction: ").strip().split("/")
            numer, denom = int(numer), int(denom)
        except (ValueError, NameError):
            print("Error: Input values not integer!!")
        else:
            if numer < denom or denom == 0:
                try:
                    percentage = ceil(numer / denom * 100)
                    return percentage
                except ZeroDivisionError:
                    print("Zero Division Error: Denominator cannot be zero!")
            else:
                print("Numerator cannot be greater than numerator!!")

def main():
    fuel_percent = fuel_percentage()
    if fuel_percent >= 99:
        print("F")
    elif fuel_percent <= 1:
        print("E")
    else:
        print(f"{fuel_percent}%")

main()