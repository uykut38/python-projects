class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        if self.grade >= 90:
            return "A"
        elif self.grade >= 80:
            return "B"
        elif self.grade >= 70:
            return "C"
        elif self.grade >= 60:
            return "D"
        else:
            return "F"

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Score:", self.grade)
        print("Grade:", self.get_grade())

    def is_passed(self):
        if self.grade >= 60:
            return True
        else:
            return False


student1 = Student("Ali", 15, 85)
student2 = Student("Ayse", 14, 92)
student3 = Student("Mehmet", 15, 55)


students = [student1, student2, student3]


for student in students:
    student.show_info()

    if student.is_passed():
        print("Status: Passed")
    else:
        print("Status: Failed")

    print("--------------------")


top_student = students[0]

for student in students:
    if student.grade > top_student.grade:
        top_student = student


print("Highest Score:")
top_student.show_info()