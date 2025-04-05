students = {"Anna": 18,
            "George": 20,
            "Maria": 18,
            "Nikos": 17,
            "Elenh": 20
}

def get_top_students(students):
    top_students = {}
    for name, grade in students.items():
        if grade > 18:
            top_students[name] = grade

    return top_students

print(get_top_students(students))
