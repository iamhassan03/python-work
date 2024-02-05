print("         *** Prime numbers print ***")

low = int(input("Enter lower limit: "))
up = int(input("Enter upper limit: "))

prime = low

print("Prime numbers from {0} to {1} (inclusive) are: " .format(low,up))
while prime < up:
    chk = 2
    prime_chk = 1
    
    while chk < prime:
        if prime % chk == 0:
            prime_chk = 0
            break
        chk+=1
        
    if prime_chk == 1:
        print("  ",prime)
        
    prime+=1 