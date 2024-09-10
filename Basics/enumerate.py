#enumarate gives index and values both

marks = [12,56,32,98,12,45,1,4]

index = 0
for index, mark in enumerate(marks):
    print(mark)
    if (index == 1):
        print("Pranjal Kumar") 
# 12
# 56
# Pranjal Kumar
# 32
# 98
# 12
# 45
# 1
# 4
print()
print()
for index, mark in enumerate(marks , start=1):#taken first index (0th) as 1 and start 
    print(mark)
    if (index == 1):
        print("Pranjal Kumar") 
# 12
# Pranjal Kumar
# 56
# 32
# 98
# 12
# 45
# 1
# 4
