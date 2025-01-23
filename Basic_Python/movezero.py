items=[0,1,0,3,12]
target=0

temp=0
j=0

for n in range(len(items)):
    if items[n] !=target:
        temp = items[n]
        items[n] =  items[j]
        items[j] =  temp
        j=j+1
print(items) 