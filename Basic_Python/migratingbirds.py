birds_type = [1,4,4,4,5,3]

occurence={}
maxkeys=[]

for n in range(len(birds_type)):
    if birds_type[n] not in occurence:
        occurence[birds_type[n]] = 1
    else:
     occurence[birds_type[n]] = occurence[birds_type[n]] + 1

maxvalue=max(occurence.values())

for n in occurence.keys():
   if occurence[n] == maxvalue:
      maxkeys.append(n)

print(min(maxkeys))
      
