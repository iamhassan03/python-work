def change (amount, coin):
    return amount - coin

def main():
    print("     --- Welcome to Coke Machine ---")
    due = 50
    while True:
        coin = int(input("Insert Coin: "))
        match coin:
            case 5 | 10 | 25:
                if due >= coin: 
                    due = change(due, coin)
                    if due > 0:
                        print(f"Amount Due: {due}")
                    else:
                        print(f"Change Owed: {due}")
                        break
                else:
                   due = change(coin, due)
                   print(f"Change Owed: {due}")
                   break

            case _:
                print("Invalid Coin!")
                continue

main()