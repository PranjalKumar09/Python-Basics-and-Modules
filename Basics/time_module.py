import time

# Checking while vs for (in reality all are better)

def usingWhile():
    i = 0
    while i<10000:
        i += 1
        print(i)

def usingFor():
    for i in range(10000):
        print(i)
        
init = time.time()
usingFor()
fortime = time.time() - init

init = time.time()
usingWhile()
whileTime = time.time()-init

print("For timeing -> " , fortime)
print("While timeing -> " , whileTime)