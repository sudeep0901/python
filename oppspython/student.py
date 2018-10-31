students = []

#all methods are public no access modifiers

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


student = Student("Sudeep Patel", 1)

new_student = Student("Sanjay", 2)
print(str(student))
print(new_student)
print(student.get_name_captalize())
print(student.get_School_name())
print(Student.schoolName)  # Class Attribute
# student.add_student('Sudeep', 1)
# student.add_student('Mark', 2)


# Inheritance
# Student parent class
# HighSchool - Derived School
class HighSchool(Student):
    pass
    schoolName = "Derived New Delhi School"

    def get_School_name(self):
        return self.schoolName + "High School"

    # super is parent class
    def get_name_captalize(self):
        origional_value = super().get_name_captalize()
        return origional_value + "Derive class modified return after using parent class method"


highSchoolStudent = HighSchool('Manasvi', 10)
print(highSchoolStudent.get_name_captalize())
print(highSchoolStudent.get_School_name())
