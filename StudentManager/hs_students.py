# Inheritance
# Student parent class
# HighSchool - Derived School

from student import Student


class HighSchool(Student):
    pass
    schoolName = "Derived New Delhi School"

    def get_School_name(self):
        return self.schoolName + "High School"

    # super is parent class
    def get_name_captalize(self):
        origional_value = super().get_name_captalize()
        return origional_value + "Derive class modified return after using parent class method"
