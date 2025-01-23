number=input("Enter the number to check if it is armstrong: ")

total_sum=0

for n in number:
    total_sum += int(n)*int(n)*int(n);

if int(number) == total_sum:
    print("Given number " +number+ " is armstrong")
else:
    print("Given number " +number+ " is not armstrong")