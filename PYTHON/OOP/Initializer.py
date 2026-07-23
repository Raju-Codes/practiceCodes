# Initializer __init__ method - it is instance method
# Used to create and initialize the attributes during object creation.

class Student1:
    def __init__(self):
        print("calling __init__ without arguments")

    def __init__(self, name):
        print("calling __init__ with single arguments", name)

    def __init__(self, name, age):
        print("calling __init__ with multiple arguments", name, age)


studentData = Student1("Raju",14)
