number1=int(input("First Number"))
number2=int(input("Second Number"))

factors_list=[]

for n in range(1, number1):
    if number1 % n == 0 and number2 % n == 0:
        factors_list.append(n)

print(str(factors_list))

    

