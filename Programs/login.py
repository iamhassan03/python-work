print('''             *** Login Screen ***
  Here are the users on this PC
    1- Hassan
    2- Unknown''')
user1 = "Hassan"
user11 = "hassan"
pass1 = "game123"

user2 = "Unknown"
user22 = "unknown"
pass2 = "computer123"
user = input("Enter username: ")

if user == user1 or user == user11:
    pswd = input("Enter your password: ")
    if pswd == pass1:
      print("Welcome! Hassan")
    else:
      print("Wrong Password! Please Try Again")
      
elif user == user2 or user == user22:
    pswd = input("Enter your password: ")
    if pswd == pass2:
      print("Welcome! Unknown")
    else:
      print("Wrong Password! Please Try Again")

else:
  print("Wrong Username")
