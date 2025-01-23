#n=int(input("Enter the number to find Prime Factors: "))

# Create a function to check if number is prime or not:
def isprime(x):
    for a in range(2, x):
        if x % a == 0:
            return False
    return True

# Now Create a function to calculate the prime factors with help of prime fucntion
def primefactor(y):
    for a in range(2, y):
        if isprime(a):
            if y % a == 0:
                print(a)


primefactor(100)