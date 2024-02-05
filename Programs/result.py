print('''         *** Result Calculation ***
  Following are the Disciplines of Intermediate(Part II): 
    1. FSC Pre-Engineering
    2. ICS
    3. FSC Pre-Medical''')
discp = input("=> Enter your discipline (numerical value only): ")

if discp == '1' or discp == '2' or discp == '3':
    
    year =  input(''' Select your year:
    1. Part I
    2. Part II
=> Enter your year (numerical value only): ''')

    if year == '1': # part 1
        isl = float(input("Enter your Islamic Studies Marks: "))
    elif year == '2': # part 2
        pak_std = float(input("Enter your Pakistan Studies Marks: "))
    else:
        print("         Wrong Input!")
        exit()
    
    eng = float(input("Enter your English Marks: "))
    urdu = float(input("Enter your Urdu Marks: "))
    phy = float(input("Enter your Physics Marks: "))
    
    if discp >= '1' and discp <= '2':
        math = float(input("Enter your Mathematics Marks: "))
        
        if discp == '1':       # pre-eng
        
            chem = float(input("Enter your Chemistry Marks: "))
        
            if year == '1': # part 1
                ob_mark = eng+urdu+isl+phy+math+chem
            else: # part 2
                ob_mark = eng+urdu+pak_std+phy+math+chem
            
            prtcg = (ob_mark/520.0)*100.0
            print('''    Obtained Marks: {:.2f}/520
    Pecentage: {:.2f}''' .format(ob_mark, prtcg))
    
        elif discp == '2':       # ics
            comp = float(input("Enter your Computer Marks: "))
        
            if year == '1': # part 1
                ob_mark = eng+urdu+isl+phy+math+comp
            else: # part 2
                ob_mark = eng+urdu+pak_std+phy+math+comp
            
            prtcg = (ob_mark/510.0)*100.0
            print('''    Obtained Marks: {:.2f}/510
    Pecentage: {:.2f}''' .format(ob_mark, prtcg))
        
    else:    # pre-med
        chem = float(input("Enter your Chemistry Marks: "))
        bio = float(input("Enter your Biology Marks: "))
        
        if year == '1': # part 1
            ob_mark = eng+urdu+isl+phy+bio+chem
        else: # part 2
            ob_mark = eng+urdu+pak_std+phy+bio+chem
            
        prtcg = (ob_mark/505.0)*100
        print('''    Obtained Marks: {:.2f}/505
    Pecentage: {:.2f}''' .format(ob_mark, prtcg))
    
    if prtcg > 0.0 and prtcg <=100.0:  # for grade
        if prtcg >= 80.0:
            print("    Grade: \'A+\'")
    
        elif prtcg < 80.0 and prtcg > 40.0:
            if prtcg > 70.0:
                print("    Grade: \'A\'")
            elif prtcg > 60.0:
                print("    Grade: \'B\'")
            elif prtcg > 50.0:
                print("    Grade: \'C\'")
            else:
                print("    Grade: \'D\'")
        else:
            print("    Grade: \'U\'")
    
else:
    print("         Wrong Input!")
    exit()