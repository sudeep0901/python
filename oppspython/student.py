
students = []


class Student:
    pass
    # adding methods to classs
    # Constructer Method

    def __init__(self, name, student_id=1000):
        # student = {"name": name, "student_id": student_id}
        self.name = name
        self.studentId = student_id
        students.append(self)

    # def add_student(self, name, student_id=1000):
    #     student = {"name": name, "student_id": student_id}
    #     students.append(student)
    def __str__(self):
        return "Students name {0} and student ID {1}".format(self.name, self.studentId)

    def get_name_captalize(self):
        return self.name.capitalize()


student = Student("Sudeep Patel", 1)

new_student = Student("Sanjay", 2)
print(str(student))
print(new_student)
print(student.get_name_captalize())

# student.add_student('Sudeep', 1)
# student.add_student('Mark', 2)
