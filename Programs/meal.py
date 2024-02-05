def main():
    print("     --- Meal Time ---")
    hours, mins = input("What time is it? ").strip().split(":")
    
    hours, mins = int(hours), int(mins)
    time = hours+(mins/60)

    if 7.00 <= time <= 8.00:
        print("It's BreakFast Time!")

    elif 12.00 <= time <= 13.00:
        print("It's Lunch Time!")
    
    elif 18.00 <= time <= 19.00:
        print("It's Dinner Time!")

    else:
        print("No Meal Time!")

main()