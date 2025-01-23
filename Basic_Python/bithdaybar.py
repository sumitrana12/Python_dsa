# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it. Lily decides to share a contiguous segment of the bar selected such that:
# The length of the segment matches Ron's birth month, and, The sum of the integers on the squares is equal to his birth day. Determine how many ways she can divide the chocolate.

# Example:
# s=[2,2,1,3,2]
# d=3
# m=2

# Lily wants to find segments summing to Ron's birth day,  with a length equalling his birth month, . In this case, there are two segments meeting her criteria:  and .


s=[2,2,2,1,3,2,2,3,3,1,4,1,3,2,2,1,2,2,4,2,2,3,5,3,4,3,2,1,4,5,4]
d=10
m=4

count=0
total=0

for n in range(len(s)):
    total=0
    for p in range(n, n+m):
        if n+m <= len(s):
            total = total + s[p]
    if (total == d):
        count+=1
print(count)
        


        

    
        
    
#print(count)