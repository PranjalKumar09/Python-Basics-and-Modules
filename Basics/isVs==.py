a = 4
b = "4"

print( a is b) #exact location of object in memory
print( a == b ) #value

#False
#False

a = [1,2,43]
b = [1,2,43]

print( a is b) #False
print( a == b) #True

a = 3
b = 3

print( a is b) #True
print( a == b) #True


# because same immutable objects not create again and again

a = "Pranjal"
b = "Pranjal"

print( a is b) #True
print( a == b) #True

a = (1,2)
b = (1,2)

print( a is b) #True
print( a == b) #True

a = None
b = None

print( a is b) #True
print( a == b) #True
print( a is None) #True



