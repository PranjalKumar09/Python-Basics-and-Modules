"""
self is a refrence to the current of the class and is class used to acess variables that belong to the class
it must be provided as extra parameter inside the method defination

method to make constructor -> if not created then default automatically created 
def __init__(self):

when constructor maked then only by this method object created
even if no argument method created then even default created


"""

class Person:
    name = "Pranjal" #defaul value
    occupation =  "Software Developer"
    networth = 10
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
    def __init__(self , name , occupation):
        print("I am person")
        self.name = name
        self.occupation = occupation
    
#a = Person() # now this will give error
a = Person("Shiva" , "God") 
print(a.name, a.occupation) # Pranjal Software Developer
a.name = "Kumar"
a.occupation = "CM"
print(a.name, a.occupation) # Kumar CM
a.info() # Kumar is a CM

b = Person("Ankit" , "CA")
