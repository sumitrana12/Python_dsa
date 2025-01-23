#*
#* *
#* * *
#* * * *
#* * * * *

# for n in range(6):
#    print("*" * n)

numbers_star=7
pattern=1

for n in range(numbers_star):
    for j in range(pattern):
        print("*")
    pattern+=1
    print("*", end="")