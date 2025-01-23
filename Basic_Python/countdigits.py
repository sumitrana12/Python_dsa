# count the digits of a given number


digit=int(input("Enter the number from which you want to count the digits: "))
count=0

while digit > 0:
    digit = digit//10
    count=count+1

print(count)

