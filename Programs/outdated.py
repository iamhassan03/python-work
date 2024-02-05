def date_verify(date):
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August","September", "October", "November", "December"]

    if "/" in date:
        month, day, year = date.split("/")
        month, day, year = int(month), int(day), int(year)

        if 1 <= month <=12 and 1 <= day <= 31 and len(str(year)) == 4:
            return year, month, day
    elif "," in date:
        if not date[0].isalpha():
            return False
        else:
            month = ""
            for letter in date:
                if letter == ",":

                    comma_index = date.index(letter)

                    if comma_index > day_index:
                        for mon in months:
                            if month.title() == mon:
                                month = months.index(mon) + 1
                                day = date[comma_index-1]

                                if date[comma_index+1] == " ":
                                    year = date[comma_index+2: ]
                                else:
                                    year = date[comma_index+1: ]
                                    
                                if 1 <= int(day) <= 31 and len(year) == 4:
                                    return year, month, day
                                else:
                                    return False
                        return False
                    else:
                        return False
                if letter.isnumeric():
                    day_index = date.index(letter)
                if letter.isalpha():
                    month += letter  
    else:
        return False


def main():
    print("     --- Date Formatter ---")
    while True:
        date = input("Enter Date: ").strip()
    
        if date_verify(date):
            year, month, day = date_verify(date)
            break
        else:
            continue
    
    print("{}-{}-{}".format(year,month,day))

main()