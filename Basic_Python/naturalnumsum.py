nth_number=int(input("Specify the nth number to calculate the sum of squares of first natural numbers: "))
sum=0

for n in range(1, nth_number+1):
    sum += n**2
    print(sum)