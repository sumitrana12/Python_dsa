price=[10,12,11,14,13,15,20,17,19]

min=price[0]
Highest_Profit =0
for n in range(len(price)-1):
    if(min>price[n]):
        min = price[n]
    elif (price[n]-min>Highest_Profit): 
        Highest_Profit = price[n]-min
    # for j in range(len(price)-1):
    #  if (price[j] - price[n]) > highest_profit:
    #      highest_profit=price[j] - price[n]

print("Highest_Profit: " +str(Highest_Profit))

