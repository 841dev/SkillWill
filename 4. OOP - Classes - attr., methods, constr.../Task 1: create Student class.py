class Student:
    university="GPI"
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age


    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade} "

    @property
    def is_passing(self):
        if self.grade > 60:
            return True
        else:
            return False

    def increase_grade(self, incr_grade):
        if not type(incr_grade) is int:
            raise TypeError("Only integers are allowed")
        elif incr_grade <= 0:
            raise ValueError("Grade must be more than 0")
        else:
            self.grade += incr_grade
            return self.grade



student = Student('David', 95, 20)


print(student.__str__())
print(student.is_passing)
print(student.increase_grade(10))