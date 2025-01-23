a=[2,6]
b=[24,36]

common_multi=[]
common_devisor=[]

output = []


for n in range(len(a)):
    for i in range(1, max(b)):
        if i % a[n] == 0:
            common_multi.append(i)

for i in range(1, min(b) + 1):
    if all(x % i == 0 for x in b):
            output.append(i)

print(output)
     
print(common_multi)
print(common_devisor)