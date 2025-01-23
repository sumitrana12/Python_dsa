
s = "Sumit rana."
new_string = ""
for ch in s:
    if ch.isupper():
        new_string = new_string + ch.lower()
    else:
        new_string = new_string+ch.upper()
print(new_string)