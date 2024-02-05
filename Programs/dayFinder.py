print("     --- Day Calculator ---")

day = int(input("What day is today? (enter number of day of week): "))
meet = int(input("Enter the number of days: "))

cal_day = (day+meet)%7

match cal_day:
    case 1:
        print(f"Day in {meet} days is: Monday")
    case 2:
        print(f"Day in {meet} days is: Tuesday")
    case 3:
        print(f"Day in {meet} days is: Wednesday")
    case 4:
        print(f"Day in {meet} days is: Thursday")
    case 5:
        print(f"Day in {meet} days is: Friday")
    case 6:
        print(f"Day in {meet} days is: Saturday")
    case _:
        print(f"Day in {meet} days is: Sunday")