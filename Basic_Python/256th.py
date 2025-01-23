number_of_input = int(input())

for n in range(number_of_input):
    year=int(input("Enter the Year to check: "))

    leap_date="12.09."+str(year)
    normal_date="13.09."+str(year)
    nineteen_eighteen_date="26.09."+str(year)



    if year == 1918:
        print(nineteen_eighteen_date)
    elif year <= 1917:
        if year % 4 == 0:
            print(leap_date)
        else:
            print(normal_date)
    elif year >= 1917: 
        if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):
            print(leap_date)
        else:
            print(normal_date)





    