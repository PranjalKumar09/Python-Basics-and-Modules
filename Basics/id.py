# The id() function
# -----------------
# The id() function in Python returns the "identity" of an object. 
# This identity is unique and constant for this object during its lifetime. 
# The identity is an integer which is guaranteed to be unique and constant for this object during its lifetime. 
# In CPython, this is the address of the object in memory.

# Syntax:
# id(object)

# Parameters:
# object: The object whose identity is to be returned.

# Return Value:
# An integer representing the identity of the object.

# Example 1: Using id() with integers
a = 10
b = 20
print(f"The id of a (10) is: {id(a)}")
print(f"The id of b (20) is: {id(b)}")

# Example 2: Using id() with strings
str1 = "hello"
str2 = "world"
print(f"The id of str1 ('hello') is: {id(str1)}")
print(f"The id of str2 ('world') is: {id(str2)}")

# Example 3: Using id() with lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"The id of list1 ([1, 2, 3]) is: {id(list1)}")
print(f"The id of list2 ([4, 5, 6]) is: {id(list2)}")

# Example 4: Showing that the id remains constant for the same object
print(f"The id of list1 before modification: {id(list1)}")
list1.append(4)
print(f"The id of list1 after modification: {id(list1)}")

# Example 5: Different objects with the same value can have different ids
c = 10
print(f"The id of a (10) is: {id(a)}")
print(f"The id of c (10) is: {id(c)}")
# Even though 'a' and 'c' have the same value, they may have different ids.

# Example 6: The id() of an object can be used to check if two variables point to the same object
d = a
print(f"The id of a (10) is: {id(a)}")
print(f"The id of d (which is also a) is: {id(d)}")
# Since 'd' is assigned to 'a', they both point to the same object and have the same id.

# Additional Information
# ----------------------
# - The id() of an object is dynamic in nature, meaning it can change if the value of the object is modified in a way that creates a new object.
# - When you change the value of an immutable object like an integer or string, the id() changes because a new object is created.
# - For mutable objects like lists or dictionaries, the id() remains the same as long as the object itself is not destroyed and recreated.

# Example 7: Changing the value of an immutable object
e = 8
print(f"The id of e (8) is: {id(e)}")
e += 1  # e is now 9
print(f"The id of e (after e += 1) is: {id(e)}")
# Since integers are immutable, modifying 'e' results in a new object with a different id.

# Example 8: Changing the type of an object
f = 42
print(f"The id of f (42) is: {id(f)}")
f = "forty-two"
print(f"The id of f (after changing to 'forty-two') is: {id(f)}")
# Changing the type of 'f' creates a new object, resulting in a different id.

# Example 9: The id of mutable objects remains the same unless explicitly changed
list3 = [7, 8, 9]
print(f"The id of list3 ([7, 8, 9]) is: {id(list3)}")
list3.append(10)
print(f"The id of list3 (after appending 10) is: {id(list3)}")
# The id of 'list3' remains the same after modification because lists are mutable.
