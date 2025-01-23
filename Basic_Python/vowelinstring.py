vowels = ['a','e','i','o','u']

given_string=input("Enter a string to check the Vowels in it: ")

for v in given_string:
    if v in vowels:
        print("String have vowel : " +v)
    elif v == " ":
        print("Ignore!, This just a space")
    else:
        print("String have consonent :" +v)


