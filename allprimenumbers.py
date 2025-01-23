n=int(input("Enter the the Numbers till where you want to print: "))

flag=0

for i in range(2, n):
    for s in range(2, i):
        if i % s == 0:
          flag=1
          break
        else:
           flag=0
    if flag == 0:
       print(i)
    
    