"""
Decorators

if want some fn execute some fn before that fn then execute it
in large no of fn then decorator used

@fn

"""

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thankss for using this funtion")
    return mfx

@greet    
def hello():
    print("Hello world")     
def add(a,b):
    print(a+b)
       
hello()  #normally call 
add(5,6)  


#greet(hello)()
# when greet(hello)() done we should comment decorator @... then output will same as in now with hello()
"""
Good Morning
Hello world
Thankss for using this funtion"""
