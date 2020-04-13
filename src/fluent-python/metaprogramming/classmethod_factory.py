from datetime import date

# random person


class Person:
    # def __new__(cls, name, age):
    #     print("New object called")
    #     # super.__new__(cls[name, age])

    def __init__(self, name, age):
        print('__init__ called')
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthyear):
        print("Factory method called")
        return cls(name, date.today().year - birthyear)

    def display(self):
        print(self.name, self.age)

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)


# person = Person('Sudeep', 19)
# person.display()
person1 = Person.fromBirthYear('John', 1985)
person1.display()
# print(id(person), id(person1))


# class Man(Person):
#     sex = 'Male'


# man = Man.fromBirthYear('John', 1985)
# print(isinstance(man, Man))

# man1 = Man.fromFathersAge('John', 1965, 20)
# print(isinstance(man1, Man), type(man1))
