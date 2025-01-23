numbers=[2,4,6,3,1,5,1]
highest=0
second_highest=0

for n in numbers:
    if n > highest:
        second_highest=highest
        highest=n
    
    
print(highest, second_highest) 