class Student:
    print("Hi!")
    def __init__(self, height=160):
        self.height = height
        print("I am alive")


first_student = Student()
print(first_student.height)
kate = Student(height=175)
print(kate.height)