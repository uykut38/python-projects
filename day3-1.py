students = []

for i in range(5):
    name = input("ئوقۇغۇچىنىڭ ئىسمىنى كىرگۈزۈڭ: ")
    students.append(name)

print("بارلىق ئوقۇغۇچىلار:")

for student in students:
    print(student)

print("ئوقۇغۇچىلارنىڭ سانى:", len(students))

if "Ali" in students:
    print("Ali is in the class.")
else:
    print("Ali is not in the class.")