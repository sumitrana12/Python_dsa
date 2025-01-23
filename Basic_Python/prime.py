given_number=int(input("Enter number to check if it is prime or not: "))

is_prime=False

if given_number == 1:
    print("Number 1 can't be a prime") 
elif given_number > 1:
    for n in range(2, given_number):
        if given_number%n != 0:
          is_prime=True
else:
     is_prime=False
print("Prime? : " + str(is_prime))