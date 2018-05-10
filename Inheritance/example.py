class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    school_name = "CareerDevs"
    def show_info(self):
       print("The student name is {} and it is {} years old. School = {}".format(self.name,self.age,self.school_name))

student = Student('Mike',31)
student.show_info()
