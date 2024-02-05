def loan():
    print("     --- Loan Calculator ---")
    yearlyInterestRate = eval(input("Enter annual interest rate: ").strip())
    loanAmount = eval(input("Enter total loan amount: ").strip())
    numYears = eval(input("Enter total years: ").strip())

    if not (yearlyInterestRate > 0 or loanAmount > 0 or numYears > 0):
        monthlyInterestRate = (yearlyInterestRate/100)/12
        monthlyPayment = loanAmount * monthlyInterestRate /\
                        (1 - 1 / (1 + monthlyInterestRate)**(numYears*12))
        totalPayment = monthlyPayment * 12 * numYears
    
        print(f"Monthly payment is: {monthlyPayment:.2f}")
        print(f"Total payment is: {totalPayment:.2f}")

    else:
        print("Invalid interest rate/loan amount or year!")

loan()  # call loan
