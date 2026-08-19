students = []
for i in range(3):
    name = input("ئوقۇغۇچىنىڭ ئىسمى:")
    age = int(input("ئوقۇغۇچىنىڭ يېشى:"))
    score = int(input("نۇمۇرى:"))

    student = {
        "name": name,
        "age": age,
        "score": score
    }

    students.append(student)

for student in students:
    print("ئىسمى:", student["name"])
    print("يېشى:", student["age"])
    print("نۇمۇرى:", student["score"])

    if student["score"] >= 90:
        print("Grade: A")
    elif student["score"] >= 80:
        print("Grade: B")
    elif student["score"] >= 70:
        print("Grade: C")
    elif student["score"] >= 60:
        print("Grade: D")
    else:
        print("Grade: F")