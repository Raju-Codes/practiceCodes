class Student:
    name = ''
    number = 0  

student1 = Student()
student2 = Student()

student1.name = "John"
student1.age= 15

print(student1)
class Student1:
    #Defining the constructor using __init__ keyword,
    #self for identifying which object is calling the class.
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Student details: {self.name}, {self.age}")

student1 = Student1("Raju",20)
student1.display()

