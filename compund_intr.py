#A = P(1 + R/100) t 
#Compound Interest = A – P  

principle=int(input("Enter the Principle amount "))
rate=int(input("Enter the interest rate "))
time=int(input("Enter the time duration "))

amount=0
ci = 0

amount = principle*(1+rate/100)**time

ci = amount-principle

print(amount)
print(ci)