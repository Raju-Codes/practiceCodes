#Class variable are declared at class level
#it shares same copy of instance to object created.

class student:
    collageName="MVJ Polytechnic"
    def __init__(self,name,rollNo):
        self.name=name
        self.rollNo=rollNo

    def displayDeatils(self):
        print(f"{self.name} is studying in {self.collageName} and his roll no is {self.rollNo}")

raju = student("Raju", 30083040)
raju.displayDeatils()
print(raju.collageName)

rahul = student("Rahul", 30083050)
rahul.displayDeatils()
print(rahul.collageName)
