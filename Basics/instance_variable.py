""" Note:
    *   class_object.method_xyz() EQUALS TO class_name.method_xyz(class_object) 
        by this you show understand that by self taken in class methods  you can see in 
        class_name.method_xyz(class_object) that class(self) is been passed
    *   Here genarally veriable attributes are instances for each different class object
        hence if we want something same for everyone like it should not depend on instance
        rather it should depend on class    
        so variable written inside __init__ is generally instance
        so variable written inside class like company_name  is generally not instance and same for everyone and 
        it is called class variable
    *   There will no error even when changing class variable from class object and class name
    *   If class variable changed from class object then it will change only for itself and it will become instance for
        that
    *   If class variable changed from class name then it will change for every class object 
    *    A good example of NoOfEmployee is added"""


class Employee:
    company_name = "Apple" #it will same for everone
    NoOfEmployee = 0
    def __init__(self , name):
        self.name = name
        Employee.NoOfEmployee = 1 +Employee.NoOfEmployee 
    # never do mistake of self.NoOfEmployee = 1 +self.NoOfEmployee  it will not do universelly
    def showDetails(self):
        print(f"The name of the Employees is {self.name} he works in {self.company_name} in workforce of {self.NoOfEmployee}")
emp1 = Employee("Pranjal")
emp1.showDetails()          # The name of the Employees is Harry
Employee.showDetails(emp1)  # The name of the Employees is Harry
emp1.company_name = "Apple India"
emp1.showDetails() #The name of the Employees is Pranjal he works in Apple India

emp2 = Employee("Bablu")
emp2.showDetails() #The name of the Employees is Bablu he works in Apple







