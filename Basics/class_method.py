# this code is not understood by myself by this output(output in last) coming it is pending to be understood
""" 
by default any method is in instance mode 
but by applying @classmethod it will apply to all class"""
class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    
    #it will do in particular instance not for all employee
    def changeCompany(cls , newCompany): # in place of cls you  can put anything you have to do it below also 
        cls.company = newCompany
    """ # like in place of above 2 line 
    def cahngeCompany(kuch_bhi , newCompany): # in place of cls you  can put anything you have to do it below also 
        kuch_bhi.company = newCompany #it will nothing effect """
    
    @classmethod
    def changeCompany2(cls , newCompany): # in place of cls you  can put anything you have to do it below also 
        cls.company = newCompany
    
    
    
e1 = Employee()
e1.name = "Kumar"
e1.show() #The name is Kumar and company is Apple
e1.changeCompany("Tesla")
e1.show() #The name is Kumar and company is Tesla
print(Employee.company) #Apple
print()
e1.changeCompany2("Google")
e1.show()
print(Employee.company) #Google


""" The name is Kumar and company is Apple
The name is Kumar and company is Tesla      
Apple

The name is Kumar and company is Tesla      
Google """