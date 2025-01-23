import array as arr

new_arr=arr.array('i',[4,5,1,6,3,8,0,1])
largest_num=0

for n in new_arr:
    if n >= largest_num:
        largest_num = n

print("Largest number in array is :"+ str(largest_num))