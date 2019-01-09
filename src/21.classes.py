# A class defines a set of attributes that are associated with, and shared by, a collection of
# objects known as instances. A class is most commonly a collection of functions (known
# as methods), variables (which are known as class variables), and computed attributes
# (which are known as properties).

# Instances of a class are created by calling a class object as a function


class Employee(object):
    classvariable = "I am global"
    def __init__(self, fname, lname):
        print("Init method initializing vars .. . . . .")
        self.fname = fname
        self.lname = lname

    def printfullname(self):
        self.fullname = self.fname + " "  + self.lname
        return self.fullname

employee = Employee("sudeep", "patel")
employee1 = Employee("sudeep", "patel")

print(dir(employee))

print(employee.printfullname())

print(employee.classvariable)
print(employee1.classvariable)
employee1.classvariable = " I a changed value"

print(employee.classvariable)
print(employee1.classvariable)
print(employee.__dict__)

class EvilEmployee(Employee): #Inheritance
    def __init__(self, fname, lname, evilFactor):
        super().__init__(fname, lname) #when init defined in derived class, 
        #super class init must be called explicityly
        self.evilFactor = evilFactor

    def evil(self):
        return self.evilFactor


eve = EvilEmployee("Sudeep", "Patel", "No")

print(eve.evil(),eve.printfullname())

