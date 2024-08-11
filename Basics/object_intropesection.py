"""
dir()  : the dir() funciton returns a list for all the attributexs and  methods available for an object. useful for what you can do from object
class_object.__dict__ : use to get all attribute we set in {varaible : value} for particular class object
help(Class_Name)  : it give documentry for help pre by class
"""

list1 = [2,1,4]
# print(dir(list1)) #['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# print(list1.__add__) #<method-wrapper '__add__' of list object at 0x00000170004CD900>

tuple1 = (2,1,4)
# print()
# print(dir(tuple1)) #['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John" , 30) #{'name': 'John', 'age': 30, 'version': 1}
print(p.__dict__)

print(help(Person))

""" 

Help on class Person in module __main__:

class Person(builtins.object)
 |  Person(name, age)
 |
 |  Methods defined here:
 |
 |  __init__(self, name, age)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object """




