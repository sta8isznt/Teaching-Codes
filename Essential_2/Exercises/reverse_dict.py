students = {"Anna": 18,
            "George": 20,
            "Maria": 18,
            "Nikos": 17,
            "Elenh": 20
}

grades = {}

for name, grade in students.items():
    # if we havent seen that grade again, add it as an empty list
    if grade not in grades:
        grades[grade] = []
    grades[grade].append(name)


# print the results
for grade, names_list in grades.items():
    print(f"Grade {grade}:", end=" ")
    for name in names_list:
        print(name, end=" ")
    print()
