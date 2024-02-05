def main():
    print("     --- Grocery List ---")
    item_list = grocery_list()
    print("Grocery Items: ")
    for item, quantity in item_list.items():
        print("{}x {}".format(quantity, item.title()))

def grocery_list():
    item_list = {}
    while True:
        try:
            item = input("Item: ").strip()
        except EOFError:
            return item_list
        else:
            if item.isalpha():
                if item.upper() in item_list:
                    print(f"Item ={item}")
                    for grocery in item_list:
                        if grocery == item.upper():
                            item_list[grocery] += 1
                else:
                    item_list[item.upper()] = 1
            else:
                print("Invalid Item Name!!")

main()