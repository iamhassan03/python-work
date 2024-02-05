prtcg = float(input("Enter your Percentage: "))

if prtcg > 0.0 and prtcg <= 100.0:
    if prtcg >= 90.0:
        print("Your grade is \'A+\'")
    
    elif 50 <= prtcg < 90.0:
        if prtcg >= 80.0:
            print("Your grade is \'A\'")
        elif prtcg >= 70.0:
            print("Your grade is \'B\'")
        elif prtcg >= 60.0:
            print("Your grade is \'C\'")
        else:
            print("Your grade is \'D\'")
    else:
            print("Your grade is \'F\'")

else:
    print("Wrong Input!")