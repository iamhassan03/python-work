def shorten_text(text):
    new_text = ""
    for char in text:
        match char:
            case "a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U":
                continue
            case _:
                new_text += char
    return new_text


def main():
    text = input("Enter Text: ").strip()
    print("Shortened Text:", shorten_text(text))


main()
