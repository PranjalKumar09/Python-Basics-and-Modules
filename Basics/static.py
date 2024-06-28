# in class not need to use self in function by using staticmethod 
# also we can call function by class name not only object na

class Math:
    def __init__(self, num):
      self.num = num
    def addtonum(self,n):
        self.num=self.num + n
        
    # static method no need of self in below funciton 
    @staticmethod #you can call directly but it is in class
    def add(a,b):
        return a + b

# result = Math.add(1,2)
# print(result) #3
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(a.add(7,2))
print(Math.add(8,3)) # also used by function



