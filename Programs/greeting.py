def main():
    print("     --- Greetings ---")
    greet = input("Enter your Greeting: ").casefold().strip()
    
    if "hello" in greet:
        print("$0")
    elif "h" in greet:
        print('Pay $20')
    else:
        print("Pay $100")

main()