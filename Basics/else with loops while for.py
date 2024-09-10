"""
else use in for and while
else only exectucted for-while loop when loop completed 
not when loop out by break
"""

for i in []:
    print(i)
else:
    print("sorry no i") #Output -> sorry no i
for i in range(5):
    print(i)
else:
    print("else work")  #else work
                        #0
                        #1
                        #2
                        #3
                        #4
                        #else work
for i in range(5):
    if i == 4:
        break
else:
    print("else executde") # nothing prints here
    
i = 0
while i<7:
    print(i)
    i +=1
    if i == 3:
        break
else:
    print("it is while exectued") #0
                                  #1
                                  #2
                                  
                                  
                                    
    