a=12
b=15
highest_one=0

if a > b:
    highest_one=a
else:
    highest_one=b

for n in range(b, a*b):
    if n % a == 0 and n % b == 0:
        print(n)
        break
