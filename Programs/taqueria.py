def menu(choice):
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    for item, price in menu.items():
        if item.casefold() == choice:
            return price

    return KeyError


def main():
    price = 0
    while True:
        try:
            food = input("Item Name: ").strip()
            price += menu(food)
            print(f"Total Bill: {price:.2f}$")
        except (ValueError, KeyError, TypeError):
            print("Desired Item not found!!")
        except EOFError:
            print("Thanks for Visiting....")
            exit()


main()
