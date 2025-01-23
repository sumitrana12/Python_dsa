
name=input("Enter the string you want to reverse")
reverse_name=""
for n in range(len(name) -1, -1, -1):
    reverse_name = reverse_name + name[n]
print(reverse_name)