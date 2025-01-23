number=int(input("Enter the number for Fibanacci series"))

a=0
b=1


for n in range(number+1):
    c = a + b
    a = b
    b = c
    print(b)


