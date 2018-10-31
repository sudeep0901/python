students = []


def get_students_titelcase():
    students_titelcase = []
    for student in students:
        students_titelcase.append(student["name"].title())

    return students_titelcase


def print_student_titlecase():
    students_titelcase = get_students_titelcase()
    print(students_titelcase)


student = {}


def add_student(name, student_id=100):
    student = {"name": name, "student_id": student_id}
    students.append(student)


add_student("Mark", 1)
add_student("Sudeep", 2)

# get_students_titelcase()
print_student_titlecase()
students_list = get_students_titelcase()

print(students_list)


def var_args(name, *args, **kwargs):
    print(name)
    print(args)
    for arg in args:
        print("Arguments passed are: ", arg)

    print("Keyword arguments: ", kwargs)
    print(kwargs['description'])


# *args - create a tuple when parst
var_args("sudeep Patel", 34, "Technology", "Learner", "India", students,
         description="Python is great", feedback="Good Language")


def save_file(student):
    try:
        f = open("student.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception as ex:
        print("Cound not write data", ex)


def read_file():
    try:
        f = open("student.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Cound not read file")


read_file()
print_student_titlecase()

# nested function
student['name'] = input("Enter Student Name: ")
student["student_id"] = input("Enter student ID:")
add_student(student["name"], student["student_id"])
save_file(student)
# print(print_student_titlecase())
