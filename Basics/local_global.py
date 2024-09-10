def f():
    global s #if we comment this line it will give error 
    print(s)
    s = "edit"
    print(s)
s = "hello"
f()
print(s)

#output