from random import randint

# account ids
account_id = [
    1001,
    1002,
    1003,
    1004,
    1005,
    1006,
    1007,
]

# account names
names = [
    "Khaqan Ali",
    "Muhammad Sarib",
    "Muhammad Hassnain",
    "Muhammad Huzaifa",
    "Muhammad Hussain",
    "Sarim Bajwa",
    "Muhammad Usama",
]
# transaction details
transactions = [
    10010,
    50000,
    70000,
    100000,
    50500,
    106000,
    300500,
]

# account pins
pins = [
    250470,
    889684,
    448238,
    157493,
    648992,
    588391,
    340729,
]


def create_account():
    print("        ----------------------")
    print("           Account Creation ")
    print("        ----------------------")
    print("  Welcome New User!")

    while True:
        inp_name = input("Enter Your Name: ").strip().title()

        valid_name = name_validator(inp_name)

        if valid_name:
            break
        else:
            continue

    # deposit amount input
    while True:
        inp_amount = input("Enter the initial deposit amount: ").strip()

        valid_amount = amount_validator(inp_amount)

        if valid_amount:
            break
        else:
            continue

    # pin input
    while True:
        inp_pin = input("Enter your pin (only integers of length 6): ").strip()

        valid_pin = pin_validator(inp_pin)

        if valid_pin:
            break
        else:
            continue

    acc_num = randint(1000, 99999)

    # storing details
    names[len(names) - 1] = valid_name
    transactions[len(names) - 1] = valid_amount
    account_id[len(names) - 1] = acc_num
    pins.append(valid_pin)

    print(
        f"Account has successfully been created!\nYour Account ID is: {acc_num}\n Your pin is: {valid_pin}"
    )

    statement = "Create Another Account"
    func_name = "create"
    prompt(statement, func_name)


def modify_account():
    print("        ----------------------------------")
    print("           Account Details Modification ")
    print("        ----------------------------------")

    success = False

    while True:
        # account id validation
        try:
            inp_id = int(input("Enter your account id: ").strip())
        except:
            print("Invalid Input! Please enter a valid input.")
            continue

        # pin validation
        try:
            inp_pin = int(input("Enter your account pin: ").strip())
        except:
            print("Invalid Input! Please enter a valid input.")
            continue

        for id in account_id:
            if id == inp_id:
                id_index = account_id.index(inp_id)
                if pins[id_index] == inp_pin:
                    print("\n Welcome {}!".format(names[id_index]))
                    print(
                        "To change:\n 1. Your Name (Press'1')\n 2. Account ID (Press'2')\n 3. Account Pin (Press'3')"
                    )
                    while True:
                        try:
                            choice = int(
                                input("Enter your selection: ").strip()
                            )  # ask for choice
                        except ValueError:
                            print("Invalid Input! Please enter a valid input.")
                            continue
                        else:
                            break

                    match choice:
                        case 1:
                            while True:
                                inp_name = input("Enter new name: ").strip().title()
                                valid_name = name_validator(inp_name)

                                if valid_name:
                                    break
                                else:
                                    continue

                            index = account_id.index(inp_id)
                            names[index] = valid_name

                            print(
                                f"Account Name has succesfully been changed!\n New Account Name is: {valid_name}"
                            )
                            success = True
                            break

                        case 2:
                            index = account_id.index(inp_id)
                            new_id = randint(1000, 99999)
                            account_id[index] = new_id

                            print(
                                f"Account ID has succesfully been changed!\n New Account ID is: {new_id}"
                            )
                            success = True
                            break

                        case 3:
                            while True:
                                inp_pin = input("Enter new pin: ").strip().title()
                                valid_pin = pin_validator(inp_pin)

                                if valid_pin:
                                    break
                                else:
                                    continue

                            index = account_id.index(inp_id)
                            pins[index] = valid_pin

                            print(
                                f"\nAccount Pin has succesfully been changed!\nNew Account Pin is: {valid_pin}"
                            )
                            success = True
                            break
                        case _:
                            print("Invalid Choice! Please enter a valid choice.")
                            continue
        if success:
            break
        else:
            print("Account not found! Invalid Account Details")

    if success:
        statement = "Modify Another Account"
        func_name = "modify"
        prompt(statement, func_name)


def account_details():
    print("        ---------------------")
    print("           Account Details ")
    print("        ---------------------")

    success = False

    while True:
        # account id validation
        try:
            inp_id = int(input("Enter your account id: ").strip())
        except:
            print("Invalid Input! Please enter a valid input.")
            continue

        # pin validation
        try:
            inp_pin = int(input("Enter your account pin: ").strip())
        except:
            print("Invalid Input! Please enter a valid input.")
            continue

        for id in account_id:
            if id == inp_id:
                id_index = account_id.index(inp_id)
                if pins[id_index] == inp_pin:
                    print("\n Welcome {}!".format(names[id_index]))
                    name = names[id_index]
                    money = transactions[id_index]

                    print(
                        "Name: {}\nAccount ID: {}\nAccount Pin: {}\nBalance: {}".format(
                            name, inp_id, inp_pin, money
                        )
                    )
                    success = True
                    break
        if success:
            break
        else:
            print("Account not found! Invalid Account Details")

    if success:
        statement = "Get Details of Another Account"
        func_name = "details"
        prompt(statement, func_name)


def add_amount():
    print("        -----------------------")
    print("           Amount Deposition ")
    print("        -----------------------")

    success = False

    while True:
        # account id validation
        try:
            inp_id = int(input("Enter your account id: ").strip())
        except:
            print("Invalid Input! Please enter a valid input.")
            continue

        # pin validation
        try:
            inp_pin = int(input("Enter your account pin: ").strip())
        except:
            print("Invalid Input! Please enter a valid input.")
            continue

        for id in account_id:
            if id == inp_id:
                id_index = account_id.index(inp_id)
                if pins[id_index] == inp_pin:
                    print("\n Welcome {}!".format(names[id_index]))

                    # amount input
                    while True:
                        inp_amount = input("Enter the amount: ").strip()
                        valid_amount = amount_validator(inp_amount)

                        if valid_amount:
                            break
                        else:
                            continue

                    transactions[id_index] += valid_amount
                    print(
                        f"Amount of {valid_amount}Rs. has successfully been deposited!"
                    )
                    print("New Balance is: {}".format(transactions[id_index]))

                    success = True
                    break
        if success:
            break
        else:
            print("Account not found! Invalid Account Details")

    if success:
        statement = "Deposit amount to another Account"
        func_name = "deposit"
        prompt(statement, func_name)


def withdraw_amount():
    print("        ----------------------")
    print("           Amount Withdrawl ")
    print("        ----------------------")

    while True:
        # account id validation
        try:
            inp_id = int(input("Enter your account id: ").strip())
        except:
            print("Invalid Input! Please enter a valid input.")
            continue

        # pin validation
        try:
            inp_pin = int(input("Enter your account pin: ").strip())
        except:
            print("Invalid Input! Please enter a valid input.")
            continue

        for id in account_id:
            if id == inp_id:
                id_index = account_id.index(inp_id)
                if pins[id_index] == inp_pin:
                    print("\n Welcome {}!".format(names[id_index]))

                    # amount input
                    while True:
                        inp_amount = input("Enter the amount: ").strip()
                        valid_amount = amount_validator(inp_amount)

                        if valid_amount:
                            break
                        else:
                            continue

                    transactions[id_index] -= valid_amount
                    print(
                        f"Amount of {valid_amount}Rs. has successfully been deposited!"
                    )
                    print("New Balance is: {}".format(transactions[id_index]))

                    success = True
                    break
        if success:
            break
        else:
            print("Account not found! Invalid Account Details")

    if success:
        statement = "Withdraw amount from another Account"
        func_name = "withdraw"
        prompt(statement, func_name)


def delete_account():
    print("        ----------------------")
    print("           Account Deletion ")
    print("        ----------------------")

    while True:
        # account id validation
        try:
            inp_id = int(input("Enter your account id: ").strip())
        except:
            print("Invalid Input! Please enter a valid input.")
            continue

        # pin validation
        try:
            inp_pin = int(input("Enter your account pin: ").strip())
        except:
            print("Invalid Input! Please enter a valid input.")
            continue

        for id in account_id:
            if id == inp_id:
                id_index = account_id.index(inp_id)
                if pins[id_index] == inp_pin:
                    print("\n Welcome {}!".format(names[id_index]))

                    account_id.pop(id_index)
                    transactions.pop(id_index)
                    names.pop(id_index)
                    pins.pop(id_index)

                    print("Account has successfully been deleted!")
                    success = True
                    break

        if success:
            break
        else:
            print("Account not found! Invalid Account Details")

    if success:
        statement = "Delete another Account"
        func_name = "delete"
        prompt(statement, func_name)


# prompt function
def prompt(statement, func_name):
    while True:
        print("\nDo you want to:")
        print("   " + statement + " (Enter 'yes')")
        print("   Exit from System (Enter 'exit')")
        print("   Return to Main Menu (Enter 'menu')")
        choice = (
            input("Enter your selection: ").lower().strip()
        )  # ask to exit or return to menu or delete account

        if choice == "exit":  # exit from system
            print("Exiting from System.....")
            exit()

        elif choice == "menu":  #  return to main menu
            print("Redirecting to Main Menu.....")
            main()

        elif choice == "yes":  # recall current function
            match func_name:
                case "create":
                    create_account()
                case "modify":
                    modify_account()
                case "details":
                    account_details()
                case "deposit":
                    add_amount()
                case "withdraw":
                    withdraw_amount()
                case "delete":
                    delete_account()
        else:
            print("Wrong Choice!")


# validation functions:

# pin validator
def pin_validator(pin):
    try:
        pin = int(pin)
    except ValueError:
        print("Invalid Input! Please enter valid input.")
    else:
        if len(str(pin)) == 6 and pin > 0:
            return pin
        else:
            print("Invalid Pin! Please enter valid input.")
            return False


# amount validator
def amount_validator(amount):
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid Input! Please enter valid input.")
    else:
        if amount > 0:
            return amount
        else:
            print("Invalid amount! Please enter valid amount.")
            return False


# name validator
def name_validator(name):
    for character in name:
        if not (character.isalpha() or character.isspace()):
            print("Invalid Name! Please enter a valid name.")
            return False

    return name



# main function
def main():
    # main home page of program
    print("             -----------------------------------")
    print("             |        CUI Banking System       |")
    print("             -----------------------------------")
    print(
        """Welcome Dear Customer!\n To:
        1. Create Account (Press \'1\')
        2. Modify Account (Press \'2\')
        3. Show Account Details (Press \'3\')
        4. Add Amount (Press \'4\')
        5. Withdraw Amount (Press \'5\')
        6. Delete Account (Press \'6\')"""
    )
    while True:
        try:
            choice = int(input("Enter your selection: ").strip())  # ask for choice
        except ValueError:
            print("Invalid Input! Please enter a valid input.")
            continue

        match choice:
            case 1:
                create_account()
            case 2:
                modify_account()
            case 3:
                account_details()
            case 4:
                add_amount()
            case 5:
                withdraw_amount()
            case 6:
                delete_account()
            case _:
                print("Invalid Choice")


if __name__ == "__main__":  # load main function if this file is directly loaded
    main()