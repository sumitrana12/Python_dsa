given_string=input("Enter a string to check occurance:  ")
target_char=input("Enter the character which you want count the occurance: ")
count=0

for o in given_string:
    if o == target_char:
        count += 1

print("You given character "+str(target_char)+ " has "+str(count)+ " occurence in the given string")
    