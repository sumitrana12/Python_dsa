#left Rotation

import array as arr

rotation_count=int(input("Enter the rotation count "))
new_arr=[4,6,1,3,6,9]
temp_arr=[]

for n in range(rotation_count, len(new_arr)):
    temp_arr.append(new_arr[n])

for i in range(0, rotation_count):
    temp_arr.append(new_arr[i])


print(temp_arr)