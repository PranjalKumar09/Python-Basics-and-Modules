# can we said type of encapsulation
class MyClass:
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f"Value is {self._value}")
        
    @property #getter 
    def ten_value(self):
        return 10* self._value
    
    @ten_value.setter #with out this and below line will give error #setter
    def ten_value(self , new_value):
        self._value = new_value/10
        return 10 * self._value
    
obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show() # 10 * x => 67 => x = 6.7