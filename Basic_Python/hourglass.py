# a=[
# [-9,-9,-9,1,1,1], 
#  [0,-9,0,4,3,2],
# [-9,-9,-9,1,2,3],
#  [0,0,8,6,6,0],
#  [0,0,0,-2,0,0],
#  [0,0,1,2,4,0]
#  ]


a=[[-1,-1,0,-9,-2,-2],
[-2,-1,-6,-8,-2,-5],
[-1,-1,-1,-2,-3,-4],
[-1,-9,-2,-4,-4,-5],
[-7,-3,-3,-2,-9,-9],
[-1,-3,-1,-2,-4,-5]]
# a[0][0], a[0][1], a[0][2]
#          a[1][1]
# a[2][0], a[2][1], a[2][2]

sum=0
highest_sum=-9

for n in range(4):
    for i in range(4):
        sum= (a[n][i]) + (a[n][i+1]) + (a[n][i+2]) + (a[n+1][i+1]) + (a[n+2][i]) + (a[n+2][i+1]) + (a[n+2][i+2])
        if sum > highest_sum:
         highest_sum = sum

print(highest_sum)





    
    