def snake_case(string):
    new_str = ""
    for char in string:
        if not char.isupper():
            new_str += char
        else:
            index = string.index(char)
            new_str += "_" + char.lower()
    return new_str

def main():
    string = input("camelCase: ").strip()
    print("snake_case:",snake_case(string))

main()