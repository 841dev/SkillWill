class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class Mixin(Person):
    def return_Person_attrs(self):
        return f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}"

class Student(Mixin, Person):
    def __init__(self, University, name, surname, age):
        self.university = University
        super().__init__(name, surname, age)






student = Student("GPI", "David", "Baiashvili", "21")

print(student.return_Person_attrs())