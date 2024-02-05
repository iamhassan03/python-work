def fruit_calorie(fruit):

    fruits = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80
        }
    for name, calorie in fruits.items():
        if name.casefold() == fruit:
            return calorie


def main():
    fruit = input("Fruit: ").strip()
    if fruit_calorie(fruit):
        print("Calorie:", fruit_calorie(fruit))
    else:
        print("Not a Fruit!")

main()