x=121
temp = x
reverse_num=0

while x != 0:
    digits = x%10
    reverse_num = reverse_num*10+digits
    x = x//10

if(temp == reverse_num):
    print("Palindrom")
else:
    print("Not Palindrom")

