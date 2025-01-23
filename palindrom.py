word_number=input("Enter you word or number: ")
reverse_word=""

for n in range(len(word_number) -1, -1, -1):
    reverse_word += word_number[n]

if word_number == reverse_word:
    print("Palindrom True")
else:
    print("Palindrom False")