students = []

# all methods are public no access modifiers


class Student:
    pass

    # Class Attribute
    schoolName = "New Delhli Public School"
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

    def get_School_name(self):
        return self.schoolName
