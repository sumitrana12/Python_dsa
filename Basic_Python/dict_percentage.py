dict = {
"Krishna": [67, 68, 69],
"Arjun": [70, 98, 63],
"Malika": [52, 56, 60]
}

query_name = input("Input the name between Krishna, Arjun and Malika")
total = 0

for name, marks in dict.items():
    if query_name == name:
        for mark in marks:
            total = total + mark

print(total/3)