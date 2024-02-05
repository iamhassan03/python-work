def is_valid(plate):
    alpha = 0
    if len(plate) >= 2 and len(plate) <= 6 and plate.isalnum():
        for char in plate:
            if char.isalpha():
                alpha += 1
                al_index = plate.index(char)
            else:
                num_index = plate.index(char)
        if alpha >= 2:
            if al_index < num_index:
                if plate[al_index + 1] != 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def main():
    plate = input("Plate #: ").strip()

    if is_valid(plate):
        print("Valid Plate #")
    else:
        print("Invalid Plate #")


main()
