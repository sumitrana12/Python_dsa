first_string=input("Enter the first String: ")
second_string=input("Now enter the second one: ")

count=0

if len(first_string) != len(second_string):
    flag=False
    print("String are not anagram")
elif len(first_string) == len(second_string):
    print("Length matches, Anagram calculation starts here....")
    for f in first_string:
        for s in second_string:
            if f == s:
                count = count+1

if count==len(first_string):
    print("String anagram Status: True")
else:
    print("String anagram Status: False")


                
