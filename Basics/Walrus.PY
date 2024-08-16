""" it is new feauture in python """
""" 
a = True
print(a)//these two line can compiled in one line using walrus operator 
 """
from tkinter import E


print(a:=True)

# Example of walrus operator 
    
# Example 1
""" numbers =[1,2,3,4,5]
while ( n:= len(numbers))>0:
    print(numbers.pop()) """

# Example 2 
 
# without walrus 
""" foods = list()
while True:
    food = input("what food do you want? " )
    if food == "quit" :
        break
    foods.append(food) """
    
# with walrus 
food = list()
while (food:= input("what food do you want? ")) != "quit" :
    food.append(food)
    