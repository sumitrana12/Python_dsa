roman = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
    }


s="MCMXCIV"
total=0

for n in range(len(s)):
    if n ==  len(s)-1:
        total = total + roman[s[n]]
        break
    if roman[s[n]] < roman[s[n+1]]:
        total = total - roman[s[n]]
    else:
        total = total + roman[s[n]]

print(total) 