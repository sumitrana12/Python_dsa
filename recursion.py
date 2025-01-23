#Recursion used for multiple things, by definition it is calling self funtion
#Used in Repetitive programme tasks like factorial, fibnacci

#Example of recursion with factorail program

def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * factorial(n -1)

print(factorial(5))
    
