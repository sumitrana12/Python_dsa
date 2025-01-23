num=int(input())
primeornot=""


for n in range(1,num):
    if num == 1:
        primeornot == "The Number is one"
    elif num % n == 0:
        primeornot = "Not Prime"
    else:
        primeornot = "Prime"
print(primeornot)
        