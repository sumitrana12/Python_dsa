# fruits = ["Banana", "Kiwi", "Mango"]

# low_fruit = [fruit+"Gu" for fruit in fruits if "a" in fruit]
# print(low_fruit)

student = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]

name_list = []
sorted_marks = sorted(set([scores for name, scores in student]))
sorted_marks.pop(0)
second_lowest = sorted_marks[0]


for name, scores in student:
    if scores == second_lowest:
        name_list.append(name)

final_list = sorted(name_list)

for name in final_list:
    print(name)