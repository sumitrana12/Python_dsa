number=int(input("Enter the number for factorial calculation"))

factorial=1

for n in range(1, number+1):
    factorial = factorial*n
print(factorial)
