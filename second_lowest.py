python_students = [['Akriti', 41], ['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Harsh', 39]]


lowest=python_students[0][1]
second_lowest=python_students[0][1]

names=[]

for n in range(len(python_students)):
   if python_students[n][1] < lowest:
      second_lowest = lowest
      lowest = python_students[n][1]
   
for name in range(len(python_students)):
   if python_students[name][1] == second_lowest:
      names.append(python_students[name][0])

names.sort()

for n in names:
   print(n)


      


