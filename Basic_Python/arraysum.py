import array as arr

new_arr=arr.array('i', [6,2,3,1,7,3])
sum=0

for n in range(len(new_arr)):
    sum += new_arr[n]

print("Total sum for given array is: "+str(sum))