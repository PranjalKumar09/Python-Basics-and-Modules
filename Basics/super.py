# if child class and parent have both same method they will run class method
class ParentClass:
    def parent_method(self):
        print("This is parent method")
        
class ChildClass(ParentClass):
    def parent_method(self):
        print("This is parent_method of Child Class")
    def child_method(self):
        print("This is called child method")
        super().parent_method() #supe  refers to ParentClass
child_object = ChildClass()
child_object.child_method()
""" This is called child method
This is parent method """

child_object.parent_method() #This is parent_method of Child Class



