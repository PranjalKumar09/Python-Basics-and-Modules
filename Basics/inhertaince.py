class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of Employee : {self.id} is {self.name}")
class Programmer(Employee): #prorammer is child class but employee is parent class
    def showLanguage(self):
        print("The default language is Python") 

e1 = Employee("Rohan das", 400)
e1.showDetails()
e2 = Programmer("Harry", 4100)
e2.showDetails()
e2.showLanguage()


