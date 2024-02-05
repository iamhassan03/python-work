print("     *** Spam Message Identification ***\n")

text = input("Enter any text: ")
spam = False

if ("make a lot of money" in text):
    spam = True

elif ("buy now" in text):
    spam = True

elif ("subscribe this" in text):
    spam = True

elif ("click this" in text):
    spam = True

if (spam == True):
    print("This a spam comment!")
else:
    print("This not a spam comment!")