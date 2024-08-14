class Shape:
    def __init__(self , x, y):
        self.x = x
        self.y = y
    def Area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self , radius ):
        self.radius = radius
    def Area(self):
        return 3.14 * self.radius *self.radius 
rec = Shape(5,3)
print(rec.Area())

crc = Circle(6)
print(crc.Area())
    
# But what if in  circle there is no area it will go to parent area (Shape) but it will cause error because there is no x and y intiliazed for x 
# so for this overriding uses 
    

class Circle2(Shape): # circle without area
    def __init__(self , radius ):
        self.radius = radius
crc2 = Circle2(6) 
# print(crc2.Area()) #Error

print()
print()

# now performing method overriding in Circle3
    
    
    
class Circle3(Shape): # circle without area
    def __init__(self , radius ):
        self.radius = radius
        super().__init__(radius , radius) #sets x , y  to radius ,radius
    
    def area(self):
        return 3.14 * super().Area()

crc3 = Circle(6)
print(crc3.Area())
        
    
    
    