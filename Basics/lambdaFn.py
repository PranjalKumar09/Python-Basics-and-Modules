#lambda is small function it is anonmous fn short period
def appl(fx ,value):
    return 6 + fx(value)
# def double(x):
#     return x*2
double = lambda x: x*2 #it is better in multiple function
avg = lambda x ,y,z : (x+y+z)/3 #they can also have multipl statements

print(double(2))
print(avg(3,4,5))
print(appl(lambda x : x*x*x , 2)) # 6 + 8
