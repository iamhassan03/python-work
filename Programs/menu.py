choice = (input('''            *** Load Screen ***
        1. New game
        2. Load
        3. Options
        4. Quit
Enter your Choice (numerical value only): '''))

if choice >= '1' and choice <= '4':
    if choice == '1':
        print("New game is Loading... Please Wait.")
    elif choice == '2':
        print("Savegame is Loading... Please Wait.")
    elif choice == '3':
        print('''         *** Options ***
        1. Profile 
        2. Music
        3. Volume
        4. Display
        5. Graphics
        6. Exit''')
    elif choice == '4' :
        print("Thank you for playing!")
    else:
        print("Wrong Input!")
else:
    print("Wrong Input!")